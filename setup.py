# this file was created by following
# https://github.com/pypa/sampleproject/blob/master/setup.py
# as example

from setuptools import setup, find_packages

setup(
    name='keras_transformer',
    # This allows to use git/hg to auto-generate new versions
    use_scm_version={"root": ".", "relative_to": __file__},
    setup_requires=['setuptools_scm'],
    description=('Library for building (Universal) Transformer models '
                 'using Keras'),
    url='https://github.com/clarencechen/keras-transformer',
    author='Clarence Chen',
    author_email='clarencechenct@berkeley.edu',
    python_requires='>=3.4.3',

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],

    keywords='development',

    packages=find_packages(where='.', exclude=['example']),
    install_requires=['Keras>=2.0.8', 'numpy'],
    tests_require=['pytest'],
    include_package_data=True,
)
