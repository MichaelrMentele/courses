# Merkle tree exercise
#
# * Generate a Merkle tree given the following body of data, using SHA-256 as your hashing algorithm
#   - Your data is the following blocks:
#   - "We", "hold", "these", "truths", "to", "be, "self-evident", "that"
# * In the internal stages, concatenate blocks as `hash("#{blockA}||#{blockB}")`
# * Do not use any special padding for leaf vs internal nodes
# * The merkle root in hex output should be equal to `4a359c93d6b6c9beaa3fe8d8e68935aa5b5081bd2603549af88dee298fbfdd0a`
#
# Bonus: create a padding scheme so that arbitrary numbers of blocks can be Merkleized.
#
# Bonus 2: add different padding to the leaves as opposed to internal nodes, so that preimage attacks are impossible.
#
# Bonus 3: implement an interface for Merkle proofs. Have a `generate_proof(block)` method and a `verify_inclusion(block, proof)` method.

require 'digest'

class Node
  attr_accessor :datum, :children, :parent

  def initialize(datum, children: nil)
    self.parent = nil
    self.datum = datum
    self.children = []
  end

  def add_children(new_children)
    self.children += new_children
    new_children.each do |child|
      child.parent = self
    end
  end

  def to_s
    "hash: #{self.datum}"
  end
end

class MerkleTree
  def self.merkleize(data)
    nodes = self.nodify(data)
    root = self.build_up(nodes)
  end

  def self.nodify(data)
    nodes = []
    data.each do |item|
        nodes.push(Node.new(self.hash(item)))
    end
    nodes
  end

  private

  def self.create_parents(nodes)
    parents = []
    nodes.each_slice(2) do |pair|
      a, b = pair
      puts pair
      puts "---"
      if(b)
        parent_datum = self.hash("#{a.datum}||#{b.datum}")
      else
        parent_datum = self.hash(a)
      end

      parent = Node.new(parent_datum)
      parent.add_children(pair)
      parents.push(parent)
    end

    parents
  end

  def self.build_up(nodes)
    parents = self.create_parents(nodes)
    if(parents.length == 1)
      return parents[0]
    else
      self.build_up(parents)
    end
  end

  def self.hash(content)
    Digest::SHA2.hexdigest(content)
  end
end


data = ["We", "hold", "these", "truths", "to", "be", "self-evident", "that"]
root = MerkleTree.merkleize(data)
puts root.datum == '4a359c93d6b6c9beaa3fe8d8e68935aa5b5081bd2603549af88dee298fbfdd0a'
