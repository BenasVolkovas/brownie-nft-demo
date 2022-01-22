from scripts.helpful_scripts import get_account
from brownie import SimpleCollectable

# https://ipfs.io/ipfs -> ipfs://
SAMPLE_TOKEN_URI = "https://ipfs.io/ipfs/QmWRVLtexfHBXHTPa1RB1zBvpnUtpaE23J82p5q4b9Zcdy?filename=corgi.json"
OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"


def deploy_and_create():
    account = get_account()
    simpleCollectable = SimpleCollectable.deploy({"from": account})
    tx = simpleCollectable.createCollectable(SAMPLE_TOKEN_URI, {"from": account})
    tx.wait(1)
    print(
        f"You can view your NFT at {OPENSEA_URL.format(simpleCollectable.address, simpleCollectable.tokenCounter()-1)}"
    )

    return simpleCollectable


def main():
    deploy_and_create()
