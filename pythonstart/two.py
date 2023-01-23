import one

one.hi()

def hello():
    print('Hi from two.py')


if __name__ == '__main__':
    print('directly run two.py file')
else:
    print('two.py is imported', __name__)