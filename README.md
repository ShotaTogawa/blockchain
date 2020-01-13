# blockchain

*Activate the virtual env*

A virtual environment allows you to create an isolated space where your project (or a group of projects) can install its external packages. 
This is especially helpful when you're managing multiple projects on your machine. 
Often, external packages update their classes and methods when new versions are released. 
However, separate virtual environments can have different versions of the same package installed - that way,
each project can rely on the versions of their dependencies to stay consistent.

```
python3 -m venv blockchain-envpython3 -m venv blockchain-env`  
source blockchain-env/bin/activate
```

*Install all package*
```
pip3 instal rquirement.txt
```

*version指定*

`library==5.1.2`

**Run the test**
Make sure to activate the virtual env

```
python3 -m pytest backend/tests
```

**package**

A package in python allows you to group together related modules. 
To create a package, create a directory with an __init__.py file. 
Python will then recognize the directory as a package, 
allowing you to import modules contained in that package with a dot syntax. 
For example, the blockchain/ directory contains both __init__.py and block.py. 
This allows other files to import the block module with blockchain.block.