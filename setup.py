# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='django-domains',
    version='1.0.0',
    description='Django Middleware for mapping domains to custom url confs.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Jose-Miguel7/PKG-20220924-MULTIDOMAIN-DJANGO',
    author='Ingeniería Novocode',
    author_email='jose.sandovalb@sansano.usm.cl',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'Framework :: Django :: 3.1',
        'Framework :: Django :: 3.2',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    packages=find_packages(),
    python_requires='>=3.6, <4',
)