data = list(map(int, input().split()))
sorted = sorted(data)

if data == sorted:
    print("ascending")
elif data == sorted[::-1]:
    print("descending")
else:
    print("mixed")

# 두 번째 방법
ascending = True
descending = True
    
for i in range(len(data) - 1):
    if data[i] < data[i+1]:
        descending = False
    else:
        ascending = False

if descending:
    print("descending")
elif ascending:
    print("ascending")
else:
    print("mixed")