
num = int(input("Enter a 4-digit number: "))

thousands = num // 1000
hundreds = (num // 100) % 10
tens = (num // 10) % 10
ones = num % 10


hundreds, tens = tens, hundreds


new_num = (thousands * 1000) + (hundreds * 100) + (tens * 10) + ones

print("After swapping:", new_num)
