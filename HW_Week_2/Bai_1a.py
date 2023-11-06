#Bài 1a: Viết hàm tính giai thừa sử dụng vòng For

n = int(input("Nhập số n: "))
def fac(n):
    if n == 0:
        return 1
    a = 1
    for i in range(1,n+1):
        a = a * i
    return a
print("Giai thừa của n là: ",n,"! = ",fac(n))