'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-05-11
 # @ Modified: 2023-05-12
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''

import gurobipy as gurobi_interface
import itertools as it

sets = it.product

POSITIVE = gurobi_interface.GRB.CONTINUOUS
INTEGER = gurobi_interface.GRB.INTEGER
BINARY = gurobi_interface.GRB.BINARY
FREE = gurobi_interface.GRB.CONTINUOUS
INFINITY = gurobi_interface.GRB.INFINITY


def generate_variable(model_object, variable_type, variable_name, variable_bound, variable_dim=0):

    if variable_bound[0] == None:
        variable_bound[0] = -INFINITY

    if variable_bound[1] == None:
        variable_bound[1] = +INFINITY

    match variable_type:

        case 'pvar':

            if variable_dim == 0:

                generated_variable = model_object.addVar(
                    vtype=POSITIVE, lb=variable_bound[0], ub=variable_bound[1], name=variable_name)

            else:

                if len(variable_dim) == 1:

                    generated_variable = {key: model_object.addVar(
                        vtype=POSITIVE, lb=variable_bound[0], ub=variable_bound[1], name=f"{variable_name}{key}") for key in variable_dim[0]}

                else:

                    generated_variable = {key: model_object.addVar(
                        vtype=POSITIVE, lb=variable_bound[0], ub=variable_bound[1], name=f"{variable_name}{key}") for key in sets(*variable_dim)}

        case 'bvar':

            if variable_dim == 0:

                generated_variable = model_object.addVar(
                    vtype=BINARY, lb=variable_bound[0], ub=variable_bound[1], name=variable_name)

            else:

                if len(variable_dim) == 1:

                    generated_variable = {key: model_object.addVar(
                        vtype=BINARY, lb=variable_bound[0], ub=variable_bound[1], name=f"{variable_name}{key}") for key in variable_dim[0]}

                else:

                    generated_variable = {key: model_object.addVar(
                        vtype=BINARY, lb=variable_bound[0], ub=variable_bound[1], name=f"{variable_name}{key}") for key in sets(*variable_dim)}

        case 'ivar':

            if variable_dim == 0:

                generated_variable = model_object.addVar(
                    vtype=INTEGER, lb=variable_bound[0], ub=variable_bound[1], name=variable_name)

            else:

                if len(variable_dim) == 1:

                    generated_variable = {key: model_object.addVar(
                        vtype=INTEGER, lb=variable_bound[0], ub=variable_bound[1], name=f"{variable_name}{key}") for key in variable_dim[0]}

                else:

                    generated_variable = {key: model_object.addVar(
                        vtype=INTEGER, lb=variable_bound[0], ub=variable_bound[1], name=f"{variable_name}{key}") for key in sets(*variable_dim)}

        case 'fvar':

            if variable_dim == 0:

                generated_variable = model_object.addVar(
                    vtype=POSITIVE, lb=variable_bound[0], ub=variable_bound[1], name=variable_name)

            else:

                if len(variable_dim) == 1:

                    generated_variable = {key: model_object.addVar(
                        vtype=POSITIVE, lb=variable_bound[0], ub=variable_bound[1], name=f"{variable_name}{key}") for key in variable_dim[0]}

                else:

                    generated_variable = {key: model_object.addVar(
                        vtype=POSITIVE, lb=variable_bound[0], ub=variable_bound[1], name=f"{variable_name}{key}") for key in sets(*variable_dim)}

        case 'ptvar':


            if variable_dim == 0:

                generated_variable = model_object.addVar(
                    vtype=POSITIVE, lb=variable_bound[0], ub=variable_bound[1], name=variable_name)

            else:

                if len(variable_dim) == 1:

                    generated_variable = model_object.addMVar(
                        (len(variable_dim[0])), vtype=POSITIVE, lb=variable_bound[0], ub=variable_bound[1], name=variable_name)

                elif len(variable_dim) == 2:

                    generated_variable = model_object.addMVar((len(variable_dim[0]), len(
                        variable_dim[1])), vtype=POSITIVE, lb=variable_bound[0], ub=variable_bound[1], name=variable_name)

                else:

                    generated_variable = model_object.addMVar(tuple(
                        [len(key) for key in variable_dim]), vtype=POSITIVE, lb=variable_bound[0], ub=variable_bound[1], name=variable_name)

        case 'ftvar':


            if variable_dim == 0:
                generated_variable = model_object.addVar(
                    vtype=FREE, lb=variable_bound[0], ub=variable_bound[1], name=variable_name)

            else:

                if len(variable_dim) == 1:
                    generated_variable = model_object.addMVar(
                        (len(variable_dim[0])), vtype=FREE, lb=variable_bound[0], ub=variable_bound[1], name=variable_name)
                elif len(variable_dim) == 2:
                    generated_variable = model_object.addMVar((len(variable_dim[0]), len(
                        variable_dim[1])), vtype=FREE, lb=variable_bound[0], ub=variable_bound[1], name=variable_name)
                else:
                    generated_variable = model_object.addMVar(tuple(
                        [len(key) for key in variable_dim]), vtype=FREE, lb=variable_bound[0], ub=variable_bound[1], name=variable_name)

        case 'btvar':

            if variable_dim == 0:
                generated_variable = model_object.addVar(
                    vtype=BINARY, lb=variable_bound[0], ub=variable_bound[1], name=variable_name)

            else:

                if len(variable_dim) == 1:
                    generated_variable = model_object.addMVar(
                        (len(variable_dim[0])), vtype=BINARY, lb=variable_bound[0], ub=variable_bound[1], name=variable_name)
                elif len(variable_dim) == 2:
                    generated_variable = model_object.addMVar((len(variable_dim[0]), len(
                        variable_dim[1])), vtype=BINARY, lb=variable_bound[0], ub=variable_bound[1], name=variable_name)
                else:
                    generated_variable = model_object.addMVar(tuple(
                        [len(key) for key in variable_dim]), vtype=BINARY, lb=variable_bound[0], ub=variable_bound[1], name=variable_name)

        case 'itvar':


            if variable_dim == 0:
                generated_variable = model_object.addVar(
                    vtype=INTEGER, lb=variable_bound[0], ub=variable_bound[1], name=variable_name)

            else:

                if len(variable_dim) == 1:
                    generated_variable = model_object.addMVar(
                        (len(variable_dim[0])), vtype=INTEGER, lb=variable_bound[0], ub=variable_bound[1], name=variable_name)
                elif len(variable_dim) == 2:
                    generated_variable = model_object.addMVar((len(variable_dim[0]), len(
                        variable_dim[1])), vtype=INTEGER, lb=variable_bound[0], ub=variable_bound[1], name=variable_name)
                else:
                    generated_variable = model_object.addMVar(tuple(
                        [len(key) for key in variable_dim]), vtype=INTEGER, lb=variable_bound[0], ub=variable_bound[1], name=variable_name)

    return generated_variable
