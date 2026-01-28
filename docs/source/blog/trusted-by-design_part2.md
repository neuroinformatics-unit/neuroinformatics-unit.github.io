:blogpost: true
:date: Feb 4, 2026
:author: Niko Sirmpilatze
:location: London, UK
:category: Blog
:language: English

(target-trusted-by-design-part2)=
# Trusted by design (part 2): release early, release often

_'Release early, release often' is an often-repeated mantra, popularised by Eric S. Raymond in his 1997 essay ["The Cathedral and the Bazaar"](https://en.wikipedia.org/wiki/The_Cathedral_and_the_Bazaar). I hadn't fully grasped its significance until I switched from academic research to full-time software development. How early? How often? And why is this so critical to establishing and maintaining trust?_

::: {note}
This is the second of three blogposts on the theme of _Trusted by design: set up your research software for community adoption_. See the [introductory blogpost](target-trusted-by-design-intro) for context.
:::

## The *Cathedral* and the *Bazaar*
The lifecycle of open-source software development differs radically from that of scientific research. As a result, researchers who write software may inherit habits that don't serve them well. In scientific projects, we tend to release our work when it's finished: our manuscript written, our data tidy, our code polished. Anticipating close scrutiny from our peers, we aim for the work to be 'camera-ready' and 'publication-quality'. We take pride in our ability to magically unveil unblemished gems. 

Some software also follows the same cadence, with releases being the equivalents of manuscripts: they arrive rarely, in big increments, and with a lot of pomp. Raymond called this the *Cathedral* model of software development. We imagine the builders of cathedrals as select craftsmen, taking pride in their ability to identify and correct every imperfection, regardless of how long it takes.

However, as the title of that essay implies, there is another way—embracing the messiness, diversity and noise of a *Bazaar*. The *Bazaar* means you are open to contributions from anyone, accept mistakes as unavoidable, but trust that ["given enough eyeballs, all bugs are shallow"](https://en.wikipedia.org/wiki/Linus%27s_law). You move in small increments and release as often as you can, being transparent at every step. Since the 90s, the *Bazaar* has gradually won over the open-source software world, following the example—and remarkable success—of [Linux](https://en.wikipedia.org/wiki/Linux). 

Raymond argues that in open-source settings the *Bazaar* leads to more trust and community adoption long-term. How can releasing small, incomplete pieces of work make you more trustworthy than building immaculate cathedrals? Let's look at what *early* and *often* mean in concrete terms, in the context of research software. Perhaps we'll start seeing why.

## Your first release
**You never get a second chance at making a first impression**, so your first release is a defining moment for establishing trust. By first, I don't mean version 1.0, but the first one you advertise and promote outside your group. What should that look like for research software?

In our [team](target-home), we've arrived at a particular 3-point check-list for what constitutes a [Minimum Viable Product (MVP)](https://en.wikipedia.org/wiki/Minimum_viable_product).

::: {admonition} Minimum Viable Product (MVP) checklist
:class: tip

1. The software contains at least one useful feature, i.e. it enables or streamlines one key task.
2. That feature is well documented, including usage examples.
3. The software installs and launches seamlessly on target platform(s).
:::

Releasing just a single useful feature may feel insufficient, but focusing on a concrete milestone keeps you from being distracted by lofty visions. You may worry that people will find your MVP too trivial. Fear not. Assuming you've clearly and publicly [articulated your mission and scope](target-trusted-by-design-part1), potential users already know what to expect next and how to interpret your MVP in light of your vision. Your communications around the first release should help them put things in context.

Not everyone in your target audience will use the MVP, and that's fine. **Your goal here is to gain a few early adopters**. These are your biggest asset: they can provide valuable feedback while the project is still small and easy to steer. If they like it, they will become ambassadors and endorse it through word of mouth. They are also your insurance. The last thing you want is to spend years building software that nobody needs. If you've set off in the wrong direction, you want people to tell you, and the earlier the better.

Seamless installation is crucial for finding and retaining those early adopters. How many times have you come across a new exciting software, decided to give it a go, and failed to install it? How often did you come back to it? If you lose people at the outset, it's hard to repair that trust. **None of your exciting features matter if people can't get them up and running.** I've seen many research software packages fumble this step, and to be fair, it's not an easy one. Hardware and operating systems are complicated; "dependency hell" is called that for a reason. But you should not give up; rather, you should devote extra time and attention to the task. 

**Don't underestimate the amount of work between 'works on my machine' and 'works on every machine my target audience may use'**. No need to support every computing device out there. In research settings, most users are our peers, and we should have a fair idea about where and how they tend to install software. For example, both [movement](https://movement.neuroinformatics.dev) and [BrainGlobe](https://brainglobe.info) are squarely part of the scientific Python ecosystem, and their installation process reflects that. We distribute packages via PyPI and conda-forge, and make sure they can be installed in 1-2 lines of code on the terminal or via a graphical user interface. If we were developing R packages, we'd try to get them on [CRAN](https://cran.r-project.org). When in doubt, look at the best known packages within your ecosystem and copy what they are doing. Testing and [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration) are your friends here: try to automatically and regularly check whether your software installs and launches as expected on your target platforms. Get your MVP in the hands of colleagues and friends and see if they can break it. You won't always succeed at ironing out all the kinks; there may be some operating system that eludes your efforts. That's okay for now. Just remember to manage expectations and state supported systems up-front.

In short, don't lose sight of the goal here: getting your MVP in the hands of as many early adopters as possible. You can't have all three: built fast, easy to install, and feature-complete. Our approach for first releases is to let go of that last one.

## Subsequent releases

You've made your first release and got some uptake and useful feedback. What now? You rinse and repeat. Subsequent releases follow the same logic as the first one.

::: {admonition} Release checklist
:class: tip

1. Release a few new features at a time.
2. Avoid releasing undocumented features.
3. Make sure you don't unknowingly break existing functionality.
:::

The key is moving in small, incremental steps and minimising surprises. This benefits everyone: your **team**, your **users**, and the open-source **ecosystem** as a whole.

**For your team**, small steps make course correction easier—you can fix missteps as they occur. A series of small wins keeps morale high and momentum going.

**For your users**, releasing documented features a few at a time lets them adapt their workflows gradually. Clear release notes are essential: state what's new, highlight breaking changes, and explain how to migrate. Nothing breaks trust like being left high and dry when the maintainers decide to rewrite everything from scratch. Researchers whose workflows you've disrupted won't recommend you to colleagues.

**For the ecosystem**, predictability is currency. Open-source software forms an interconnected, interdependent web. Your package has neighbours—software you depend on, and software that depends on you. Every time you move a node, the whole neighbourhood jostles until it settles in a new equilibrium. Move too abruptly and the local fabric tears. Repairing ruptures takes effort from you and your neighbours. Do it often and the ecosystem will quietly cut you off—not through a formal decision, but through countless small choices. Developers may rewrite your functionality from scratch rather than depend on you. Predictability earns you a place in the web; unpredictability isolates you.

**A last tip: frequent releases are greatly helped by automation.** You want doing the right thing to also be the easy thing. [Linters](https://en.wikipedia.org/wiki/Lint_(software)), [tests](https://en.wikipedia.org/wiki/Software_testing), and [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration) should make releasing as simple as pressing a button. These topics are out of scope for this blogpost, but—as always—when in doubt, copy what your favourite projects do.

## The takeaway
Every release is a conversation with your community. Release early to start that conversation sooner. Release often to keep it going. The trust you build through consistent, predictable releases compounds over time—worth far more than the polish you sacrifice by not waiting for perfection. In the *Bazaar*, reliability beats brilliance.

_In the next and final post of the series, we'll look at where those conversations happen and how to conduct them with radical openness._