# Development guidelines for specific languages and frameworks

## Python

### Setting up a project
* To set up a new Python project, use the [NIU cookiecutter](https://github.com/neuroinformatics-unit/python-cookiecutter) 
repository. This ensures that the required tooling is in place (e.g. CI) and also that we are all using a familiar 
project structure. Part of using this cookiecutter is keeping it updated (e.g. Python versions, best practices) and 
communicating those changes to all users.

* Whenever possible, we will use `pyproject.toml` as the main configuration file for the project. Support for 
`setup.cfg` and `setup.py` will be deprecated in future Python versions. This will also be the default option for the SWC cookiecutter.

### Virtual environments
* We will use [conda](https://docs.conda.io/en/latest/) environments for all Python projects.
* Package installations will be handled by either `conda` or `pip`.
  
### Testing and coverage
* All Python software should have automated tests written using [pytest](https://docs.pytest.org) that run quickly on 
all operating systems. Tests that take many minutes on low-powered systems (e.g. GitHub actions) are often ignored.
* We will use [codecov](https://about.codecov.io/) as the coverage reporting tool. This is free for open-source 
projects and integrates with GitHub actions.

### Formatting and QC
* We use [Black](https://black.readthedocs.io/en/stable/), [ruff](https://beta.ruff.rs/docs/), and [mypy](https://mypy.readthedocs.io/en/stable/) to ensure a consistent
code style.
* Currently, the above tools are automated in the SWC cookiecutter using [pre-commit](https://pre-commit.com/). Running 
`pre-commit install` once locally will set up the pre-commit hooks to be executed automatically before each commit.

### Continuous integration
* All pushes and pull requests will be built by [GitHub actions](https://docs.github.com/en/actions). This will usually include linting, testing and deployment.
* As a rule, actions will run on all operating systems (Linux, macOS, Windows) and on all Python versions that are supported by the project.
* GitHub actions workflows should be contributed to the [NIU actions repository](https://github.com/neuroinformatics-unit/actions) to aid reuse.

### Automated versioning
We use [`setuptools_scm`](https://github.com/pypa/setuptools_scm) to automatically version packages. It should be 
configured in the `pyproject.toml` file (as per the [cookiecutter template](https://github.com/neuroinformatics-unit/python-cookiecutter)). 
`setuptools_scm` will automatically infer the version using git. 
To manually set a new semantic version, create a tag and make sure the tag is pushed to GitHub. Make sure you commit 
any changes you wish to be included in this version. E.g. to bump the version to `1.0.0`:

```bash
git add .
git commit -m "Add new changes"
git tag -a v1.0.0 -m "Bump to version 1.0.0"
git push --follow-tags
```

### Dependency support
Packages have to choose which versions of dependencies they officially support, with minimum supported versions of each 
dependency used in continuous integration testing. All NIU projects should follow 
[NEP 29 — Recommend Python and NumPy version support as a community policy standard](https://numpy.org/neps/nep-0029-deprecation_policy.html) 
to determine the **minimum** set of supported package versions:

- The last 42 months of Python releases
- The last 24 months of NumPy releases

In addition to this, the last 24 months of other dependencies should also be supported.

### Licensing
* Unless the software has commercial potential or depends upon other software with a restrictive license, we will default to using
[The 3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause) (BSD-3-Clause).
* A `LICENSE` file should be included in the root of the repository (already present in the SWC cookiecutter).
* To learn more about our licensing policies, see [our licensing guide](https://howto.neuroinformatics.dev/open_science/Licensing.html).

### Documentation
* We will use [Sphinx](https://www.sphinx-doc.org/en/master/) to generate documentation for Python projects. 
We will build the documentation websites with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html).
* Docstrings should be written in [numpydoc](https://numpydoc.readthedocs.io/en/latest/format.html) format.
* The documentation structure should be informed by the [diataxis](https://diataxis.fr) framework.

### Logging
All Python software should use the inbuilt Python logging module, rather than e.g. print statements. To standardise 
this, we will use [fancylog](https://github.com/neuroinformatics-unit/fancylog). This tool should be updated 
regularly to reflect best practices and ensure it is suitable for use with all projects.

### Configuration files
User-editable configuration files should use the YAML format. As far as possible, machine-readable outputs from software should also use this format.

### Release
* All Python software should be released on PyPI to enable a simple `pip install`. At a minimum, each project should 
have two owners — [Adam (adamltyson)](https://github.com/adamltyson) and the lead developer. Others can be added as owners/maintainers as appropriate.
* We will also aim to release projects on [conda-forge](https://conda-forge.org/), especially for packages with non-Python dependencies.
