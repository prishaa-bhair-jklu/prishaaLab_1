#lab7
#que1
'''s = input("Enter a string: ")

rev_s = ""
for ch in s:
    rev_s = ch + rev_s   

print("Reversed:", rev_s)'''

#que2
'''sen = input("Enter a sentence: ")

words = sen.strip().split()
if words:
    print("Length of last word:", len(words[-1]))
else:
    print("No words entered.")'''
 
    #que3
'''sentence = input("Enter a sentence: ")
word = input("Enter a word to search: ")

if word in sentence:
    print("Word found!")
    print("Occurrences:", sentence.count(word))
else:
    print("Word not found.")'''
    
'''sentence = input("Enter a sentence: ")
word = input("Enter a word to search: ")

n = len(sentence)
m = len(word)
count = 0
i = 0

while i <= n - m:
    match = True
    for j in range(m):
        if sentence[i + j] != word[j]:
            match = False
            break
    if match:
        count += 1
        i += m        # skip past this match
    else:
        i += 1

if count > 0:
    print("Word found!")
    print("Occurrences:", count)
else:
    print("Word not found.")'''
    
#que4
'''text = input("Enter a string: ").lower()

alp = "abcdefghijklmnopqrstuvwxyz"
is_pan = True

for letter in alphabet:
    if letter not in text:
        is_pan = False
        break

if is_pan:
    print("It is a pangram.")
else:
    print("It is not a pangram.")'''
    
#que5
'''text = input("Enter text (English letters only): ")
shift = int(input("Enter shift: "))

result = ""
for ch in text:
    if ch.isupper():
        result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
    elif ch.islower():
        result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
    else:
        result += ch

print("Cipher text:", result)'''

#que6
'''counts = [0, 0, 0, 0, 0]
total = 0

while True:
    n = int(input("Enter a number (1-10, -1 to stop): "))
    if n == -1:
        break
    if 1 <= n <= 10:
        counts[(n - 1) // 2] += 1
        total += 1
    else:
        print("Out of range, ignored.")

if total == 0:
    print("No valid input given.")
else:
    for g in range(5):
        low = 2 * g + 1
        high = low + 1
        pct = counts[g] / total * 100
        hashes = "# " * round(pct / 5)
        print(f"{low} - {high}: {hashes}{pct:.2f} %")'''
        
#que7
'''s = input("Enter a string: ")

is_pal = True
i = 0
j = len(s) - 1
while i < j:
    if s[i] != s[j]:
        is_pal = False
        break
    i += 1
    j -= 1

print("Palindrome" if is_pal else "Not a palindrome")'''

#que8
'''nums = [int(x) for x in input("Enter integers separated by spaces: ").split()]

# i. Sum
total = 0
for x in nums:
    total += x
print("Sum:", total)

# ii. Product
product = 1
for x in nums:
    product *= x
print("Product:", product)

# iii. Smallest
if len(nums) > 0:
    smallest = nums[0]
    for x in nums:
        if x < smallest:
            smallest = x
    print("Smallest:", smallest)
else:
    print("List is empty.")'''
    
#que9
'''nums = [int(x) for x in input("Enter integers separated by spaces: ").split()]

n = len(nums)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if nums[j] < nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print("Descending:", nums)'''

#que10
'''text = input("Enter hyphen-separated words: ")

words = text.split("-")
n = len(words)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if words[j] > words[j + 1]:
            words[j], words[j + 1] = words[j + 1], words[j]

print("-".join(words))'''

