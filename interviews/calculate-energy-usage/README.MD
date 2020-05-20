# calculate-energy-usage

Input readings structure is translated into `Member`, `Account` and `Reading` composite objects which are defined in `readings.py`. Lookup of individual Readings in an Account at runtime is implemented with a multi-value tuple being used as a dictionary key (this is sometimes called a composite-key dict). Some additional helper functions are also present in for potential use in later challenge stages.

Gas bill calculation based on https://www.gov.uk/guidance/gas-meter-readings-and-bill-calculation

# Issues

- I was unable to ask more questions about the challenge requirements over the weekend, and so there is a fine amount of guesswork in the solution :) I was uncertain whether `tariff.py` denominates all prices per unit of kWh regardless of fuel type, as only the electricity price is commented with instructions. My solution assumed that all rates are per kWh. Tests have been omitted entirely in the current version due to uncertainty around correct final bill price in pounds. Possible misunderstanding of tariff calculation on my part. To be fixed/discussed with interviewer, as by the time I was able to contact Bulb, the challenge timer was already running out.
- `README.MD` appears to be missing from original zip file, whereas it appears mentioned as present on the challenge's description on the website. I was unsure whether to infer that other files are also missing - i.e. input gas readings, which I have coded my solutions around their lack, but still under the assumption that they should be there under a `gas` key.

# TODO

- Implement better logging - currently, we cannot change our arg parser file to handle --verbosity due to challenge restrictions.
- Handle more exceptions, inputs, edge cases and out-of-memory errors.
