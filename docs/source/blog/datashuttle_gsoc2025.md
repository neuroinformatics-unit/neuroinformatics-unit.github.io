:blogpost: true
:date: August 25, 2025
:author: Shrey Singh
:location: Delhi, India
:category: Blog
:language: English
:image: 1


(datashuttle-gsoc2025-title)=
# Add Google Drive and AWS as remote storage options to Datashuttle - Final Report

```{image} /_static/blog_images/gsoc2025/gsoc-niu.png
:align: center
:width: 50%
```

<br>

## Introduction

I am Shrey, this summer I contributed to Datashuttle, a tool for the creation, validation and transfer of neuroscience project folders. I worked on adding Google Drive and AWS buckets as remote storage options to Datashuttle.

**Mentors:** Joseph Ziminski, Niko Sirmpilatze, Adam Tyson

## Project Overview

Neuroscientists typically collect diverse types of data during experiments, including behavioral data (such as camera feeds tracking animal movement), electrophysiological data from neural probes, imaging data from microscopes, and physiological measurements. When researchers use different data organization schemes across labs or even within the same lab, it creates significant challenges: analysis scripts may fail to locate files, data becomes difficult to share between collaborators, and valuable research time is lost navigating inconsistent folder structures.

Datashuttle addresses these challenges by automating the creation, validation, and transfer of neuroscience project folders organized according to the NeuroBlueprint standard. This standardization ensures that research data follows consistent naming conventions and folder hierarchies, making it easier for researchers to share analysis pipelines, collaborate across institutions, and maintain organized projects as they scale.

Prior to this project, Datashuttle supported data transfers only to remote central machines via SSH connections. While effective, this approach limited adoption to labs with dedicated server infrastructure and technical expertise to maintain SSH-accessible systems. Many neuroscience labs, particularly smaller research groups or those at institutions with limited IT resources, rely on cloud storage solutions like Google Drive or AWS for their data management needs.

This project aimed to democratize Datashuttle's capabilities by extending remote storage options to include Google Drive and AWS S3 buckets. This expansion significantly broadens Datashuttle's accessibility, allowing researchers without dedicated servers to benefit from standardized data organization and automated transfers.

## Technical Implementation Overview

**Dual Interface Development**: Datashuttle provides both a Python API for programmatic use and a Terminal User Interface (TUI, a user interface that runs in the terminal) built with [Textual](https://textual.textualize.io/) for interactive use. Every new feature needed to be implemented across both interfaces, requiring careful consideration of user experience patterns in both programmatic and interactive contexts while minimizing code duplication.

**Cloud Storage Integration:** Rather than implementing custom transfer protocols, Datashuttle leverages [Rclone](https://rclone.org/) - a powerful command-line program for managing cloud storage. This project required an understanding of Rclone's configuration system, authentication workflows, and transfer mechanisms for both Google Drive and AWS S3. Each cloud provider has distinct authentication requirements: Google Drive uses OAuth2 flows requiring browser-based authorization, while AWS uses access keys and secret keys with various authentication methods.

**Asynchronous Operations:** Cloud authentication processes, particularly Google Drive's OAuth flow require user interaction. The TUI implementation needed sophisticated background processing to prevent interface freezing during connection setup, requiring careful orchestration of Python's threading and subprocess APIs.

## What I did

<h4> Background </h4>

While finding organizations to contribute to for GSoC 2025, I came across Neuroinformatics Unit (NIU), which was their first time participating in GSoC. Amongst all the projects, Datashuttle caught my attention because of my interest in SSH and cloud storage and a user interface in the terminal seemed very astonishing.

I followed a very simple process while contributing: reproduce the bug from the issue description, identify the top-level function most likely to contain the bug, then use debuggers and print statements to trace through the call stack (using a pen and paper really helps). I would iteratively drill down through each function call, following the execution path until I located the specific code that needed to be fixed. With time, you start putting together a mental map of how things work. To understand framework specific code, documentation is one's best friend.

<h4> Contributions </h4>

Before the GSoC coding period began, I worked on fixing issues on the Datashuttle repository and merged 3 PRs. 
Here are the PRs that were merged - 

1. [Add Workers for transferring data and Loading Animation](https://github.com/neuroinformatics-unit/datashuttle/pull/479) - Moved the data transfer logic to run in thread workers to free up the main thread for GUI/TUI rendering.
2. [Add Tests for Renaming File/Folder on directorytree](https://github.com/neuroinformatics-unit/datashuttle/pull/496) - Added test for a shortcut key for renaming file/folder on directory tree.
3. [Correct mainwindow typehints](https://github.com/neuroinformatics-unit/datashuttle/pull/505) - Fixed incorrect type hints for a function argument across the codebase.

These PRs helped me explore various parts of the codebase and understand the overall architecture better.

During the coding period, the primary focus was on the implementation, tests and documentation for the storage options. 

1. **Suggest next sub ses remote - PR [#484](https://github.com/neuroinformatics-unit/datashuttle/pull/484)**
    - Exposed the python API functions in the TUI to search remote folders for suggesting next subject and session folders.
    - Implemented thread workers to handle background searching of folders whilst displaying a loading indicator.

2. **Implemented the core logic for Google Drive and AWS connection setup via Python API and Terminal User Interface (TUI) - PR [#503](https://github.com/neuroinformatics-unit/datashuttle/pull/503)**
    - Implemented the core functions to authenticate to Google Drive and AWS and use [Rclone](https://rclone.org/) for data transfers.
    - Exposed the underlying functions of Datashuttle's Python API in the Terminal User Interface.
    - Created a single unified function to search central storages via any connection method.

3. **Implemented process management and threads to run connection setup in the background - PR [#503](https://github.com/neuroinformatics-unit/datashuttle/pull/503)**
    - Used threading library to run connection setup without blocking the TUI. 
    - Used Python's subprocess API to implement cancellation of connection setup via killing the underlying process.

4. **Wrote tests with `pytest` to test data transfers to Google Drive and AWS buckets - PR [#570](https://github.com/neuroinformatics-unit/datashuttle/pull/570/)**
    - Refactored existing transfer tests for SSH transfers to extend them for Google Drive and AWS.
    - Used Github secrets for connection credentials to run tests in the CI.
    - Wrote tests for connection setup via the TUI.
    - Wrote backward compatibility tests and extended existing TUI tests to test the new connection widgets.

5. **Added documentation for users to set up connection via the new connection methods - PR [#580](https://github.com/neuroinformatics-unit/datashuttle/pull/580)**
    - Updated and enhanced documentation to include instructions to connect to Google Drive and AWS buckets and added relevant examples.
    - Focused on providing clear instructions for setup, usage, and functionality, benefiting future contributors and users.

In addition to writing code, I performed code review for about 10 PRs, for which I was the sole approver prior to merging. Examples - [#515](https://github.com/neuroinformatics-unit/datashuttle/pull/515), [#208](https://github.com/neuroinformatics-unit/datashuttle/pull/208), [#551](https://github.com/neuroinformatics-unit/datashuttle/pull/551). Here is a [comprehensive list](http://github.com/search?q=is%3Apr+reviewed-by%3Acs7-shrey+repo%3Aneuroinformatics-unit%2Fdatashuttle+created%3A2025-04-01..2025-09-01&type=pullrequests&p=1).

<h4 align="center">Screenshots</h4>

```{image} /_static/blog_images/datashuttle_gsoc2025/datashuttle-new-project-dark.png
:align: center
:width: 80%
:class: only-dark
```

```{image} /_static/blog_images/datashuttle_gsoc2025/datashuttle-new-project-light.png
:align: center
:width: 80%
:class: only-light
```

<br>

```{image} /_static/blog_images/datashuttle_gsoc2025/datashuttle-gdrive-setup-dark.png
:align: center
:width: 80%
:class: only-dark
```

```{image} /_static/blog_images/datashuttle_gsoc2025/datashuttle-gdrive-setup-light.png
:align: center
:width: 80%
:class: only-light
```

## PRs created during the coding period

1. [Add Google Drive and AWS S3 as a Remote Storage option](https://github.com/neuroinformatics-unit/datashuttle/pull/503)

    **Status:** Merged <br>
    **Description:** This PR implemented the core functionality to connect to Google Drive and AWS S3 buckets, enabling users to store and retrieve neuroscience data from these cloud platforms. It included authentication workflows, background processing for non-blocking UI operations, and integration with the existing Datashuttle infrastructure.

2. [Add Tests for Google Drive and AWS Connection Methods](https://github.com/neuroinformatics-unit/datashuttle/pull/570)

    **Status:** Merged <br>
    **Description:** This PR implemented comprehensive tests for the new storage options, ensuring reliable data transfer and connection setup validation. It also extended existing tests for backward compatibility and added new TUI tests to validate the connection widgets.

3. [Add docs for Google Drive and AWS connections](https://github.com/neuroinformatics-unit/datashuttle/pull/580)

    **Status:** Merged <br>
    **Description:** This PR updated the documentation to include detailed instructions for setting up and using Google Drive and AWS S3 connections. It provided step-by-step guides and examples to ensure users can easily configure and use the new storage options.

4. [Google Drive and AWS S3 - Implementation, Tests and Documentation](https://github.com/neuroinformatics-unit/datashuttle/pull/556)

    **Status:** Merged <br>
    **Description:** This PR serves as an integration point for all the changes related to Google Drive and AWS S3 functionality. To maintain code clarity and facilitate reviews, we split the implementation, testing, and documentation into separate PRs that merge into this one. This approach allowed for focused development and reviews while keeping the final integration streamlined before merging into the main branch.

All of these PRs were merged into the main branch and the new functionality is now available in Datashuttle.

## Challenges / Learnings

The project was a smooth sail for the most part. However, a few parts felt a bit challenging.

1. ### Developing a multi step authentication flow

    Creating the complex, multi-step authentication workflows in Textual presented a significant paradigm shift from traditional web development. The connection setup process required orchestrating several sequential UI states, dynamically managing UI elements and flow control based on user input.

2. ### Writing tests to run in the CI environment

    Since CI environments don't have access to browsers (needed for Google's OAuth for Google Drive access), me and my mentor discussed several strategies for automated testing in the CI until we found a suitable one.


## Future work

This project lays groundwork for several potential improvements. Future work could focus on expanding test coverage to include more edge cases and user journeys, enhancing logging, improving documentation with detailed guides and troubleshooting sections, and refining error propagation. These enhancements would make Datashuttle more robust, user-friendly, and maintainable. 

Issues - [#525](https://github.com/neuroinformatics-unit/datashuttle/issues/525), [#549](https://github.com/neuroinformatics-unit/datashuttle/issues/549), [#554](https://github.com/neuroinformatics-unit/datashuttle/issues/554), [#577](https://github.com/neuroinformatics-unit/datashuttle/issues/577), [#582](https://github.com/neuroinformatics-unit/datashuttle/issues/582)


## Conclusion

The integration of Google Drive and AWS S3 storage capabilities significantly expands Datashuttle's accessibility and utility for neuroscience researchers. By extending beyond SSH connections to incorporate widely-used cloud storage platforms, this project removes a key barrier to adoption for labs without dedicated central servers. Through careful implementation, testing, and documentation, these new features maintain Datashuttle's core mission of standardizing neuroscience data management while making it accessible to a broader scientific community.

## Acknowledgements

I would like to express my gratitude to my mentor, [Joe Ziminski](https://github.com/JoeZiminski), for his constant encouragement and and support throughout this project. His constant positive comments on Github kept me motivated and I have learnt a lot on how to write clean and documented code from him. My coding style has improved a lot as a result of the regular code reviews. It was an absolute pleasure working with him.

Finally, I would like to thank Google for organizing GSoC helping first time contributors like me to enter the world of open source.

## Related Links

- [Datashuttle repository](https://github.com/neuroinformatics-unit/datashuttle)
- [GSoC Project Proposal](https://github.com/neuroinformatics-unit/gsoc/pull/9/files?short_path=fa70552#diff-fa70552f23074b47d370279a91cc831c563a2045143034e7d2ec56cab36de2e0)
- [My Github profile](https://github.com/cs7-shrey)