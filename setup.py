# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import audioadmin



setup(
    name='django-audioadmin',
    version=audioadmin.__version__,
    description='A reusable Django app for uploading/previewing audio files plus a simple id3 tag reader (Title/Artist/Album)',
    long_description=open('README.rst', 'r').read(),
    keywords="django, audio, id3",
    url='http://github.com/ngrinkevich/django-audioadmin',
    author='Nik G',
    author_email='subzeromedia@gmail.com',
    license='MIT License',
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    package_data={},
    install_requires=[
        'Django >= 1.7.1',
        'Pillow >= 2.6.1',
        'django-imagekit >= 3.2.4',
        'mutagen >= 1.22'
    ],
    classifiers=[
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Framework :: Django',
        'Environment :: Web Environment',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
)
