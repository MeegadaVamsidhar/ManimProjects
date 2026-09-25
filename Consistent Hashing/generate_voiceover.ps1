param(
    [string]$VoiceName = "Microsoft Ravi"
)

$ErrorActionPreference = "Stop"
Add-Type -AssemblyName System.Speech

$projectDir = $PSScriptRoot
$audioDir = Join-Path $projectDir "voiceover_audio"
$videoPath = Join-Path $projectDir "output\videos\main\480p15\CompleteConsistentHashingVideo.mp4"
$outputPath = Join-Path $projectDir "output\videos\main\480p15\CompleteConsistentHashingVideo_voiceover.mp4"

New-Item -ItemType Directory -Force -Path $audioDir | Out-Null

$chapters = @(
    @{ Start = 2.8; End = 23.6; Text = "Consistent hashing is a technique used in distributed systems to spread data across multiple servers. Imagine many users sending requests to a single server. As traffic grows, that server becomes overloaded, creating slow responses and a single point of failure. We need a way to distribute requests and stored data efficiently, while still knowing exactly where each item belongs. That is the problem consistent hashing helps us solve." },
    @{ Start = 28.0; End = 53.0; Text = "As the number of users increases, one server can no longer handle the complete load. We can add more servers, but this creates an important question: which server should store a particular key, such as Alice, Bob, Charlie, or David? Every client must follow the same predictable rule. The rule should distribute data evenly, find data quickly, and continue working when servers are added or removed." },
    @{ Start = 59.3; End = 97.0; Text = "A simple approach is traditional modulo hashing. First, convert each key into a numeric hash. Then take that value modulo the number of servers. With three servers, Alice's hash of one hundred fifty-four maps to server one. Bob maps to server zero, Charlie to server two, and David to server zero. This works until capacity changes. When a fourth server is added, the formula changes from modulo three to modulo four. Most keys now produce a different result. In this example, three out of four keys move, causing expensive data transfers and many cache misses." },
    @{ Start = 102.3; End = 123.5; Text = "Consistent hashing changes the shape of the hash space. Instead of treating it as a straight line, we wrap the end back to the beginning, forming a circle called the hash ring. Here the values run from zero through one thousand twenty-three, and after the final value we return to zero. Both servers and data keys will be hashed into positions on this same ring. Searches move around it in the clockwise direction." },
    @{ Start = 127.2; End = 157.1; Text = "We begin by hashing each server identifier. Server A lands at position one hundred twenty, server B at four hundred twenty, and server C at eight hundred ten. A server owns the range immediately before its position, up to and including its own point on the ring. The colored arcs show these ownership ranges. Notice that the ranges are not necessarily equal, because normal hash values are distributed randomly. Next, we will place the data keys into this same circular space." },
    @{ Start = 160.8; End = 190.6; Text = "Each data key is passed through the same hash function. Apple lands at two hundred ten, Banana at five hundred sixty, Mango at seven hundred thirty, and Orange at nine hundred twenty. At this stage, the dots only show hash positions; the keys have not yet been assigned to servers. To determine ownership, start at a key and move clockwise around the ring. The first server reached becomes the owner of that key." },
    @{ Start = 194.1; End = 237.3; Text = "Now let us apply the lookup rule. Apple is at two hundred ten. Moving clockwise, the first server is B, so B stores Apple. Banana is at five hundred sixty, and the first server clockwise is C. Orange is at nine hundred twenty. Moving forward wraps around past zero, making server A its owner. Mango, at seven hundred thirty, also reaches server C first. The rule is always identical: begin at the key's hash position and move clockwise until the first server is found. This simple rule gives every key one deterministic owner." },
    @{ Start = 241.4; End = 274.0; Text = "Suppose we add server D at hash position six hundred twenty. Before the change, the existing servers own their colored regions and all keys follow the clockwise rule. After D joins the ring, it takes only the interval immediately before its new position. Banana falls inside this interval, so its ownership changes from server C to server D. The other keys stay where they are. This is the central advantage of consistent hashing: adding capacity moves only a small, local portion of the data rather than remapping almost every key." },
    @{ Start = 278.3; End = 308.3; Text = "The same local behavior applies when a server is removed or fails. Here server B leaves the ring. Only the keys that were owned by B need to be reassigned. Each affected key continues clockwise and moves to the next available server. Keys belonging to A, C, or D remain unchanged. Because failures affect only a limited interval, recovery requires much less data movement than modulo hashing and the rest of the system can continue operating normally." },
    @{ Start = 312.4; End = 365.4; Text = "There is still one practical issue. With only one position per physical server, randomly sized ownership regions can create an uneven load. Virtual nodes solve this by placing each physical server at several positions around the ring. The virtual nodes for A, B, and C are spread throughout the hash space, and every virtual node points back to its physical server. Many smaller regions are therefore mixed across the ring. As more keys are added, the load becomes much more balanced. Virtual nodes also make capacity weighting easier and reduce the impact of a single server failure, while preserving minimal data movement." },
    @{ Start = 369.5; End = 409.6; Text = "Distributed storage also needs protection against failure. For each key, the first server clockwise stores the primary copy. Additional copies are placed on the next distinct servers around the ring. In this example, every key has one primary and two replicas. If the primary server becomes unavailable, another server can still serve the data. Replication improves high availability, fault tolerance, and durability. In a real system, the replication factor can be adjusted to balance reliability, storage cost, and consistency requirements." },
    @{ Start = 413.6; End = 431.2; Text = "In summary, consistent hashing places servers and keys on a ring, finds owners clockwise, and limits remapping when membership changes. Virtual nodes balance the load, while replication protects the data. The result is a scalable, fault-tolerant system with minimal key movement. Thank you." }
)

function Get-WavDuration([string]$Path) {
    $durationText = & ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 $Path
    return [double]::Parse($durationText.Trim(), [Globalization.CultureInfo]::InvariantCulture)
}

$segmentPaths = @()
for ($index = 0; $index -lt $chapters.Count; $index++) {
    $chapter = $chapters[$index]
    $segmentPath = Join-Path $audioDir ("chapter_{0:D2}.wav" -f ($index + 1))
    $allowed = [double]$chapter.End - [double]$chapter.Start
    $selected = $false

    foreach ($rate in 0..5) {
        $speaker = New-Object System.Speech.Synthesis.SpeechSynthesizer
        # PowerShell 7 can expose the Windows voices but fail to select some
        # legacy voice registrations. The synthesizer's default voice is used
        # as a safe fallback when the requested voice is unavailable.
        try {
            $voice = $speaker.GetInstalledVoices() |
                Where-Object { $_.VoiceInfo.Name -eq $VoiceName } |
                Select-Object -First 1
            if ($null -ne $voice) {
                $speaker.SelectVoice($voice.VoiceInfo.Name)
            }
        } catch {
            Write-Warning "Could not enumerate '$VoiceName'; using the default Windows voice."
        }
        $speaker.Rate = $rate
        $speaker.Volume = 100
        $speaker.SetOutputToWaveFile($segmentPath)
        try {
            $speaker.Speak([string]$chapter.Text)
        } catch {
            throw "Windows speech synthesis failed. Enable/install a Windows SAPI voice, then rerun this script. Details: $($_.Exception.Message)"
        }
        $speaker.Dispose()

        $duration = Get-WavDuration $segmentPath
        if ($duration -le $allowed) {
            $selected = $true
            break
        }
    }

    if (-not $selected) {
        throw "Chapter $($index + 1) narration is too long for its video interval."
    }

    $segmentPaths += $segmentPath
    Write-Host ("Chapter {0:D2}: {1:N2}s of {2:N2}s, voice rate {3}" -f ($index + 1), $duration, $allowed, $rate)
}

$ffmpegArgs = @("-y", "-i", $videoPath)
foreach ($segmentPath in $segmentPaths) {
    $ffmpegArgs += @("-i", $segmentPath)
}

$filters = @()
for ($index = 0; $index -lt $chapters.Count; $index++) {
    $delayMs = [int]([double]$chapters[$index].Start * 1000)
    $inputNumber = $index + 1
    $filters += "[$inputNumber`:a]adelay=$delayMs|$delayMs,volume=1.0[a$index]"
}
$mixInputs = (0..($chapters.Count - 1) | ForEach-Object { "[a$_]" }) -join ""
$filters += "${mixInputs}amix=inputs=$($chapters.Count):duration=longest:normalize=0,alimiter=limit=0.95[voice]"
$filterGraph = $filters -join ";"

$ffmpegArgs += @(
    "-filter_complex", $filterGraph,
    "-map", "0:v:0",
    "-map", "[voice]",
    "-c:v", "copy",
    "-c:a", "aac",
    "-b:a", "192k",
    "-ar", "48000",
    "-shortest",
    "-movflags", "+faststart",
    $outputPath
)

& ffmpeg @ffmpegArgs
if ($LASTEXITCODE -ne 0) {
    throw "FFmpeg failed while combining the narration and video."
}

Write-Host "Created: $outputPath"
