import json

def print_json(data):
    """"Function that will print a dictionary or list in an easy to read format."""
    json_formatted = json.dumps(data, indent=2, sort_keys=True)
    print(json_formatted)

def flatten(l):
    """Returns a list without sublists"""
    return [item for sublist in l for item in sublist]
