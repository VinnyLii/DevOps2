from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys

class UnitTestCommand(TestCommand):
    def run_tests(self):
        import unittest
        test_loader = unittest.TestLoader()
        test_runner = test_loader.discover('test')
        test_runner.run(test_loader.loadTestsFromName('test_testFile'))

setup(
    name='TimeMgt',
    version='1.0',
    packages=find_packages(),
    url='',
    license='',
    author='Your Name',
    author_email='',
    description='Time Management Application',
    install_requires=[
        'datetime'
    ],
    tests_require=[
        'pytest'
    ],
    cmdclass={
        'test': UnitTestCommand
    }
)
