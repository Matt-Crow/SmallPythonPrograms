oldData = [[1,2,3, 4, 5],[1,2,3, 4, 5],[1,2,3, 4, 5],[1,2,3, 4, 5],[1,2,3, 4, 5]]
newData = []
rows = 1;
for column in oldData:
    rows *= len(column)

for column in range(0, rows):
    newData.append([])
    for i in range(0, len(oldData)):
        newData[column].append(0)

period = 1
for col in range(0, len(oldData)):
    spaceInPeriod = int(rows / period)
    for row in range(0, rows):
        newData[row][col] = oldData[col][int(row / (spaceInPeriod / len(oldData[col])) % len(oldData[col]))]
    period *= len(oldData[col])

for row in newData:
    print(row)
