#coding:utf-8
from distutils.core import setup
import py2exe

setup(
    name=u'Exercise Generator',
    version='1.2',
    description='automatically generate exercises',
    author='Peng Shulin',
    windows = [
        {
            "script": "ExerciseGeneratorApp.py",
        }
    ],
    options = {
        "py2exe": {
            "compressed": 1,
            "optimize": 2,
            "dist_dir": "dist",
        }
    },
)
