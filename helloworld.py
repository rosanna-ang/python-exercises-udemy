import math as m

print(' =======   Lists   ======= ')
print('let\'s create a list')
square_list = [0,1,4,9,16,25]
print(square_list)
print("Print the first item: ", square_list[0])
print("Print the second item: ", square_list[1])
print("Print the last item: ", square_list[-1])
square_list.reverse()
print("Print the reverse of the list: ", square_list)
square_list.sort()
print("Print the sorted of the list: ", square_list)
square_list.append(100)
print("Print the appended of the list: ", square_list)
square_list.remove(100)
print("Print the shortened of the list: ", square_list)
square_list.pop(0)
print("Print the shortened of the list first item removed: ", square_list)
print(' ======= the end ======= ')
print('  ')
print('  ')

print(' =======   Strings   ======= ')
print('let\'s create a string')
string_variable = "Python strings are immutable."
print(string_variable)
print(string_variable[0]) #print first character
print(len(string_variable)) #print length of the string
string_variable = "Python strings are immutable...?"
print(string_variable)
#string_variable[1:] = "?"
print(string_variable)
print(' =======   the end   ======= ')
print('  ')
print('  ')

print(' =======   Tuples   ======= ')
print('What\'s a tuple? It\'s simply a immutable list of values seperated by commas.')
print('Since Tuples are immutable and can not change, they are faster in processing as compared to lists. Hence, if your list is unlikely to change, you should use tuples, instead of lists.')
tuple_variable = 1,2,3,4,5,6,7,8,9,0
print(tuple_variable)
print(tuple_variable[0]) #print first character
print(len(tuple_variable)) #print length of the tuple
tuple_variable = 1,2,3,4,5,6,7,8,8
print(tuple_variable)
print(' =======   the end   ======= ')
print('  ')
print('  ')

print(' =======   Dictionary   ======= ')
print('What\'s a dictionary? It\'s simply key-value pairs.')
dict = {"Mommy":"Ann", 'Daddy':"Jan"}
print(dict)
print(dict["Mommy"]) #print first character
print(' =======   the end   ======= ')
print('  ')
print('  ')

print(' =======   Iterations   ======= ')
N = 5
mul=1
add=1
min=1
for i in range(2,N):
  mul *= i
  add += i
  min -= i
  print(i)

print(mul)
print(add)
print(min)

print(' =======   the end   ======= ')
print('  ')
print('  ')

print(' =======   Conditions   ======= ')

if 1==1:
    print("true")
else:
    print("else")


print(' =======   the end   ======= ')
print('  ')
print('  ')


fact = m.factorial(6)
print(fact)
print('  ')
