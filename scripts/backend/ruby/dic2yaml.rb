#!/usr/bin/env ruby
# create yaml

require 'yaml'

users = [
  {'name' => 'yumemo', 'age' => 80},
  {'name' => 'yumemonogatari', 'age' => 99},
]

puts users.to_yaml
