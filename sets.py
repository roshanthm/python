my_set={1,2,3,4,5,6,7}
print(my_set)

n_set=set([1,22,33,44])

print(n_set)

n_set.add(1221)
print(n_set)

n_set.remove(1)

#if element not in the set it shows an error to avoid it we use discard

n_set.discard(1112121)

x=my_set.pop()
print(x ,"......",my_set )

# to clear all the elemts just use

n_set.clear() #simply print the code 

#to check wheather the element present in the code or not 

print(3 in my_set)

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Using intersection (does NOT change set1)
result = set1.intersection(set2)
print("Result (new set):", result)
print("set1 after intersection:", set1)

# Using intersection_update (modifies set1)
set1.intersection_update(set2)
print("set1 after intersection_update:", set1)


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

result = set1.difference(set2)

print("Difference:", result)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

symmetric_diff = A.symmetric_difference(B)
print(symmetric_diff)  # Output: {1, 2, 5, 6}


A = {1, 2}
B = {1, 2, 3, 4}

print(A.issubset(B))  # True, because all elements of A are in B
print(B.issubset(A))  # False, B has elements not in A

A = {1, 2}
B = {1, 2, 3, 4}

print(B.issuperset(A))  # True, B contains everything in A
print(A.issuperset(B))  # False


