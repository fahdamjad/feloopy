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
m = learner_model('exact', 'logistic_regression_problem', 'gekko', key=0)

# Dataset
a = np.array([[1, 2, 2], [2, 3, 3], [3, 4, 5], [4, 5, 6], [5, 7, 8]])  # Features
b = np.array([0, 1, 0, 1, 0])  # Target

# Sets
U = m.set(np.shape(a)[1])  # Features
T = range(np.shape(a)[0])  # Observations

# Preprocessing Dataset
ran_a = np.array([np.ptp(a[:,i]) for i in U]) #Range of feature values 
ave_a = np.array([np.average(a[:,i]) for i in U]) #Average of feature values
nor_a = (a-ave_a)/ran_a #Normalized feature values

# Variables
x = m.fvar('x', [U])
z = m.fvar('z')

# Objective
m.obj((2*len(T))**(-1)*sum(((1+m.exponent(-(sum(a[t,i]*x[i] for i in U) + z)))**(-1)-b[t])**2 for t in T))

# Solve
m.sol(['min'], 'apopt')

# Display
m.report()

# Store
w = [] 
for i in U: 
    w.append(m.get(x[i]))
    
b = m.get(z)

def approximator_model(w,b,a): 
    print(f"Input = {a} -> Output = {round((1+exponent(-(sum(w[i]*a[i] for i in U) + b)))**(-1))}")

#Test dataset
aa = [[1, 2.1, 2], [1.9, 3, 3], [3.2, 4, 5], [4.1, 5, 6], [4.9, 7, 8]]  # Features
bb = [0, 1, 0, 1, 0]  # Target

for item in aa:
    approximator_model(w,b,item)