'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-06-21
 # @ Modified: 2023-07-06
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''


from feloopy import *

m = model('exact', 'cw-dea', 'gurobi')

I = m.set(10) # DMUs
J = m.set(5)  # Input(3)-Output(2) Criteria

z = m.fvar('z')
d = m.pvar('d',[I])
w = m.pvar('w',[J], bound=[0.000001, None])

data = np.array([[1.51746106e-01, 7.14746106e-01, 1.33017461e+01, 1.44797461e+01, 2.33746106e-01],
                 [1.71746106e-01, 1.07274611e+00, 1.69017461e+01, 1.95037461e+01, 3.41746106e-01],
                 [2.36746106e-01, 1.22574611e+00, 2.40017461e+01, 2.09537461e+01, 3.64746106e-01],
                 [2.12746106e-01, 3.64746106e-01, 1.56017461e+01, 1.39037461e+01, 2.12746106e-01],
                 [1.34746106e-01, 4.10746106e-01, 1.84867461e+01, 1.52077461e+01, 2.38746106e-01],
                 [4.98746106e-01, 5.84774611e+00, 5.64217461e+01, 8.11877461e+01, 1.10474611e+00],
                 [6.17461059e-02, 9.19746106e-01, 5.64217461e+01, 8.11877461e+01, 1.10474611e+00],
                 [7.27461059e-02, 1.23674611e+00, 1.20017461e+01, 1.14427461e+01, 2.00746106e-01],
                 [1.50174611e+00, 1.81217461e+01, 8.95117461e+01, 1.24073746e+02, 1.85974611e+00],
                 [1.21746106e-01, 1.82274611e+00, 1.98017461e+01, 1.74267461e+01, 2.75746106e-01]])

m.obj(z)

for i in I:
    m.con(sum(data[i,j]*w[j] for j in J) + d[i] == 1)

for i in I:
    m.con(z >= d[i])

m.sol(['min'], 'gurobi')

m.report()

for i in I:
    print('performance: ', 1-m.get(d[i]))