'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-05-11
 # @ Modified: 2023-05-12
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''

import itertools as it
import pandas as pd

sets = it.product


def generate_variable(model_object, variable_type, variable_name, variable_bound, variable_dim=0):

    match variable_type:

        case 'pvar':

            '''

            Positive Variable Generator


            '''
            if variable_dim == 0:
                GeneratedVariable = model_object.add_variables(
                    lower=variable_bound[0], upper=variable_bound[1], name=variable_name)
            else:
                GeneratedVariable = model_object.add_variables(
                    lower=variable_bound[0], upper=variable_bound[1], coords=pd.Index(variable_dim), name=variable_name)

        case 'bvar':

            '''

            Binary Variable Generator


            '''

            if variable_dim == 0:
                GeneratedVariable = model_object.add_variables(
                    name=variable_name, binary=True)
            else:
                GeneratedVariable = model_object.add_variables(
                    coords=pd.Index(variable_dim), name=variable_name,  binary=True)

        case 'ivar':

            '''

            Integer Variable Generator


            '''

            if variable_dim == 0:
                GeneratedVariable = model_object.add_variables(
                    lower=variable_bound[0], upper=variable_bound[1], name=variable_name, binary=True)
            else:
                GeneratedVariable = model_object.add_variables(
                    lower=variable_bound[0], upper=variable_bound[1], coords=pd.Index(variable_dim), name=variable_name,  integer=True)

        case 'fvar':

            '''

            Free Variable Generator


            '''

            if variable_dim == 0:
                GeneratedVariable = model_object.add_variables(
                    lower=variable_bound[0], upper=variable_bound[1], name=variable_name)
            else:
                GeneratedVariable = model_object.add_variables(
                    lower=variable_bound[0], upper=variable_bound[1], coords=pd.Index(variable_dim), name=variable_name)

    return GeneratedVariable
