# demonstrate hashtable usage


# TODO: create a hashtable all at once
item1 = dict({"key1" : 1, "key2" : 2, "key3" : 3})
print(item1)

# TODO: create a hashtable progressively
item2 = {}
item2["ade"] = 2
item2["bola"] = 1
item2["tope"] = 3
print(item2)

# TODO: try to access a nonexistent key
# print(item1["key7"])

# TODO: replace an item
item1["key2"] = "two"
print(item1)

# TODO: iterate the keys and values in the dictionary
for key, value in item2.items():
    print("key: ", key , "Value:", value)