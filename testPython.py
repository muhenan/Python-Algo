

print("hello")

a = 1
b = 2
c = 3

# b, a = c, b
a, b = b, a

print(a,b,c)


res = ["", ""] * 5
print(res)

res = ["" for i in range(5)] # quicker
print(res)