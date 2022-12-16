# Neuroinformatics Unit Website

The main website of the [SWC](https://www.sainsburywellcome.org/web/)/[GCNU](https://www.ucl.ac.uk/gatsby/gatsby-computational-neuroscience-unit) Neuroinformatics Unit.

## Website structure

The website is built using [Sphinx](https://www.sphinx-doc.org/en/master/) and the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/latest/).
* Build requriements are listed in `docs/requirements.txt`.
* The source files are located in `docs/source` and include:
  * `conf.py`: Sphinx configuration file
  * `index.md`: landing page linking to all other pages
  * Other pages are defined as `<page-name>.md` files in the source directory, or its subdirectories.
* The built website is deployed from the `gh-pages` branch to the [neuroinformatics.dev](https://neuroinformatics.dev) domain.
  
## Editing the website
* Clone the GitHub repository, and create your `new_branch`.
* Edit the website and commit your changes to the `new_branch`.
* Check how the edited website looks by [building it locally](#local-build).
* Push the `new_branch` to GitHub and create a pull request. This will automatically trigger a [GitHub Action](https://github.com/ammaraskar/sphinx-action) that checks if the website still builds correctly.
* If the checks pass, assign someone to review your changes. 
* When the reviewer merges your changes into the `main` branch, a different [GitHub Action](https://github.com/peaceiris/actions-gh-pages) will be triggered, which will build the website and publish it to the `gh-pages` branch.
* Check the deployed build at [neuroinformatics.dev](https://neuroinformatics.dev)

## Local build
If you wish to view the website locally, before you push it,
you can do so by running the following commands from the
root of the repository:

```bash
# only need to do this once
pip install -r docs/requirements.txt
# do this every time you want to refresh the build
sphinx-build docs/source docs/build
```
You can view the local build at `docs/build/index.html`
