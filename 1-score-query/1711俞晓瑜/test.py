record_data = []
f = open(".\\score.txt")
data = f.read()
rows = data.split('\n')
number = raw_input ('please input your number: ')
a = 0
while rows[a].find (number, 0, 8) == -1:
    a = a+1
print 'your score is', rows[a][9:11]

for a in range(len(rows)-1):
    for b in range(len(rows)-1-a):
        if rows[b][9:11] > rows[b+1][9:11]:
            rows[b], rows[b+1] = rows[b+1], rows[b]

rowss = ''.join(rows)

print  'the order is'
i=0
while i < len(rows)-1:
   print rowss[i*11:(i+1)*11]
   i = i+1


#第一次写代码 很多写得很勉强
   #有些漏洞
