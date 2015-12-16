from setuptools import setup

setup(
    name="awsenv-profiles",
    version="0.0.1",
    author="Anthony Grimes",
    author_email="awsenv@raynes.me",
    include_package_data=True,
    url="https://github.com/Raynes/awsenv-profiles",
    install_requires=[
        "botocore==1.3.12"
    ],
    py_modules=['awsenv'],
    scripts=['bin/awsenv.sh'],
    entry_points={
        'console_scripts': ['awsenvp=awsenv:main']
    }
)
