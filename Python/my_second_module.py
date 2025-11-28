
print("I am in second module")

import my_first_module as my_new_name # importing the entire module 
# from my_first_module import my_name,my_list  # import part of modules 
 
print("second module output :> my_name in first module is ===>>>>>> " , my_new_name.my_name)
print("second module output :> my_list in first module is ===>>>>>> " , my_new_name.my_list)



