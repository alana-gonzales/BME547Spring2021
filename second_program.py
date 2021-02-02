import blood_tests
## OR
# from blood_tests import check_HDL     
## ^only imports a single function, then you can just call check_HDL instead of blood_tests.check_HDL
## OR
# from blood_tests import *
## ^imports all functions, then you can still use the functions without typing blood_tests
## BUT this is not recommended if you're importing more than one module in case any functions have the same name
## OR
# import blood_tests as bt
## then, you call bt.check_HDL()

x = blood_tests.check_HDL(55)
print("The HDL result for 55 is {}".format(x))

y = blood_tests.check_LDL(120)
print("The LDL result for 120 is {}".format(y))