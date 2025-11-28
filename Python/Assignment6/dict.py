
my_dict_store = {
    "india": "New-Delhi", "USA": "Washington", "Nepal": "Kathmandu", '"Ukraine"': "Kyuiv"
     
}

userInput =  int(input("please Enter the no. of inputs:- "))


for i in range(userInput):
  key = str(input("Enter the key :- "))
  value= str(input("Enter the value :- "))
  my_dict_store[key] =value
  



print(my_dict_store)


switchInput = int(input("Enter the below Input as pr your choice :-"))

match  switchInput