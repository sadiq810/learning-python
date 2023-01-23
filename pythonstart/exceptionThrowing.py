## manually raise an exception
# a = -3
#
# if a < 0 :
#     raise Exception('Sorry, the number should be greater than 0.')


## Raise type error
a = "hello there"

if not type(a) is int:
    raise TypeError("Only integer numbers are allowed")