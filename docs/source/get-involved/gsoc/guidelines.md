# GSoC NIU Contributor Application Guidelines

## General tips
These tips are largely based on the [OpenAstronomy guidelines](https://openastronomy.org/gsoc/student_guidelines.html), with adaptations for the NIU organisation.

1. **Get in touch with the community**

    Open source work is done and communicated in public - the idea here is to demonstrate that you can do this! Join our [Zulip](https://neuroinformatics.zulipchat.com/), or browse through our GitHub repositories - you can find a full list of the NIU repositories under the [NIU GitHub organisation](https://github.com/neuroinformatics-unit) and the [Brainglobe](https://github.com/brainglobe) one. Read, ask questions, get to know the people involved, and participate in discussions. 
    
    Introduce yourself, and feel free to can ask questions about specific projects, the development process, recommended readings or the community. If you are not familiar with Zulip, have a look at this [quick guide](https://zulip.com/help/getting-started-with-zulip) first.

2. **Become a user**

    A great way to get started in the community of our open-source tools is to experience them as a user. Try to install and use our tools, experiment with the code, and report any issues you find. This will help you understand the tools better and will give you a better idea of what you can contribute.

    A good starting point as a user could be `movement`'s [gallery of examples](https://movement.neuroinformatics.dev/examples/index.html) or [BrainGlobe's tutorials](https://brainglobe.info/tutorials/index.html).

3. **Get ready to be a developer**

    Create a [GitHub](https://github.com/) account and learn how to use [git](https://git-scm.com/) - the version control system used by most open-source projects. 
    
    If you are not familiar with either, there are many resources available online to help you get started. Some nice ones are:

    - [Software carpentry's Version Control with Git](https://swcarpentry.github.io/git-novice/)
    - [GitHub skills courses](https://skills.github.com/) - especially the first day and first week series.
    - [git visualisation tool](https://cfinnberg.github.io/visualizing-git/)
    - [Oh my git!](https://ohmygit.org/) an open-source game about Git.
    - [Julia Evan's How Git Works! zine](https://jvns.ca/blog/2024/04/25/new-zine--how-git-works-/)
    - the [NIU's software skills courses](https://software-skills.neuroinformatics.dev/courses/index.html)

    We can help you with this if needed! Feel free to start a new topic in our [Zulip GSoc channel](https://neuroinformatics.zulipchat.com/#narrow/channel/487898-GSoC) if you have any questions, and someone from the community will be happy to help you.
   
4. **Get started with open-source development**

    Check the GitHub issues for the projects you are interested in. Sometimes issues are labeled as "good first issue" or "help wanted". These are usually easier to solve and are a good way to get started with the project. Otherwise, have a look and see if there are any issues you can help with!

    You will need to submit a pull request (ideally to one of the NIU projects) as part of your application. It does not have to be accepted - the goal is to show that you know how git, GitHub, pull requests and code reviews work. This also allows mentors to evaluate your application based on a real code contribution. If you have previously contributed to an NIU or other open source project, you can point to those pull requests in your application too.

    If you are new to open source software or would like a refresher, these are some nice resources to check:

    - the [First contributions project](https://github.com/firstcontributions/first-contributions)
    - the GitHub blog post: [New to open source? Here’s everything you need to get started](https://github.blog/open-source/new-to-open-source-heres-everything-you-need-to-get-started/)

    Before contributing to a project, make sure you read through their contributing guidelines. These will give you an idea of the required steps, and what is expected of you. An example is `movement`'s [How to Contribute guide](https://movement.neuroinformatics.dev/community/contributing.html#target-contributing). The NIU also publishes some general [development guidelines](https://neuroinformatics.dev/get-involved/languages_frameworks.html).

    You can check the issues from the tools involved in the GSoC projects in the links below:
    - [`movement` issues](https://github.com/neuroinformatics-unit/movement/issues)
    - [`ethology` issues](https://github.com/neuroinformatics-unit/ethology/issues)
    - [`BrainGlobe cellfinder` issues](https://github.com/brainglobe/cellfinder/issues)
    - [`BrainGlobe brainrender` issues](https://github.com/brainglobe/brainrender/issues)
    - [`BrainGlobe Atlas API` issues](https://github.com/brainglobe/brainglobe-atlasapi/issues)
    - [`BrainGlobe registration` issues](https://github.com/brainglobe/brainglobe-registration/issues)
    - [`datashuttle` issues](https://github.com/neuroinformatics-unit/datashuttle/issues)
    - [`spikewrap` issues](https://github.com/neuroinformatics-unit/spikewrap/issues)



5. **Prepare your application**

    Make sure you carefully read through the [GSoC guidelines](https://google.github.io/gsocguides//student/writing-a-proposal) (and these guidelines!) when preparing your application. 

    Select one of the projects from our [project list](projects_2025/index) and prepare a plan on how to tackle it, and the time you will need to complete it. Or if you have an idea that is not covered by the project list, feel free to pitch it to us. Use our [application template](#application-template) to structure your proposal and don't be shy to ask for feedback from the community. 
    
    To discuss your project proposal with the us, please create a new page in the [NIU GitHub wiki](https://github.com/neuroinformatics-unit/gsoc/wiki) with the project title prefixed with "GSoC 2025:" - we will discuss and polish your idea there. Please note that project proposals that are not previously discussed in the wiki will not be considered. 

    Include specific examples in your application to support your skills - these will help reviewers build a better picture of you. These could be things like "Qualified in final round of XXXX" or "Participated in XXXX hackathon".


6. **Submit your application**

    Remember to submit your application before [the deadline](https://developers.google.com/open-source/gsoc/timeline#april_8_-_1800_utc)! 
    
    Please do not send any applications directly to the NIU team, they won't be considered - all applications must go through [Google's application system](https://summerofcode.withgoogle.com/)
    

## Application template

Please use the following template to submit your application to the NIU GSoC 2025 program.

The more closely you follow this template, the easier it will be for us to review your application! Please include clear headings for all the different sections.

### Project title to use for the GSoC application
Please clearly include in the title the tool the project refers to, and the title of the project you are applying for. E.g. "movement: support for Kalman filters".

### Personal details
Please include the following information:
- **Full name** (include preferred name if desired)
- **Email**
- **GitHub username**
- **Zulip username**
- **Location & time-zone**
- **Personal website / project portfolio** (optional)
- **Code contribution**

    Please link a pull request, ideally submitted to your chosen project or one of the NIU tools. Applications without a code contribution won't be considered. It must be publicly visible and represent your own work, although you may have help from other developers in the community to further improve it. It must be meaningful code contribution (i.e. not just fixing a minor spelling mistake). While AI tools (such as Copilot etc) can be a very useful, contributions mostly created by AI are unlikely to be useful, and will not be accepted. You can link more than one pull request if desired.

### Project proposal 
Extension: <u> max 1 page </u> 
- **Title.**
    Please use the same title as in the GSoC application.

- **Synopsis.**
    Briefly explain: what is the project about? Why is it important? What are the goals? What are the deliverables? How would the open source community benefit from this project?

- **Implementation timeline.**
    Please include the following information:
    1. A bullet point list with **minimal set of deliverables**
    2. Additional **stretch goals** or "if time allows" deliverables (optional)
    3. A detailed **weekly timeline**: when do you plan to do what? 
        - Please use a week as a minimal unit of time, and include any planned vacations or other commitments. 
        - This timeline could be formatted as a table. 
        - Remember to also include the number of hours per week you plan to work on the GSoC project. 
        - When estimating the required time for a task, keep in mind deliverables should include investigation/research, coding and documentation. 
        - The default schedule for GSoC is 12 weeks - see the [GSoC timeline](https://developers.google.com/open-source/gsoc/timeline) for precise dates. 
        - Also please specify any prep work you plan to do during the "Community bonding period".
        - Usually week 1's deliverables already include some code. Week 6 marks the mid-term point, where usually more than half of the project should be completed. At the end of week 11 you may want to try to "freeze" the code and complete any remaining tests or documentation in weeks 11 and 12.

- **Communication plan.**
    Please explain: how do you plan to communicate with your mentor? How often? (e.g., daily or weekly stand-ups, longer meetings..?) What communication channels will you use? (e.g., video calls, Zulip chat...?)

### Personal statement

Extension: <u> max 3/4 page </u>

- **Past experience.** 
    Please describe your past experience with programming, open source, or any other experience you deem relevant for the project you are applying for. Any successful open source projects, published work or content of the like should definitely be highlighted.
- **Motivation: why this project?**
    Why are you interested in this specific project? What aspects of it motivate you to work on it? How does it link to your personal or professional interests? How do you envision its impact in the open source community?
- **Match: why you?**
    Why should we choose you for this project? What unique skills or experiences can you bring to the project and the community? Is there something you have worked on in the past that makes you particularly well-suited for this project?
- **Availability.**
    Please state if you have any other plans for the work period (school work, another job, planned vacation)? If so, how do you plan to combine them with your GSoC work?

### GSoC

Extension: <u> max 1/4 page </u> 

- **GSoC experience.**
    Have you participated in GSoC before? If so, when and with which project? What was your experience like? If you haven't, what do you expect from the program?
- **Are you also applying to projects with other organisations in GSoC 2025?**
    If so, which ones? What would be your preference in case of a tie?


## References
- [GSoC Contributor guide: writing a proposal](https://google.github.io/gsocguides/student/writing-a-proposal)
- [INCF Application template 2022](https://www.incf.org/sites/default/files/files/INCF_GSoC_2022_Application_template.pdf)
- [OpenAstronomy Application template](https://github.com/OpenAstronomy/openastronomy.github.io/wiki/Contributor-Application-template)
- [Python Software Foundation Application template](https://github.com/python-gsoc/python-gsoc.github.io/blob/main/ApplicationTemplate.md)