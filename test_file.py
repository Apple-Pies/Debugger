from debugger import Debugger, Problem


a_problem = Problem("ModuleNotFoundError", 1, "x", "pygame")
Solve_Problem = Debugger(a_problem)
Solve_Problem.Solve()
Solve_Problem.Tell_if_Var("test_file.py")
Solve_Problem.get_docs_help()