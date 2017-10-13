import xlrd
score_list = []
score_per = []
x=0
if __name__ == '__main__':
    data = xlrd.open_workbook('score.xlsx')
    table = data.sheet_by_index(0)
    number_of_rows = table.nrows
    number_of_cols = table.ncols
    number_of_students = 0
    for i in range(1, number_of_rows):
        for o in range(1, number_of_cols+1):            
            score_per.append(table.cell(i,x).value)
            x+=1
        score_list.append(score_per)
        number_of_students+=1
        score_per=[]
        x=0
        i+=1    
student_list = [row[0]for row in score_list]
print(student_list)
print("Hello, World!")
student = int(input("The student number is: "))
num=student_list.index(student)
print("The student's score is:")
print(score_list[num])