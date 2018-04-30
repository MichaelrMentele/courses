# Gossip Homework
## Bitcoin and Cryptocurrencies
### 3.5 The Bitcoin Network
What is a gossip protocol? This is a protocol that 'floods' the network by asking all known peers for a piece of information or telling all known peers about a piece of information.
How does a node decide whether to propogate a transaction? If the transaction is valid (determined by checking inputs/outputs and checking signatures) then it will typically propogate a transaction.
what is a zero confirmation transaction? You don't confirm the transaction at all, because you want to prevent the double spend issue, so if you just take the first one and ignore the next transaction where the same asset is spent then they can't doublespend.
what is replace by fee? this means that validating nodes have the option to replace a transaction of there is another transaction with a higher fee.

## Architecture of Peer to Peer Systems
### Chapter 2
What is grid computing? This is the idea of a system of computers linked over a network working together to act as a super computer
What is an overlay network? A network built on top of another network so you can decouple network infraastructure from services
what is overlay topology? This is how nodes are organized at the meta level. So nodes in the overaly network might have a flat or hierarchechal relationship
What is a centralized p2p system? This is where a list of peers is kept in some central store and once you get started you largely interact with the network on a P2P basis
What are the advantages and disadvatages of a centralized p2p system? The advantage is you can be more efficient in how you are organized. You could have a registry as well for the ditributed hash table that describes data held by the nodes in a network. Otherwise you can have inefficiencies in time and bandwidth blindly asking the network for where to find or send data
What are adv/disadvantages of decentralized p2p system? The disadvantage is you trade knowledge of the system for flexibility of the system. So if you have a fixed centralized server you can store knowledge about the network in that central server. However, than this can become a bottleneck or fault area in case this server goes down. There is also a concentration of power, a malicious user could mislead nodes in the network. You have an uneven distribution of trust and powewr.
What are the tradeoffs of a flat topology vs. hierarchechal topology? This is like the question above but scaled out, you could have many 'master' nodes that handle high level orchestraton resulting in a more effiecient system. But the high nodes have extra trust and more power. A flat topology lessens the opportunity for abuse but is less efficient.
What are the first unstructured p2p systems? Gnutella I think, as well as tor
What are strategies for finding resources in a flat p2p network? Gossip protocol (ask everyone) or unicast (ask someone and see if they can help pdirect you) this is a gradient where you could do some level of multi cast.
What is SETI? Why did it fail? SETI is one of the first decentralized forms of payments. It failed due to usability issues. They issued coins in fixed denominations and then it was painful for merchants to use and users becuase everyone needed RSA keys which the lay person knows nothing about.
What is Napster? Why did it fail? It was a peer-to-peer file sharing internet service primarily sharing music. It failed because it head a centralized p2p model and once the head of the snake was removed the protocol failed. This was attacked due to percieved copyright infringement.

### 2.3 p2p networks
TODO
What is an unstructured p2p network?
What is a structured p2p network?
What are the difficulties Gnutella networks faces when scaling?
What is a chord ring?
What is tha advantages of a hierarchechal DHT?
What is data locality?
Why does hashing destroy it?
What is a skip list?
What is a probalistic based structured network overlay for P2p networks?
What is a skip graph?
What are hybrid p2p systems?
What is BestPeer?
What is onion routing?

# (1000) Crypto Class on Gossip
A lot of better P2P systems were unused because academia responded to existing systems.

Interesting to consider DNS as a network. This would be good to learn more about.
- need to follow up on this
- direct democracy in switzerland...???
- bit torrent is worth studying?
- weak on graphs, how to find nearest k neighbors?
- fasttrack or kazaa? what is this
- reverse IP lookups
- what is defimity? a crypto network
- what is the napster reboot? rhapsody

Seems like hybrid network is incredibily useful for any meaningful amount of impact.

Why is there a long winter of P2P networks? It lead people to getting content on demand and then when companies created better services. Stigma on P2P due to 'stink' on the system.

What is the advantage of a centralized network? There is more consistency to the network, there is more efficieny in the network.

Interesting, blockchain is basically a semi structured network because of miners verifying data. They are rewarded for their extra work. Why can't we slap this idea on top of TOR?

This iis the major challenge... how can creators of the network make money from the market?

Could a free p2p network fro sharing content for cheapness? You could have content filter through like movie theaters, netflix, then some cheapo network where content is now ridiculously cheap.

The problems with napster were mostly:
1. single point of failure
2. no security around content

The nice part is the speed for looking up files is great :D

What is an infection factor? THe number of nodes you are sending to.

Gossip protocol doesn't broadcast to everyone but it has a multicast system. Flooding is to everyone. You have some randomity around gossip protocol.

Moving on to Gnutella who did a fully p2p architecture. Five diffent message types:
1. query
2. query hit
3. ping
4. pong
5. push - initiate transfer

How do you dedup queries? You can have a cache of messages you've seen before. Each message you have should have a UUID in case the querier is retrying.

In Gnutella you don't use the IP address directly. You obfusicate the IP. You could still try and find someone but you'd have to run around the whole network.

- how does nat hole punching work?
- look up self organizing and self electiing 'republics'
- graphs, graphs, graphs!
- what is a spanning tree?
- what is an eclipse attack?

It like a village network, do you want everyone to just be an unspecialzed laborer.

What is a gossip protocol? Basically just multicast. Wifi is broadcast.

- how did haseeb approach and ramp up on all fo ths?
- why the interest in this space?

What are the two kinds of gossipping system? poll vs. push
What are the properties of gossip protocol?
1. lowish latency to reach half the network
2. fault tolerant

Gossip protocols was mostly used in sensor netowkrs and also is used often in the interent and distributed DBs and crypto.

Why is gossip good for bitcoin?
1. everyone wants to see the same data (blockchain)
2. fault tolerance
3. speed of propagation

summary:
pure p2p networks can hold their own from not getting killed and not getting censored

## Questions
[ ] need to follow up on this
[ ] direct democracy in switzerland...???
[ ] bit torrent is worth studying?
[ ] weak on graphs, how to find nearest k neighbors?
[ ] fasttrack or kazaa? what is this
[ ] reverse IP lookups
[ ] what is defimity? a crypto network
[ ] what is the napster reboot? rhapsody
[ ] how does nat hole punching work?
[ ] look up self organizing and self electiing 'republics'
[ ] graphs, graphs, graphs!
[ ] what is a spanning tree?
[ ] what is an eclipse attack?
[ ] how did haseeb approach and ramp up on all fo ths?
[ ] why the interest in this space?
[ ] how does the ethereum VM work with ethereum implementations?
[] answer questions written down in bradfield blockchain facts.md
[ ] summarize and elaborate on p2p networks, the history of them, the tradeoffs of them etc. in a blog post / article or other proof
