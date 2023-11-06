#Bài 2b: Plot mối quan hệ giữa chiều dài và chiều rộng cánh hoa của giống Versicolor

import matplotlib.pyplot as plt
import pandas as pd           

iris = pd.read_csv(r'D:/Programming/Python/Projects/HW_Week_2/iris.csv')

iris_versicolor = iris[iris['variety'] == 'Versicolor']
print(iris_versicolor)

x = iris_versicolor['petal.width']      
y = iris_versicolor['petal.length']     

plt.scatter(x,y, color ='orange')        
plt.title('Mối quan hệ giữa chiều dài và chiều rộng cánh hoa của giống Versicolor')
plt.xlabel('Chiều rộng đài hoa')
plt.ylabel('Chiều dài đài hoa')
plt.show()      