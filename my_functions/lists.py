# lists can hold strings, numbers, booleans
friends = ["Luffy", "Zoro", "Nami", "Usoppu", "robin"]
friends[2] = "Nammi"
sets_of_numb = [1, 4, 9, 4, 33]
sets_with_something = [2, 7, 88, 88, 88, 6]

# give you the content from 0, 1, 2, ..., which start from left
print(friends[2])
# give you the content from -1, -2, -3, ...， which start from right
print(friends[-1])
# give you the content without the content on the 1 place
print(friends[1:])
# show the content from 1 to 2 without 3, so it is basically [1, 3)
print(friends[1:3])
print(friends[2])

friends.append("Franky")
friends.extend(sets_of_numb)
friends.insert(6, "chopper")
friends.remove(33)
print(friends)
print("-------------------------")

friends2 = friends.copy()
print(friends2)

sets_with_something.sort()
print(sets_with_something)

sets_with_something.reverse()
print(sets_with_something)

sets_with_something.pop()
print(sets_with_something)
print(sets_with_something.index(88))
print(sets_with_something.count(88))
sets_with_something.clear()
print(sets_with_something)
