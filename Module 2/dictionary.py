contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Carmen": "555-8765"
}

# print(contacts)

# print(type(contacts))
# k = "Alice"
# print(contacts[k])
# print(contacts["Bob"])

# print(contacts['alice'])
# if "alice" in contacts:
#     print(contacts['alice'])
# else:
#     print("Not found")
    
# print(contacts.get('alice', 'not found'))

contacts['David'] = '555-0001'
contacts['Alice'] = '555-0000'
contacts['alice'] = '333-2222'
print(contacts)

# del contacts['alice']
# print(contacts)

# removed = contacts.pop('alice','error on key')
# print(removed)

# allKeys = contacts.keys()
# print(allKeys)
# print(type(allKeys))

# allValues = contacts.values()
# print(allValues)
# print(type(allValues))

allItems = contacts.items()
print(allItems)
print(type(allItems))

for k in contacts.keys():
    print(k)
for v in contacts.values():
    print(v)
for i in contacts.items():
    print (i)
for k, v in contacts.items():
    print(f'The key {k}, the Value {v}')