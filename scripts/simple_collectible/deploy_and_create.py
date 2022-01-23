from scripts.helpful_scripts import get_account, OPENSEA_URL
from brownie import SimpleCollectible

# https://ipfs.io/ipfs -> ipfs://
SAMPLE_TOKEN_URI = "https://ipfs.io/ipfs/QmWRVLtexfHBXHTPa1RB1zBvpnUtpaE23J82p5q4b9Zcdy?filename=corgi.json"


def deploy_and_create():
    account = get_account()
    simpleCollectible = SimpleCollectible.deploy({"from": account})
    tx = simpleCollectible.createCollectible(SAMPLE_TOKEN_URI, {"from": account})
    tx.wait(1)
    print(
        f"You can view your NFT at {OPENSEA_URL.format(simpleCollectible.address, simpleCollectible.tokenCounter()-1)}"
    )

    return simpleCollectible


def main():
    deploy_and_create()
