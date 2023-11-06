#Bai 3a: Sử dụng phương pháp Newton để tính nghiệm gần đúng của phương trình f(x) = 0

def f(x):       #Hàm tính f(x) = 3x^3 - 7
    return float(3*x**3 - 7)

def df(x):      #Hàm tính đạo hàm của f(x) = 3x^3 - 7
    return float(9*x**2)

def newton_method(x, tolerance):        #Hàm tính nghiệm gần đúng theo phương pháp Newton
    for i in range(1,1000):
        x_next = float(x - f(x) / df(x))
        if abs(x - x_next) < tolerance:     #Sai số e < 0.001
            break
        x = x_next
    return x_next

x = float(input('Nhập giá trị ban đầu x0 = '))
tolerance = float(input('Nhập sai số yêu cầu: e < '))
approx_root = newton_method(x, tolerance)
print('Nghiệm gần đúng của phương trình 3x^3 - 7 = 0 là: x = ',approx_root)