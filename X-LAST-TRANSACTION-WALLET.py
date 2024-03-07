import requests
import json

def get_last_30_transaction_hashes(api_key, wallet_address):
    base_url = f"https://api.etherscan.io/api?module=account&action=txlist&address={wallet_address}&sort=desc&apikey={api_key}&page=1&offset=30"
    response = requests.get(base_url)
    data = json.loads(response.text)
    if 'status' in data and data['status'] == "1":
        transactions = data['result']
        transaction_hashes = [tx['hash'] for tx in transactions]
        return transaction_hashes
    else:
        print("Error:", data['message'])
        return []

# usage
api_key = 'J1Z5DPIB2NHUUEMJ9TP39DW76IBWCXTP37'
wallet_address = '0x220AbCDCF39882B4a7380ac50bb4e47b3C379e8a'
transaction_hashes = get_last_30_transaction_hashes(api_key, wallet_address)

print(transaction_hashes)
