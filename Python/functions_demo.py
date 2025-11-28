# key takeways 
"""
1) def defines the function
2) def function_name(arg1,arg2):
     body of the function (indent it within def )
     return is optional if you dont return python returns None
3) default args (arg1=10,arg2=10)     
    arguments are defaulted to respective values if NOT passed 
4) the caller needs to know the signature [name of the function and the input paramters ]    
   function_name(param1,param2) --> positional arguments
   function_name(arg1=param1,arg2=param2) --> keyword arguments
5)  lambda argument/s: expression to return  
"""



# #function without a return statement 
# def my_functionname():
#     print("I am printing some value")
    
    
# return_val  = my_functionname()    
# print("Returned value from the function is " , return_val)


#function with a return statement 
# def my_functionname():
#     print("I am printing some value")
#     return 1 
    
# return_val = my_functionname()    
# print("Returned value from the function is " , return_val)

#-------------------------------------------------------------

#function with a return statement and input parameters
# def my_addition_function(num1,num2):
#     return num1+num2

# my_first_number = 1
# my_second_number = 2

# return_val = my_addition_function(my_first_number,my_second_number)
# print("Returned value from my_addition_function is ", return_val)

#-------------------------------------------------------------

#function with default value from a literal 
# def my_addition_function(num1=11,num2=10,num3=90):
#     return num1+num2+num3

# return_val = my_addition_function(9999, num3=888888, num2=999999,)
# print("Returned value from my_addition_function is ", return_val)

#-------------------------------------------------------------

#function with default value from a variable 
# my_second_default_number = 10 
# def my_addition_function(num1=my_second_default_number,num2=10,num3=90):
#     return num1+num2+num3

# my_second_default_number = 1000
# return_val = my_addition_function( num2=10 , num3=10)
# print("Returned value from my_addition_function is ", return_val)

#-------------------------------------------------------------

# pass by value
# num1 = 10 
# def pass_by_value(num1):
#     num1 = 100
#     print("num1 inside function invocation", num1)

# print("num1 value before function invocation", num1)
# pass_by_value(num1)
# print("num1 value after function invocation", num1)
#-------------------------------------------------------------

# # pass by reference
# num_list = [10,]
# def pass_by_ref(num_list):
#     num_list.append(100)
#     print("num_list inside function invocation", num_list)

# print("num_list value before function invocation", num_list)
# pass_by_ref(num_list)
# print("num_list value after function invocation", num_list)

#-------------------------------------------------------------

# # pass by value
# num_list = [10,]
# def pass_list_by_value(num_list):
#     num_list= [10000]
#     print("num_list inside function invocation", num_list)

# print("num_list value before function invocation", num_list)
# pass_list_by_value(num_list)
# print("num_list value after function invocation", num_list)


# #--------------------------------------------------------------------
# #Simple demo about Lambda and HOF available in lambda_function_demo.py
# #---------------------------------------------------------------------

# # lambda arguments: expression    
# my_addition_lambda = lambda first_num , second_num : first_num + second_num
# print(my_addition_lambda(1,2))

# # below are the lambda functions for each of the operation
# my_square_lambda = lambda first_num: first_num * first_num # for square 
# my_expo_lambda = lambda first_num,second_num : first_num ** second_num # for exponentation

# print(my_square_lambda(9))
# print(my_expo_lambda(2,3))




