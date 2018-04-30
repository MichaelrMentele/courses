Bitcoin has an extremely limited programming model. Doesn't really support 'smart contracts'.

It's too slow, only have a few operations given the stack based language.

Altcoin is a derivative coin alternative to bitcoin.

Mastercoin: created in 2012, allowed any user to create it's own currency on top of mastercoin. This was in reaction to color coins. How do you have the flexibility to do arbitrary computation?

Vitalik started bitcoin magazine?! He was excited about mastercoin, met with the team. Wanted to do more with it.

[ ] Turing complete... define this

At 19 he created a whitepaper for what Ethereum should be. Vitalik has been programming for years since he was like 10. He is a domain expert. He was ready for this.

[ ] investigate Vitalik's story/life

Ethereum implements consensus for a giant virtual computer. They use blockchain to implement a computer. Vitalik found Gavin Wood and others helped formalize the spec for ethereum.

Initial version is called Geth. Ethereum was bootstrapped via an ICO.

> Rootstock builds smart contracts on top of bitcoin

[ ] how does mining work with transactions, you have to have a lagging view or something right? ask in slack?

Sidechains basically incentivize miners to add extra behavior on top of the bitcoin protocol.

Internet of data -> Internet of value (big idea of cryptocurrencies)

Smart contracts gives first class access to value.

Current paper contracts are enforced by law. If you don't follow the contract men with guns come to the house.

What if the rules were baked into the contract? Wouldn't it be more efficient?

> THE AGREEMENT IS SELF-ENFORCING

No need for arbiters, judges, etc. to enforce the agreement but you can still use them to adjudicate.

> code is law

You could have most of the economy running on smart contracts, throw away all the current overhead (accountants, meter maids, blah) this could all be self-enforcing.

How can we bring this to market...?

## Ethereum
What does is mean that it's Turing complete? It can do arbitrary computation and anything Turing machines could do. Need loops or recursion to be Turing complete.

What is a Turing machine? An infinite tape with read/write to the tape. The other model is called lambda calculus.

What is lambda calculus? Lisp is the first implementation.

Turing formalized infinite Turing machines as the Halting Problem.

`F(source_code) returns T/F if the program is infinite.` This is proof there is no program that can determine if a program will halt (for all programs)

[ ] turing is amazing, look into his life

Two building blocks:
1. accounts
  1. externally owned account (EOA) --> basically a user
    - nonce stored within them
  2. contract accounts --> first class citizens, just like EOA's
    - contracts have code
    - have data stored within them
2. transactions
  1. contract call (invocation)
  2. contract deployment
  3. ether transfer

BusyBeaver Function--how do you find BusyBeaver numbers?

To limit computation you use Gas (ethereum), gas is how you pay for EVM opcodes to be performed.

Gasprice is the conversion of ethereum to gas.

You want them separate so that the gas price is fixed, then you can decouple network load. Decouples program complexity from network load.

> Ether was not meant to be money, it is a commodity that can be exchanged fro utility

Ether is a side effect of building a global world computer. There are some big competitors with Ether.

An VM separates you from teh native OS. But this allows you to be platform agnostic.

The EVM is a stack based virtual machine. Has memory and disk storage. You have first calss action to the block chain

Can you have a multichain, chain?

Solidity is the most popular language. Vitalik is writing a new language called Vyper.

Ethereum stores all of it's data in a Patricia Merkle Trie. There are three merkle trees:
1. state
2. accounts
3. reciepts

State tree is the state of accoutns (both EOA and contracts).

contracts store:
- code
- storage
- balance

EOA store
- balance
- nonce

Why do accounts need a nonce? So you can uniquely identify a transaction and prevent replay attacks.

[ ] tradeoffs between utxo and account based state

When you update the tree, you re-merkelize the tree and now you have a new state root that encapsulates the state of the entire EVM. That's amazing.

This is very different from the accounting system in Bitcoin where you have a more functional style state machine.

Transactions describe the diffs that led to the change in the state tree.

When you update these three trees, you have your new block header:
- previous_hash
- your address
- state root
- transaction root
- reciepts root
=> need to compute a nonce from this

# Mining
Block size is not limited in Ethereum, it's gas constrained, whereas in Bitcoin we are space constrained (bytes).

You have a mempool and you try to maximize the amount of transactions you can fit into the block.

Once they are selected you execute the transactions on the EVM.

[ ] How do miners determine the gas limit on a block

What is frontrunning? You see someone's transaction fee and then you jump in front of them by offering a higher fee. You might want to do this to get a contract in front of someone else.

Miner's can still frontrun and reorder transactions (unless they are from the same account)

Why doesn't ordering matter in bitcoin? Because payments in bitcoin are communative, there is no difference in order...

But EVM transactions aren't communative.

Haseeb, frontrunning attack on bancor.

# CPU Hard vs. Memory Hard
What is CPU hard vs memory hard? If you use SHA256 that's CPU hard due to the operations used--really this is computationally hard.

What is memory hard? Scrypt is a popular hashing algorithm, requires a lot of memory. You can't specialize further with memory. So everyone can compete, you can't buy specialized hardward for computation.

Ethereum invented its own hashing algorithm, called dagger Hashimoto

# stats
- 2 minute finality
- 10 second blocks

Ghost protocol:
consensus is chosen by the chain with the most work that has been done on it. don't discard work (even on orphan blocks)--in ehtereum the orphan is called an 'uncle' block

Pays up to 12.5% to uncle miner--called ommers in the protocol

We are moving to a world of bounties? DAO's?
