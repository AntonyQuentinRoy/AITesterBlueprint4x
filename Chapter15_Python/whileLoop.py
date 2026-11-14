count = 1
while count <= 5:
    print(count)
    count += 1
#Output: 1,2,3,4,5

count = 0
while count < 5:
    print("Count is: " + str(count))
    count += 1
#Output: 0,1,2,3,4


for i in range(5):
    print("Count is: " + str(i))
    #Output: 0,1,2,3,4  

for i in range(1, 6):
    if  i == 3:
        continue
    print(i)
#Output: 1,2,4,5

for i in range(1, 3):
    for j in range(1, 4):
        print(i, j)
#Output: 1 1, 1 2, 1 3, 2 1, 2 2, 2 3

for number in [2,4,6]:
    if number == 5:
        break
else:
    print("5 is not found in the list")
#Output: 5 is not found in the list

# for i in range(1, 6):
#     if i == 3:
#         break
# else:
#     continue

for i in range(101):
    if (i% 2 == 0):
        print(i)
        #Output: 0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90

