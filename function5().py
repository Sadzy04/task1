
array = []
for i in range(5):
    name = input("Enter a name: ")
    number = int(input("Enter a number: "))
    array.append([name, number])
dictionary = {}
for item in array:
    dictionary[item[0]] = item[1]


sorted_dictionary = {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1])}

print(sorted_dictionary)
