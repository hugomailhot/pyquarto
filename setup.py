from setuptools import setup, find_packages

requirements = [
    'terminaltables'
]

setup(name='pyquarto',
      version='0.1',
      description='The great game of Quarto.',
      url='https://github.com/Delphia/data_utils',
      install_requires=requirements,
      author='Hugo Mailhot',
      author_email='mailhot.hugo@gmail.com',
      packages=find_packages(include=['pyquarto']),
      zip_safe=False)

