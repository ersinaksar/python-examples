n0,n1,n2,n3,n4,n5,n6,n7,n8,n9 = input("Enter ten numbers: ").split()

list1 = [n0, n1, n2, n3, n4, n5, n6, n7, n8, n9]

list2 = list()

for i in list1:
    if i not in list2:
        list2.append(i)

print("The distinct numbers are: ", end=" ")
for i in list2:
    print(i, end=" ")
