from ortools.linear_solver import pywraplp

#
# class LPPSolver:
#     _solver = pywraplp.Solver.CreateSolver('GLOP')
#
#     @staticmethod
#     def number_of_variables(cls):
#         print('Number of variables =', cls._solver.NumVariables())
#
#     @staticmethod
#     def initiate_variables(cls, listOfVars):
#         for var in listOfVars:
#             cls._solver.NumVar(0, cls._solver.infinity(), str(var))


def solve_lpp():
    """Linear programming sample."""
    # Instantiate a Glop solver, naming it LinearExample.
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Create the two variables and let them take on any non-negative value.
    x1 = solver.NumVar(0, solver.infinity(), 'x1')
    x2 = solver.NumVar(0, solver.infinity(), 'x2')
    x3 = solver.NumVar(0, solver.infinity(), 'x3')
    x4 = solver.NumVar(0, solver.infinity(), 'x4')
    x5 = solver.NumVar(0, solver.infinity(), 'x5')
    x6 = solver.NumVar(0, solver.infinity(), 'x6')
    y1 = solver.NumVar(0, solver.infinity(), 'y1')
    y2 = solver.NumVar(0, solver.infinity(), 'y2')
    y3 = solver.NumVar(0, solver.infinity(), 'y3')
    y4 = solver.NumVar(0, solver.infinity(), 'y4')
    y5 = solver.NumVar(0, solver.infinity(), 'y5')

    # number_of_variables()
    print('Number of variables =', solver.NumVariables())
    #

    #

    # Constraint 0: x + 2y <= 14.
    solver.Add(x1 + 200 - 1300 <= y1)
    solver.Add(x1 + 200 - 1300 >= y1)

    solver.Add(y1 + x2 - 1400 <= y2)
    solver.Add(y1 + x2 - 1400 >= y2)

    solver.Add(y2 + x3 - 1000 <= y3)
    solver.Add(y2 + x3 - 1000 >= y3)

    solver.Add(y3 + x4 - 800 <= y4)
    solver.Add(y3 + x4 - 800 >= y4)

    solver.Add(y4 + x5 - 1700 <= y5)
    solver.Add(y4 + x5 - 1700 >= y5)

    solver.Add(y5 + x6 - 1900 <= 100)
    solver.Add(y5 + x6 - 1900 >= 100)

    solver.Add(y1 <= 250)
    solver.Add(y2 <= 250)
    solver.Add(y3 <= 250)
    solver.Add(y4 <= 250)
    solver.Add(y5 <= 250)
    # solver.Add()

    # # Constraint 1: 3x - y >= 0.
    # solver.Add(3 * x - y >= 0.0)
    #
    # # Constraint 2: x - y <= 2.
    # solver.Add(x - y <= 2.0)

    #

    #

    print('Number of constraints =', solver.NumConstraints())

    # Objective function: 3x + 4y.
    solver.Minimize(100 * x1 + 105 * x2 + 110 * x3 + 115 * x4 + 110 * x5 + 110 * x6 + 4 * y1 + 4 * y2 + 4 * y3 + 4 * y4 + 4 * y5)

    # Solve the system.
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Objective value =', solver.Objective().Value())
        print('x1 =', x1.solution_value())
        print('x2 =', x2.solution_value())
        print('x3 =', x3.solution_value())
        print('x4 =', x4.solution_value())
        print('x5 =', x5.solution_value())
        print('x6 =', x6.solution_value())
        print('y1 =', y1.solution_value())
        print('y2 =', y2.solution_value())
        print('y3 =', y3.solution_value())
        print('y4 =', y4.solution_value())
        print('y5 =', y5.solution_value())
    else:
        print('The problem does not have an optimal solution.')

    print('\nAdvanced usage:')
    print('Problem solved in %f milliseconds' % solver.wall_time())
    print('Problem solved in %d iterations' % solver.iterations())


solve_lpp()
