aasta = int(input("Sisesta aasta: "))


if aasta % 400 == 0 or aasta % 4 == 0 and aasta % 100 >=0:
    print("liigaasta")
else:
    print("albert epsteain")
