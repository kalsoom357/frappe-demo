from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in daily_life/__init__.py
from daily_life import __version__ as version

setup(
	name="daily_life",
	version=version,
	description="about daily routine",
	author="kalsoom",
	author_email="daily-life@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
