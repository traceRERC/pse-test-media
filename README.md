
# Photosensitive Epilepsy (PSE) Test Media 
pse-test-media

> [!WARNING]
> All generated test videos contain flashing sequences and may be hazardous to people with photosensitive epilepsy.
> Failing videos exceed all thresholds of the respective standards (but are constructed to be less hazardous than full screen, full intensity flashing).
> It is safer to view such videos in a small player window in a well-lit environment with one eye covered.

## Contents
 - [Introduction](#introduction)
 - [Usage](#usage)
   - [Create single video](#create-single-video)
   - [Create a set of videos](#create-a-set-of-videos)
 - [Documentation](#documentation)
   - [Spatial patterns (PNG)](#spatial-patterns-png)
   - [Time-and-color patterns (CSV)](#time-and-color-patterns-csv)
   - [Video generation JSON files](#video-generation-json-files)
   - [Video configuration file (JSON)](#video-configuration-file-json)
 - [Background: What is PSE?](#background-what-is-pse)
 - [Acknowledgement](#acknowledgement)


## Introduction
This project aims to provide

 - A set of tools for creating benchmark videos for testing PSE hazard algorithms
 - A set of spatial patterns for benchmark videos (in PNG) that cover area-related benchmark cases
 - A set of patterns in time and color for benchmark videos (in CSV) that cover intensity (both luminance flashes and red flashes) and flash-count-related benchmark cases
 - A set of combined spatial and time/color patterns (in JSON) to be used for benchmark video generation

### Academic citation
This project was first described in the paper: 

Jordan, J. B. (2025). Evaluating Conformance of Video Safety Tools for Photosensitive Epilepsy. In M. Antona & C. Stephanidis (Eds.), *Universal Access in Human-Computer Interaction, HCII 2025*, Lecture Notes in Computer Science, vol. 15780 (pp. 85–98). Springer, Cham. [https://doi.org/10.1007/978-3-031-93848-1_7]("https://doi.org/10.1007/978-3-031-93848-1_7)

 - Free [author version](https://pmc.ncbi.nlm.nih.gov/articles/PMC12249941/) is available on PubMed Central.

## Dependencies
The main frame and video generation scripts have 3 dependencies:

 - OpenCV
 - Numpy
 - Pillow

To install these, you can use:

`pip install opencv-python numpy Pillow`

## Usage
The format and codec of the output video files can be changed in the video configuration file `./video_config.json` ([see details below](#video-configuration-file-json)).

### Create single video
To create a single video run `./make_single_video.py` with a video generation JSON file as an argument.
The video output will be in a `videos/` subdirectory of where the JSON file is.

For example:
```
python ./make_single_video.py ./video_creation/trace24_30fps_01/f001f034.json
```

This creates unique PNG frames with `./generate_frames.py`, sequences the frames to create a video file with `./generate_video.py`, and cleans up the temporary files with `./clean_up.py`.

### Create a set of videos
[Precompiled sets of videos](./video_creation/README.md) are available in `./video_creation/`.

A set of videos are listed in a CSV file, which also contains information about whether videos are expected to pass or not.
Such CSV files list the filenames (without extensions) of the JSON files (as well as the filenames of the resultant videos).
The video output will be created in a `videos/` subdirectory where the video listing CSV file is.

The `./make_videos.py` script has two options:
 - `--silent` - reduces output to the terminal
 - `--max_threads` - the maximum number of parallel threads for video creation.

An example of creating a set of videos:
```
python ./make_videos.py .video_creation/trace24_30fps_01/trace24_30fps_01.csv --silent --max_threads 4
```

Note: If the video listing CSV file has the same name as the containing folder, then one can simply call the containing folder, for example:

```
python ./make_videos.py .video_creation/broadcast_30fps_red01/ --silent --max_threads 4
```

## Documentation
In this project, there are two types of patterns (spatial and time-and-color patterns) that are combined to create video sequences.
There are also other files that are used to define the format, codec, and other characteristics of the resulting videos.

### Spatial patterns (PNG)
Spatial patterns are PNG images with 0% or 100% transparent pixels so that multiple images can be layered as necessary.
Each pattern must be the resolution of the video (e.g., 1920 x 1080 for FHD video).

Spatial patterns included with this project are in the `./area_patterns/` directory. 
There are README files in sub-directories to describe the types of patterns. 

### Time-and-color patterns (CSV)
The time-and-color patterns are CSV files that list the values for each color channel for each frame of the video output.
In the generation process, each spatial pattern is recolored to match the color specified for that frame.

In the sRGB color space, the channels are `r` red, `g` green, `b` blue, and `a` alpha. 
Each channel has its own column with 8-bit decimal representation (range 0-255).

In the future, the project is expected to include support for other color spaces, but sRGB is the only color space supported today.

Such patterns included with this project are in the `./lum_flash_patterns/` directory for luminance flashes and the `./red_flash_patterns/` directory for red flashes. There are README files in sub-directories that further describe the characteristics of specific patterns. 

### Video generation JSON files
Video generation files define how the spatial and time-and-color patterns are combined to make a video. 
The following are required components of the JSON:

 - `"framerate:"` - \[Float] The frame rate for the resulting video.
 - `"colormodel"` - \[String {"sRGB"}] Color model or color space of the colors given in the time-and-color pattern(s).
 - `"bgcolor"` - \[String] Background color (in the color model specified) to fill all otherwise transparent areas of all frames.
 - `"pattern"` - \[Object] One or more pairs of spatial + time-and-color patterns that are to be combined to make frames.
   - `"spatial"` - \[String] path to the spatial pattern (PNG).
   - `"temporal_color"` - \[String] path to the time-and-color pattern (CSV).


By default, video generation files override values in the video configuration file, but this can be changed with the option `--precedence=config`.

### Video configuration file (JSON)
The video configuration file `./video_config.json` defines the parameters that should be used across many videos. 
They can be defined in individual video generation JSON files, but that would lead to extensive duplication.
The following are required components of the JSON:

 - `"codec"` - \[String] The FOURCC identifier for the file output's video codec, compression format, color or pixel format ([more information](https://fourcc.org/)). This must be supported by OpenCV.
 - `"video_extension:"` - \[String] The extension to be used for the video file.
 
Optional parameters include:
 - `"padding"` - \[Integer] The number of frames of padding at the beginning of the video (repeats the first frame)


## Background: What is PSE?
People with photosensitive epilepsy (PSE) can have seizures when viewing particular visual stimuli with flashing, flicker, and bold patterns.
While specific hazards are unique to each individual, there are guidelines and standards available that set safety thresholds:

 - [Recommendation ITU-R BT.1702](https://www.itu.int/rec/R-REC-BT.1702/en). Guidance for the reduction of photosensitive epileptic seizures caused by television.
 - [ISO 9241-391 \[non-free standard\]](https://www.iso.org/standard/56350.html). Ergonomics of human-system interaction—Part 391: Requirements, analysis and compliance
test methods for the reduction of photosensitive seizures. 
 - [WCAG 2.2 Success Criterion 2.3.1](https://www.w3.org/TR/WCAG22/#three-flashes-or-below-threshold) Success Criterion 2.3.1 Three Flashes or Below Threshold. In Web Content Accessibility Guidelines (WCAG) 2.2.
 - [NAB-J guidelines](https://www.j-ba.or.jp/category/broadcasting/jba103852). アニメーション等の映像手法に関するガイドライン \[Guidelines on video methods such as animation\] by Japan Broadcasting Corporation & Japan Commercial Broadcasters Association.
 - [Ofcom guidelines](https://www.ofcom.org.uk/siteassets/resources/documents/tv-radio-and-on-demand/broadcast-guidance/programme-guidance/broadcast-code-guidance/section-2-guidance-notes.pdf) Annex 1: Ofcom Guidance Note on Flashing Images and Regular Patterns in Television. In: Ofcom Guidance Notes, Section 2: Harm and offence, pp. 18–21.

These standards are not fully harmonized, but all of them have safety thresholds related to the following criteria. In order to be considered hazardous, a flashing sequence must meet or exceed all three thresholds:

 - Intensity: the brightness (luminance) of the flash or the degree of color change (chromaticity) of flashes involving saturated red.
 - Area: the flashing area.
 - Flash count: the number of flashes in a specific time period.

Thus, if a flashing sequence passes at least one threshold (i.e., falls short of at least one threshold), then the whole sequence passes. More details are available in the 2024 article [International Guidelines for Photosensitive Epilepsy: Gap Analysis and Recommendations](https://doi.org/10.1145/3694790).


## Acknowledgement
The contents of this code repository were developed under a grant from the National Institute on Disability, Independent Living, and Rehabilitation Research (NIDILRR grant #90REGE0024). 
NIDILRR is a Center within the Administration for Community Living (ACL), Department of Health and Human Services (HHS). 
The contents are those of the authors and do not necessarily represent the official views of, nor an endorsement by NIDILRR, ACL/HHS, or the U.S. Government. 
