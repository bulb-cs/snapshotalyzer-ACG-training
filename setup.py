from setuptools import setup

setup(
    name='Snapshotalyzer',
    version='0.1',
    author='Yann J',
    author_email='bulb.cloud.services@gmail.com',
    description='Snapshotalyzer is a command-line tool to manage AWS EC2 snapshots',
    license='GPLv3+',
    packages=['shotty'],
    url="https://github.com/bulb-cs/snapshotalyzer-ACG-training",
    install_requires=[
        'click',
        'boto3',
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    '''
)
