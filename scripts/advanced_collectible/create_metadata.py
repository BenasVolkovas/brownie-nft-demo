from curses import meta
from brownie import AdvancedCollectible, network
from scripts.helpful_scripts import get_clone_type
from metadata.sample_metadata import metadataTemplate

# from pathlib import Path


def create_metadata():
    advancedCollectible = AdvancedCollectible[-1]
    numberOfCollectibles = advancedCollectible.tokenCounter()
    # print(f"Have created {numberOfCollectibles} collectibles")

    # for tokenId in range(numberOfCollectibles):
    #     cloneType = get_clone_type(advancedCollectible.tokenIdToClone(tokenId))
    #     metadataFileName = (
    #         f"./metadata/{network.show_active()}/{tokenId}-{cloneType}.json"
    #     )

    #     # if Path(metadataFileName).exists():
    #     #     print(f"{metadataFileName} already exists! Delete it to overwrite.")
    #     # else:
    #     #     print(f"Creating metadata file: {metadataFileName}")


def main():
    create_metadata()
