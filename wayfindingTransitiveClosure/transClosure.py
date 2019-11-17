file = open("nodeConn.csv")
universalSet = list()
set = dict()
count = 0
pairWasAdded = True
transitiveClosure = 1
split = []
id1 = -1
id2 = -2
for line in file:
    try:
        split = line.strip().split(",")
        id1 = int(split[0])
        id2 = int(split[1])
        if id1 not in universalSet:
            universalSet.append(id1)
            set[id1] = dict()
        if id2 not in universalSet:
            universalSet.append(id2)
            set[id2] = dict()
        set[id1][id2] = True
        count += 1
        #print(id1, "=>", id2)
    except:
        #is header
        pass
file.close()

while pairWasAdded:
    pairWasAdded = False
    for n1 in universalSet:
        for n2 in universalSet:
            for n3 in universalSet:
                if n1 in set and n2 in set[n1] and n2 in set and n3 in set[n2] and not (n1 in set and n3 in set[n1]):
                    pairWasAdded = True
                    set[n1][n3] = True
                    count += 1
    transitiveClosure += 1
    print(transitiveClosure, "transitive closure")

print(len(universalSet), "nodes")
print(count, "connections")
print(transitiveClosure, "transitive closure")
