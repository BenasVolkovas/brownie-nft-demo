from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_account,
)
from scripts.advanced_collectible.deploy_and_create import deploy_and_create
from brownie import network, AdvancedCollectible
import pytest
import time


def test_can_create_advanced_collectible_integration():
    # Arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for integration testing")

    # Act
    account = get_account()
    advancedCollectible, creationTx = deploy_and_create()
    time.sleep(1500)  # 25 minutes
    # Assert
    assert advancedCollectible.tokenCounter() == 1
