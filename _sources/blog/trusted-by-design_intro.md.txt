:blogpost: true
:date: Jan 28, 2026
:author: Niko Sirmpilatze
:location: London, UK
:category: Blog
:language: English

(target-trusted-by-design-intro)=
# Trusted by design (intro): set up your research software for community adoption

_So, you want to create an open-source research software package—and not just for yourself or your group. You'd like people around the world to use it, and even contribute to it. How do you persuade them it's worth their time?_

::: {admonition} Who is this for?
:class: note

Read on if you've written code that solves a problem—maybe for your own analysis, maybe for your lab—and hope it can be of use to others. You don't need to think of yourself as a "software developer".

By *research software package*, I mean a reusable library or toolbox that others can install and apply to their own data. I'm not talking about one-off analysis scripts, or web apps deployed as a service.
:::

**Open-source projects rise and fall on trust.** You may hope to build trust on technical merits: your algorithm is novel; your implementation fast; your tests thorough. All great, but not enough. Many technically excellent projects never break through because they neglect the social foundations of trust, which are laid long before a project matures.

**And that's good news:** you don't need to be a top-tier programmer to build a successful open-source tool. Researchers do this all the time. What matters most is how you run the project, not how fancy the code is.

In a series of three blogposts, I'll distil lessons from years of building and maintaining scientific Python tools used by researchers worldwide. I'll outline the practices that signal reliability and sustainability across a project's lifecycle: 

1. Defining and communicating your mission from the start.
2. Making a reasonable first release and following it up with consistency.
3. Using open communication to embody your values and model healthy norms.

I'll draw on examples from [BrainGlobe](https://brainglobe.info/), [movement](https://movement.neuroinformatics.dev/) and other tools built and maintained by the [Neuroinformatics Unit](target-home). That said, the lessons should be applicable to any free open-source project that aspires to attract and sustain a healthy community.

The blogpost series is meant as a long-form companion to my [talk](https://fosdem.org/2026/schedule/event/VPJH8F-trusted-by-design/) at the [Open Research devroom of FOSDEM 2026](https://fosdem.org/2026/schedule/track/open-research/). The content is inspired by thoughts long simmering below the surface, and brought about through conversations with my colleague [Laura Porta](https://github.com/lauraporta) and my recent participation in the [Birdaro Training Program](https://www.birdaro.org/birdaro-training-program-pilot-cohort/) for open-source leaders.

**The key takeaway:** If you behave like a trustworthy project from the beginning, people will treat you like one, and help the project grow into what it promises to be.
