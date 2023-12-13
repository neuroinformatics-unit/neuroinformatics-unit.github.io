# Development guidelines

All our software is built as a team, and this means we must agree on some development conventions. This page 
covers our internal development guidelines, which we hope are also useful to external contributors.


## General guidelines

* All projects will use [Git](https://git-scm.com/) for version control and [GitHub](https://github.com/) for hosting.

* By default we will use the [neuroinformatics-unit](https://github.com/neuroinformatics-unit) organisation for new projects. 
Otherwise we may use other organisations, e.g. the [SWC organisation](https://github.com/SainsburyWellcomeCentre) when 
working with SWC researchers, or when releasing software to the community. Often we will use a project-specific organisation (e.g. [BrainGlobe](https://github.com/brainglobe)).

* Unless there is a specific reason not to, we will develop all software in the open (i.e. public). 
This facilitates collaboration and encourages good software development practices.

* All changes to a codebase must be via a 
[Pull Request (PR)](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) approved by another member of the team. 
How detailed the review should be will depend depends on the changes made, and the current status of the project. E.g. 
a brand new, exploratory project may not need every line of code checked in detail, but a heavily used community project may do.

* All software is developed in branches. When developing a new feature, or planning to make substantive changes 
(e.g. not a quick bug fix which could go straight to a ready to review PR), make a new branch as well as a draft 
PR detailing the purpose of the new code. Then, new commits can be easily tracked and commented on in-progress, 
and extended periods of coding in isolation avoided. When the code is ready to be merged, the PR can be changed to 
"ready to review" for full review. All code must be reviewed by at least one other team member 
(or collaborator) before merging.

* Code should be reviewed often, in as small a block as is practical. There should be no "magic unveiling" of code 
developed in secret over a long time. Commits should be pushed to GitHub as often as practical, and feedback from 
others (code review, and informal conversation) solicited as often as possible.

* We will use the best tool (language, framework etc.) for the job. This depends on many factors such as the 
computation itself, relevant other packages and collaborators. We will always prefer to work in open-source languages. 
Python is likely to often be the most appropriate language due to the level of adoption in the community (we want 
researchers to contribute to the code). 
Guidelines specific to each language or framework can be found in 
[Development guidelines for specific languages and frameworks](./languages_frameworks).

* We aim that software can be used across operating systems, by novice users and using anything from a standard laptop 
to HPC.

* All software will be fully documented. Our understanding of documentation is guided by the systematic 
[diataxis](https://diataxis.fr/) framework. We will strive to standardise the documentation structure across projects 
by [gradually adopting the diataxis approach](https://diataxis.fr/how-to-use-diataxis/#).

* All software will have (close to) 100% test coverage. This applies at all stages, i.e. tests shouldn't be added 
"later" (later often doesn't come). **All code should be fully tested (and passing those tests) before submitting for 
review**. If the code cannot be fully tested, or is failing the tests, the PR should be marked as "draft" to enable discussion.

* All tests should run automatically on GitHub actions on macOS, Windows and Linux where appropriate. Other testing 
permutations will depend on the language, e.g. for Python, all supported Python versions should be tested on at least 
one operating system.

* As far as possible, we should follow [Test Driven Development](https://en.wikipedia.org/wiki/Test-driven_development) practices.

* We will use [semantic versioning](https://semver.org/) for all projects.

## Pull requests
- Please submit _draft_ pull requests as early as possible (you can still push to the branch once submitted) to
  allow for discussion.
- One approval of a PR is enough for it to be merged.
- Unless someone approves the PR with optional comments, the PR can be immediately merged by the approving reviewer.
- Please merge via "Squash and Merge" on GitHub to maintain a clean commit history.
- Ask for a review from someone specific if you think they would be a particularly suited reviewer (possibly noting
  why they are suited on the PR description)


## Starting a new project
When beginning a new project, the above guidelines can be relaxed until the basic structure of the code is established. 
In particular, rather than waiting for a series of small PRs to be merged, one model could be:

* Start the project in a `dev` branch
* Open a draft PR, and assign someone as a reviewer (for another set of eyes, not necessarily a proper review)
* Keep committing to `dev` until a good initial project structure is defined
* Merge `dev` into `main`
* Move to feature branch/PR workflow (branching from `dev` if necessary while waiting for `dev` to be merged)


## Issue tags

All new repositories in the NIU organisation will have the following tags. These can be added to existing projects to 
help standardise how we categorise issues. As a general rule, `critical` issues should be tackled ASAP and 
`priority` issues should be tackled before any others.

| Label                 | Description                             |
|-----------------------|-----------------------------------------|
| critical              | To be addressed first                  |
| priority              | More important than other issues       |
| documentation         | Improvements or additions to documentation  |
| bug                   | Something isn't working                |
| enhancement           | New feature or request                 |
| duplicate             | This issue or pull request already exists |
| good first issue      | Good for newcomers                     |
| question              | Further information is requested       |
| wontfix               | This will not be worked on             |

## Further details
```{toctree}
:maxdepth: 2
languages_frameworks
```
