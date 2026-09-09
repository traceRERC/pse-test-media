# 30 fps syncronicity flash set for Trace24 01 

 - **File:** trace24_30fps_sync01.csv
 - **Standard:** trace24  
 - **Flash type:** Luminance
 - **Frame rate:** 30 fps
 - **Dynamic range:** SDR
 - **Color space:** sRGB
 - **Number of videos:** 8

**Description:**
These videos have a flashing area made of two subareas with the same luminance.
The only variable that changes between passing and failing is the timing of one of the subarea transitions: transitions are exactly in sync OR one transition is one-frame out of sync.

 - _Out of sync:_ Both subareas transition in the same direction, but one of the transitions is offset by one frame (33 ms, which is greater than the 20 ms syncronicity threshold) between the two subareas.
    - `01m50ff032_01n50f032.json`
    - `02m90ff015_02n10f015.json`
    - `04m70f021_04n30ff021.json`
    - `05m70f007_05n30ff007.json`
 - _Failing videos:_ Failing videos are constructed such that the luminance, count, and area (taken together) exceed the respective thresholds by a small margin. The subareas are in sync.
    - `01m70f018_01n30f018.json`
    - `02m50f024_02n50f024.json`
    - `03m90f006_03n10f006.json`
    - `05m90f033_05n10f033.json`
