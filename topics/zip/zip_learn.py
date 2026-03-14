for item in zip([1, 2, 3], ['sugar', 'spice', 'everything nice']):
    print(item)

# zip return a zip object instead of a list
# if you want a list, you should convert it to list
my_zip = zip(range(3), ['fee', 'fi', 'fo', 'fum'])
my_list = list(zip(range(3), ['fee', 'fi', 'fo', 'fum']))
print(my_list)

# list(zip(('a', 'b', 'c'), (1, 2, 3), strict=True))
# if you add strict=True option
# python will throw exception if the lengths are different
