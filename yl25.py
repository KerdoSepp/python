dictionary = {
    "firstName" : "Kerdo",
    "lastName" : "Sepp",
    "birthYear": 2009,
    "elukoht" : "Kuressaare",
    "favouriteDessert" : "Jan",
}


print(dictionary.get("elukoht"))
print(dictionary["elukoht"])

dictionary.update({"favouriteDessert": "ikkagi Jan"})

for x in dictionary.keys():
  print(x)

for x in dictionary.values():
  print(x)


if dictionary.get("isikukood"):
    print("Isikukood on", dictionary.get("isikukood"))
else:
    print("Isikukoodi pole")

print(len(dictionary))

dictionary.update({"pikkus": 167})

print(dictionary["pikkus"])