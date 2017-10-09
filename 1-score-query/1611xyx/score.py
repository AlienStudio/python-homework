#coding=utf-8

import xlrd
import time
import sys
student_list = []
number_of_students = 0
subject = 0
score_mode = 0
score_list = []
Subpage = 0
table = 0

#程序开始时读取表格和学生列表
def read():
	global student_list,number_of_students,table
	data = xlrd.open_workbook('score.xls')
	table = data.sheet_by_index(0)
	number_of_rows = table.nrows
	number_of_cols = table.ncols
	for i in range(1, number_of_rows):
		student_list.append(table.cell(i,0).value)
	number_of_students = len(student_list)
	

#对输入进行初步分类
def catalog(Input):
	global subject,Subpage,score_mode
	if (Input == '语文' or Input == '数学' or Input == '英语') and (Subpage == 0):
		subject = Input
		score_subject(Input)
		score_mode = '原始'
		output_subject()
		Subpage = 1
	elif (Input == 'Asc' or Input == 'Desc' or Input == 'Return') and (Subpage == 1):
		sort(Input)
		score_list[:] = []
		Subpage = 0
	elif (Input in str(student_list)) and (Subpage == 0):
		Input = int(Input)
		score_student(Input)
		output_student()
		score_list[:] = []
	elif Input == 'exit':
		exit()
	else:
		print('输入错误，请重试')
	time.sleep(1)

def score_student(Input):
	global student_list,score_list
	Index = student_list.index(Input)
	for i in range(5):
		score_list.append(table.cell(Index+1,i).value)

def score_subject(Input):
	global score_list,number_of_students
	if Input == '语文':
		for i in range(1,number_of_students+1):
			score_list.append(table.cell(i,2).value)
	elif Input == '数学':
		for i in range(1,number_of_students+1):
			score_list.append(table.cell(i,3).value)
	elif Input == '英语':
		for i in range(1,number_of_students+1):
			score_list.append(table.cell(i,4).value)
			
def output_student():
	global score_list
	print('学号： %d' % score_list[0])
	print('姓名：'),;print(score_list[1])
	print('语文成绩： %d' % score_list[2])
	print('数学成绩： %d' % score_list[3])
	print('英语成绩： %d' % score_list[4])

def output_subject():
	global subject,score_mode,number_of_students,student_list,score_list
	print('%s科目%s成绩:' %(subject,score_mode))
	print('学号     成绩')
	for i in range(number_of_students):
		print('%d %d' %(student_list[i],score_list[i]))

#排序成绩并输出，兼并返回语句
#python有自带的列表排序，但是为了让学号列表也一起排序还是用了手动的
def sort(Input):
	global score_list,score_mode,Subpage
	if Input == 'Asc':
		for i in range(0, len(score_list)):
			for j in range(0,len(score_list)-i-1):
				if score_list[j] > score_list[j+1]:
					t = score_list[j]
					score_list[j] = score_list[j+1]
					score_list[j+1] = t
					p = student_list[j]
					student_list[j] = student_list[j+1]
					student_list[j+1] = p
		score_mode = '升序'
		output_subject()
	elif Input == 'Desc':
		for i in range(0, len(score_list)):
			for j in range(0,len(score_list)-i-1):
				if score_list[j] < score_list[j+1]:
					t = score_list[j]
					score_list[j] = score_list[j+1]
					score_list[j+1] = t
					p = student_list[j]
					student_list[j] = student_list[j+1]
					student_list[j+1] = p
		score_list.sort()
		score_list.reverse()
		score_mode = '降序'
		output_subject()
	elif Input == 'Return':
		Subpage = 0
					
#本来想搞点恶作剧，搞个溢出或者崩溃什么的，不过发现python简直固若金汤，遂放弃，直接正常退出
def exit():
	print('最后祝您')
	time.sleep(0.8)
	print('提前射精')
	time.sleep(0.8)
	print('再见')
	time.sleep(1)
	sys.exit(1)	
		
if __name__ == '__main__':

	print('听说要有欢迎界面？一个作业做什么欢迎界面了啦，又没人看')
	read()
	time.sleep(1)
	while 1:
		if Subpage == 0:
			print('输入学号查询成绩，输入科目(语文/数学/英语)查询单科全部成绩，输入exit退出')
		else:
			print('输入Asc/Desc进行升/降序排列，输入Return返回，exit退出')
		Input = raw_input('')
		catalog(Input)