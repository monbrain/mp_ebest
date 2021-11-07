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
    # python_requires='>=3.8',  # Python 3.8.6-32 bit
    # install_requires=[ # 패키지 사용을 위해 필요한 추가 설치 패키지
    #     'pythoncom', 
    #     'win32com'
    # ],
    # zip_safe=False
)

