#!/usr/bin/env ruby
require 'yaml'

File.open(ARGV[0]) do |io|
  YAML.load_documents(io) do |d|
    p d
  end
end
