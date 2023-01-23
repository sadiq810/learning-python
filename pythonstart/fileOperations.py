# write to a file.
f = open('hi.txt', 'w') # write mode, but overwrite the existing text.
#f = open('hi.txt', 'a') read/write mode, but with append option

f.write('Hello, How are you! .')

f.close()

# Read from a file, read mode.
file = open('file.txt', 'r')
text = file.read()
file.close()
print(text)

