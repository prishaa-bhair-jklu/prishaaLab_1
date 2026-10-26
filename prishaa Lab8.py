#lab8
#que1
'''s = input("Enter a string: ")

vowels = consonants = digits = spaces = others = 0

for ch in s:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        others += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Others:", others)'''

#que2
'''s = input("Enter a string: ")

result = ""
for i, ch in enumerate(s):
    if i % 2 == 0:
        result += ch.upper()
    else:
        result += ch.lower()

print(result)'''

#que3
'''pw = input()

if len(pw) < 8:
    print("WEAK")
else:
    has_upper = has_lower = has_digit = has_special = False

    for ch in pw:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch != " ":
            has_special = True

    kinds = has_upper + has_lower + has_digit + has_special

    if kinds == 4:
        print("STRONG")
    elif kinds >= 2:
        print("MODERATE")
    else:
        print("WEAK")'''
        
#que4
'''s = input()
c = input()

positions = [str(i) for i, ch in enumerate(s) if ch == c]

print("Count:", len(positions))
if positions:
    print("Positions:", " ".join(positions))
else:
    print("Positions:", -1)'''
    
#que5
'''sentence = input()

lengths = [str(len(word)) for word in sentence.split()]
print(" ".join(lengths))'''

#que6
'''plate = input()

def is_upper(ch):
    return 'A' <= ch <= 'Z'

def is_digit(ch):
    return '0' <= ch <= '9'

valid = (
    len(plate) == 10
    and plate[:2] == "RJ"
    and is_digit(plate[2]) and is_digit(plate[3])
    and is_upper(plate[4]) and is_upper(plate[5])
    and all(is_digit(ch) for ch in plate[6:])
)

print(valid)'''

#que7
'''s = input()

changes = 0
for i in range(len(s) // 2):
    if s[i] != s[len(s) - 1 - i]:
        changes += 1

print("Changes needed:", changes)'''

#que8
'''s = input()

result = ""
seen = set()
for ch in s:
    if ch not in seen:
        seen.add(ch)
        result += ch

print(result)'''

#que9
'''message = input()
k = int(input())

encoded = ""
for ch in message:
    if ch == " ":
        encoded += ch
    else:
        shifted = (ord(ch) - ord('a') + k) % 26
        encoded += chr(shifted + ord('a'))

print(encoded)'''

#que10
s = input()

best_char = s[0]
best_len = 1

run_char = s[0]
run_len = 1

for ch in s[1:]:
    if ch == run_char:
        run_len += 1
    else:
        run_char = ch
        run_len = 1
    if run_len > best_len:
        best_char = run_char
        best_len = run_len

print(best_char, best_len)