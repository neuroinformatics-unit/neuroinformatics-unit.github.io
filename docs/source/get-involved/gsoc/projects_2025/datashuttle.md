# GSoC NIU Projects 2025: `datashuttle`

If you are interested in any of these [datashuttle](https://github.com/neuroinformatics-unit/datashuttle) projects, [get in touch](https://datashuttle.neuroinformatics.dev/pages/community/index.html)! Feel free to open a new topic on our [Zulip GSoC channel](https://neuroinformatics.zulipchat.com/#narrow/channel/487898-GSoC) and ask the community.

Our working language is English.


<!-- ------------------------------ -->
:::{dropdown} {fas}`database;sd-text-primary` Allow Google Drive or AWS as remote storage

In systems neuroscience, a lack of standardisation in data organisation schemes creates a barrier to data-sharing
and collaboration. ``datashuttle`` provides a Python API and terminal user interface (TUI) to allow researchers
to create, validate and transfer folders in a standardised way.

Projects can be transferred between computer systems in ``datashuttle`` via SSH or mounting drives.
We would like to support transfer to Google Drive or and Amazon Web Services (AWS) buckets.
Under the hood ``datashuttle`` uses [RClone](https://rclone.org/), which already implements transfer to Google Drive and AWS.

**Deliverables**
<!-- Goals, or expected status after Community Bonding Period, Start of Coding, End of Coding. Stretch goals? -->
- Extend ``datashuttle`` functionality to permit transfer between a local filesystem and Google Drive or AWS. This will involve exposing new functionality within the Python API as well as the terminal user interface.
- Tests to cover any added functionality.
- Documentation for the new functionality.

- **Duration**
<!-- Small (~90 hours), Medium (~175 hours) or Large (~350 hours)  -->
Medium (~175 hours)


**Difficulty**
<!-- Is this project geared more toward a student level or a more advanced developer level? -->
This project is well-suited for a beginner contributor to open source. 


**Required skills**
Experience with Python

**Nice-to-haves**
Experience with network data transfers (e.g. rsync, rclone, Google Drive, AWS)

**Potential mentors**
- [@JoeZiminski](https://github.com/JoeZiminski)

**Further reading**
<!-- The best pages include links to more detailed descriptions and related materials for each project. They might even include actual use cases! -->

[``datashuttle``](https://datashuttle.neuroinformatics.dev/index.html) and [RClone](https://rclone.org/) websites.

:::


:::{dropdown} {fas}`database;sd-text-primary` Deploy datashuttle as installable package

Currently, ``datashuttle`` requires conda to use. It would be great if the terminal-user-interface
it could be deployed as an executable installation across Windows, macOS and Linux. This would make it
 accessible for those without coding experience.

Unfortunately, [textual](https://github.com/Textualize/textual) renders poorly in native system terminals, and so would likely require also deploying a terminal to run in.
There are existing implementations [packaging textual in cross-platform executables](https://github.com/Textualize/textual/discussions/3834)
but no standard way to proceed.

This project would involve researching approaches, and implementing the most robust and  maintainable approach for ``datashuttle``.

**Deliverables**
<!-- Goals, or expected status after Community Bonding Period, Start of Coding, End of Coding. Stretch goals? -->
- Research approaches for cross-platform distribution of a ``datashuttle`` executable
- Assess how robust and maintainable these are
- Implement the best approach for ``datashuttle``
- Document and test in our GitHub CI

- **Duration**
<!-- Small (~90 hours), Medium (~175 hours) or Large (~350 hours)  -->

Large (~175 hours)


**Difficulty**
<!-- Is this project geared more toward a student level or a more advanced developer level? -->

The project will require research deep into the python packaging ecosystem and mechanics,
and so would best suit someone who is already experienced with Python. Knowledge of 
Python packaging is not required, but a good understanding of Python to use as a 
starting point is.


**Required skills**
Experience with Python

**Nice-to-haves**
Experience with created executable Python distributions (e.g. with PyInstaller).

**Potential mentors**
- [@JoeZiminski](https://github.com/JoeZiminski).

**Further reading**
<!-- The best pages include links to more detailed descriptions and related materials for each project. They might even include actual use cases! -->

[``datashuttle``](https://datashuttle.neuroinformatics.dev/index.html) and [textual](https://github.com/Textualize/textual).

:::
