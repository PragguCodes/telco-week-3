

import json

# your full JSON string here
json_data = """
{
    "location1": {  
        "latitude": 25.625,
        "longitude": -80.20833,
        "generationtime_ms": 0.14674663543701172,
        "utc_offset_seconds": 0,
        "timezone": "GMT",
        "timezone_abbreviation": "GMT",
        "elevation": 1.0,
        "hourly_units": {
            "time": "iso8601",
            "wave_height": "m"
        },
        "hourly": {
            "time": ["2025-12-04T00:00", "2025-12-04T01:00"],
            "wave_height": [0.18, 0.18]
        }
    },
    "location2": {
        "latitude": -34.041668,
        "longitude": 151.29167,
        "generationtime_ms": 0.027298927307128906,
        "utc_offset_seconds": 0,
        "timezone": "GMT",
        "timezone_abbreviation": "GMT",
        "elevation": 0.0,
        "hourly_units": {
            "time": "iso8601",
            "wind_speed_10m": "undefined"
        },
        "hourly": {
            "time": ["2025-12-04T00:00", "2025-12-04T01:00"],
            "wind_speed_10m": [null, null]
        }
    }
}
"""

# convert JSON string → Python dict
nested_dict = json.loads(json_data)

# print nicely (line-by-line)
print(json.dumps(nested_dict, indent=4))
