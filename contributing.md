# Contributing to AcadeMe

Thank you for supporting AcadeMe and looking for ways to help. 
We surely apperciate open source contributers! But before you contribute, please make sure to follow these guidelines.

## Setting up
1. Fork the repository! <img align="right" width="250" src="https://camo.githubusercontent.com/fcf9a4ed664cc63de2fcb14d1135072ba6d4c74a8e9bdb224ad6ab1e72600c3b/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f666f726b2e706e67">
2. Clone the repository!
###### Make sure you set up the development environment by downloading the following:
1. Vagrant
2. VitualBox (or any other hypervisor)

Now, a development environment will automatically be set up for you when typing `vagrant up` in the directory of the repository.


## Issues

### Bug Reports

We use GitHub [issues](https://github.com/redhat-beyond/AcadeMe/issues) to track public bugs. Report a bug by opening a new issue; it's that easy!
Great Bug Reports tend to have:

- A quick summary and/or background
- Steps to reproduce
- Be specific!
- Give sample code if you can.
- What actually happens

People love thorough bug reports. I'm not even kidding.


## Pull requests

<img align="right" width="250" height="150" src="https://theindecisiveeejit.files.wordpress.com/2014/12/size-matters.jpg">

- Make SMALLER pull requests --------------->
- Write useful description and titles
- Have on-point commit messages
- Add comments on your pull request to help guide the reviewer
- Make it visual


### Follow the Code Style Guidelines

Ensure that your code follows the [PEP 8 Style guide for Python code](https://www.python.org/dev/peps/pep-0008/) before submitting a pull request.

We have also set up Flake8 to ensure that our style guides are being followed.



### Submit finished and well-tested pull requests

Please do not submit pull requests that are still a work in progress. Pull requests should be thoroughly tested and ready to merge before they are submitted.

To test your code, run `pipenv run pytest` while inside the Vagrant machine. Make sure you add your tests too.