
def convert_to_nanoseconds(s):
    nanoseconds_per_unit = {"ns": 1, "us": 1000, "ms": 1000000, "s": 1000000000, "m": 60000000000, "h": 3600000000000, "d": 86400000000000, "w": 604800000000000}
    return int(s[:-1]) * nanoseconds_per_unit[s[-1]]