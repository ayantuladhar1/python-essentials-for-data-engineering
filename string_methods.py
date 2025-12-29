x = "hello world how are you"
#To Capitalize first letter in word
print (x.capitalize())
#To replace letters in words
print (x.replace("h", "T"))
#To split using a delimeter such as space " "
my_list = x.split(" ")
print (my_list)
#Ends With and Starts With
file = "raw_data.csv"
if (file.endswith(".csv")):
    print("CSV File")
if (file.startswith("raw")):
    print("RAW File")
#To perform word counts
statement = "Hello World. I am doing fine, it's a beautiful day."
print (statement.count("o"))
#is Functions
demo_str = "Hello"
demo_var = 10
print(demo_str.isnumeric()) #Booloean result
#print(demo_var.isnumeric()) #Does not work as it only works with strings
demo_var1 = "10"
print (demo_var1.isnumeric())
#To check numberwithstrings
demo_var2 = "10abc"
print (demo_var2.isalnum())
