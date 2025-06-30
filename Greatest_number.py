n = int(input("How many numbers? "))
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
if len(numbers) != n:
    print(f"Expected {n} numbers, but got {len(numbers)}.")
number = numbers[0]
for num in numbers[1:]:
    if num>number:
        number=num
        print('The greatest number is ',number)