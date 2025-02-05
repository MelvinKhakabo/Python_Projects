#Write a function called inter_section that takes two lists and finds the intersection (the elements that are present in both lists).
#The function should return a tuple of intersections. Use list comprehension in your solution. Use the lists below. 
#Your function should return (30, 65, 80).
#list1 = [20, 30, 60, 65, 75, 80, 85]
#list2 = [ 42, 30, 80, 65, 68, 88, 95]
def inter_section(list1, list2):
    return tuple([x for x in list1 if x in list2])
print(inter_section([20, 30, 60, 65, 75, 80, 85], [42, 30, 80, 65, 68, 88, 95])) #(30, 65, 80)






