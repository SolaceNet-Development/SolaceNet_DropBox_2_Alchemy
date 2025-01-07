from dropbox_integration import upload_to_dropbox
from alchemy_integration import web3
from erc20_utils import get_usdt_balance
from crypto_host import send_to_crypto_host

def main():
    # Example wallet address
    wallet_address = "0xYourWalletAddress"
    usdt_contract_address = "0xF48EF396AFcF359c42C7388b833fE0eC31f7822E"

    # Fetch USDT balance
    balance = get_usdt_balance(web3, wallet_address, usdt_contract_address)
    print(f"USDT Balance: {balance}")

    # Upload a file to Dropbox
    upload_to_dropbox("example.txt", "/example.txt")

    # Send a file to the Crypto Host
    status, response = send_to_crypto_host("example.txt")
    print(f"Crypto Host Response: {status} - {response}")

if __name__ == "__main__":
    main()
