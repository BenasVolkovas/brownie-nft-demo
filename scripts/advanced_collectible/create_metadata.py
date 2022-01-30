from brownie import AdvancedCollectible, network
from scripts.helpful_scripts import get_clone_type
from metadata.sample_metadata import metadataTemplate
from pathlib import Path
import requests
import json
import os

cloneToImageUri = {
    "DRAGON": "https://ipfs.io/ipfs/QmUR5wDiKfSVgMg7w1dq6uZPHxfmQ72F5sPKCJg6HqdZkF?filename=dragon.png",
    "SPY": "https://ipfs.io/ipfs/QmPHxyT344dTCmA3fJvVz5LBKx8FqQdhLtpHYLVFZmG1HT?filename=spy.png",
    "PRISONER": "https://ipfs.io/ipfs/QmNbpZvmCyb39zXSG1yn7DeqjZqgEUKewgqpWZi5Lbndyf?filename=prisoner.png",
}


def create_metadata():
    advancedCollectible = AdvancedCollectible[-1]
    numberOfCollectibles = advancedCollectible.tokenCounter()
    print(f"Have created {numberOfCollectibles} collectibles")

    for tokenId in range(numberOfCollectibles):
        cloneType = get_clone_type(advancedCollectible.tokenIdToClone(tokenId))
        metadataFileName = (
            f"./metadata/{network.show_active()}/{tokenId}-{cloneType}.json"
        )
        collectibleMetadata = metadataTemplate

        if Path(metadataFileName).exists():
            print(f"{metadataFileName} already exists! Delete it to overwrite.")
        else:
            print(f"Creating metadata file: {metadataFileName}")
            collectibleMetadata["name"] = cloneType
            collectibleMetadata["description"] = f"Powerful {cloneType} clone."

            # Upload image to ipfs
            imagePath = f"./img/{cloneType.lower().replace('_', '-')}.png"

            # Don't actually need to use it. Only makes code little faster
            if os.getenv("UPLOAD_IPFS") == "true":
                imageUri = upload_to_ipfs(imagePath)
            else:
                imageUri = cloneToImageUri[cloneType]

            collectibleMetadata["image"] = imageUri

            # Dump all metadata to its own file
            with open(metadataFileName, "w") as file:
                json.dump(collectibleMetadata, file)

            # Upload metadata to ipfs
            if os.getenv("UPLOAD_IPFS") == "true":
                upload_to_ipfs(metadataFileName)


def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        imageBinary = fp.read()
        ipfsUrl = "http://127.0.0.1:5001"
        endpoint = "/api/v0/add"
        response = requests.post(ipfsUrl + endpoint, files={"file": imageBinary})
        ipfsHash = response.json()["Hash"]
        filename = filepath.split("/")[-1]
        imageUri = f"https://ipfs.io/ipfs/{ipfsHash}?filename={filename}"
        print(imageUri)

        return imageUri


def main():
    create_metadata()
