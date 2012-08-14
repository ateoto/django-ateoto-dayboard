from setuptools import setup

version = __import__('ateoto_dayboard').__version__

setup(name = 'django-ateoto-dayboard',
    version = version,
    author = 'Matthew McCants',
    author_email = 'mattmccants@gmail.com',
    description = 'Informational Dashboard for ateoto.com.',
    license = 'BSD',
    url = 'https://github.com/Ateoto/django-ateoto-dayboard',
    packages = ['ateoto_dayboard'],
    install_requires = ['django>=1.4', 'requests', 'requests_oauth2'])
