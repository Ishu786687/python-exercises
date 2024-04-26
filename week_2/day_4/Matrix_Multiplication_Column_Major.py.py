print("Column-Major Matrix Multiplication")

m1 = [[12, 8, 4],
      [3, 17, 14],
      [9, 8, 10]]
m2 = [[5, 19, 3],
      [6, 15, 9],
      [7, 8, 16]]
m3 = []
print("First Matrix: ",m1)
print("Second Matrix: ",m2)
n = 3
temp = [0, 0, 0]
for i in range(n):
    for j in range (n):
        for k in range(n):
            temp[j] += m1[k][j]*m2[i][k]
    # print(temp)
    m3.append(temp)
    temp = [0, 0, 0]
print("Matrix after multiplication",m3)
      