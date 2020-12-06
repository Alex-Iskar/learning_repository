# Поиск наибольшей цифры в числе
m = 0
nums = input("Введите целое положительное число: ")
n = int(len(nums)) - 1
while n >= 0:
    if int(nums[n]) > m:
        m = int(nums[n])
    n -= 1
print(m)
