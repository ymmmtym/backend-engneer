#!/usr/bin/env ruby
require 'yaml'

File.open('sample.yml') do |io|
  YAML.load_documents(io) do |d|
    p d
  end
end
