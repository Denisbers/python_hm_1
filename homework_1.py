number_input = int(input('enter a four-digit number:'))

digit_1 = number_input // 1000
digit_2 = (number_input // 100) % 10
digit_3 = (number_input % 100) // 10
digit_4 = number_input % 10

print(digit_1)
print(digit_2)
print(digit_3)
print(digit_4)
