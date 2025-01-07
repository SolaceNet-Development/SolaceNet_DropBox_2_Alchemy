ERC20_ABI = [
    # Minimal ERC20 ABI
    {"constant": True, "inputs": [{"name": "_owner", "type": "address"}], "name": "balanceOf", "outputs": [{"name": "balance", "type": "uint256"}], "type": "function"},
    {"constant": True, "inputs": [], "name": "decimals", "outputs": [{"name": "", "type": "uint8"}], "type": "function"},
    {"constant": True, "inputs": [], "name": "symbol", "outputs": [{"name": "", "type": "string"}], "type": "function"},
    {"constant": True, "inputs": [], "name": "name", "outputs": [{"name": "", "type": "string"}], "type": "function"}
]

def get_usdt_balance(web3, wallet_address, contract_address):
    try:
        contract = web3.eth.contract(address=contract_address, abi=ERC20_ABI)
        balance = contract.functions.balanceOf(wallet_address).call()
        decimals = contract.functions.decimals().call()
        return balance / (10 ** decimals)
    except Exception as e:
        raise Exception(f"Failed to get balance: {str(e)}")

def get_token_info(web3, contract_address):
    contract = web3.eth.contract(address=contract_address, abi=ERC20_ABI)
    try:
        symbol = contract.functions.symbol().call()
        name = contract.functions.name().call()
        decimals = contract.functions.decimals().call()
        return {"symbol": symbol, "name": name, "decimals": decimals}
    except Exception as e:
        raise Exception(f"Failed to get token info: {str(e)}")
