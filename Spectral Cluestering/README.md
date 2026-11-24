# Spectral Clustering with Manim

An animated, Manim-only explanation of spectral clustering. The project does
not use text-to-speech or external narration.

## Topics covered

1. Building a similarity graph
2. Similarity and degree matrices
3. The graph Laplacian `L = D - W`
4. Eigenvectors and spectral embedding
5. Clustering the embedding with k-means
6. Strengths and trade-offs

## Requirements

- Python 3.10 or newer
- [Manim Community Edition](https://docs.manim.community/en/stable/installation.html)

## Render the complete video

Open a terminal in this folder and run:

```powershell
manim -pqh main.py CompleteSpectralClusteringVideo
```

For a fast preview, use `-pql`. For a production-quality render, use:

```powershell
manim -p --quality=production_quality main.py CompleteSpectralClusteringVideo
```

Individual chapters can also be rendered by their scene names, for example:

```powershell
manim -pql main.py CompleteSpectralClusteringVideo
```
