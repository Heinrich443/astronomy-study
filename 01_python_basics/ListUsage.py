import operator

list = ['ab', 'cd', 'ef', 'gh', 'ij']
list += ['kl']
print(list)

list.append('mn')
print(list)

del list[5]
print(list)

list.remove('cd')
print(list)

a = ['1', '2', '3', '4']
b = ['a', 'b', 'c', 'd']
c = ['a', 'b', 'c', 'd']
x = [a, b]
print(x)
print(x[0][1])

# list comparison
print(operator.eq(a, b))
print(operator.eq(b, c))

# list functions
print(len(x))
print(max(b))
c.reverse()
print(c)            # return c reverse
print(c.reverse())  # return None
list.sort()
print(list)         # return list sort
print(list.sort())  # return None