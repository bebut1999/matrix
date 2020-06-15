
from algorithms import func1


no_of_rows = int(input("Enter the number of rows:"))
no_of_columns = int(input("Enter the number of columns:"))

matrix=[]
print("Enter the entries rowwise:")

for i in range(no_of_rows):
    a=[]
    for j in range(no_of_columns):
        a.append(int(input()))
    func1(a)    
    matrix.append(a)
     

for i in range(no_of_rows):
    for j in range(no_of_columns):
        print(matrix[i][j], end = " ")
    print()    
    
    