mylist = ["apple", "banana", "cherry"]
print(mylist[0])
mylist.append("kiwi")

print(mylist[3])
mylist[2] = "mango"
print(mylist)

if "mango" in mylist:
    print(len(mylist))
    mylist.remove("banana")
    print(mylist)
    list(reversed(mylist))
    mylist.sort()
    print(mylist)