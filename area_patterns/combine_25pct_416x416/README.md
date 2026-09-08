# Two-part combination patterns for "25% of 416x416 px" threshold
All source images in this folder are patterns for testing the following area threshold:
> Fail where 25% or more of the pixels are involved from any 416 x 416 px subarea

Files are intended to be used as pairs, which make up a failing (or passing) combined flash area.

## File naming and usage convention
Filenames are of the form `01m50.png` and `01n50.png`.

 - First two numbers are the pattern. The pattern number is intended to match with a pair.
 - Third character is either the letter `m` or `n`. An `m` pattern is intended to pair with an `n` pattern.
 - Last two numbers are the rough percentage of the (potentially) failing area. If the numbers of a pair add to 100, the combined area exceeds the area threshold.
     - A `𝑝𝑝m50` pattern combined with the corresponding `𝑝𝑝n50` pattern is slightly more than what is required to fail. The pixels of each area are equal.
     - A `𝑝𝑝m50` pattern combined with the corresponding `𝑝𝑝n45` pattern is less than the failing area threshold (similarly a `𝑝𝑝m45` and `𝑝𝑝n50` combination)
     - A `𝑝𝑝m70` pattern combined with the corresponding `𝑝𝑝n30` pattern is slightly more than what is required to fail. Approximately 70% of the pixels are in `m` and 30% in `n`.
     - A `𝑝𝑝m70` pattern combined with the corresponding `𝑝𝑝n25` pattern is less than the failing area threshold (similarly a `𝑝𝑝m65` and `𝑝𝑝n30` combination).
     - A `𝑝𝑝m90` pattern combined with the corresponding `𝑝𝑝n10` pattern is slightly more than what is required to fail. Approximately 90% of the pixels are in `m` and 10% in `n`.
     - A `𝑝𝑝m90` pattern combined with the corresponding `𝑝𝑝n05` pattern is less than the failing area threshold (similarly a `𝑝𝑝m85` and `𝑝𝑝n10` combination).

For any failing spatial pattern combination incorporated into a video, 
all of the other thresholds also need to fail for a video sequence to be 
considered potentially hazardous.

| File | Passing `m` area (pair with failing `n` area) | Failing `m` area (pair with failing `n` area) | Failing `n` area (pair with failing `m` area) | Passing `n` area (pair with failing `m` area) |
| --- | --- | --- | --- | --- |
| Pattern 01, 50:50 split | `01m45.png` ![ ](./thumbnails/01m45_thumb.png) | `01m50.png` ![ ](./thumbnails/01m50_thumb.png) | `01m50.png` ![ ](./thumbnails/01n50_thumb.png) | `01n45.png` ![ ](./thumbnails/01n45_thumb.png) |
| Pattern 01, 70:30 split | `01m65.png` ![ ](./thumbnails/01m65_thumb.png) | `01m70.png` ![ ](./thumbnails/01m70_thumb.png) | `01m30.png` ![ ](./thumbnails/01n30_thumb.png) | `01n25.png` ![ ](./thumbnails/01n25_thumb.png) |
| Pattern 01, 90:10 split | `01m85.png` ![ ](./thumbnails/01m85_thumb.png) | `01m90.png` ![ ](./thumbnails/01m90_thumb.png) | `01m10.png` ![ ](./thumbnails/01n10_thumb.png) | `01n05.png` ![ ](./thumbnails/01n05_thumb.png) |
| Pattern 02, 50:50 split | `02m45.png` ![ ](./thumbnails/02m45_thumb.png) | `02m50.png` ![ ](./thumbnails/02m50_thumb.png) | `02m50.png` ![ ](./thumbnails/02n50_thumb.png) | `02n45.png` ![ ](./thumbnails/02n45_thumb.png) |
| Pattern 02, 70:30 split | `02m65.png` ![ ](./thumbnails/02m65_thumb.png) | `02m70.png` ![ ](./thumbnails/02m70_thumb.png) | `02m30.png` ![ ](./thumbnails/02n30_thumb.png) | `02n25.png` ![ ](./thumbnails/02n25_thumb.png) |
| Pattern 02, 90:10 split | `02m85.png` ![ ](./thumbnails/02m85_thumb.png) | `02m90.png` ![ ](./thumbnails/02m90_thumb.png) | `01m20.png` ![ ](./thumbnails/02n10_thumb.png) | `02n05.png` ![ ](./thumbnails/02n05_thumb.png) |
| Pattern 03, 50:50 split | `03m45.png` ![ ](./thumbnails/03m45_thumb.png) | `03m50.png` ![ ](./thumbnails/03m50_thumb.png) | `03m50.png` ![ ](./thumbnails/03n50_thumb.png) | `03n45.png` ![ ](./thumbnails/03n45_thumb.png) |
| Pattern 03, 70:30 split | `03m65.png` ![ ](./thumbnails/03m65_thumb.png) | `03m70.png` ![ ](./thumbnails/03m70_thumb.png) | `03m30.png` ![ ](./thumbnails/03n30_thumb.png) | `03n25.png` ![ ](./thumbnails/03n25_thumb.png) |
| Pattern 03, 90:10 split | `03m85.png` ![ ](./thumbnails/03m85_thumb.png) | `03m90.png` ![ ](./thumbnails/03m90_thumb.png) | `03m10.png` ![ ](./thumbnails/03n10_thumb.png) | `03n05.png` ![ ](./thumbnails/03n05_thumb.png) |
| Pattern 04, 50:50 split | `04m45.png` ![ ](./thumbnails/04m45_thumb.png) | `04m50.png` ![ ](./thumbnails/04m50_thumb.png) | `04m50.png` ![ ](./thumbnails/04n50_thumb.png) | `04n45.png` ![ ](./thumbnails/04n45_thumb.png) |
| Pattern 04, 70:30 split | `04m65.png` ![ ](./thumbnails/04m65_thumb.png) | `04m70.png` ![ ](./thumbnails/04m70_thumb.png) | `04m30.png` ![ ](./thumbnails/04n30_thumb.png) | `04n25.png` ![ ](./thumbnails/04n25_thumb.png) |
| Pattern 04, 90:10 split | `04m85.png` ![ ](./thumbnails/04m85_thumb.png) | `04m90.png` ![ ](./thumbnails/04m90_thumb.png) | `04m10.png` ![ ](./thumbnails/04n10_thumb.png) | `04n05.png` ![ ](./thumbnails/04n05_thumb.png) |
| Pattern 05, 50:50 split | `05m45.png` ![ ](./thumbnails/05m45_thumb.png) | `05m50.png` ![ ](./thumbnails/05m50_thumb.png) | `05m50.png` ![ ](./thumbnails/05n50_thumb.png) | `05n45.png` ![ ](./thumbnails/05n45_thumb.png) |
| Pattern 05, 70:30 split | `05m65.png` ![ ](./thumbnails/05m65_thumb.png) | `05m70.png` ![ ](./thumbnails/05m70_thumb.png) | `05m30.png` ![ ](./thumbnails/05n30_thumb.png) | `05n25.png` ![ ](./thumbnails/05n25_thumb.png) |
| Pattern 05, 90:10 split | `05m85.png` ![ ](./thumbnails/05m85_thumb.png) | `05m90.png` ![ ](./thumbnails/05m90_thumb.png) | `05m10.png` ![ ](./thumbnails/05n10_thumb.png) | `05n05.png` ![ ](./thumbnails/05n05_thumb.png) |




## Construction
These patterns can be combined in ways that test the following (and other possibilities):

 - Flashes where the transitions are synchronized, but the color(s) across the combined area are not identical (both luminance & red).
 - Flashes where most transitions are synchronized, but in one transition the two sub areas transition in opposite directions. (Passing tests.)
 - Flashes where the transitions are close enough to be considered synchronized vs. not quite close enough. This would apply to guidelines that have (TRACE guidelines) or have an assumed synchronization metric.
     