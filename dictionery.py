# dictionery = A changeable, unordered collection of unique key: value pairs
#               Fast bacausethey use hashing, allow us to access value quickly

capitals = {'USA': 'washinton DC',
            'India': 'New Delhi',
            'China': 'Beijing',
            'Russia': 'Moscow'}

capitals.update({'Germany': 'Berlin'})
capitals.pop('China')
# capitals.clear()

# print(capitals['Russia'])
# print(capitals.get('Germany'))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

for key, value in capitals.items():
    print(key, value)
