import re

countPasswords = int(input())
passArr = []
resultArr = []
for i in range(0, countPasswords):
    passArr.append(input())

for item in passArr:
    if re.search(r'a...55661', item):
        resultArr.append(item)

print(resultArr)
