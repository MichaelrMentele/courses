# Build a blockchain!
#
# In this assignment, you'll be building a blockchain from scratch.
# You'll want to build a block class, and then a blockchain class that includes
# all blocks.
#
# * Block
#   - `content` (string)
#   - `previous_hash` (string)
#   - `nonce` (string/number)
#
# * Blockchain
#   - `blocks` (array)
#
# I should be able to initialize your blockchain as
#{ }`Blockchain.new("this is a string".split(" "))` and have it automatically
# create blocks, compute proof of work for each block, and chain them all
# together in a blockchain. You should also be able to append new blocks to this
################################################################################
# The blockchain class represents the data structure, it needs to include
# the proof of work ie. the nonce that was the solution for the prior puzzle
# therefore need a way to propose puzzles as part of the chain. This will
# then rely on the prior block hash. So, when we are adding a new block,
# we look at the prior block, compute the puzzle, take the nonce and try it,
# to see whether it is a solution.
require 'digest'
require 'securerandom'


class Block
  @attr_reader :content, :previous_hash, :nonce

  def initialize(content, previous_hash, nonce)
    @content = content
    @previous_hash = previous_hash
    @nonce = nonce
  end

  def block_hash
    # reurn hash of block content, nonce, and previous hash
    Digest::SHA2.hexdigest("#{self.content}||#{self.previous_hash}||#{self.nonce}")
  end
end

class Blockchain
  attr_reader :difficulty, :chain

  def initialize(transactions)
    # create a new blockchain, with a genesis block
    @difficulty = 1
    @chain = [self.genesis_block]

    # optionally add all blocks to the chain
    if(transactions)
      transactions.each do |transaction|
        self.mint(transaction)
      end
    end
  end

  def head
    self.chain[-1]
  end

  def valid_nonce?(nonce)
    result = Digest::SHA2.hexdigest("#{self.puzzle}||#{nonce}")
    to_check = result.slice(0, work_factor)
    to_check.each_char do |c|
      return false if c != '0'
    end
    true
  end

  def valid_block?(block)

  end

  def puzzle
      # H(previous.hash + some_nonce) == some hash with self.difficulty leading zeros
      self.head.hash
  end

  def mint(content)
    nonce = self.proof_of_work(self.puzzle, self.difficulty)
    block = Block.new(content, self.head.block_hash, nonce)
    self.add!(block)
    return block
  end

  private

  def is_genesis?
    self.chain.length == 0
  end

  def genesis_block
    content = "genesis"
    prior_hash = "genesis"
    nonce = self.proof_of_work(content, 0)
    Block.new("genesis", "genesis", nonce)
  end

  def add!(block)
    self.chain.push(block)
  end

  def proof_of_work(puzzle, difficulty)
    while true do
      token = SecureRandom.hex
      if(self.valid_nonce?(puzzle, difficulty, nonce))
        return nonce
      end
    end
end

blockchain = Blockchain.new()
blockchain.mint
