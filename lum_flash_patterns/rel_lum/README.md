# Luminance flash patterns for 0.1 relative luminance and >3 flashes/s thresholds
All source CSV files in this folder are patterns for testing the luminance flash thresholds:
> - luminance threshold of 0.1 relative luminance (RL)
> - flash count threshold of >3 flashes per second (i.e., 7 or more alternating transitions)

Filenames that start with 
 - 'f' are failing - fail luminance threshold (0.1 RL) and fail count threshold (>3 flash/s)
 - 'c' are passing - fail luminance threshold (0.1 RL) and pass count threshold (>3 flash/s)
 - 'l' are passing - pass luminance threshold (0.1 RL) and fail count threshold (>3 flash/s)
 - 'y' are passing - pass luminance threshold with only one flash in the sequence below threshold (0.1 RL) and fail count threshold (>3 flash/s)

For any failing pattern incorporated into a video, 
all of the other thresholds also need to fail for a video sequence to be 
considered potentially hazardous.

Note that many of the flashes marked 'f' in this folder would pass the NAB-J standards.

## Patterns
Representations of temporal-color patterns.

### 30 fps tests

| Scheme | Description | *f* - Failure | *l* - Lum. Pass | *c* - Flash Count Pass | *y* - Single Lum. Pass |
| --- | --- | --- | --- | --- | --- |
| *x*00*n*_ srgba. csv | 6 or 7 quick transitions right away | ![Failure with 7 quick transitions](./documentation/f00n_srgba.svg) | ![Low luminance pass with 7 quick transitions](./documentation/l00n_srgba.svg) | ![Count pass with 6 quick transitions](./documentation/c00n_srgba.svg) | ![Luminance pass with a single flash in a quick sequence not above threshold](./documentation/y00n_srgba.svg) | 
| *x*r00*n*_ srgba. csv | 6 or 7 quick transitions right away (reversed polarity) | ![Failure with 7 quick transitions (reversed polarity)](./documentation/fr00n_srgba.svg) | ![Low luminance pass with 7 quick transitions (reversed polarity)](./documentation/lr00n_srgba.svg) | ![Count pass with 6 quick transitions (reversed polarity)](./documentation/cr00n_srgba.svg) | N/A | 
| *x*01*n*_ srgba. csv | Evenly spaced quick flashes | ![Failure with 4 quick, evenly-spaced flashes](./documentation/f01n_srgba.svg) | ![Low luminance pass with 4 quick, evenly-spaced flashes](./documentation/l01n_srgba.svg) | ![Count pass with 4 quick, evenly-spaced flashes](./documentation/c01n_srgba.svg) | ![Luminance pass with a single flash not above threshold out of 4 quick, evenly-spaced flashes](./documentation/y01n_srgba.svg) | 
| *x*r01*n*_ srgba. csv | Evenly spaced quick flashes (reversed polarity) | ![Failure with 4 quick, evenly-spaced flashes (reversed polarity)](./documentation/fr01n_srgba.svg) | ![Low luminance pass with 4 quick, evenly spaced flashes (reversed polarity)](./documentation/lr01n_srgba.svg) | ![Count pass with 4 quick, evenly spaced flashes (reversed polarity)](./documentation/cr01n_srgba.svg) | N/A | 
| *x*02*n*_ srgba. csv | Square wave (nearly so) | ![Failure with a square wave](./documentation/f02n_srgba.svg) | ![Low luminance pass with a square wave](./documentation/l02n_srgba.svg) | ![Count pass with a square wave](./documentation/c02n_srgba.svg) | ![Luminance pass with a single flash in a square wave sequence not above threshold](./documentation/y02n_srgba.svg) | 
| *x*03*n*_ srgba. csv | Various multi-step flashes where each step does/doesn't exceed luminance threshold (checks if alternating transitions are being counted properly) | ![Failure with multi-step flashes](./documentation/f03n_srgba.svg) | ![Low luminance pass with multi-step flashes](./documentation/l03n_srgba.svg) | ![Count pass with a multi-step flashes](./documentation/c03n_srgba.svg) | ![Luminance pass with a one multi-step flash not above threshold](./documentation/y03n_srgba.svg) | 

### Synchronicity tests

For testing the synchronicity of multiple flashing areas, patterns that start with `ff...` have a single transition that is one-frame (at 30 fps) out of sync with the corresponding `f...` pattern.
