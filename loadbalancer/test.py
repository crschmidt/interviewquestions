import solution
import time

b = solution.Balancer([['a', 1], ['b', 1], ['c', 8]])
matches = {'a': 0, 'b': 0, 'c':0}
for i in range(20000):
    matches[b.request()] += 1
print matches    
t = time.time()
b = solution.Balancer([['a', 10000000], ['b', 1]])
matches = {'a': 0, 'b': 0}
for i in range(20000):
    matches[b.request()] += 1
print matches , time.time() - t   
t = time.time()
b = solution.Balancer2([['a', 10000000], ['b', 1]])
matches = {'a': 0, 'b': 0}
for i in range(20000):
    matches[b.request()] += 1
print matches , time.time() - t   
