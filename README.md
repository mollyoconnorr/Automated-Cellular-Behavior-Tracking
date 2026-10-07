# Automated Cellular Behavior Tracking

An automated image and video analysis workflow for studying the behavior of *Tetrahymena thermophila* under simulated microgravity conditions.

This research project combines Python, CellProfiler, and image-analysis workflows to reduce the amount of manual analysis required for large microscopy datasets. The goal is to detect, track, and quantify cellular movement and morphology across thousands of images and video frames, creating reproducible quantitative data for downstream biological analysis.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Research Objectives](#research-objectives)
- [Analysis Workflow](#analysis-workflow)
- [CellProfiler Pipeline](#cellprofiler-pipeline)
- [Python Components](#python-components)
- [Technologies Used](#technologies-used)
- [Experimental Context](#experimental-context)
- [Getting Started](#getting-started)
- [Repository Structure](#repository-structure)
- [Future Work](#future-work)
- [Research Significance](#research-significance)
- [Research Team](#research-team)
- [References](#references)
- [Project Status](#project-status)

---

## Project Overview

Spaceflight introduces environmental stressors such as microgravity and radiation that can disrupt cellular processes including mitochondrial function, energy metabolism, and oxidative stress.

This project investigates how *Tetrahymena thermophila*, a single-celled ciliate, responds to simulated microgravity and whether antioxidant treatments such as N-acetylcysteine (NAC) and L-ergothioneine may help mitigate cellular stress.

From a computational perspective, the project focuses on developing automated workflows for:

- Processing microscopy videos and image sequences
- Extracting individual video frames
- Detecting and segmenting cells
- Tracking individual cells across frames
- Measuring cell movement and morphology
- Exporting quantitative measurements for statistical analysis
- Reducing manual analysis and improving reproducibility

The project is part of an interdisciplinary research effort combining computer science, data analysis, image processing, and experimental biology.

---

## Research Objectives

The primary objective is to develop and optimize automated image-analysis pipelines capable of quantifying behavioral and morphological changes in *T. thermophila* under different experimental conditions.

The project focuses on:

1. **Cell Detection** — Automatically identify individual cells within microscopy images.
2. **Cell Tracking** — Follow individual cells across sequential video frames.
3. **Behavioral Analysis** — Quantify movement-related measurements such as displacement, distance traveled, trajectory, linearity, and cell lifetime.
4. **Morphological Analysis** — Extract measurements that can be used to evaluate changes in cellular structure and morphology.
5. **High-Throughput Processing** — Process large collections of microscopy images and video frames more efficiently than manual analysis.
6. **Reproducible Data Collection** — Produce structured measurements that can be combined with existing biological assay data for statistical analysis.

---

## Analysis Workflow

The current workflow combines Python preprocessing with CellProfiler-based image analysis:

```
Microscopy Video
       ↓
Python Video Processing
       ↓
Crop Region of Interest
       ↓
Extract Individual Frames
       ↓
CellProfiler Pipeline
       ↓
Image Preprocessing
       ↓
Cell Detection & Segmentation
       ↓
Cell Tracking
       ↓
Movement & Object Measurements
       ↓
CSV Data Export
       ↓
Statistical Analysis
```

Python is used to prepare video data before analysis. The current preprocessing scripts crop videos to the relevant region of interest and extract individual frames as PNG images.

CellProfiler then processes the image sequence, identifies cells, tracks them through time, and exports measurements to a CSV file.

---

## CellProfiler Pipeline

The repository includes a CellProfiler pipeline (`pipeline.cppipe`) designed for automated cell detection and tracking.

The current pipeline:

- Loads grayscale microscopy images
- Extracts frame and date metadata from filenames/folders
- Groups images into experimental series
- Performs image inversion
- Identifies primary objects representing cells
- Uses a 10–60 pixel expected cell diameter
- Applies Minimum Cross-Entropy thresholding
- Tracks cells using CellProfiler's Overlap tracking method
- Exports tracking and location measurements to CSV

The tracking configuration includes measurements such as:

- Integrated distance
- Distance traveled
- Displacement
- Linearity
- X/Y trajectory
- Cell lifetime
- Object number
- Cell center location

> **Note:** These settings are tuned to the microscopy data used in this project and may require adjustment for different imaging conditions.

---

## Python Components

### `Testing.py`

Handles video preprocessing and frame extraction.

The current workflow:

1. Opens the input microscopy video.
2. Crops the video to a selected region.
3. Saves the cropped video.
4. Extracts individual frames.
5. Saves each frame as a numbered PNG image.

OpenCV is used for video processing and frame extraction.

### `SizeTesting.py`

A helper script used to determine the dimensions of the region of interest within a microscopy video.

The script allows a user to select an ROI from the first video frame and returns the selected coordinates and dimensions.

### `TestingCellProfiler.py`

Automates execution of the CellProfiler pipeline from Python.

The script launches CellProfiler in headless mode, passes the input image directory and pipeline file, and writes the resulting measurements to an output directory.

---

## Technologies Used

**Programming**

- Python
- OpenCV
- NumPy
- Pandas

**Image Analysis**

- CellProfiler
- ImageJ / Fiji

**Data Analysis**

- CSV-based measurement data
- Statistical analysis in Python or R
- Visualization and exploratory analysis

---

## Experimental Context

The computational pipeline supports analysis of several *Tetrahymena thermophila* assays, including:

- Motility
- Feeding
- Deciliation
- Cellular morphology

The broader research examines cellular behavior under simulated microgravity and investigates whether antioxidant treatments such as NAC and ergothioneine may reduce oxidative stress and support normal cellular function.

The computational analysis is intended to complement experimental measurements rather than replace biological validation.

---

## Getting Started

### Requirements

To work with this repository, install:

- Python 3
- OpenCV
- NumPy
- Pandas
- CellProfiler
- ImageJ / Fiji for complementary image and video analysis

Install the Python dependencies with:

```bash
pip install opencv-python numpy pandas
```

CellProfiler can be downloaded from the official CellProfiler website: <https://cellprofiler.org/>

### Running the Workflow

#### 1. Prepare the video

Place the microscopy video in the project directory. For example:

```
example_of_deciliation.mp4
```

#### 2. Determine the region of interest

Run:

```bash
python SizeTesting.py
```

Select the portion of the video that contains the cells to be analyzed.

#### 3. Extract video frames

Update the input and output paths in `Testing.py` as needed, then run:

```bash
python Testing.py
```

This creates a sequence of PNG images for CellProfiler analysis.

#### 4. Run the CellProfiler pipeline

Open `pipeline.cppipe` in CellProfiler and verify the input/output directories.

The pipeline can also be launched programmatically using:

```bash
python TestingCellProfiler.py
```

The Python script is configured to run CellProfiler without opening the graphical interface and save the resulting measurements to the specified output directory.

> **Note:** The current Python scripts contain local file paths that were used during development. These paths must be updated before running the workflow on another computer.

---

## Repository Structure

```
automated-cellular-behavior-tracking/
│
├── SizeTesting.py
│       # Selects and measures the region of interest in a video
│
├── Testing.py
│       # Crops videos and extracts individual frames
│
├── TestingCellProfiler.py
│       # Runs the CellProfiler pipeline programmatically
│
├── pipeline.cppipe
│       # CellProfiler image analysis and tracking pipeline
│
├── pipeline.cpproj
│       # CellProfiler project file
│
├── .gitignore
└── README.md
```

The repository currently contains the core preprocessing and CellProfiler development files used to test the automated tracking workflow.

---

## Future Work

Planned and potential extensions include:

- Refine cell segmentation for different experimental conditions
- Improve tracking accuracy across crowded or overlapping cells
- Automate processing across larger datasets
- Add additional behavioral measurements
- Quantify mitochondrial and vacuole morphology
- Integrate processed measurements with existing biological assay data
- Perform statistical testing such as t-tests and ANOVAs
- Develop visualization tools for cell trajectories and movement patterns
- Validate automated measurements against manually analyzed samples
- Explore machine learning approaches for classifying cellular behaviors

The long-term goal is to create a reliable and reproducible computational workflow that can be applied to large microscopy datasets with minimal manual intervention.

---

## Research Significance

Manual analysis of microscopy videos can be time-consuming and difficult to reproduce consistently across large datasets.

Automating cell detection, tracking, and measurement provides a way to transform microscopy data into structured quantitative datasets that can be analyzed statistically.

By combining computational image analysis with experimental biology, this project demonstrates how software engineering and data science can support biological research, particularly in the study of cellular responses to spaceflight-related environmental stressors.

---

## Research Team

| Name | Role |
|------|------|
| **Molly O'Connor** | Computer Science & Data Science Researcher |
| **Stefanie Otto-Hitt, PhD** | Carroll College |
| **C. Jack Conway** | Associate Professor of Biology, Carroll College |

---

## References

1. Carpenter, A. E., Jones, T. R., Lamprecht, M. R., et al. (2006). CellProfiler: Image analysis software for identifying and quantifying cell phenotypes. *Genome Biology, 7*, R100. <https://doi.org/10.1186/gb-2006-7-10-r100>

2. Deiana, M., Rosa, A., Casu, V., Piga, R., Dessì, M. A., & Aruoma, O. I. (2004). L-ergothioneine modulates oxidative damage in the kidney and liver of rats in vivo. *Clinical Nutrition, 23*(2), 183–193. <https://doi.org/10.1016/S0261-5614(03)00108-0>

3. Feger, B. J., Thompson, J. W., Dubois, L. G., et al. (2016). Microgravity induces proteomics changes involved in endoplasmic reticulum stress and mitochondrial protection. *Scientific Reports, 6*, 34091. <https://doi.org/10.1038/srep34091>

4. Garrett-Bakelman, F. E., et al. (2019). The NASA Twins Study: A multidimensional analysis of a year-long human spaceflight. *Science, 364*(6436), eaau8650. <https://doi.org/10.1126/science.aau8650>

5. Michaletti, A., Gioia, M., Tarantino, U., & Zolla, L. (2017). Effects of microgravity on osteoblast mitochondria: A proteomic and metabolomics profile. *Scientific Reports, 7*, 15376. <https://doi.org/10.1038/s41598-017-15612-1>

6. Smith, D. G. S., Gawryluk, R. M. R., Spencer, D. F., Pearlman, R. E., Su, K. W., & Gray, M. W. (2007). Exploring the mitochondrial proteome of the ciliate protozoon *Tetrahymena thermophila*. *Journal of Molecular Biology, 374*(4), 837–863.

7. Aldini, G., Altomare, A., Baron, G., et al. (2018). N-Acetylcysteine as an antioxidant and disulphide breaking agent. *Free Radical Research, 52*(7), 751–762. <https://doi.org/10.1080/10715762.2018.1468564>

---

## Project Status

**Status:** Research / Development

This repository contains an actively developed image-processing and automated cell-tracking workflow. Pipeline parameters and processing scripts are being refined as experimental datasets and analysis requirements evolve.
