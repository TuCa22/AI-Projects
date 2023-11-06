#Bài 2a: Plot mối quan hệ giữa chiều dài và chiều rộng đài hoa của giống Setosa

import matplotlib.pyplot as plt     #Import thư viện matplotlib.pyplot
import pandas as pd                 #Import thư viện pandas

iris = pd.read_csv(r'D:/Programming/Python/Projects/HW_Week_2/iris.csv')    #Đặt biến iris lưu dữ liệu của file CSV

iris_setosa = iris[iris['variety'] == 'Setosa']       #Lọc các dữ liệu của các cột có variety là Setosa
print(iris_setosa)        #In dữ liệu đã lọc có variety là Setosa

x = iris_setosa['sepal.width']      #Biến x lưu dữ liệu của cột sepal.width
y = iris_setosa['sepal.length']     #Biến y lưu dữ liệu của cột sepal.length

plt.scatter(x,y, color ='green', marker ='x')        #Vẽ đồ thị scatter cho biến x, y
plt.title('Mối quan hệ giữa chiều dài và chiều rộng đài hoa của giống Setosa')
plt.xlabel('Chiều rộng đài hoa')
plt.ylabel('Chiều dài đài hoa')
plt.show()      #Hiển thị đồ thị scatter