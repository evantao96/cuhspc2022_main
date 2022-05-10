def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

wordToNum = {'heaven':1, 'life':0, 'earth':2}
numToWord = {1:'heaven', 0:'life', 2:'earth'}

line1 = input()
line2 = input().split()
line3 = input().split()

num1 = ''.join([str(wordToNum[char]) for char in line2])
num2 = ''.join([str(wordToNum[char]) for char in line3])

num1 = int(num1, 3)
num2 = int(num2, 3)
sum = num1 + num2
sum = numberToBase(sum, 3)

ans = ' '.join([numToWord[digit] for digit in sum])
print(ans)
