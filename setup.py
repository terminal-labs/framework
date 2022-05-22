# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['framework', 'framework.config', 'framework.config._build_resources']

package_data = \
{'': ['*'], 'framework': ['payload/*']}

install_requires = \
['arrow==1.2.2',
 'click==8.1.3',
 'colorama==0.4.4',
 'poethepoet>=0.13.1,<0.14.0',
 'six==1.16.0']

entry_points = \
{'console_scripts': ['framework = framework.cli:app']}

setup_kwargs = {
    'name': 'framework',
    'version': '0.1.4',
    'description': '',
    'long_description': 'None',
    'author': 'Michael Verhulst',
    'author_email': 'michael@terminallabs.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
