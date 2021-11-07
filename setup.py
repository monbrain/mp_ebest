from setuptools import setup
import mp_ebest

setup(
    name='mp_ebest',
    version=mp_ebest.__version__,
    description='Moon Package for Ebest API',
    url='https://github.com/moonstock/mp_ebest',
    author='Moon Jung Sam',
    author_email='monblue@snu.ac.kr',
    license='MIT',
    packages=['mp_ebest'],
    # entry_points={'console_scripts': ['mp_ebest = mp_ebest.__main__:main']},
    keywords='ebest xingapi',
    # python_requires='~=3.3',
    # zip_safe=False
)