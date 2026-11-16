#lab10
#que1
'''nums = list(map(int, input().split()))
v = int(input())
t = tuple(nums)
print("Tuple:", t)
print("Length:", len(t))
print(f"Count of {v}:", t.count(v))
print(f"First index of {v}:", t.index(v))'''

#que2
'''def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
text = input()
print("Vowels:", count_vowels(text))'''

#que3
'''votes = input().split()
counts = {}
for name in votes:
    counts[name] = counts.get(name, 0) + 1
for name, count in counts.items():
    print(f"{name}: {count}")
winner = ""
max_votes = -1
for name, count in counts.items():
    if count > max_votes:
        max_votes = count
        winner = name
print("Winner:", winner)'''

#que4
'''word = input()
freq = {}
for char in word:
    freq[char] = freq.get(char, 0) + 1
print(freq)'''

#que5
'''def simple_interest(p, r, t=1):
    return p * r * t / 100
p = float(input())
r = float(input())
print("1 year:", simple_interest(p, r))
print("3 years:", simple_interest(p, r, 3))'''

#que6
'''def get_grade(marks):
  if marks >= 80:
    return 'A'
  elif marks >= 60:
    return 'B'
  elif marks >= 40:
    return 'C'
  else:
    return 'F'
n = int(input())
grade_count = {}
for _ in range(n):
  name, marks = input().split()
  marks = int(marks)
  grade = get_grade(marks)
  print(f'{name}: {grade}')
  grade_count[grade] = grade_count.get(grade, 0) + 1
print('Grade count:')
print(grade_count)'''

#que7
'''numbers = tuple(map(int, input().split()))
even_numbers = tuple(x for x in numbers if x % 2 == 0)
print(even_numbers)'''

#que8
'''n = int(input())
capitals = {}
for _ in range(n):
  country, capital = input().split()
  capitals[country] = capital
query = input().strip()
print(capitals.get(query, 'Not found'))'''

#que9
'''n = int(input())
stock = {}
for _ in range(n):
  item, qty = input().split()
  stock[item] = int(qty)
q = int(input())
for _ in range(q):
  action, item, qty = input().split()
  qty = int(qty)

  if action == 'SELL':
    if stock[item] < qty:
      print(f'Insufficient stock: {item}')
    else:
      stock[item] -= qty
  elif action == 'ADD':
    stock[item] = stock.get(item, 0) + qty

for item, qty in stock.items():
  print(f'{item} {qty}')'''
  
#que10
'''def stats(nums):
  smallest = min(nums)
  largest = max(nums)
  average = sum(nums) / len(nums)
  return (smallest, largest, average)
nums = list(map(int, input().split()))
print(stats(nums))'''


