import json


def parse_json(json_file_name):
    with open(json_file_name) as json_file:
        data = json.load(json_file)

    timeline_segment = []
    for timeline_object in data.get('timelineObjects'):
        segment = timeline_object.get("activitySegment")
        timeline_segment.append({
            "startLocation": segment.get("startLocation"),
            "startTime": segment.get("duration").get("startTimestampMs"),
            "endLocation": segment.get("endLocation"),
            "endTime": segment.get("duration").get("endTimestampMs"),
            "activityType": segment.get("activityType"),
            "waypointPath": segment.get("waypointPath")})

    return timeline_segment


if __name__ == '__main__':
    parse_json("2020_JANUARY.json")