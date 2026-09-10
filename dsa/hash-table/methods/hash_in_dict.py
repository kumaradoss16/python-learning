phonebook = {}
phonebook["Alice"] = "555-0100"
phonebook["Bob"] = "555=0142"

print(phonebook.get("Alice"))
print("Charlie" in phonebook)
del phonebook["Bob"]
print(phonebook.get("Bob"))