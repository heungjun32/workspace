matrix_x= [[2, 5], [1, 1]]
result = [col for col in zip(*matrix_x)]
print(result)

a = []
for t in zip(*matrix_x):
    for i in (*t):
        result2 = a.append(i)
print(result2)

