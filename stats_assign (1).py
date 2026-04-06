 
import numpy as np
import pandas as pd
import math 

#Q.1:
#given sample :
#3, 2, 5, 4, 7, 2, 3, 3, 1, 6, 4, 2, 3, 5, 2, 4, 2, 1, 3, 5, 6, 3, 2, 1, 4, 2, 4, 5, 3, 2, 7, 2, 3,
#4, 5, 1, 6, 2, 4, 3, 5, 3, 2, 4, 2, 6, 3, 2, 4, 5

data=[3, 2, 5, 4, 7, 2, 3, 3, 1, 6, 4, 2, 3, 5, 2, 4, 2, 1, 3, 5, 6, 3, 2, 1, 4, 2, 4, 5, 3, 2, 7, 2, 3,
4, 5, 1, 6, 2, 4, 3, 5, 3, 2, 4, 2, 6, 3, 2, 4, 5]
#a.  Mean: What is the average rental duration for customers at the car rental company?
mean_duration=np.mean(data)
print("Mean rental duration is ",mean_duration)

#b. Median: What is the typical or central rental duration experienced by customers?
median_duration=np.median(data)
print("Median rental duration is :",median_duration)
#c. Mode: Are there any recurring or most frequently occurring rental durations for customers?
series_data=pd.Series(data)
mode_duration=series_data.mode()[0]
print("Mode rental duration is :",mode_duration)



#Q.2
#Given data :
#3, 5, 2, 4, 6, 2, 3, 4, 2, 5, 7, 2, 3, 4, 2, 4, 2, 3, 5, 6, 3, 2, 1, 4, 2,
#  4, 5, 3, 2, 7, 2, 3, 4, 5, 1, 6, 2, 4, 3, 5, 3, 2, 4, 2, 6, 3, 2, 4, 5, 3

data=[3, 5, 2, 4, 6, 2, 3, 4, 2, 5, 7, 2, 3, 4, 2, 4, 2, 3, 5, 6,
3, 2, 1, 4, 2, 4, 5, 3, 2, 7, 2, 3, 4, 5, 1, 6, 2, 4, 3, 5, 3, 2, 4, 2, 6, 3, 2, 4, 5, 3]
array_data=np.array(data)
#a. Range: What is the range of the delivery times?

data_range=np.max(array_data)-np.min(array_data)
print("Range is :",data_range)

#b. Variance: What is the variance of the delivery times?

variance_time=np.var(array_data)
print("variance of delivery time is :",variance_time)

#c. Standard Deviation: What is the standard deviation of the delivery times?

std_time=np.std(array_data)
print("Standard deviation of delivery time is :",std_time)



#Q.3
#Given data :
#$120, $150, $110, $135, $125, $140, $130, $155, $115, $145, $135, $130

data=np.array([120, 150, 110, 135, 125, 140, 130, 155, 115, 145, 135, 130])

#a. Measure of Central Tendency: What is the average monthly revenue for the product?

avg_revenue=np.mean(data)
print("average monthly revenue is :",avg_revenue)

#b. Measure of Dispersion: What is the range of monthly revenue for the product?

range_revenue=np.max(data)-np.min(data)
print("Range of monthly revenue is :",range_revenue)



#Q.4
#Given Data :
#Model A: 30, 32, 33, 28, 31, 30, 29, 30, 32, 31,
#Model B: 25, 27, 26, 23, 28, 24, 26, 25, 27, 28,
#Model C: 22, 23, 20, 25, 21, 24, 23, 22, 25, 24,
#Model D: 18, 17, 19, 20, 21, 18, 19, 17, 20, 19,
#Model E: 35, 36, 34, 35, 33, 34, 32, 33, 36, 34

model_A = np.array([30,32,33,28,31,30,29,30,32,31])
model_B = np.array([25,27,26,23,28,24,26,25,27,28])
model_C = np.array([22,23,20,25,21,24,23,22,25,24])
model_D = np.array([18,17,19,20,21,18,19,17,20,19])
model_E = np.array([35,36,34,35,33,34,32,33,36,34])

models = {
    "Model A": model_A,
    "Model B": model_B,
    "Model C": model_C,
    "Model D": model_D,
    "Model E": model_E
}

for name, data in models.items():
    print(name)
    #a. Measure of Central Tendency: What is the average fuel efficiency for each vehicle model?
    mean = np.mean(data)
    print("Mean:", mean)
    
    #b. Measure of Dispersion: What is the range of fuel efficiency for each vehicle model?
    data_range = np.max(data) - np.min(data)
    print("Range:", data_range)
    
    #c. Measure of Dispersion: What is the variance of the fuel efficiency for each vehicle model?
    variance = np.var(data)
    print("Variance:", variance)



#Q.5

import matplotlib.pyplot as plt

defects = ['A','B','C','D','E','F','G']
frequency = [30,40,20,10,45,25,30]

#a. Bar Chart: Create a bar chart to visualize the frequency of different defect types

plt.bar(defects, frequency)
plt.title("Defect Frequency")
plt.xlabel("Defect Type")
plt.ylabel("Frequency")
plt.show()

# Most common defect: Which defect type has the highest frequency?
max_defect = defects[frequency.index(max(frequency))]
print("Most common defect:", max_defect)

# Histogram: Create a histogram to represent the defect frequencies.
plt.hist(frequency)
plt.title("Histogram of Defects")
plt.show()



#Q.6
 
data = [4, 5, 3, 4, 4, 3, 2, 5, 4, 3, 5, 4, 2, 3, 4, 5, 3, 4, 5, 3, 4, 3, 2, 4, 5, 3, 4, 5, 4, 3, 3, 4, 5,
2, 3, 4, 4, 3, 5, 4, 3, 4, 5, 4, 2, 3, 4, 5, 3, 4, 5, 4, 3, 4, 5, 3, 4, 5, 4, 3, 3, 4, 5, 2, 3, 4,
4, 3, 5, 4, 3, 4, 5, 4, 2, 3, 4, 5, 3, 4, 5, 4, 3, 4, 5, 3, 4, 5, 4, 3, 3, 4, 5, 2, 3, 4, 4, 3, 5,
4]

 
df = pd.DataFrame({"Data": data})

 
#a. Skewness: Calculate the skewness of the satisfaction ratings.
 
skew=df["Data"].skew()
print("Skewness:",  skew)

#b. Kurtosis: Calculate the kurtosis of the satisfaction ratings.
 
kurt=df["Data"].kurt()
print("Kurtosis:",  kurt)



#Q.7

arr = np.array([55, 60, 62, 65, 68, 70, 72, 75, 78, 80, 82, 85, 88, 90, 92, 95, 100, 105, 110, 115,
120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195,
200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275,
280, 285, 290, 295, 300, 305, 310, 315, 320, 325, 330, 335, 340, 345, 350, 355,
360, 365, 370, 375, 380, 385, 390, 395, 400, 405, 410, 415, 420, 425, 430, 435,
440, 445, 450, 455, 460, 465, 470, 475, 480, 485, 490, 495, 500, 505, 510, 515])

#a. Quartiles: Calculate the first quartile (Q1), median (Q2), and third quartile (Q3) of the weight distribution
Q1 = np.percentile(arr, 25)
Q2 = np.percentile(arr, 50)
Q3 = np.percentile(arr, 75)
print(arr.size)
print("Q1:", Q1)
print("Median (Q2):", Q2)
print("Q3:", Q3)

#b. Percentiles: Calculate the 15th percentile, 50th percentile, and 85th percentile of the weight distribution
p15 = np.percentile(arr, 15)
p50 = np.percentile(arr, 50)
p85 = np.percentile(arr, 85)

print("15th percentile:", p15)
print("50th percentile:", p50)
print("85th percentile:", p85)



#Q.8

hours = [10,12,15,18,20,22,25,28,30,32,35,38,40,42,45,48,50,52,55,58,60,62,65,68,70,72,75,78,80,82]
scores = [60,65,70,75,80,82,85,88,90,92,93,95,96,97,98,99,100,102,105,106,107,108,110,112,114,115,116,118,120,122]

#Calculate the correlation coefficient between the hours spent studying and the
#exam scores. Interpret the value of the correlation coefficient and explain the
#nature of the relationship between studying hours and exam scores

corr = np.corrcoef(hours, scores)

print("Correlation coefficient:", corr[0,1])



# Q9. Binomial Probability
 
# P(X >= 8) where n=10, p=1/4

n = 10
p = 1/4

def binomial_pmf(x, n, p):
    return math.comb(n, x) * (p**x) * ((1-p)**(n-x))

prob = sum(binomial_pmf(x, n, p) for x in range(8, 11))

print(" Probability (at least 8 correct):", prob)



#Q.10

mean = 1000
std = 100

# Generate large sample (approximation)
data = np.random.normal(mean, std, 1000000)

# Probability between 900 and 1100
prob = np.mean((data >= 900) & (data <= 1100))

print(" Probability:", prob)



# Q11. Confidence Interval for Mean Height

import numpy as np

# Given data
mean = 170          # sample mean (x̄)
std = 8             # sample standard deviation (s)
n = 100             # sample size
z = 1.96            # z-value for 95% confidence


# Step 1: Calculate Standard Error
# SE = s / sqrt(n)

SE = std / np.sqrt(n)

# Step 2: Calculate Margin of Error
# Margin = z * SE

margin = z * SE


# Step 3: Confidence Interval
# CI = mean ± margin

lower = mean - margin
upper = mean + margin

print("Confidence Interval:", (lower, upper))

# Interpretation
 
print("\nInterpretation:")
print("We are 95% confident that the true population mean height")
print("lies between", lower, "and", upper)



#Q.12

sample_mean = 510
population_mean = 500
std = 20
n = 25

t_stat = (sample_mean - population_mean) / (std / np.sqrt(n))

print("t-statistic:", t_stat)

print("\nInterpretation:")
print("If t-value is large (greater than ~2), we reject H0")
print("Here t ≈", t_stat, "so we reject H0")

print("Conclusion: The company's claim is likely incorrect.")



#Q.13 Hypothesis Testing (Two groups comparison)

# Problem:
# Compare student performance between:
# 1. New teaching method
# 2. Traditional teaching method

# Step 1: Define Hypotheses

# H0 (Null Hypothesis):
# There is NO difference in mean scores between the two methods

print("H0: Mean score (new method) = Mean score (traditional method)")

# H1 (Alternative Hypothesis):
# There is a difference in mean scores between the two methods

print("H1: Mean score (new method) ≠ Mean score (traditional method)")


# Step 2: Understanding the Test

# This is a TWO-SAMPLE TEST because:
# - We have TWO groups
# - We are comparing their MEANS

# In real Data Science:
# We would use an Independent t-test

# Step 3: Interpretation 

print("\nInterpretation:")
print("If sample data shows a significant difference, we reject H0")
print("and conclude that the new teaching method improves performance.")

print("If no significant difference is found, we fail to reject H0")
print("and conclude that both methods perform similarly.")



#Q.14

n = 500
x = 320

p_hat = x / n

z = 1.645

margin = z * np.sqrt((p_hat * (1 - p_hat)) / n)

lower = p_hat - margin
upper = p_hat + margin

print("Confidence Interval:", (lower, upper))

print("\nInterpretation:")
print("We are 90% confident that the true population proportion")
print("lies between", lower, "and", upper)



# Q15. Poisson Distribution (Manual)
 
#Data: Mean number of defects (λ) = 2, Number of defects (x) = 3

lam = 2
x = 3

poisson_prob = (np.exp(-lam) * (lam**x)) / math.factorial(x)

print(" Probability (exactly 3 defects):", poisson_prob)