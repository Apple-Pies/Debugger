class Debugger():
    def __init__(self, problem):
        self.problem = problem.attributes
        self.line_number = problem.line_number
        self.variable = problem.variable
        self.module = problem.docs_help

    def Solve(self):
        '''
        Gives solutions based on the 'attributes' parameter.
        This is intended to be used for basic syntax corrections
        '''
        Title = "Solution: "
        problem = str(self.problem)
        line_number = str(self.line_number)
        tell_problem = f"Your Problem is: '{problem}', at line {line_number}"
        print(tell_problem)
        if 'is not defined' in problem:
            print(f"{Title}A variable has not been declared or hasn't been refrenced.")
        if 'ModuleNotFoundError' in problem:
            print(f"{Title}You have imported a module that dosen't exist.")
        if 'TypeError' in problem:
            print(f"{Title}An incorrect type is being used in your code.")
        if 'Index out of range' in problem:
            print(f"{Title}You do not have enough elements in a tuple, list or set.")
        if 'IndentationError' in problem:
            print(f"{Title}Incorrect indentation at a certain point.")
        if 'TabError' in problem:
            print(f"{Title}You dont have a good use of spaces or tabs in your program.")

    def Tell_if_Var(self, file):
        '''
        Tells if a variable exists in the code of a file.
        This file is refrenced by the 'file' parameter, needed for this method.
        '''
        self.file = file
        the_file = str(self.file)
        MakeFile = open(the_file, "r")
        hold_file_data = MakeFile.read()
        file_data = str(hold_file_data)
        variable = str(self.variable)
        first = f'{variable}='
        second = f'{variable} ='
        third = f'{variable} = '
        scenarios = [first, second, third]
        if scenarios[0] in file_data or scenarios[1] in file_data or scenarios[2] in file_data:
            print(f"The variable {variable}, is found in {the_file}.")
        elif scenarios[0] in file_data or scenarios[1] in file_data or scenarios[2] not in file_data:
            print(f"The variable {variable}, is not found in {the_file}")

    def get_docs_help(self):
        '''
        Brings up relevant documentation based on the module given in the
        'docs_help' parameter.
        '''
        print(help(self.module))

class Problem:
    def __init__(self, attributes="", line_number=1, variable="", docs_help=""):
        self.attributes = attributes
        self.line_number = line_number
        self.variable = variable
        self.docs_help = docs_help
