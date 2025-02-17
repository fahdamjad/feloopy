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
m = target_model('exact', 'distribution_planning_problem', 'pyomo', key=0)

# Data
I = m.set(2)  # Number of suppliers
J = m.set(2)  # Number of warehouses
K = m.set(3)  # Number of customers
P = m.set(3)  # Type of products
T = m.set(4)  # Time periods

# Dataset
dk = m.uniformint(10, 20, [K, P, T])      # Customer demand
cap = m.uniformint(60, 90, [I, P, T])     # Supplier capacity
c = m.uniformint(1, 4, [I, J, P, T])      # Cost of sending each unit of goods from the supplier to the warehouse
cp = m.uniformint(1, 4, [J, K, P, T])     # Cost of sending each item from the warehouse to the customer
cpp = m.uniformint(2, 8, [I, K, P, T])    # Cost of sending each unit of goods from the supplier to the customer

# Variables
x = m.ivar('x', [I, J, P, T])  # Transfer rate of products from the supplier to the warehouse
y = m.ivar('y', [J, K, P, T])  # Transfer rate of products from the warehouse to the customer
z = m.ivar('z', [I, K, P, T])  # Amount of direct transfer of products from the supplier to the customer

# Objective
m.obj(sum(x[i, j, p, t] * c[i, j, p, t] for i, j, p, t in sets(I, J, P, T)) + sum(y[j, k, p, t] * cp[j, k, p, t] for j, k, p, t in sets(J, K, P, T)) + sum(z[i, k, p, t] * cpp[i, k, p, t] for i, k, p, t in sets(I, K, P, T)))

# Constraints
# Supplier capacity constraint
for i, p, t in sets(I, P, T):
    m.con(sum(x[i, j, p, t] for j in J) + sum(z[i, k, p, t] for k in K) <= cap[i, p, t])

# Warehouse flow constraint
for j, p, t in sets(J, P, T):
    m.con(sum(x[i, j, p, t] for i in I) >= sum(y[j, k, p, t] for k in K))

# Customer demand constraint
for k, p, t in sets(K, P, T):
    m.con(sum(y[j, k, p, t] for j in J) + sum(z[i, k, p, t] for i in I) >= dk[k, p, t])

# Solve
m.sol(['min'], 'cbc')

# Display
m.report()
