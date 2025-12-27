#Variables are used as containers to store values
my_var = "Hello World"
your_var = "Nice World"
print (my_var)

x = 10
print(my_var, x)

y = 5
#Adding integers
print (x + y)

#Combine Strings
print (my_var + your_var)

#We cannot combine integer and string
#print(x + my_var) --> will not work
#To combine string and integer we have to convert the integer to sting
a = "10"
print(a + my_var)

#Multiple Assignments
x,y,z = 10,5,20
x = y= z = 10

#Multi Line Code
total_sum = 10+20+30+20+20+10
print(total_sum)
#Use BackSlash \
total_sum = 10+20\
            +30+20+20+10
print(total_sum)
#Use Paranthesis ()
total_sum = (10+20
            +30+20+20+10)
print(total_sum)

#To check data type of variables
b = 10
print(type(b))

#Explicit Type Casting
a = 10 
b = "10" 
#String To integer
b_new = int(b) #Convert into Integer
a_new = str(a) #Convert into String
print (type(a))
print (type (b))
#Implicit Type Casting
a = 10 #Integer
b = 10.5 #Float
print (a + b)
