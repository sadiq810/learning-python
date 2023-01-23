class firstCalss:
    #constructor
    def __init__(self, name):
        self.a = "Hi"
        self.name = name

    def printMsg(self):
        return 'Hello and this is print function'

    def hello(self, name):
        print('Hello, '+name+", Welcome to Paython class.")

    def hi(self):
        print('Hello there! '+self.a+" my name is "+ self.name)




obj = firstCalss("Ali")

print(obj.printMsg())

obj.hello('Khan')

print("This is constructor variable value:"+obj.a)
obj.hi()

## to remove object project use del keyword as below
#del obj.name
#print(obj.name) # it will throw error

## to delete whole object use del keyword
# del  obj
# print(obj) #throw error

## Modify object project
obj.name = "sadiq"
obj.hi()

## self is just a reference to current object, and its not a keyword, you can use any other word instead, but it's a convention to use self.