#Write a function called make_tuples that takes two lists, equal lists, and combines them into a list of tuples. For example if list a is 
#[1,2,3,4] and list b is [5,6,7,8], your function should return [(1,5),(2,6),(3,7),(4,8)].

def make_tuples(a, b):
    return list(zip(a, b))
a = [1,2,3,4]
b = [5,6,7,8]
print(make_tuples(a, b)) #[(1, 5), (2, 6), (3, 7), (4, 8)]
a = [1,2,3,4,5]
b = [5,6,7,8]
print(make_tuples(a, b)) #[(1, 5), (2, 6), (3, 7), (4, 8)]
a = [1,2,3,4,5,6]
b = [5,6,7,8]
print(make_tuples(a, b)) #[(1, 5), (2, 6), (3, 7), (4, 8)]