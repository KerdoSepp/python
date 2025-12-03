name = input("Enter name: ")
print("Hi", name+"!")
elukoht = input("Where do you live :):")

if elukoht == "Saaremaa":
    print("runnime keskas yhtesid")
    age = input("Visesta vanus: ")
    if age == 18:
        print("Palju õnne")
    else:
        if age >= 18:
            print("Sa võid autago sõita")