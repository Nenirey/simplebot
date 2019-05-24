# -*- coding: utf-8 -*-
import re
import os

from setuptools import setup


MODULE_NAME = 'simplebot_ddg'
CLASS_NAME = 'DuckDuckGo'
with open(os.path.join(MODULE_NAME, '__init__.py'), 'rt', encoding='utf8') as fd:
    source = fd.read()
PLUGIN_NAME = re.search(r'name = \'(.*?)\'', source, re.M).group(1)
VERSION = re.search(r'version = \'(.*?)\'', source, re.M).group(1)
AUTHOR = re.search(r'author = \'(.*?)\'', source, re.M).group(1)
AUTHOR_EMAIL = re.search(r'author_email = \'(.*?)\'', source, re.M).group(1)

setup(
    name=MODULE_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description='A plugin for SimpleBot, a Delta Chat bot (http://delta.chat/)',
    long_description='For more info visit https://github.com/adbenitez/simplebot',
    long_description_content_type='text/x-rst',
    url='https://github.com/adbenitez/simplebot',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Topic :: Utilities'
    ],
    keywords='deltachat simplebot plugin',
    #project_urls={},
    packages=[MODULE_NAME],
    install_requires=['simplebot', 'beautifulsoup4', 'Jinja2'],
    python_requires='>=3.5',
    entry_points={
        'simplebot.plugins': '{} = {}:{}'.format(PLUGIN_NAME, MODULE_NAME, CLASS_NAME)
    },
    include_package_data=True
)
