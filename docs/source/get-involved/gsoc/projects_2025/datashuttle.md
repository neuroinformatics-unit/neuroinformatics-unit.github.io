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


<!-- ------------------------------ -->
:::{dropdown} {fas}`database;sd-text-primary` Extend the functionality of the terminal user interface

In systems neuroscience, a lack of standardisation in data organisation schemes creates a barrier to data-sharing
and collaboration. ``datashuttle`` provides a Python API and terminal user interface (TUI) to allow researchers
to create, validate and transfer folders in a standardised way.

In ``datashuttle``, there are a number of features which are available in the Python API but not yet exposed in the terminal interface.
``datashuttle`` uses [textual](https://github.com/Textualize/textual) to create the TUI. This project would
involve extending the functionality of the TUI, providing experience in coding for graphical user interfaces,
in particular terminal user interfaces.

**Deliverables**
<!-- Goals, or expected status after Community Bonding Period, Start of Coding, End of Coding. Stretch goals? -->
- A python implementation adding [textual](https://github.com/Textualize/textual) widgets that perform and display project validation. This will include buttons, radio-buttons and drop down menus and a [log display](https://textual.textualize.io/widgets/rich_log/) for validation errors.
- Improvements to user experience:
  - Implement code to allow a responsive user interface while a transfer job is performed.
  - Add buttons and drop-down list to edit a [directory tree](https://textual.textualize.io/widgets/directory_tree/).
- Tests to cover any added functionality.
- Documentation for the new functionality.

**Duration**
<!-- Small (~90 hours), Medium (~175 hours) or Large (~350 hours)  -->
Medium (~175 hours)


**Difficulty**
<!-- Is this project geared more toward a student level or a more advanced developer level? -->
This project is well-suited for a student or a beginner contributor to open source. No experience
in graphical or terminal user interfaces is required.


**Required skills**
Experience with Python

**Potential mentors**
- [@JoeZiminski](https://github.com/JoeZiminski)

**Further reading**
<!-- The best pages include links to more detailed descriptions and related materials for each project. They might even include actual use cases! -->

The[NeuroBlueprint](https://neuroblueprint.neuroinformatics.dev/latest/index.html) and 
[``datashuttle``](https://datashuttle.neuroinformatics.dev/index.html) websites.

:::
