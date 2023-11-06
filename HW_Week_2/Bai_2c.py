#Bài 2c: Lưu lại thông tin chiều dài và chiều rộng cánh hoa của giống Versicolor vào file versicolor.csv

import pandas as pd           
import _csv

iris = pd.read_csv(r'D:/Programming/Python/Projects/HW_Week_2/iris.csv')        #Đọc dữ liệu file iris.csv

iris_petal = pd.DataFrame(iris, columns = ['petal.length', 'petal.width', 'variety' ])      #Lưu dữ liệu được lọc sang dạng DataFrame 
iris_versicolor = iris_petal[iris_petal['variety'] == 'Versicolor']         #Lưu và lọc dữ liệu với variety là Versicolor
print(iris_versicolor)

iris_versicolor.to_csv('D:/Programming/Python/Projects/HW_Week_2/versicolor.csv', index = False)        #Ghi dữ liệu mới vào địa chỉ chứa file versicolor.csv