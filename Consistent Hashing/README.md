# Consistent Hashing with Manim

An animated explanation of consistent hashing for distributed systems, created with [Manim](https://www.manim.community/).

## Generated video

[Watch or download the completed render](output/videos/main/480p15/CompleteConsistentHashingVideo_FINAL.mp4).

> Note: The generated animation may contain minor visual errors or timing imperfections.

The video covers:

1. The scaling problem and traditional modulo hashing
2. Hash rings and clockwise key lookup
3. Adding and removing servers
4. Virtual nodes for better load distribution
5. Replication and fault tolerance

## Requirements

- Python 3.10 or newer
- [Manim Community Edition](https://docs.manim.community/en/stable/installation.html)

Install Manim in a virtual environment using the official installation instructions, then open a terminal in this directory.

## Render the animation

Render the complete lesson in preview quality:

```powershell
manim -pqh main.py CompleteConsistentHashingVideo
```

For a faster low-quality preview, use `-pql`. For a higher-quality render, use `-p --quality=production_quality`.

## Run the tests

```powershell
python -m unittest test_consistent_hashing.py
```

The tests cover clockwise lookup, wraparound, localized key movement, virtual nodes, server removal, and replication targets.

## Project files

- `main.py` combines all chapters into `CompleteConsistentHashingVideo`.
- `commonFun.py` contains the hash-ring model and shared animation helpers.
- `voiceover_script.md` contains the narration script.
- `generate_voiceover.ps1` contains the optional voiceover generation workflow.