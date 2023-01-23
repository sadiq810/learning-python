# listItems = [1, 2, 3, 4, 6]
# listItems[2] = 33
#
# listItems.append('appended item')
# del listItems[4]
# print(listItems)

#tuple,

# players = ('ali', 'wali', 'jan')
# players2 = 'salam', 'khan'
#
# mixed = ('first', [0, 1, 2, 3, 4])
#print(mixed[1][1:3])

#print(players)

#players = ("gul", 'khan')
#del players

# allplayers = players + players2
# print(allplayers)

#Dictionary

#player_numbers = {'Ali': 2, 'wali': 4, 'Jan': 5}
# player_numbers = dict({'Ali': 2, 'wali': 4, 'Jan': 5})
# player_numbers['Salam'] = 44
# player_numbers['Ali'] = 3333
#del player_numbers['Jan']
#del player_numbers
# print(player_numbers)
#print(player_numbers['wali'])
#print(player_numbers.get('Jan'))
#accessing non existing key will return None



## Sets: unordered and unindexed

#fruits = {"banana", "apple", "orange"}
# for x in fruits:
#     print(x)

#print("graps" in fruits) # check if condition here.

#fruits.add('graps') # to add new item to sets

#fruits.update(['graps', 'mango']) #to add multiple items.
#print(len(fruits))

#fruits.remove('apple')
#fruits.pop()
#fruits.clear()
#del fruits
#print(fruits)

# x = 10
#
# if x > 8:
#     print("Greater")
# elif x <= 10:
#     print('Less or equal')
# else:
#     print("Else part executed")
#
#
# print("x is greater" if x == 10 else "else part")

# num = 1
# while(num < 8):
#     print(num)
#     num +=1
#     if num > 5:
#         break

# y = 1
# while(y < 8):
#     print(y)
#     y += 1
# else:
#     print("Loop is completed")


fruits = ['Apple', 'Mango', "Orange"]

for fruit in fruits:
    print(fruit)
else:
    print("Loop completed")