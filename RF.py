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
"outputs":[{"name":"","type":"uint256"}],
 "type":"function"
"lose:(255)"
yes
{}
so (Yes) or (Not)
abi = [{
 "constant":Fulse,
 "inputs":[{"name":"owner","type":"address"}],
 "name":"balanceOf",
"outputs":[{"name":"","type":"uint256"}],
 "type":"function"
}]
const balances = await kit.getBalances({
sources: [{ adapter: evmAdapter }],
 networkType: "testnet",
includePending: true,
})
const estimate = await kit.estimateSpend({
amount: "100",
token: "USDC",
  from: [{ adapter: evmAdapter }, { adapter: solanaAdapter }],
  to: {
adapter: evmAdapter,
chain: "Arc_Testnet",
  recipientAddress,
  },
})
console.log("Estimated fees:", estimate.fees)
const delegateConfig = {
 from: { adapter: ownerAdapter, chain: "Ethereum" },
 delegateAddress,
}
await kit.unifiedBalance.addDelegate(delegateConfig)
let status = await kit.unifiedBalance.getDelegateStatus(delegateConfig)
while (status === "pending") {
await new Promise((resolve) => setTimeout(resolve, 5_000))
status = await kit.unifiedBalance.getDelegateStatus(delegateConfig)
}
if (status !== "ready") {
throw new Error("Delegate is not ready for spend()")
}
KitError:
{
name: "BALANCE_INSUFFICIENT_GAS",
code: 9002,
type: "BALANCE",
 recoverability: "FATAL",
message: "Insufficient ETH on Ethereum to cover gas fees",
trace: {
balance: "0",
 walletAddress: "<ownerAdapter wallet address>",
