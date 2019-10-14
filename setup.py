


from setuptools import setup, find_packages

setup(name='pandora_online',
      version='0.1',
      description='The Pandora Online Class Helper',
      long_description='Really, this class help for pro.p-on.ru requests.',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6.8',
        'Topic :: Utilites :: API Hepler',
      ],
      keywords='pandora pandect',
      url='http://github.com/vladimir1marchenko/pandora_oline',
      author='Vladimir Marchenko',
      author_email='vladimir1marchenko@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'markdown','requests','json'
      ],
      include_package_data=True,
      zip_safe=False)
