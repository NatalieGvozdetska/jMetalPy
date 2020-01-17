from jmetal.algorithm.singleobjective.simulated_annealing import SimulatedAnnealing
from jmetal.operator import ScrambleMutation
from jmetal.problem import TSP
from jmetal.util.solution import print_function_values_to_file, print_variables_to_file
from jmetal.util.termination_criterion import StoppingByTime

if __name__ == '__main__':
    problem = TSP(instance='resources/TSP_instances/kroA100.tsp')

    print(f"Solving TSP problem with {problem.number_of_cities} cities")

    algorithm = SimulatedAnnealing(
        problem=problem,
        mutation=ScrambleMutation(probability=1.0 / problem.number_of_cities),
        termination_criterion=StoppingByTime(max_seconds=30)
    )

    algorithm.run()
    result = algorithm.get_result()

    # Save results to file
    print_function_values_to_file(result, 'FUN.'+ algorithm.get_name() + "." + problem.get_name())
    print_variables_to_file(result, 'VAR.' + algorithm.get_name() + "." + problem.get_name())

    print(f'Algorithm: {algorithm.get_name()}')
    print(f'Problem: {problem.get_name()}')
    print(f'Solution: {result.variables}')
    print(f'Fitness:  {str(result.objectives[0])}')
    print(f'Computing time: {str(algorithm.total_computing_time)}')
    print(f'Problem evaluations: {str(algorithm.evaluations)}')
