from pathlib import Path
from metadata import clone_to_metadata
import os
import requests

PINATA_BASE_URL = "https://api.pinata.cloud"
PIN_FILE_ENDPOINT = "/pinning/pinFileToIPFS"
HEADERS = {
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_secret_api_key": os.getenv("PINATA_API_SECRET"),
}


def upload_to_pinata(filepath, cloneType):
    with Path(filepath).open("rb") as fp:
        imageBinary = fp.read()
        filename = filepath.split("/")[-1]

        response = requests.post(
            PINATA_BASE_URL + PIN_FILE_ENDPOINT,
            files={"file": (filename, imageBinary)},
            headers=HEADERS,
        )
        ipfsHash = response.json()["IpfsHash"]
        imageUri = f"https://ipfs.io/ipfs/{ipfsHash}?filename={filename}"
        print(imageUri)

        if filename[-5:] == ".json":
            clone_to_metadata[cloneType] = imageUri
        
        return imageUri


def main():
    upload_to_pinata()
