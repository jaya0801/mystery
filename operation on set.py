my_set = {1,2,3,4}
my_list = [4,5,6]
my_set = set(my_list)
my_set.add(9)
my_set.update([6,7]
my_set.remove(4)
my_set.discard(5)
print(2 in my_set)
print(8 in  my_set)
set1 = {1,2,3}
set2 = {3,4,5}
union_set = set1.union(set2)
print(union_set)
intersection_set = set1.intersection(set2)
print(intersection_set)
difference_set = set1.difference(set2)
print(difference_set)
set1.update(set2)
print(set1)
set1.intersection_update(set2)
print(set1)
set1.difference_update(set2)
print(set1)
set1 = {1,2,3}
set2 = {3,4,5}
symmetric_diff=set1.symmetric_difference(set2)
print(symmetric_diff)
set1 = {1,2,3}
set2 = {1,2}
print(set2.issubset(set1))
print(set1.issuperset(set2))




