from distutils.core import setup, Extension

module1 = Extension('balancemodule',
                    sources = ['balancemodule.c'])

setup (name = 'balancemodule',
       version = '1.0',
       description = 'This is a demo package',
       ext_modules = [module1])
