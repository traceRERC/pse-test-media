# Area patterns
Children directories contain patterns as PNG files with 0% and 100% transparency.
Opaque pixels (transparency = 0) are recolored to the colors specified in either luminance flash patterns (`../lum_flash_patterns/`) 
or red flash patterns (`../red_flash_patterns/`).


| Directory | Description of contents | Area test type | iso |itu_r1702 | ofcom | trace24 | wcag2 | nab_j |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 25pct_416x416| Patterns for testing area thresholds of 25% of any 416x416 subset of the screen. A 416x416 square in screen-and-distance-independent CSS pixels has a similar area as a 10-degree field of view. | Area of subset of screen |  x | x | x | ✔️ | x | x |
| 25pct_screen | Patterns for testing area thresholds of 25% of the entire screen | Area of screen | ✔️ | ✔️ | ✔️ | x | x | ✔️ |
| 80pct_screen | Patterns for testing area thresholds of 80% of the entire screen (scene changes) | Area of screen | x | x | x | x | x | ✔️ |
