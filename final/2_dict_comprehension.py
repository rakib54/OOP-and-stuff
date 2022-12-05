data={1:[2,3,4,5],2:[1,3,4,5],3:[1,2,4,5],4:[1,2,3,5],5:[1,2,3,4]}

data = {key: [val for val in range(1, 6) if val != key] for key in range(1, 6)}
print(data)
