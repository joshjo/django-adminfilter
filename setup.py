from setuptools import setup, find_packages

setup(
    name='django-adminfilter',
    version='0.1',
    author='COEX',
    author_email='josue.ttito@ucsp.edu.pe',
    url='https://github.com/joshjo/django-adminfilter',
    install_requires=[
        'django-mptt>=0.4',
    ],
    description='Django admin filters.',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)
