'''
import os
import pkgutil
pkgapth = os.path.dirname(__file__)
pkgname = os.path.basename(pkgapth)

for _, file, _ in pkgutil.iter_modules([pkgapth]):
    abfile = os.path.join(pkgapth, file)
    __import__(pkgname+'.'+file)
'''