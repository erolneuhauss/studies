length = 3
grin = '😁'
spaces = '😱'
for line in range(length):
    for space in range(length - line):
        print(spaces, end='')
    print(grin)
    grin += '😁😁'
    
