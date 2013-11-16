# Initial solution; doesn't preserve order of input terms, not clear
# if that's necessary? n log n on each term, plus n log n on output
def anagrams(words):
    groups = {}
    for word in words:
        key = "".join(sorted(word))
        if not key in groups:
            groups[key] = []
        groups[key].append(word)
    output = []
    for key in groups:
        output.append(groups[key])
    return sorted(output)

# If the goal is to return each sub-list in the order that it was first
# seen in the input list, then we can cope by adding an extra item
# to the start of the list in the hash key.
def anagrams_ordered(words):
    groups = {}
    i = 0
    for word in words:
        i += 1
        key = "".join(sorted(word))
        if not key in groups:
            groups[key] = [i]
        groups[key].append(word)
    output = []
    for value in sorted(groups.values()):
        output.append(value[1:])
    return output
