import json


def main():
    with open("./metadata/clone_to_metadata.json", "r") as jsonFile:
        data = json.load(jsonFile)
        print(data)
