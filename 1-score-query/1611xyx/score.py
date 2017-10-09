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

#����ʼʱ��ȡ����ѧ���б�
def read():
	global student_list,number_of_students,table
	data = xlrd.open_workbook('score.xls')
	table = data.sheet_by_index(0)
	number_of_rows = table.nrows
	number_of_cols = table.ncols
	for i in range(1, number_of_rows):
		student_list.append(table.cell(i,0).value)
	number_of_students = len(student_list)
	

#��������г�������
def catalog(Input):
	global subject,Subpage,score_mode
	if (Input == '����' or Input == '��ѧ' or Input == 'Ӣ��') and (Subpage == 0):
		subject = Input
		score_subject(Input)
		score_mode = 'ԭʼ'
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
		print('�������������')
	time.sleep(1)

def score_student(Input):
	global student_list,score_list
	Index = student_list.index(Input)
	for i in range(5):
		score_list.append(table.cell(Index+1,i).value)

def score_subject(Input):
	global score_list,number_of_students
	if Input == '����':
		for i in range(1,number_of_students+1):
			score_list.append(table.cell(i,2).value)
	elif Input == '��ѧ':
		for i in range(1,number_of_students+1):
			score_list.append(table.cell(i,3).value)
	elif Input == 'Ӣ��':
		for i in range(1,number_of_students+1):
			score_list.append(table.cell(i,4).value)
			
def output_student():
	global score_list
	print('ѧ�ţ� %d' % score_list[0])
	print('������'),;print(score_list[1])
	print('���ĳɼ��� %d' % score_list[2])
	print('��ѧ�ɼ��� %d' % score_list[3])
	print('Ӣ��ɼ��� %d' % score_list[4])

def output_subject():
	global subject,score_mode,number_of_students,student_list,score_list
	print('%s��Ŀ%s�ɼ�:' %(subject,score_mode))
	print('ѧ��     �ɼ�')
	for i in range(number_of_students):
		print('%d %d' %(student_list[i],score_list[i]))

#����ɼ���������沢�������
#python���Դ����б����򣬵���Ϊ����ѧ���б�Ҳһ�������������ֶ���
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
		score_mode = '����'
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
		score_mode = '����'
		output_subject()
	elif Input == 'Return':
		Subpage = 0
					
#������������磬���������߱���ʲô�ģ���������python��ֱ�����������������ֱ�������˳�
def exit():
	print('���ף��')
	time.sleep(0.8)
	print('��ǰ�侫')
	time.sleep(0.8)
	print('�ټ�')
	time.sleep(1)
	sys.exit(1)	
		
if __name__ == '__main__':

	print('��˵Ҫ�л�ӭ���棿һ����ҵ��ʲô��ӭ������������û�˿�')
	read()
	time.sleep(1)
	while 1:
		if Subpage == 0:
			print('����ѧ�Ų�ѯ�ɼ��������Ŀ(����/��ѧ/Ӣ��)��ѯ����ȫ���ɼ�������exit�˳�')
		else:
			print('����Asc/Desc������/�������У�����Return���أ�exit�˳�')
		Input = raw_input('')
		catalog(Input)