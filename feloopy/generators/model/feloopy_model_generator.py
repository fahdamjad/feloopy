'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-05-11
 # @ Modified: 2023-05-12
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''


def generate_model(total_variables, directions, solver_name, solver_options):

    match solver_name:

        case 'hco':
            from ...algorithms.heuristic.HCO import HCO
            model_object = HCO(f=total_variables, d=directions, s=solver_options.get('epoch', 100), t=solver_options.get('pop_size', 50), e=solver_options.get(
                'elitism_number', 3), ac=solver_options.get('archive_cap', 100), rep=solver_options.get('episode', 1), ben=solver_options.get('benchmark', False))

        case 'gwo':

            from ...algorithms.heuristic.GWO import GWO
            model_object = GWO(f=total_variables, d=directions, s=solver_options.get('epoch', 100), t=solver_options.get(
                'pop_size', 50), ac=solver_options.get('archive_cap', 50), rep=solver_options.get('episode', 1), ben=solver_options.get('benchmark', False))

        case 'ga':
            from ...algorithms.heuristic.GA import GA
            model_object = GA(f=total_variables, d=directions, s=solver_options.get('epoch', 100), t=solver_options.get('pop_size', 50), mu=solver_options.get('mutation_rate', 0.02), cr=solver_options.get(
                'crossover_rate', 0.7), sfl=solver_options.get('survival_lb', 0.4), sfu=solver_options.get('survival_ub', 0.6), ac=solver_options.get('archive_cap', 50), rep=solver_options.get('episode', 1), ben=solver_options.get('benchmark', False))

        case 'de':
            from ...algorithms.heuristic.DE import DE
            model_object = DE(f=total_variables, d=directions, s=solver_options.get('epoch', 100), t=solver_options.get('pop_size', 50), mu=solver_options.get('mutation_rate', 0.02),
                              cr=solver_options.get('crossover_rate', 0.7), ac=solver_options.get('archive_cap', 50), rep=solver_options.get('episode', 1), ben=solver_options.get('benchmark', False))

        case 'sa':
            from ...algorithms.heuristic.SA import SA
            model_object = SA(f=total_variables, d=directions, s=solver_options.get('epoch', 100), t=1, cc=solver_options.get('cooling_cycles', 10), mt=solver_options.get(
                'maximum_temperature', 1000),  ac=solver_options.get('archive_cap', 50), rep=solver_options.get('episode', 1), ben=solver_options.get('benchmark', False))

        case 'bo':
            from ...algorithms.heuristic.BO import BO
            model_object = BO(f=total_variables, d=directions, s=solver_options.get(
                'epoch', 100), t=10, rep=solver_options.get('episode', 1), ben=solver_options.get('benchmark', False))

        case 'ts':
            from ...algorithms.heuristic.TS import TS
            model_object = TS(f=total_variables, d=directions, s=solver_options.get('epoch', 100), t=1, c=solver_options.get(
                'tabu_list_size', 10), ac=solver_options.get('archive_cap', 50), rep=solver_options.get('episode', 1), ben=solver_options.get('benchmark', False))

        case 'pso':
            from ...algorithms.heuristic.PSO import PSO
            model_object = PSO(f=total_variables, d=directions, s=solver_options.get('epoch', 100), t=solver_options.get('pop_size', 50), w=solver_options.get('velocity_weight', 0.8), c1=solver_options.get(
                'p_best_weight', 0.1), c2=solver_options.get('g_best_weight', 0.1), ac=solver_options.get('archive_cap', 50), rep=solver_options.get('episode', 1), ben=solver_options.get('benchmark', False))
    return model_object
