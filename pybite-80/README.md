Get to know pytz! pytz brings the Olson tz database into Python (docs). Let's see how many hours Bob and Julian have to bridge in order to deliver you PyBites. It differs depending on whether it's Winter or Summer in their relative hemispheres.

Complete the what_time_lives_pybites function which receives a naive / not timezone aware datetime object:

There are two kinds of date and time objects: naive and aware: an aware object has sufficient knowledge of applicable algorithmic and political time adjustments, such as time zone and daylight saving time information, to locate itself relative to other aware objects. An aware object is used to represent a specific moment in time that is not open to interpretation. - docs

First convert the passed in naive_utc_dt to a aware datetime, then convert it to AUSTRALIA and SPAIN localized datetimes returning them in a tuple. For a bit more advanced pytz Bite try Bite 73 ...

Have fun and keep coding in Python!

