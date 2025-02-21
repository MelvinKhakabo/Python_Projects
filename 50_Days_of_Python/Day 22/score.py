#Create three functions. The first called add_hash takes a string and adds a hash # between the words. The second function called 
#add_underscore removes the hash(#) and replaces it with an underscore ( _ ) The third function called remove_underscore,
#removes the underscore and replaces it with nothing. if you pass ‘Python’ as an argument for the three functions, and you call them at 
#the same time like:print(remove_underscore(add_underscore(add_hash('Python'))))
#it should return ‘Python’.

def add_hash(string):
    return string.replace('', '#')[1:-1]
print(add_hash('Python')) #P#y#t#h#o#n  

def add_underscore(string):
    return string.replace('#', '_')
print(add_underscore('P#y#t#h#o#n')) #P_y_t_h_o_n

def remove_underscore(string):
    return string.replace('_', '' )
print(remove_underscore('P_y_t_h_o_n')) #Python
