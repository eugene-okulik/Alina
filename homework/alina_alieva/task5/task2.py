str1 = "результат операции: 42"
str2 = "результат операции: 514"
str3 = "результат работы программы: 9"

add_number = 10
result1 = str1.find(":")
result2 = str2.find(":")
result3 = str3.find(":")

number = (str1.index(":")) + 1
number2 = (str2.index(":")) + 1
number3 = (str3.index(":")) + 1
res = int(str1[number:]) + add_number
res2 = int(str2[number2:]) + add_number
res3 = int(str3[number3:]) + add_number
print(res, res2, res3)
