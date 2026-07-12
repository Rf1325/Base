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
   chain: "Ethereum",
  },
}
import { createViemAdapterFromProvider } from "@circle-fin/adapter-viem-v2";
const adapter = await createViemAdapterFromProvider({
  provider: window.ethereum,
});
// Swap: percentage-based
config: { customFee: { percentageBps: 50, recipientAddress: "0xYourWallet" } }

// Bridge and Unified Balance spend: absolute value
config: { customFee: { value: "0.10", recipientAddress: "0xYourWallet" } }
const result = await kit.swap({
  from: { adapter, chain: "Arc" },
  tokenIn: "USDT",
  tokenOut: "USDC",
  amountIn: "1.00",
  config: { kitKey: process.env.KIT_KEY },
});
const estimate = await kit.estimateSwap({
  from: { adapter, chain: "Arc" },
  tokenIn: "EURC",
  tokenOut: "USDC",
  amountIn: "1.00",
  config: { kitKey: process.env.KIT_KEY },
});
console.log(estimate.estimatedOutput.amount, estimate.stopLimit.amount);
// Cross-chain: swap USDC on Ethereum, receive on Base at a specific wallet
const result = await kit.swap({
  from: { adapter, chain: "Ethereum" },
  tokenIn: "USDC",
  tokenOut: "USDC",
  amountIn: "100",
  to: { chain: "Base", recipientAddress: "0xRecipient" },
  config: { kitKey: process.env.KIT_KEY },
});
const final = await kit.waitForSwap({ result, kitKey: process.env.KIT_KEY });
const result = await kit.swap({
  from: { adapter, chain: "Arc" },
  tokenIn: "USDT",
  tokenOut: "USDC",
  amountIn: "1.00",
  to: { recipientAddress: "0xDifferentWallet" },
  config: { kitKey: process.env.KIT_KEY },
});
const result = await kit.swap({
  from: { adapter, chain: "Arc" },
  tokenIn: "USDT",
  tokenOut: "USDC",
  amountIn: "1.00",
  to: { recipientAddress: "0xDifferentWallet" },
  config: { kitKey: process.env.KIT_KEY },
});
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
    chain: "Ethereum",
  },
}
import { AppKit, KitError } from "@circle-fin/app-kit"
const kit = new AppKit()
try {
  const result = await kit.unifiedBalance.spend(params)
  console.log("Success:", result.txHash)
} catch (error) {
  if (
    error instanceof KitError &&
    error.recoverability === "RESUMABLE" &&
    error.cause?.trace
  ) {
    const { attestation, signature } = error.cause.trace as {
