from distutils.core import setup


def get_version(relpath):
    """read version info from file without importing it"""
    from os.path import dirname, join
    for line in open(join(dirname(__file__), relpath)):
        if '__version__' in line:
            if '"' in line:
                # __version__ = "0.9"
                return line.split('"')[1]
            elif "'" in line:
                return line.split("'")[1]

setup(
    name='python3-wget',
    version=get_version('wget.py'),
    author='anatoly techtonik <techtonik@gmail.com> | Jamie Lindsey AKA JamieJackHerer',
    author_email='<jackherer026@gmail.com>',
    url='https:github.com/jamiejackherer/python3-wget/',

    description="pure python 3.x download utility",
    license="Public Domain",
    install_requires=[
          'hurry.filesize',
    ],
    classifiers=[
        'Environment :: Console',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Networking',
        'Topic :: Utilities',
    ],

    py_modules=['wget'],

    long_description=open('README.txt').read(),
)
