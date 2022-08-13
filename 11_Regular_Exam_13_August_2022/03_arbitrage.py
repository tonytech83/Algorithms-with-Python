import sys


class TradingPair:
    def __init__(self, source, destination, price):
        self.source = source
        self.destination = destination
        self.price = price


trading_pairs = int(input())

graph = {}

for _ in range(trading_pairs):
    source, destination, price = [str(x) for x in input().split(' ')]
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []
    graph[source].append(TradingPair(source, destination, price))

start = input()
end = start

max_node = max(graph.keys())

price = [sys.maxsize] * (max_node + 1)
# create parent array
parent = [None] * (max_node + 1)

price[start] = 0

# TODO
