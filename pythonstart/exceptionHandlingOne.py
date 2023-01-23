# try/except

# try:
#     print(a)
# except:
#     print('this is an exception!!!')

# try:
#     print(a)
# except NameError:
#     print('Variable a is not defined!')
# except:
#     print('this is an exception!!!')

## else body will be executed when there is no exception
# try:
#     print("Python is a fun")
# except:
#     print('An Error or something went wrong')
# else:
#     print('Everything is good and nothing is wrong')

# try:
#     print(x)
# except:
#     print('An Error or something went wrong')
# else:
#     print('Everything is good and nothing is wrong')

## finally block will be executed regardless of any exception or not
try:
    #print("Hello there!")
    print(x)
except:
    print('An error occurred')
finally:
    print('exception handling completed.')