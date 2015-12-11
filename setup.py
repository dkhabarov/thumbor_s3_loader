from setuptools import setup, find_packages

setup(
	name = 'thumbor_s3_loader',
	version = "1",
	description = 'Thumbor S3 extension',
	author = 'Denis Khabarov',
	author_email = 'admin@saymon21-root.pro',
	zip_safe = False,
	include_package_data = True,
	packages=find_packages(),
	requires=['dateutil','thumbor','boto']
)
