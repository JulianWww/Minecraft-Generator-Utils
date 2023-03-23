from distutils.core import setup

setup(
    name = "mc_generator_utils",
    packages=["mc_generator_utils"],
    version="0.0.0.1",
    license='CCO-0',
    description="Utility functions for minecraft data and assets generation",
    long_description="""
    A library containing utility functions for minecraft data and asset generation. Usefull for mod authos, who use python generation scripts to avoid creating all the files themselves."
    """,
    author = 'Julian Wandhoven',                   # Type in your name
    author_email = 'julian.wandhoven@gmail.com',

    url="https://github.com/JulianWww/jpe_types",
    keywords=["minecraft", "datageneration"],
    classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Programming Language :: Python :: 3'], #Specify which pyhton versions that you want to support
)