# finding maximum number
# a = [1,2,3,4,5]
# max = a[0]
# for i in range(len(a)):
#     if a[i] > max:
#         max = a[i]
# print(max)

# finding minimum number
# a = [1,2,3,4,5]
# min = a[0]
# for i in range(len(a)):
#     if a[i] < min:
#         min = a[i]
# print(min)

# second largest number in ginven array
# a = [1,2,3,4,5]
# max1 = a[0]
# max2 = a[0]

# for i in range(len(a)):
#     if a[i] > max1:
#         max2 = max1
#         max1 = a[i]
#     elif max2 > max1:
#         max2 = max1
        
# print(max2)

# second minimum number in given array
a = [1,2,3,4,5]
l1 = a[0]
l2 = None

for i in a[1:]:
    if i< l1:
        l2 = l1
        l1 = i
    elif l2 is None or l2 > i:
        l2 = i
print(l2)