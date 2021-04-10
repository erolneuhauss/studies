#!/usr/bin/env python

print('--- 1. Cell ---')
for i in range(5):
    print('Jimmy Five Times ' + str(i))

print('\n--- 2. Cell ---')
total = 0
for num in range(101):
    total = total + num
print(total)

print('\n--- 3. Cell ---')
# Gauss
# 0 + 1 + 2 + 3 + 4 + 5 + 6 + 7
count = 1
total = 0
while count < 101:
    total = total + count
    count = count + 1
print(total)

print('\n--- 4. Cell ---')
count = 0
while count < 5:
    print('Jimmy Five Times ' + str(count))
    count = count + 1
