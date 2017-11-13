from setuptools import setup

setup(name='news',
      version='1.1',
      py_modules=['news'],
      install_requires=['click',
                        'psycopg2',
                        'pygments',
                        'tabulate'],
      entry_points='''
        [console_scripts]
        question=news:cli
        ''', )
