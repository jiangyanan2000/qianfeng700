l1 = [1, 2, 3, 4, ['alex']]
l2 = l1[::]
l1[-1].append(666)
print(l2)