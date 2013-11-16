# First attempt; won't work because you'll scroll off the bounds of the
# list.
def intersect1(j, k):
    i1 = 0
    i2 = 0
    ret = []
    while i1 < len(j) and i2 < len(k):
        while j[i1] < k[i2]:
            i1 += 1
        while k[i2] < j[i1]:
            i2 += 1
        if j[i1] == k[i2]:
            ret.append(j[i1])
            i1 += 1
            i2 += 1
    return ret            

# Works. Is kinda goofy, and had a 'code smell' that I failed to identify
# the source of.
def intersect2(j, k):
    i1 = 0
    i2 = 0
    ret = []
    while i1 < len(j) and i2 < len(k):
        while i1 < len(j) and j[i1] < k[i2]:
            i1 += 1
        while i2 < len(k) and k[i2] < j[i1]:
            i2 += 1
        if i1 < len(j) and i2 < len(k) and j[i1] == k[i2]:
            ret.append(j[i1])
            i1 += 1
            i2 += 1
    return ret           

def intersect_nodupes(j, k):
    # first, just talked through what I would do to start;
    # this led to a conversation about why we wouldn't do that,
    # including the overall complexity. (Apparently, sorting a
    # list is O(n log n), things that I don't know off the top
    # of my head.)
    return sorted(list(set(intersect2(j, k))))

# then actually modified the code; first, failed to notice that this
# won't work...
def intersect_nodupes2(j, k):
    i1 = 0
    i2 = 0
    ret = []
    while i1 < len(j) and i2 < len(k):
        while i1 < len(j) and j[i1] < k[i2]:
            i1 += 1
        while i2 < len(k) and k[i2] < j[i1]:
            i2 += 1
        if i1 < len(j) and i2 < len(k) and j[i1] == k[i2] and ret[-1] != j[i1]:
            ret.append(j[i1])
            i1 += 1
            i2 += 1
    return ret           

# then got to this, which fails differently... goes into infinite loop
def intersect_nodupes3(j, k):
    i1 = 0
    i2 = 0
    ret = []
    while i1 < len(j) and i2 < len(k):
        while i1 < len(j) and j[i1] < k[i2]:
            i1 += 1
        while i2 < len(k) and k[i2] < j[i1]:
            i2 += 1
        if i1 < len(j) and i2 < len(k) and ret and ret[-1] != j[i1] and j[i1] == k[i2]:
            ret.append(j[i1])
            i1 += 1
            i2 += 1
    return ret           

# and finally to this
def intersect_nodupes4(j, k):
    i1 = 0
    i2 = 0
    ret = []
    while i1 < len(j) and i2 < len(k):
        while i1 < len(j) and j[i1] < k[i2]:
            i1 += 1
        while i2 < len(k) and k[i2] < j[i1]:
            i2 += 1
        if i1 < len(j) and i2 < len(k) and j[i1] == k[i2]:
            if (not ret or ret[-1] != j[i1]):
                ret.append(j[i1])
            i1 += 1
            i2 += 1
    return ret          

# after that, interviewer pointed out that my 3 while loops were kinda
# silly, and rewrote it like so:
def intersect_nodupes5(j, k):
    i1 = 0
    i2 = 0
    ret = []
    while i1 < len(j) and i2 < len(k):
        if j[i1] < k[i2]:
            i1 += 1
        if k[i2] < j[i1]:
            i2 += 1
        if i1 < len(j) and i2 < len(k) and j[i1] == k[i2]:
            if (not ret or ret[-1] != j[i1]):
                ret.append(j[i1])
            i1 += 1
            i2 += 1
    return ret          
