def hi():
    print('Hi from one.py')


if __name__ == '__main__':
    print('directly run one.py file')
else:
    print('one.py is imported')

### multi level loop shorthand example.
list = [1, 3, 4, 5, 6]
arr = ['a', 'b', 'c', 'd']

nArr = [(l, a) for l in list for a in arr]
## this is a nested loop: eg
## above is the short hand.

nnArr = []

for l in list:
    for a in arr:
        nnArr.append((l, a))

print(nArr)
print(nnArr)