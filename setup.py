from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in rh/__init__.py
from rh import __version__ as version

setup(
	name="rh",
	version=version,
	description="Recursos Humanos - Si Hay Sistema",
	author="Si Hay Sistema",
	author_email="m.monroyc22@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
