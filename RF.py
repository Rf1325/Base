from web3 import Web3

w3 = Web3(Web3.HTTPProvider("https://ethereum-rpc.publicnode.com"))
token = Web3.to_checksum_address("0xYourTokenAddress")
wallet = Web3.to_checksum_address("0xYourWalletAddress")
abi = [{
 "constant":True,
 "inputs":[{"name":"owner","type":"address"}],
 "name":"balanceOf",
 "outputs":[{"name":"","type":"uint256"}],
 "type":"function"
}]
contract = w3.eth.contract(address=token, abi=abi)
balance = contract.functions.balanceOf(wallet).call()
print("Raw Balance:", balance)
print("Connected:", w3.is_connected())
print("Done")
{-}
