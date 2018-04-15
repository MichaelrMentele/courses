# (1845) Gossip + Cryptography
- symmetric cryptology uses the same key for both sides of the equation
- asymmetric is public/private keys
- digital sigs must be hard to break, tied to some data, and easy to verify, non-transferable
- amazing we can do this all with fucking math! fascinating
- for dig keys need to generate, sign, and verify
- hash first, so that the verification is cheap (hash the content)
- ECDSA relies on the discrete logarithm problem
- the atoms in the universe is 2^260 ???
- how do you choose your eliptic curves?
- ECDSA should be able to be broken by quantum computers
- why does bitcoin hash your public key?
- break hashing fn:
  - collision attack try to find two inputs with same output
  - you can find a collision in 2^sqrt(hash_size)
- bitcoin uses sha2
- hashcash: pay for sending packets over the web
- hashcash very important pre-cursor to bitcoin

[ ] what is a digital signature?
[ ] what are the properties of a digital signature?
[ ] what functions do you need for a digital sig scheme?
[ ] how does RSA work?
[ ] why is hashing cheaper than encrpytion
[ ] what are trapdoor functions?
[ ] what is an example of a trapdoor function?
[ ] what is the other asymmetric algorithm besides RSA? How does it compare?
[ ] what MUST a hashing algorithm have (in general) as props?
[ ] what props should a cyrptographic hashing algo have?
[ ] what is an example hash function?
[ ] what is the avalanching effect?
[ ] how can you break a hashing function?
[ ] what is a collision attack?
[ ] what is a birthday attack?
[ ] what is a pre-image attack?
[ ] what is 2nd pre-image resistance?
[ ] what is iterative hashing?
[ ] dig into Hashcash
[ ] create hashcash minter and hash cash verifier
[ ] what is a merkle tree? What are the advantages?
[ ] what is proof of inclusion?
