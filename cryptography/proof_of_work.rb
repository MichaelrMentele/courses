# Write two methods, one called `mint` and one called `verify`.
#
# * `mint`
#   - Mint should take two arguments: a `challenge` (random string) and a `work_factor` (number of leading 0s in the hash).
#   - It should return a `token`, which is a random string such that SHA2(`challenge` || `token`) starts with at least `work_factor` many 0s.
#   - Use hex encoding rather than binary encoding for simplicity. (You'll want no more than 4 for your work factor.)
# * `verify`
#   - This should take three arguments: the `challenge`, the `work_factor`, and the `token`.
#   - It should return `true` or `false` based on whether the token is valid.
#
# Bonus: if you have extra time, add timestamping and implement a cache of recent tokens so that double-spends are rejected.
require 'digest'
require 'securerandom'
require 'set'

def mint(challenge, work_factor)
  while true do
    token = SecureRandom.hex
    if(verify?(challenge, work_factor, token))
      return token
    end
  end
end

def verify?(challenge, work_factor, token)
  result = Digest::SHA2.hexdigest("#{challenge}||#{token}")
  to_check = result.slice(0, work_factor)
  to_check.each_char do |c|
    return false if c != '0'
  end
  true
end

class HashCash
  def initialize
    @cache = Set.new
  end

  def verify?(challenge, work_factor, token)
    return false if @cache.include?(token)

    result = Digest::SHA2.hexdigest("#{challenge}||#{token}")
    to_check = result.slice(0, work_factor)
    to_check.each_char do |c|
      return false if c != '0'
    end

    @cache.add token

    true
  end
end

token = mint("blah", 2)
server = HashCash.new
puts server.verify?("blah", 2, token) == true
puts server.verify?("blah", 2, token) == false
