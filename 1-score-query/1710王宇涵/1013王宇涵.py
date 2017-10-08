print("Hello! World")
fileName = 'score.txt'
f = open(fileName, 'r')
wordList = f.readlines() #所有文本逐行读入列表wordList
f.close()
titleList = wordList[0].split(',') #标题行特殊处理
wordList = wordList[1:] #数据list剪掉标题行
sList = [] #二维list，存放每个分数
for w in wordList: #遍历文本每一行
    wN = w.split(',') #以','为分隔符，把数据填入wN，wN是一维list
    sN = [] #存放此人的多门成绩
    sN.append(wN[0]) #[0]是学号
    sN.append(wN[1]) #[1]是姓名
    for i in range(2, len(wN)): #遍历此人多门成绩
        sN.append(eval(wN[i])) #字符串转为数字，append入列表sN
    sList.append(sN) #sN数据append入大列表sList
print(sList) 
while True:
    select = input(u""" 
------------------------------------------------------------
   程序：建平中学期中考试成绩查询
   作者：wyh
   日期：2017.10 
   语言：Python
   操作: 请输入1:学号，2：姓名，3：科目  --
   接受命运的制裁吧哈哈哈哈！！！！                                    
------------------------------------------------------------
"""  )
    if select == '1': #输入学号处理
        num = input('请输入学号：')
        for sN in sList:
            if sN[0] == num:
                print(sN)
                break
    elif select == '2': #输入姓名处理
        name = input('请输入姓名：')
        for sN in sList:
            if sN[1] == name:
                print(sN)
    elif select == '3': #输入科目处理
        for i in range(2, len(titleList)): #打印科目编号
            print(i - 1, titleList[i], '\t')
        subNum = eval(input('\n请输入科目编号:'))
        subScList = [] #以下形成指定科目冒泡排序临时list
        for sN in sList:
            sub = []
            sub.append(sN[0])
            sub.append(sN[1])
            sub.append(sN[subNum + 1])
            subScList.append(sub)
        print(subScList)
        while True: #冒泡排序
            flag = 0
            for i in range(len(subScList) - 1):
                if subScList[i][2] < subScList[i + 1][2]:
                    subScList[i], subScList[i + 1] = subScList[i + 1], subScList[i]
                    flag = 1
            if flag == 0:
                break
        for i in range(len(subScList)): #排序结果输出
            print(subScList[i])

    


