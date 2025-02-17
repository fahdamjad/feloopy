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

#Environment
m = target_model('exact', 'single machine scheduling', 'pulp', key=0)

#Dataset
w = [0.1, 0.4, 0.15, 0.35] #Priority weight of each job
p = [  7,   3,    9,    4] #Processing time of each job
s = 5 #Setup time of the machine

#Sets
I = range(len(p)) #Set of jobs
J = range(len(I)) #Set of positions

#Variables
x = m.bvar('x', [I,J])
c = m.pvar('c', [J])

#Objective
m.obj(sum(w[j]*c[j] for j in J))

#Constraints
for i in I: 
    m.con(sum(x[i,j] for j in J) == 1)

for j in J: 
    m.con(sum(x[i,j] for i in I) == 1)

m.con(c[0] == s + sum(x[i,0]*p[i] for i in I))

for j in J:
    if j!=0: m.con(c[j] >= c[j-1] + sum(x[i,j]*p[i] for i in I))

#Solve
m.sol(['min'], 'highs')

# Display
m.report()