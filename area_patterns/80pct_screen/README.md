# Spatial patterns for screen change (80%) threshold
All source images in this folder are patterns for testing the following area threshold:
> Fail where 80% or more of the pixels on the screen are involved

Filenames that start with 'f' are failing (i.e., more pixels than the threshold). 
Those starting with 'a' pass the area threshold.

For any failing spatial pattern incorporated into a video, 
all of the other thresholds also need to fail for a video sequence to be 
considered potentially hazardous.

| File | Description | *f* - Fail area threshold | *a* - Pass area threshold |
| --- | --- | --- | --- |
| *x*01 ... | Hollow shape | ![Failure of a hollow shape](./thumbnails/f01_thumb.png) | ![Pass of a hollow shape](./thumbnails/a01_thumb.png) |
| *x*02 ... | Large area on the right side | ![Failure of a large area on the right side](./thumbnails/f02_thumb.png) | ![Pass of a large area on the right side](./thumbnails/a02_thumb.png) |
| *x*03 ... | Large central area | ![Failure of a large central area](./thumbnails/f03_thumb.png) | ![Pass of a large central area](./thumbnails/a03_thumb.png) |
| *x*04 ... | Middle area missing | ![Failure of a shape with the middle area missing](./thumbnails/f04_thumb.png) | ![Pass of a shape with the middle area missing](./thumbnails/a04_thumb.png) |
| *x*05 ... | Large shape missing areas on the right | ![Failure](./thumbnails/f05_thumb.png) | ![Pass](./thumbnails/a05_thumb.png) |
