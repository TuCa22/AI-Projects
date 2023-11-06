import matplotlib.pyplot as plt

x = float(input('Nhập giá trị của x = '))

hor = []        
ver = []

def f(x):
    return float(3*x**3 - 7)

def df(x):
    return float(9*x**2)

for i in range(1,1000,10):
    x_next = float(x - f(x) / df(x))
    x = x_next
    hor.append(i)
    ver.append(x_next)

plt.plot(hor,ver)    
plt.xlabel("Số lần lặp n")
plt.ylabel("Gía trị x_n")
plt.title("Mối quan hệ giữa x_n và n")
plt.show()
