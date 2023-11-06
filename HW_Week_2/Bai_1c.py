#Bài 1c: Viết hàm tính giai thừa sử dụng đệ quy

n = int(input("Nhập số n: "))
def fac(n):
    if n == 0:
        return 1
    return n * fac(n - 1)
print("Giai thừa của n là: ",n,"! = ",fac(n))