from ortools.linear_solver import pywraplp


def solve_lpp():

    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Create the two variables and let them take on any non-negative value.

    # x1 = solver.NumVar(0, solver.infinity(), 'x1')
    # x2 = solver.NumVar(0, solver.infinity(), 'x2')
    # x3 = solver.NumVar(0, solver.infinity(), 'x3')
    # x4 = solver.NumVar(0, solver.infinity(), 'x4')
    # x5 = solver.NumVar(0, solver.infinity(), 'x5')
    # x6 = solver.NumVar(0, solver.infinity(), 'x6')
    z1 = solver.NumVar(0, solver.infinity(), 'z1')
    z2 = solver.NumVar(0, solver.infinity(), 'z2')
    z3 = solver.NumVar(0, solver.infinity(), 'z3')
    # y4 = solver.NumVar(0, solver.infinity(), 'y4')
    # y5 = solver.NumVar(0, solver.infinity(), 'y5')

    # number_of_variables()
    print('Number of variables =', solver.NumVariables())
    #

    #

    # Constraint 0: x + 2y <= 14.

    solver.Add(z1 + z2 <= z3)
    solver.Add(z3 <= 40)
    solver.Add(z3 >= 40)
    solver.Add(30 * z1 + 28.125 * z2 + 78.75 * (z3 - z2 - z1) <= 6000)
    # solver.Add(0.04 * y1 + 0.045 * y2 + 0.21 * y3 <= 6000)

    solver.Add(750 * z1 >= 5000)
    solver.Add(750 * z1 <= 10000)

    solver.Add(375 * (z3 - z2 - z1) >= 4000)
    solver.Add(375 * (z3 - z2 - z1) <= 8000)

    solver.Add(625 * z2 <= 15000)
    # solver.Add(30000 * x1 <= 10000)

    # solver.Add(y1 <= 250)
    # solver.Add(y2 <= 250)
    # solver.Add(y3 <= 250)
    # solver.Add(y4 <= 250)
    # solver.Add(y5 <= 250)

    print('Number of constraints =', solver.NumConstraints())

    # Objective function: 3x + 4y.
    solver.Maximize(3000 * z1 + 3750 * z2 + 3750 * (z3 - z2 - z1))

    # Solve the system.
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Objective value =', solver.Objective().Value())
        # print('x1 =', x1.solution_value())
        # print('x2 =', x2.solution_value())
        # print('x3 =', x3.solution_value())
        # print('x4 =', x4.solution_value())
        # print('x5 =', x5.solution_value())
        # print('x6 =', x6.solution_value())
        print('z1 =', z1.solution_value())
        print('z2 =', z2.solution_value())
        print('z3 =', z3.solution_value())
        # print('y4 =', y4.solution_value())
        # print('y5 =', y5.solution_value())
    else:
        print('The problem does not have an optimal solution.')

    print('\nAdvanced usage:')
    print('Problem solved in %f milliseconds' % solver.wall_time())
    print('Problem solved in %d iterations' % solver.iterations())


solve_lpp()
