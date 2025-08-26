:blogpost: true
:date: August 25, 2025
:author: Shrey Singh
:location: Delhi, India
:category: Blog
:language: English
:image: 1


(datashuttle-gsoc2025-title)=
# Add Google Drive and AWS as remote storage options to DataShuttle - Final Report

```{image} /_static/blog_images/gsoc2025/gsoc-niu.png
:align: center
:width: 50%
```

<br>

## Introduction

I am Shrey, this summer I contributed to DataShuttle, a tool for the creation, validation and transfer of neuroscience project folders. I worked on adding Google Drive and AWS buckets as remote storage options to DataShuttle.

**Mentors:** Joseph Ziminski, Niko Sirmpilatze, Adam Tyson

## Project Overview

DataShuttle allows transfer of neuroscience project folders to remote central machines via SSH. This project aims to extend the remote storage options to Google Drive and AWS.

## What I did

Before the GSoC coding period began, I worked on fixing issues on the DataShuttle repository and merged 3 PRs. Here are the PRs that were merged - [#479](https://github.com/neuroinformatics-unit/datashuttle/pull/479), [#496](https://github.com/neuroinformatics-unit/datashuttle/pull/496), [#505](https://github.com/neuroinformatics-unit/datashuttle/pull/505). During the coding period, the primary focus was on the implementation, tests and documentation for the storage options. Additionally, I was involved in code reviews on other PRs on the repository as well.

1. **Implemented the core logic for Google Drive and AWS connection setup via Python API and Terminal User Interface (TUI) - PR [#503](https://github.com/neuroinformatics-unit/datashuttle/pull/503)**
    - Implemented the core functions to authenticate to Google Drive and AWS and use [Rclone](https://rclone.org/) for data transfers.
    - Exposed the underlying functions of DataShuttle's Python API in the Terminal User Interface.
    - Created a single unified function to search central storages via any connection method.

2. **Implemented process management and threads to run connection setup in the background - PR [#503](https://github.com/neuroinformatics-unit/datashuttle/pull/503)**
    - Used threading library to run connection setup without blocking the TUI. 
    - Used Python's subprocess API to implement cancellation of connection setup via killing the underlying process.

3. **Wrote transfer tests to test data transfers to Google Drive and AWS buckets - PR [#570](https://github.com/neuroinformatics-unit/datashuttle/pull/570/)**
    - Refactored existing transfer tests to extend them for Google Drive and AWS.
    - Used Github secrets for connection credentials to run tests in the CI.
    - Wrote tests for connection setup via the TUI.
    - Wrote backward compatibility tests and extended existing TUI tests to test the new connection widgets.

4. **Added documentation for users to set up connection via the new connection methods - PR [#580](https://github.com/neuroinformatics-unit/datashuttle/pull/580)**
    - Updated and enhanced documentation to include instructions to connect to Google Drive and AWS buckets and added relevant examples.
    - Focused on providing clear instructions for setup, usage, and functionality, benefiting future contributors and users.

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

## The current state

The core implementation, tests and documentation have been written and is awaiting a final review.

## What's left to do

The PRs are currently under review and once they are approved, they will be merged into the main branch.

## PRs created during the coding period

1. [Add Google Drive and AWS S3 as a Remote Storage option](https://github.com/neuroinformatics-unit/datashuttle/pull/503)

    **Status:** Merged <br>
    **Description:** This PR implemented the core functionality to connect to Google Drive and AWS S3 buckets, enabling users to store and retrieve neuroscience data from these cloud platforms. It included authentication workflows, background processing for non-blocking UI operations, and integration with the existing DataShuttle infrastructure.

2. [Add Tests for Google Drive and AWS Connection Methods](https://github.com/neuroinformatics-unit/datashuttle/pull/570)

    **Status:** Merged <br>
    **Description:** This PR implemented comprehensive tests for the new storage options, ensuring reliable data transfer and connection setup validation. It also extended existing tests for backward compatibility and added new TUI tests to validate the connection widgets.

3. [Add docs for Google Drive and AWS connections](https://github.com/neuroinformatics-unit/datashuttle/pull/580)

    **Status:** Under review <br>
    **Description:** This PR updated the documentation to include detailed instructions for setting up and using Google Drive and AWS S3 connections. It provided step-by-step guides and examples to ensure users can easily configure and use the new storage options.

4. [Google Drive and AWS S3 - Implementation, Tests and Documentation](https://github.com/neuroinformatics-unit/datashuttle/pull/556)

    **Status:** Under review <br>
    **Description:** This PR serves as an integration point for all the changes related to Google Drive and AWS S3 functionality. To maintain code clarity and facilitate reviews, we split the implementation, testing, and documentation into separate PRs that merge into this one. This approach allowed for focused development and reviews while keeping the final integration streamlined before merging into the main branch.

## Challenges / Learnings

The project was a smooth sail for the most part. However, a few parts felt a bit challenging.

1. ### Developing a multi step authentication flow

    Creating the complex, multi-step authentication workflows in Textual presented a significant paradigm shift from traditional web development. The connection setup process required orchestrating several sequential UI states, dynamically managing UI elements and flow control based on user input.

2. ### Writing tests to run in the CI environment

    Since CI environments don't have access to browsers (needed for Google's oauth), me and my mentor discussed several strategies for automated testing in the CI until we found a suitable one.


## Future work

This project lays groundwork for several potential improvements. Future work could focus on expanding test coverage to include more edge cases and user journeys, enhancing logging, improving documentation with detailed guides and troubleshooting sections, and refining error propagation. These enhancements would make DataShuttle more robust, user-friendly, and maintainable. 

Issues - [#525](https://github.com/neuroinformatics-unit/datashuttle/issues/525), [#549](https://github.com/neuroinformatics-unit/datashuttle/issues/549), [#554](https://github.com/neuroinformatics-unit/datashuttle/issues/554), [#577](https://github.com/neuroinformatics-unit/datashuttle/issues/577), [#582](https://github.com/neuroinformatics-unit/datashuttle/issues/582)


## Conclusion

The integration of Google Drive and AWS S3 storage capabilities significantly expands DataShuttle's accessibility and utility for neuroscience researchers. By extending beyond SSH connections to incorporate widely-used cloud storage platforms, this project removes a key barrier to adoption for labs without dedicated central servers. Through careful implementation, testing, and documentation, these new features maintain DataShuttle's core mission of standardizing neuroscience data management while making it accessible to a broader scientific community.

## Acknowledgements

I would like to express my gratitude to my mentor, [Joe Ziminski](https://github.com/JoeZiminski), for his constant encouragement and and support throughout this project. His constant positive comments on Github kept me motivated and I have learnt a lot on how to write clean and documented code from him. My coding style has improved a lot as a result of the regular code reviews. It was an absolute pleasure working with him.

Finally, I would like to thank Google for organizing GSoC helping first time contributors like me to enter the world of open source.

## Related Links

- [DataShuttle repository](https://github.com/neuroinformatics-unit/datashuttle)
- [GSoC Project Proposal](https://github.com/neuroinformatics-unit/gsoc/pull/9/files?short_path=fa70552#diff-fa70552f23074b47d370279a91cc831c563a2045143034e7d2ec56cab36de2e0)
- [My Github profile](https://github.com/cs7-shrey)