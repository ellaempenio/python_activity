numbers = (1, 4, 7, 10, 13, 16)
total = 0
count = 0

for number in numbers:
    if number % 2 == 0:
        total += number
        count += 1

if count > 0:
    average = total / count
    print("Average of even numbers:", average)
else:
    print("No even numbers found")