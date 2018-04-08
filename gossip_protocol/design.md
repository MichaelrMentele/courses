# Suggested strategy:
* Start by defining your message format (write out some example messages)
* Figure out the state that each node needs to hold
* Write up your message update logic—upon receiving a gossip message, how do you update your view of the world? You should be able to run this on your example message and get a correct state transition.
* Then write a little UI code so you can easily inspect what each node is doing.
* Then write your networking and gossip logic, and test across multiple nodes!

NOTE: Observing and debugging distributed systems can be hard. I recommend investing in your UI: try adding some colors and an organized table to display your state for each node. It'll make debugging a lot easier.

# Message Format
* UUID (for deduplication)
* Originating port (your identity)
* Version number
* TTL
* Payload

{
  uuid: 'asdijfaojf3232',
  address: '196.18.1.0'
  port: '80'
  ttl: 4 # decremented each time it is forwarded
  payload: 'bookname'
}

# Information on the UI
We should display:
1. what the current node thinks the global state is (what the favorite books are)
2. what the list of peers is, what their names are, or ports are

activity
current messages

books table
node name | node port | favorite book
----------+-----------+--------------
jimmy     | 81        | gatsby
----------+-----------+--------------
tod       | 82        | blah

etc.

# Testing
1. we might want some kind of 'god' project that can 'freeze' all the running processes at once
2. we are going to want some process management anyway, to add and kill processes as we go, so we need some code that creates new nodes on demand, I'm not quite sure how to bootstrap--we have two options here, we should be able to pass in a port via a command util--so I can manually manage the project, the other approach would be... to have this automated
3. but basically for the use case I want to do something like...

`watercooler new jimmy:81`

# Approach
There are three components:
1. the flask servers
  a. periodic update per server
  b. gossip logic
  c. serve react client
2. cli
  a. create new nodes
  b. stop all processes

1. How do I manage multiple flask processes?
2. What logic should I have to implement the features of a gossip protocol
