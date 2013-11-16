import solution

b = solution.Balancer([['a', 1], ['b', 1], ['c', 8]])
matches = {'a': 0, 'b': 0, 'c':0}
for i in range(20000):
    matches[b.request()] += 1
print matches    
