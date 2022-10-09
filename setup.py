from setuptools import setup

setup(
	name="blog_gen",
	packages=["blog_gen"],
	include_package_data=True,
	install_requires=[
		"flask",
	],
)