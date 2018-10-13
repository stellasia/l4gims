#!/usr/bin/ruby

require 'json'
require 'pp'

struct = JSON::load(File.read('sankey.json'))

nodes = struct['nodes']

tree = {}

root = nil
mid = nil
nodes.each do |node|
    name = node["name"]
    if node.has_key?("type")
        type = node["type"]
    else
        type = "mid"
    end
    case type
        when "root"
            root = name
            tree[name] ||= {}
        when "mid"
            mid = name
            tree[root][name] ||= []
        when "tail"
            tree[root][mid] << name
    end
end

links = []

tree.each do |s1,h1|
    h1.each do |s2,a2|
        links << { "source": s1, "target": s2, "value": sprintf("%.1f", rand) }
        a2.each do |impact|
            links << { "source": s2, "target": impact, "value": sprintf("%.1f", rand) }
        end
    end
end

puts JSON.pretty_generate(links)

