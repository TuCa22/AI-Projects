#Bài 1b: Viết hàm tính giai thừa sử dụng vòng While

n = int(input("Nhập số n: "))
def fac(n):
    if n == 0:
        return 1
    a = 1
    i = 1
    while i <= n:
        a *= i
        i += 1
    return a
print("Giai thừa của n là: ",n,"! = ",fac(n))