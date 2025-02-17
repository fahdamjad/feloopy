'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-06-18
 # @ Modified: 2023-07-06
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''

from feloopy import *

# Environment
m = learner_model('exact', 'linear_regression_problem', 'gekko', key=0)

# Dataset
a = np.array([[1, 2, 2], [2, 3, 3], [3, 4, 5], [4, 5, 6], [5, 7, 8]])  # Features
b = np.array([1, 2, 3, 4, 5])  # Target

# Sets
U = m.set(np.shape(a)[1])  # Features
T = range(np.shape(a)[0])  # Observations

# Preprocessing Dataset
ran_a = np.array([np.ptp(a[:,i]) for i in U]) #Range of feature values 
ave_a = np.array([np.average(a[:,i]) for i in U]) #Average of feature values
nor_a = (a-ave_a)/ran_a #Normalized feature values

ran_b = np.ptp(b) #Range of target values 
ave_b = np.average(b) #Average of target values
nor_b = (b-ave_b)/ran_b #Normalized target values

# Variables
x = m.fvar('x', [U])
z = m.fvar('z')

# Objective
m.obj((2*len(T))**(-1)*sum(( sum(nor_a[t, i]*x[i] for i in U) + z-nor_b[t])**2 for t in T))

# Solve
m.sol(['min'], 'apopt')

# Display
m.report()

# Store
w = [] 
for i in U: 
    w.append(m.get(x[i]))

b = m.get(z)

# Approximator
#Prediction function
def approximator_model(w,b,a): 
    print(f"Input = {a} -> Output = {sum(w[i]*a[i] for i in range(len(a))) + b}")

#Test dataset
aa = [[6,8,9],[7,4,3],[8,3,5],[9,1,6],[10,9,3]] #Features
bb = [ 6     , 7     , 8     , 9     , 10     ] #Target

for item in aa:
    approximator_model(w,b,item)