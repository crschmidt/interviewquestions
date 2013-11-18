import random
class Balancer:
    def __init__(self, weights):
        self.weights = weights
        self.total = sum([weight[1] for weight in weights])
        start = 0
        match_list = []
        for weight in self.weights:
            for i in range(0, weight[1]):
                match_list.append(weight[0])
        self.match_list = match_list       
    def request(self):
        balancer = random.randint(0,self.total-1)
        return self.match_list[balancer]

# After writing this, I realized that my solution above is hacky as
# heck; it works fine for the case where the sum is a small number and
# the weights are all integers, but fails in any other case. This bugged
# me enough to do something about it.
class Balancer2:
    def __init__(self, weights):
        self.weights = weights
        self.total = sum([weight[1] for weight in weights])
        start = 0
        match_list = []
        cur = 0
        for weight in self.weights:
            match_list.append((cur, cur + weight[1], weight[0]))
            cur += weight[1]
        self.match_list = match_list       
    def request(self):
        balancer = random.random()*self.total
        for item in self.match_list:
            if balancer >= item[0] and balancer < item[1]:
                return item[2]
        print "What?!"        
