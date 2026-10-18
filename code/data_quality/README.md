# Data quality

Planned responsibility: detect issues before records enter analytical storage.

## Initial checks to define

- required fields and expected data types by notice type;
- duplicate source identifiers;
- date parsing and date-window consistency;
- currency and amount validity where award values are present;
- missingness rates for key dimensions;
- valid code formats for CPV and geographic identifiers;
- traceable links between notices and award notices.

Missing or unavailable values must not be silently replaced with zero. Rules should report counts and examples without exposing secrets or unnecessary personal data.

No automated checks are implemented yet.
