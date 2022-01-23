import imp
from webbrowser import get
from brownie import AdvancedCollectible
from scripts.helpful_scripts import fund_with_link, get_account
from web3 import Web3


def create_collectible():
    account = get_account()
    advancedCollectible = AdvancedCollectible[-1]
    fund_with_link(advancedCollectible.address, amount=Web3.toWei(0.1, "ether"))
    creationTx = advancedCollectible.createCollectible({"from": account})
    creationTx.wait(1)
    print("Collectible created.")


def main():
    create_collectible()
