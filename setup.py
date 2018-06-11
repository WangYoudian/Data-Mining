from cx_Freeze import setup, Executable

base = None    

executables = [Executable("runtime0.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Apriori",
    options = options,
    version = "0.1",
    description = 'This is the simplest set of mining association rules. With three different methods in realizing Apriori Algorithm.',
    executables = executables
)
