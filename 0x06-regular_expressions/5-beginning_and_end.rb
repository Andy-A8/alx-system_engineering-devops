#!/usr/bin/env ruby
# The regular expression exactly matches a string starting with:
#   h ends with n and can have any single character in between.
puts ARGV[0].scan(/^h.n$/).join
