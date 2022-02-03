from brownie import network, AdvancedCollectible
from scripts.helpful_scripts import OPENSEA_URL, get_account, get_clone_type
import json


def set_token(tokenId, nftContract, tokenURI):
    account = get_account()
    tx = nftContract.setTokenURI(tokenId, tokenURI, {"from": account})
    tx.wait(1)
    print(f"Awesome! View NFT at {OPENSEA_URL.format(nftContract.address, tokenId)}")
    print("Please wait up to 20 minutes and refresh metadata")


def set_token_uri():
    print(f"Working on {network.show_active()}")
    advancedCollectible = AdvancedCollectible[-1]
    numberOfCollectibles = advancedCollectible.tokenCounter()
    print(f"Currently have {numberOfCollectibles} collectibles")

    cloneToMetadata = open("./metadata/clone_to_metadata.json", "r")
    data = json.load(cloneToMetadata)

    for tokenId in range(numberOfCollectibles):
        cloneType = get_clone_type(advancedCollectible.tokenIdToClone(tokenId))

        if not advancedCollectible.tokenURI(tokenId).startswith("https://"):
            print(f"Setting tokenURI of {tokenId}")
            set_token(tokenId, advancedCollectible, data[cloneType])


def main():
    set_token_uri()
