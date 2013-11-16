import solutions
l1 = [-1, 4, 5, 8, 12]
l2 = [1,2,3,4,5,6]
print solutions.intersect2(l1, l2)

l1_dupes = [1,4,5,5,8,12]
l2_dupes = [2,4,5,5,9]
print solutions.intersect2(l1_dupes, l2_dupes)
print solutions.intersect_nodupes(l1_dupes, l2_dupes)
try:
    print solutions.intersect_nodupes2(l1_dupes, l2_dupes)
except Exception, E:
    print E
print solutions.intersect_nodupes4(l1_dupes, l2_dupes)
print solutions.intersect_nodupes5(l1_dupes, l2_dupes)
