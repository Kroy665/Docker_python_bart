from os.path import dirname, basename, isfile, join
import glob
import sys
import importlib
from inspect import getmembers, isfunction
def getModules():
    modules = glob.glob(join(dirname(__file__), "*.py"))
    __all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]

    print("__all__:",__all__)

    allModules = []

    #  Import all modules from __all__ list
    for module_name in __all__:
        if module_name != "app":
            # module = importlib.import_module(__import__(module_name))
            # globals()[module_name] = importlib.import_module(module_name)
            functions = getmembers(__import__(module_name), isfunction)
            allModules.append({
                __import__(module_name): functions
            })
            # print(main)
    # print(allModules) 

    return allModules

    # for modules in allModules:
    #     # print(modules.keys())
    #     for module in modules.keys():
    #         print(module)
    #         print(modules[module])

# mod = getModules()
# print("getModules()::",mod)




