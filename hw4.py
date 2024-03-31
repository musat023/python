lamps = list(input())

for i in range(1, len(lamps)-1):
    if lamps[i-1] == 'O' and lamps[i] == 'O' and lamps[i+1] == 'O':
        lamps[i] = '-'

print(''.join(lamps))