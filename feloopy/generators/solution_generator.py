
def generate_solution(features):

    match features['interface_name']:

        case 'pulp':

            from .solution import pulp_solution_generator 
            ModelSolution = pulp_solution_generator.generate_solution(features)

        case 'pyomo':

            from .solution import pyomo_solution_generator
            ModelSolution = pyomo_solution_generator.generate_solution(features)

        case 'ortools':

            from .solution import ortools_solution_generator
            ModelSolution = ortools_solution_generator.generate_solution(features)

        case 'ortools_cp':

            from .solution import ortools_cp_solution_generator
            ModelSolution = ortools_cp_solution_generator.generate_solution(features)

        case 'gekko':

            from .solution import gekko_solution_generator
            ModelSolution = gekko_solution_generator.generate_solution(features)

        case 'picos':

            from .solution import picos_solution_generator
            ModelSolution = picos_solution_generator.generate_solution(features)

        case 'cvxpy':

            from .solution import cvxpy_solution_generator
            ModelSolution = cvxpy_solution_generator.generate_solution(features)

        case 'cylp':

            from .solution import cylp_solution_generator
            ModelSolution = cylp_solution_generator.generate_solution(features)

        case 'pymprog':

            from .solution import pymprog_solution_generator
            ModelSolution = pymprog_solution_generator.generate_solution(features)

        case 'cplex':

            from .solution import cplex_solution_generator
            ModelSolution = cplex_solution_generator.generate_solution(features)

        case 'cplex_cp':

            from .solution import cplex_cp_solution_generator
            ModelSolution = cplex_cp_solution_generator.generate_solution(features)

        case 'gurobi':

            from .solution import gurobi_solution_generator
            ModelSolution = gurobi_solution_generator.generate_solution(features)

        case 'xpress':

            from .solution import xpress_solution_generator
            ModelSolution = xpress_solution_generator.generate_solution(features)

        case 'mip':

            from .solution import mip_solution_generator
            ModelSolution = mip_solution_generator.generate_solution(features)

        case 'linopy':

            from .solution import linopy_solution_generator
            ModelSolution = linopy_solution_generator.generate_solution(features)

    return ModelSolution
