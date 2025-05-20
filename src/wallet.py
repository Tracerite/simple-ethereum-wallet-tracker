import json
import time
import os
from web3 import Web3
from utils import validate_address, resolve_ens

class WalletTracker:
    def __init__(self):
        self.wallets = []

        # Load config
        config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'settings.json')
        with open(config_path) as f:
            config = json.load(f)

        network = config.get("network", "mainnet")
        infura_key = config["api_keys"].get(network)
        if not infura_key:
            raise ValueError("Missing Infura key for the selected network")

        self.w3 = Web3(Web3.HTTPProvider(f"https://{network}.infura.io/v3/{infura_key}"))

    def add_wallet(self, address_or_ens):
        address = resolve_ens(address_or_ens) if address_or_ens.endswith(".eth") else address_or_ens
        if not validate_address(address):
            raise ValueError("Invalid address")
        self.wallets.append(address)
        return f"Added wallet: {address}"

    def batch_add_wallets(self, addresses):
        valid_addresses = [addr for addr in addresses if validate_address(addr)]
        self.wallets.extend(valid_addresses)
        return f"Added {len(valid_addresses)} wallets"

    def get_balance(self, address):
        if self.w3.is_connected():
            balance = self.w3.eth.get_balance(address)
            return self.w3.from_wei(balance, "ether")
        return 0.0

    def get_token_balance(self, address, token_contract):
        contract = self.w3.eth.contract(address=token_contract, abi=[
            {
                "constant": True,
                "inputs": [{"name": "_owner", "type": "address"}],
                "name": "balanceOf",
                "outputs": [{"name": "balance", "type": "uint256"}],
                "type": "function"
            }
        ])
        balance = contract.functions.balanceOf(address).call()
        return self.w3.from_wei(balance, "ether")

    def save_balance_history(self, address):
        balance = self.get_balance(address)
        history = {
            "timestamp": time.time(),
            "address": address,
            "balance": balance
        }

        history_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'history.json')
        try:
            with open(history_file, "r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        data.append(history)
        with open(history_file, "w") as f:
            json.dump(data, f, indent=2)

        return history

# Doc comment 62



# Doc comment 90




