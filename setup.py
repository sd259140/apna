from setuptools import find_packages, setup
setup(
    name='wdvgt2',
    packages=find_packages(include=['wdvgt2']),
    version='0.2.0',
    description='My second ',
    author='Me',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)