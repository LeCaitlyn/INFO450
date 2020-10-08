# Week 4 Notes

# we can store different data types in different keys of a dictionary
# Dictionaries can store 0 or more 'keys'
# Keys must be hashable (can't really change) - strings, numbers, tuple (but NO LISTS!)

d={}
d['colors'] = ['blue', 'green', 'black']
# print(d)

# del d['colors']
# print(d)

# The get function will safely get a key
print(d.get('colors'))



# Looping on Dicts
product = {"product_id":"14322", "name":"65 inch TV","price":499.99}
for key, value in product.items():
    print(f"{key}: {value}")

# A set object is an unordered collection of distinct hashable object 
# (if we wanted to show all items without duplicates)

# q is used as a deafult searchign parameter













