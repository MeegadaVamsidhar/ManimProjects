from manim import Scene

from build_graph03 import Scene03_BuildGraph
from degree_matrix05 import Scene05_DegreeMatrix
from eigenvectors07 import Scene07_Eigenvectors
from introduction01 import Scene01_Introduction
from kmeans09 import Scene09_KMeans
from laplacian06 import Scene06_Laplacian
from similarity_matrix04 import Scene04_SimilarityMatrix
from spectral_embedding08 import Scene08_SpectralEmbedding
from summary11 import Scene11_Summary
from when_to_use_it10 import Scene10_WhenToUseIt
from what_is_spectral02 import Scene02_WhatIsSpectral


VIDEO_CHAPTERS = (
    Scene01_Introduction,
    Scene02_WhatIsSpectral,
    Scene03_BuildGraph,
    Scene04_SimilarityMatrix,
    Scene05_DegreeMatrix,
    Scene06_Laplacian,
    Scene07_Eigenvectors,
    Scene08_SpectralEmbedding,
    Scene09_KMeans,
    Scene10_WhenToUseIt,
    Scene11_Summary,
)


class CompleteSpectralClusteringVideo(Scene):
    """Render every chapter as one continuous spectral-clustering lesson."""

    def construct(self):
        for chapter_number, chapter in enumerate(VIDEO_CHAPTERS):
            chapter.construct(self)
            if chapter_number != len(VIDEO_CHAPTERS) - 1:
                self.wait(0.5)
                self.clear()


Scene00_CompleteVideo = CompleteSpectralClusteringVideo
