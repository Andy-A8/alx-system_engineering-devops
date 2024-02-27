#!/usr/bin/env ruby
# The regular expression that matches a given pattern: sender, receiver, flags.
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(',')
