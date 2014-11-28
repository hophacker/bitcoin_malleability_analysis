f = open("result.txt",'r')

push_data1 = {}
push_data2 = {}

strings = f.readlines()
for s in strings:
    listStr = s.split(',')
    if listStr[0][:9] == 'PUSHDATA1':
        height = int(listStr[1])
        index = height
        if index in push_data1:
            push_data1[index] = push_data1[index] + 1
        else:
            push_data1[index] = 1
    if listStr[0][:9] == 'PUSHDATA2':
    #print listStr[]
        height = int(listStr[1])
        index = height
        if index in push_data2:
            push_data2[index] = push_data2[index] + 1
        else:
            push_data2[index] = 1


for i in range(270000,290000):
    if i not in push_data1 and i not in push_data2:
        continue

    print i, '\t',

    if i in push_data1:
        print push_data1[i],'\t',
    else:
        print 0,'\t',

    if i in push_data2:
        print push_data2[i]
    else:
        print 0

