# Introduction to Third-Party Package Management in Python

'''
Introduction to PIP and the Python Package Index (PyPI)

- Python Package Index (PyPI) is the official third-party software repository for Python.
    - Thousands of modules.
    - Offers a mechanism to share modules.
    - Maintained by the Python community.

- Module is a file containing Python code. Packages are a collection of modules.

- Package in PyPI refers to a distribution package. It could include modules, data files, and other resources.
- PyPI consists of two parts: 1) the repository itself and 2) the tools to interact with it.
- Look at Pypi.org for more packages and use PIP to install them. If packages include modules, they cn be imported.

- Package types pertain to text-based template engine, web application servers, natural language processing libraries, video game engines, and more.

- PIP is Package Installer for Python.
- Code in packages is considered untrusted code.

- Takeaways:
    1. The PPI is a repository of community-created Python packages.
    2. Each of the packages listed falls under a license: licenses specify how developers can use the package.
    3. PIP is a tool used to install, update, and remove packages.
    4. The code on the Package Index is considered untrusted code b/c it's should be considered not fully viewed and could contain buggy or malicious code.
'''

# --------------------------------------------------------

'''
Considerations for Package Versions

- The third-party packages should exist on the operating systems file system. Usually located at python/lib/python3.9/site-packages.
- Import syntax: used to import packages and/or modules into our code.
- The site-packages directory location will depend on what OS your're using and how Python was installed.

- Could be multiple versions of the same package installed on the system. Could be a problem if the code is not compatible with the version of the package.
- Could end of up with multiple applications using different versions of the same package.
- PIP provides a mechanism for installing specific versions of packages. PIP can also determine which versions are allowed to be installed during updates.

- VENV module provides support for creating lightweight, 'virtual environments' with their own site directories, optionally isolated from system site directories.

'''

# --------------------------------------------------------

'''
Considerations for Package Selections

- Licensing: does the package's license allow you to use the code as needed?
- Documentation: does the package contain useful documentation?
- Effort savings: does the introduction fo this package save enough effort to justify its use?
- Quality: does the package contain tests that validate the code? Is the code close enough to be considered idiomatic?
- Security: does the package take reasonable considerations to maintain security?






'''