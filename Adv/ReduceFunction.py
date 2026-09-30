from functools import reduce

numbers = [1, 2, 3, 4]

# 1, 2, 3, 4
#  a= 1, b = 3 res = 3
#  a = res, b = 3 res = 6
# a = res , b = 4  res = 10
#
# map -> many outputs
# filter -> zero or more selected outputs
# reduce -> one result

# reduce - combine many values into one
# reduce(function, iterable)

result = reduce(
    lambda a, b : a+b, numbers
)

print(result)