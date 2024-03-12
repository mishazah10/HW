def min_n_variables(elements):
    second = elements[0]
    for x in elements:
      if x < second:
       second = x
    return second

elements = [4,7,2,8,9,3]
print('second of elements=', min_n_variables(elements))