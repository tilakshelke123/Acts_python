"""
https://docs.python.org/3/library/stdtypes.html#common-sequence-operations

			      collections
    sequence type		  mapping type	              set Type	
		string		   dictionary			set
		list						frozen set
		tuple
		range		


operations on mutable sequence types:		    
a) add --> .append(x)/.extend(s) [at the end] or .insert(0,x) /+= [at the start]
b) remove ->  pop()/pop(i)/remove(x) [single values] or del slicing logic [multiple elements]
c) update -> s[i]= value [single element] /  s[i:j:k] = chunk slicing logic [multiple elements]

"""

##### Example of CRUD Starts ######
#creation
l1= [1,2,3] 
l2= list([1,2,3])

print(l1)
print(l2)

t1= (1,2,3)
t2= tuple([1,2,3])

print(t1)
print(t2)

r1= range(1,10,1) #start: stop:step
print(r1)
print(list(r1))

r2= range(10) #stop
print(r2)
print(list(r2))

r3= range(0,10,2)
print(r3)
print(list(r3))


r4= range(10,0,-2)
print(r4)
print(list(r4))

for i in range(10,0,-1):
    print(i,end=",")

s1= "12345"    
# -------

# retrival
print("\n",l1)
print(l1[0],l1[1])
print(t1[0],t1[1])
print(r1[0],r1[1])
print(s1[0],s1[1])

print(l1[0:2])
print(t1[0:2])
print(list(r1[0:2]))
print(s1[0:2])


print(l1[0:2:2])
print(t1[0:2:2])
print(r1[0:2:2])
print(s1[0:2:2]) 
   
print(l1[0:4:2])
print(t1[0:4:2])
print(r1[0:4:2])
print(s1[0:4:2]) 

# ----
# Updation -- existing element/s
print(l1)
l1[2]=30
print(l1)

l1[1:3:1]=[200,300]
print(l1)

# ----
# Updation - add
l1.append(99)
print(l1)
#or
l1+=[44]
print(l1)

l1.extend([88,77])
print(l1)
#or
l1+=[66,55]
print(l1)

l1.insert(0,11)
print(l1)

l1.insert(3,00)
print(l1)
# # -----
# # deletion
l1.pop()
print(l1)

l1.pop(0)
print(l1)

l1.remove(300)
print(l1)

# ## miscellaneous 

# # check if the element is present in the collection or not 
# # in/not in

print(1 in l1)
print(10 not in l1)


print('1' in s1)
print('10' not in s1)

# # create a copy of a collection

l1_copy = l1
print(id(l1_copy))
print(id(l1))

l1_copy=l1.copy()
print(id(l1_copy))
print(id(l1))
print(l1)
print(l1_copy)

# min/max
print("minimum value ", min(l1))
print("maximum value ", max(l1))

# len
print("count of elements ", len(l1))

# element count within the collection
print("count of 200 is", l1.count(200))

# index of an element
print("Index of 99 is", l1.index(99))

l1.append(99)
print(l1)
print("Index of 99 is", l1.index(99))
print("Index of 99 is", l1.index(99,l1.index(99)+1))

# reverse of the collection
print(l1)
print(l1.reverse())
print(l1)

# # https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
# ##### Example of CRUD Ends ######



my_string = "ICC-T20-2022-WC"
my_list=['I', 'C', 'C', '-', 'T', '2', '0', '-', '2', '0', '2', '2', '-', 'W', 'C']
my_tuple=('I', 'C', 'C', '-', 'T', '2', '0', '-', '2', '0', '2', '2', '-', 'W', 'C')
my_range = range(0,5,1)

print("The operations in the following table are defined on Mutable/Immutable sequence types")
print("--------------------------------------------------------------------------")

print("x in s -- True if an item of s is equal to x, else False")
x= "C"
print(x in my_string)
print(x in my_list)
print(x in my_tuple)
print(1 in my_range)

print("x not in s -- False if an item of s is equal to x, else True")
x= "C"
print(x not in my_string)
print(x not in my_list)
print(x not in my_tuple)
print(1 not in my_range)

print("s+t -- 	the concatenation of s and t")
list_t= ['A','U','S','T','R','A','L','I','A']
tuple_t = ('A','U','S','T','R','A','L','I','A')
string_t = "Australia"

print(my_string + string_t)
print(my_list + list_t)
print(my_tuple + tuple_t)
# print(my_range + my_range ) # TypeError: unsupported operand type(s) for +: 'range' and 'range'

print("s * n or n * s -- 	equivalent to adding s to itself n times")
n = 2 
print(my_string * n)
print(my_list * n)
print(my_tuple * n)
#print(my_range *n ) # TypeError: unsupported operand type(s) for *: 'range' and 'range'

print("s[i] -- ith item of s, origin 0")
print(my_string[1])
print(my_list[1])
print(my_tuple[1])
print(my_range[1])

print("s[i:j] -- slice of s from i to j(Exclusive) and step 1 ")
print(my_string[1:10])
print(my_list[1:10])
print(my_tuple[1:10])
print(my_range[1:10])


print("s[i:j:k] -- 	slice of s from i to j with step k")
print(my_string[1:10:2])
print(my_list[1:10:2])
print(my_tuple[1:10:2])
print(my_range[1:10:2])


print("len(s) -- length of s")
print(len(my_string))
print(len(my_list))
print(len(my_tuple))
print(len(my_range))

print("min(s) -- smallest item of s ")
print(min(my_string)) # ascii value of - is 45 and 1 is 49
print(min(my_list))
print(min(my_tuple))
print(min(my_range))

print("max(s) -- largest item of s ")
print(max(my_string))
print(max(my_list))
print(max(my_tuple))
print(max(my_range))


print("s.index(x[, i[, j]]) -- 	index of the first occurrence of x in s (at or after index i and before index j)")
print(my_string.index('C'))
print(my_list.index('C'))
print(my_tuple.index('C'))
print(my_range.index(1))

print("s.count(x) -- 	total number of occurrences of x in s")
print(my_string.count('C'))
print(my_list.count('C'))
print(my_tuple.count('C'))
print(my_range.count(1))

print("The operations in the following table are defined on mutable sequence types")
print("------------------------------------------------------------------------")

print("s[i] = x -- 	item i of s is replaced by x")
#my_string[1] = 'T'  # TypeError: 'str' object does not support item assignment 
my_list[1] =  "G"
#my_tuple[1] = "G" # TypeError: 'tuple' object does not support item assignment
#my_range[1] = 1 # TypeError: 'range' object does not support item assignment
print(my_list)

print("s[i:j] = t -- slice of s from i to j is replaced by the contents of the iterable t ");
#my_string[1:3] = ["G","A"]  # TypeError: 'str' object does not support item assignment 
my_list[1:3] =   ["G","A"]
#my_tuple[1:3]  = ["G","A"] # TypeError: 'tuple' object does not support item assignment
#my_range[1] = [1,2] # TypeError: 'range' object does not support item assignment
print(my_list)

print("del s[i:j] -- 	same as s[i:j] = []")
del my_list[1:3] 
print(my_list)

print("s[i:j:k] = t -- 	the elements of s[i:j:k] are replaced by those of t")
my_list[4:11:2] =   ["T","T","T","T"]
print(my_list)

print("del s[i:j:k] -- 	removes the elements of s[i:j:k] from the list")
del my_list[1:6:2]
print(my_list)

print("s.append(x) -- 	appends x to the end of the sequence (same as s[len(s):len(s)] = [x])")
my_list.append("Appended String")
print(my_list)

print("s.append(x) -- Trying to append multiple values by passing a list but , did not work as anticipated ")
my_list.append(["Appended String1","Appended String2"])
print(my_list)

print("s.clear() -- removes all items from s (same as del s[:])")
my_list.clear()
print(my_list)

print("s.copy() -- creates a shallow copy of s (same as s[:])")
my_list_copy = my_list.copy()
print(my_list)
print(my_list_copy)

print("s.extend(t) or s += t -- extends s with the contents of t (for the most part the same as s[len(s):len(s)] = t)")
my_list.extend(["Extended Val1","Extended Val2"])
print(my_list)
my_list += ["Extended Val3","Extended Val4"]
print(my_list)

print("s *= n -- updates s with its contents repeated n times")
my_list *= 2
print(my_list)

print( "s.insert(i, x) -- inserts x into s at the index given by i (same as s[i:i] = [x])")
my_list.insert(0,"My Inserted Val1")
print(my_list)

print( "s.insert(i, x) -- trying to add multiple elements but did not succeeded as anticipated")
my_list.insert(0,["My Inserted Val2","My Inserted Val3"])
print(my_list)

print("s.pop() or s.pop(i) -- retrieves the item at i and also removes it from s")
print(my_list)
print("Popped value was ", my_list.pop())
print(my_list)
print("Popped value was ", my_list.pop(0))
print(my_list)

print("s.remove(x) -- 	remove the first item from s where s[i] is equal to x")
print(my_list)
my_list.remove('Extended Val1')
print(my_list)
my_list.remove('Extended Val1')
print(my_list)

print("s.reverse() -- 	reverses the items of s in place")
print(my_list)
my_list.reverse()
print(my_list)
