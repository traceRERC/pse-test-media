# Combined area flash set for Trace24 01 

 - **File:** trace24_30fps_area_combo01.csv
 - **Standard:** trace24  
 - **Flash type:** Luminance
 - **Frame rate:** 30 fps
 - **Dynamic range:** SDR
 - **Color space:** sRGB
 - **Number of videos:** 20

**Description:** These videos have a flashing area made of two subareas.
Subareas start with either of two luminance levels.
Passing videos are constructed such that only one dimension passes, with other dimensions exceeding thresholds by a small amount.

 - _Luminance:_ Both subareas transition in the same direction, however some transitions fall short of the luminance threshold to exercise the luminance pass:
    - `01m90f008_01n10y001.json`
    - `03m50f024_03n50y022.json`
    - `05m50y016_05n50f013.json`
 - _Count:_ Most subareas transition at the same time, except for tests that exercise the count pass:
    - `01m50c004_01n50f003.json`
    - `02m70f021_02n30c028.json`
    - `04m90c032_04n10f037.json`
 - _Area:_ Taken together, the sum of the subareas exceeds the area threshold , except for tests that exercise the area threshold:
    - `01m70f024_01n25f025.json`
    - `02m45f002_02n50f006.json`
    - `03m85f038_03n10f031.json`
    - `04m65fr003_04n30fr007.json`
    - `05m90f013_05n05f016.json`
 - _Failing videos:_ Failing videos are constructed such that the luminance, count, and area (taken together) exceed the respective thresholds by a small margin.
    - `01m70f018_01n30f016.json`
    - `02m50f001_02n50f007.json`
    - `02m90f024_02n10f022.json`
    - `03m70f035_03n30f033.json`
    - `03m90f006_03n10f004.json`
    - `04m50fr013_04n50fr015.json`
    - `04m70f012_04n30f011.json`
    - `05m70f027_05n30f028.json`
    - `05m90fr007_05n10fr004.json`
