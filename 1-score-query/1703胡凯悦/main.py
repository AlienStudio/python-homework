# coding:utf-8
# Created by ncj on 2017-9-25

# 如果报错module not found，你需要打开命令行输入pip install xlrd. 对于其他包也是如此
import xlrd

# 声明一个列表用来存放学生成绩
score_list = []

# 此处相当于java的public static void main(){}
# 此处也相当于C++的int main(){}
# 也就是一个python程序的最主要部分，整个程序从这里开始执行
# 一个python程序可以由很多函数、对象和.py文件组成，但下面的这句话只能出现一次
if __name__ == '__main__':

    # 打开一个文件，此时变量data就是'score.xls'的全部内容
    # sheet_by_index 即根据下标获取工作表，此处获取了文件中的第一个工作表
    # 不知道table和sheet的区别的同学请复习一下excel
    data = xlrd.open_workbook('score.xls')
    table = data.sheet_by_index(0)

    # 得到工作表的行数和列数，便于接下来的循环读取
    number_of_rows = table.nrows
    number_of_cols = table.ncols
    number_of_students = 0

    # 循环读入所有学生成绩，每次循环学生数+1，append即将成绩添加到score_list列表中
    for i in range(1, number_of_rows):
        score_list.append(table.cell(i,2).value)
        number_of_students += 1

    print('排序之前:')
    print(score_list)

    # 冒泡排序python版本
    # range(i,j) 实际循环是i,i+1,i+2...j-1
    for i in range(0, len(score_list)):
        for j in range(0,len(score_list)-i-1):
            if score_list[j] > score_list[j+1]:
                t = score_list[j]
                score_list[j] = score_list[j+1]
                score_list[j+1] = t

    print('升序排序之后:')
    print(score_list)



# 思考：print()也是一个函数，为什么不import任何东西的情况下就可以使用，
# 而xlrd.open_workbook('score.xls')这种函数在不import的情况下就不能使用？