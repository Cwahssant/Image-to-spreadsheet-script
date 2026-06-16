from sys import executable
from pkgutil import iter_modules
from subprocess import run
from importlib.util import find_spec

#Checks whether the user has the required dependencies installed. If not then it'll download them.
def check_dependencies():
    installed_modules = list(iter_modules())
    required = ['easyocr']
    missing = []

    for library in required:
        if library not in installed_modules:
            missing.append(library)

    if len(missing) > 0:
        install_libraries(missing)


#Installs the missing libraries onto the user's device        
def install_libraries(libraries_list):
    for library in libraries_list:
        if find_spec(library) is None:
            run([executable, '-m', 'pip', 'install', library], check = True)