from math import ceil
points = int(input())
pointers = []
for i in range(points):
  pointers.append([int(x) for x in input().split()])
# print(pointers)

forth=0
back = 0

for i in range(len(pointers)):
  forth += pointers[i][0] * pointers[i-1][1]
for i in range(len(pointers)):
  back += pointers[i][1] * pointers[i-1][0]
print(ceil(abs(forth-back)/2))
