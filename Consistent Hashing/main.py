from manim import Scene

from addingServer import Scene08_AddServer
from clockwiseLookup import Scene07_ClockwiseLookup
from hashRing import Scene04_HashRing
from intro import Scene01_Introduction
from keysOnRing import Scene06_PlaceKeys
from normalHash import Scene03_TraditionalHashing
from problem import Scene02_ScalingProblem
from removingServer import Scene09_RemoveServer
from replication import Scene11_Replication
from serversOnRing import Scene05_PlaceServers
from summary import Scene12_Summary
from virtualNodes import Scene10_VirtualNodes

VIDEO_CHAPTERS = (
    Scene01_Introduction,
    Scene02_ScalingProblem,
    Scene03_TraditionalHashing,
    Scene04_HashRing,
    Scene05_PlaceServers,
    Scene06_PlaceKeys,
    Scene07_ClockwiseLookup,
    Scene08_AddServer,
    Scene09_RemoveServer,
    Scene10_VirtualNodes,
    Scene11_Replication,
    Scene12_Summary,
)

class CompleteConsistentHashingVideo(Scene):
    """Render every chapter as one continuous consistent-hashing lesson."""
    def construct(self):
        for chapter_number, chapter in enumerate(VIDEO_CHAPTERS):
            chapter.construct(self)
            if chapter_number != len(VIDEO_CHAPTERS) - 1:
                self.wait(0.5)
                self.clear()

Scene00_CompleteVideo = CompleteConsistentHashingVideo
