#lab9
#que1
'''numbers = list(map(int, input().split()))
even=[]
odd=[]

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print("Even:", even)
print("Odd:", odd)'''

#que2
'''sentence =input().split()
long_words =[]
for word in sentence:
    if len(word) > 3:
        long_words.append(word)

print(long_words)'''

#que3
'''balls =input().split()
total_runs = 0
wickets = 0
boundaries = 0
runs_per_over = []
current_over_runs = 0
for i in range(len(balls)):
    ball = balls[i]
    if ball == 'W':
        wickets += 1
    else:
        runs = int(ball)
        total_runs += runs
        current_over_runs += runs
        if runs == 4 or runs == 6:
            boundaries += 1
    if (i + 1) % 6 == 0 or i == len(balls) - 1:
        runs_per_over.append(current_over_runs)
        current_over_runs = 0

print("Total Runs:", total_runs)
print("Wickets:", wickets)
print("Boundaries:", boundaries)
print("Runs per over:", runs_per_over)'''

#que4
'''numbers =list(map(int, input().split()))
largest = numbers[0]
smallest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
       smallest = num
print("Largest:", largest)
print("Smallest:", smallest)'''

#que5
'''words =input().split()
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
print(longest)'''

#que6
'''menu_items =input().split()
prices = list(map(int, input().split()))
orders = input().split()
total_bill = 0
for i in range(len(menu_items)):
    item = menu_items[i]
    qty = orders.count(item)
    if qty > 0:
        cost = qty * prices[i]
        total_bill += cost
        print(f"{item} x {qty} = {cost}")
print("Total:", total_bill)'''

#que7
'''words =input().split()
reversed_words = []
for word in words:
    reversed_words.append(word[::-1])
print(" ".join(reversed_words))'''

#que8
'''text =input()
digits =[]
for char in text:
    if char.isdigit():
        digits.append(int(char))
print(digits)
print("Sum:", sum(digits))'''

#que9
'''n =int(input())
seen_names = []
for _ in range(n):
    first, last = input().split()
    base_name = f"{first.lower()}.{last.lower()}"
    seen_names.append(base_name)
    count = seen_names.count(base_name)
    if count == 1:
        print(f"{base_name}@jklu.edu.in")
    else:
        print(f"{base_name}{count}@jklu.edu.in")'''
        
#que10
'''numbers =list(map(int, input().split()))
non_zeros =[]
zeros = []
for num in numbers:
    if num == 0:
        zeros.append(num)
    else:
        non_zeros.append(num)
result = non_zeros + zeros
print(result)'''









