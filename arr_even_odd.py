# python program to find total number of odd and even elements in a list.

# list1 = [2,3,4,5,6,7,8,9,34,54,33,12]
# even = 0
# odd = 0
# for i in list1:
#     if i%2==0:
#         even = even+1
#     else:
#         odd = odd+1
# print("Even number in list ",even)
# print("odd number in list",odd)
        
        
#  *************  Second Method ***********
list1 = [12,3,4,3,4,4,5,5,6,6,7,5,4,2,4,5,5,3,23,3,5]
for i in list1:
    if i%2==0:
        print("Even Number is")
        print(i)
        
    elif i%2==1:
        print("odd Number is")
        print(i)