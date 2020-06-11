phonebook = {}
count = int(input())
while count > 0:
    details = input()
    listDetails = details.split()
    name = listDetails[0]
    number = listDetails[1]
    phonebook.update ( {name : number} )
    count = count -1
try:
    while True:
        searchName = input()
        if searchName in phonebook.keys():
            print(searchName+"="+phonebook[searchName])
        else:
            print("Not found")
except EOFError:
    pass
