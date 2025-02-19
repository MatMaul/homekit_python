#
# Copyright 2018 Joachim Lusiardi
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from distutils.core import setup

setup(
    name='homekit',
    packages=['homekit', 'homekit.model'],  # this must be the same as the name above
    version='0.5',
    description='Python code to interface HomeKit Accessories and Controllers',
    author='Joachim Lusiardi',
    author_email='pypi@lusiardi.de',
    url='https://github.com/jlusiardi/homekit_python',  # use the URL to the github repo
    download_url='https://github.com/jlusiardi/homekit_python/archive/0.5.tar.gz',  # I'll explain this in a second
    keywords=['HomeKit'],  # arbitrary keywords
    classifiers=[],
    install_requires=[
        'zeroconf',
        'gmpy2',
        'py25519',
        'hkdf',
        'ed25519',
    ],
)
