import sys
all_data = sys.stdin.read().split('\n')
ugly = 0
count = int(all_data[0])
for i in range(1,count+1):
    pre = int(all_data[i])
    if i == 1:
        if count == 1:
            if pre <= 41:
                ugly += 1
        else:
            if pre <= 41 and int(all_data[i+1]) <= 41:
                ugly += 1
    elif i == count:
        if pre <= 41 and int(all_data[i-1]) <= 41:
            ugly+=1

    else:
        if pre <= 41 and int(all_data[i+1]) <= 41 and int(all_data[i-1]) <= 41:
            ugly += 1
print(ugly)
