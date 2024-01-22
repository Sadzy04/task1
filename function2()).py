
names = []


for i in range(5):
    name = input("Enter a name: ")
    name = name.replace(" ", "")

    name = name[0].upper() + name[1:].lower()
    name = name[:-2]
    names.append(name)
names.sort()
for i, name in enumerate(names):
    print(f"{i + 1}. {name}")
