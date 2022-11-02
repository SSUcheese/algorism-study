word = input()

word = word.upper()
alphabet = [0] * 26
count = 0

for i in word:
    alphabet[ord(i)-65] += 1

significant = max(alphabet)

for i in range(len(alphabet)):
    if significant == alphabet[i]:
        sig_index = i
        count += 1

if count > 1:
    print("?")
else:
    print(chr(sig_index+65))
