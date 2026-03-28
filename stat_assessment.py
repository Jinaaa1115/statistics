import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#--------NUMPY--------

#Q.1

arr = np.array([1,2,3,4,5,6])

# Reshape into 2 rows
result = arr.reshape(2, 3)

print("Result:\n", result)


#Q.2

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

common = np.intersect1d(a, b)

print(" Common elements:", common)


#Q.3

a = np.array([2, 6, 1, 9, 10, 3, 27])

result = a[(a >= 5) & (a <= 10)]

print(" Output:", result)


#Q.4

a = np.arange(15)

np.set_printoptions(threshold=6)

print(" Output:", a)

# Reset 
np.set_printoptions(threshold=1000)


#---------PANDAS-----------

#Q.1

ser = pd.Series(np.random.randint(1, 100, 20))

print(" Statistics:\n", ser.describe())


#Q.2

data = {
    "Name": ["A", "B", "C", "D"],
    "Age": [20, 21, 19, 22],
    "Marks": [85, 90, 78, 88]
}

df = pd.DataFrame(data)

print(" DataFrame:\n", df)


#Q.3

data_np = np.random.randint(1, 50, size=(5,3))

df_np = pd.DataFrame(data_np, columns=["A", "B", "C"])

print(" DataFrame:\n", df_np)


#Q.4

print(" Answer:")
print("Rows default labels: 0,1,2,...")
print("Columns default labels: 0,1,2,...")


#Q.5

df_large = pd.DataFrame({
    "col1": np.random.randint(1,100,10000),
    "col2": np.random.rand(10000),
    "col3": np.random.choice(['A','B','C'],10000)
})

print(df_large)


#Q.6

print(" Shape:", df_large.shape)

 
#Q.7

print(" Head:\n", df_large.head())


#Q.8
col = df_large["col1"]

print("Type:", type(col))


#Q.9

x = [3, 4, 5, 6]
y = [1.5, 2, 2.5, 3]

plt.plot(x, y)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Line Plot")

plt.show()


#Q.10

#This question is not attempted as the plotting styles and advanced visualization concepts have 
# not yet been covered in class. It will be completed after learning the topic.


#Q.11

# Given data
height = [179, 155, 191, 152, 188, 177]
names = ['QA', 'WB', 'EC', 'RD', 'TE', 'YF']

# Create bar plot
plt.bar(names, height)

# Labels and title
plt.title("Height Comparison")
plt.xlabel("Individuals")
plt.ylabel("Height")

plt.show()


#Q.12

#This question is not attempted as histogram variations and detailed visualization 
# techniques are yet to be discussed in class.


#Q.13

#This question is not attempted as TensorFlow and its features have 
# not yet been introduced in the syllabus.


#Q.14

#This question is not attempted as the limitations of TensorFlow 
# have not been covered in class yet.


#Q.15

#This question is not attempted as the concepts of supervised and 
#unsupervised machine learning are yet to be taught.

