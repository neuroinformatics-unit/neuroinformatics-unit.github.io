:blogpost: true
:date: Feb 5, 2026
:author: Niko Sirmpilatze
:location: London, UK
:category: Blog
:language: English

(target-trusted-by-design-part3)=
# Trusted by design (part 3): embrace radically open communication

_Open-source software is public, yet much of the communication around it may happen in private emails, internal Slack channels and meetings with no minutes. This disconnect can erode the very trust that openness is meant to build. What if communication were radically open—a habit of constant, multi-way interactions visible to anyone who cares to look?_

::: {note}
This is the last of three blogposts on the theme of _Trusted by design: set up your research software for community adoption_. See the [introductory blogpost](target-trusted-by-design-intro) for context.
:::

The trust-building practices we covered in the two previous blogposts—articulating your project's mission and making incremental releases—can be thought of as announcing your project to the world. But communication can be—and should be—more than occasional announcements. Here we'll look at communication at its most granular: the day-to-day conversations that take place in issues, pull requests and discussion forums.

Our team's approach to communication could be summarised as:
**write everything down, make it public by default, and let the magic happen.**

## Issues as a public scratchpad

We use GitHub issues[^issue-trackers] as a scratchpad. Our recipe is simple:

::: {admonition} How to use issues
:class: tip

- If you get a new idea, write it down as an issue.
- If you obtain new information about an existing idea, comment under the issue.
- If an idea grows to burst its banks, break it down into smaller, more manageable issues.
- If two ideas are related, cross-link the issues.
- If an idea is no longer relevant, close the issue.
:::

Ideas don't have to be fully-fleshed to end up in issues. **If you can formulate it as a sentence, it's ready to be written down.**

Minimise the time between forming a thought and writing it down. Do it, even if it feels like talking to yourself. **I forget, you forget, everyone forgets.** At least once a week I thank my past self for having written something down. A long list of issues also guarantees you'll never run out of things to do. And writing clarifies your thinking—don't think of it as keeping records, but as prying order out of your disordered thoughts. You will often realise that something makes no sense while writing it down.

Wait, you'll say, I can achieve the same with a private notebook. Why write publicly, risking looking ignorant or incoherent? It goes against our urge to cultivate an image of expertise and authority. But the open-source ethos not only acknowledges that everyone is fallible, it takes it for granted. **Good software emerges from the interactions of many fallible agents, not from the works of a lone genius.** A public, lively issue tracker is one of the most effective ways to enable those interactions.

Let's drive this point home with a thought experiment. You are using software made by someone else and stumble on a bug. You go to the project's GitHub page, hoping to find an existing report. Instead you find only a handful of issues, all by the main developer, the last one from a year ago. Will you open an issue to report the bug? Probably not. You lack social context and don't know what to expect. Will the maintainers respond to a stranger? Will they be nice about it? If only there was a track record of interactions between the developers and the community!

**Every unreported bug and unrequested feature is a missed opportunity**—not only for the developers but for everyone seeking answers in that repository. That loss is largely invisible. But you're also missing out on the greatest joy of open-source development: like-minded strangers who volunteer to solve your problems. Strangers will pick up issues more often than you think. Some will turn into regular contributors, long-term collaborators, or even friends. People are the engine of open-source, and they are attracted by interesting problems. Give them—and your project—a chance by writing things down.

## Pull requests as an open workshop

If issues are a collaborative public scratchpad, pull requests are the workshop where ideas become code. You may feel the urge to work behind closed doors and only emerge when the pie is baked. But just like with issues, every private process is a missed opportunity for learning, collaboration, and trust-building. Open the doors and let anyone peek in, ask questions, and suggest improvements throughout.

Pull requests are a workflow for contributing to a software project. They allow anyone to create a copy of the codebase, make changes, and propose those changes to be merged back into the original. That proposal is the [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/).[^merge-request]

Typically, pull requests are accompanied by a description documenting why the changes were made and what they accomplish. Maintainers review them and can approve outright, reject, or ask for changes before merging. **It's like scientific peer review, but for code and at a much faster pace**. Imagine writing your manuscript in a public Google doc, with reviewers suggesting changes line-by-line and anyone in the world being able to chime in with a comment. It sounds chaotic, but it's probably the most effective collaboration workflow ever invented.

::: {tip}
If you want to see an example, check out the [pull request proposing this very blogpost](https://github.com/neuroinformatics-unit/neuroinformatics-unit.github.io/pull/240).
:::

My first advice about **pull requests: just use them, without exception**. Don't succumb to the urge of pushing changes directly to 'main' (the conventional name for the canonical copy of the codebase). Get into the habit of always going through a pull request, even if you are the only developer. It may feel strange to propose changes to yourself and then review them. But self-review is a great way to improve: it disciplines you in writing informative descriptions and checking your own work with a critical eye before rushing ahead.

If you are blessed to have at least one collaborator, the benefits multiply. You can review each other's work, ask questions, suggest improvements, and hold each other accountable. Pull requests provide a fantastic interface for code review—use it. You will feel slowed down at first, perhaps even annoyed that you have to justify your every choice to someone else. But that's the point. You are not just writing code; you are communicating your thinking to others. **Over time, everyone involved will build a shared understanding of the codebase**. The project will stop being the property of your mind and continue life in shared mental models. That step is crucial on the path to community adoption.

Pull requests also create a lasting record. If you invite contributions from the community, it helps to have an established track record of your own publicly visible work. Others will see how you write pull requests, review them, and respond to feedback. This sets expectations and implicitly establishes norms. It's not enough to trumpet your 'design principles' and 'community guidelines'—**pull requests are where you walk the talk**. Hold yourself to your stated standards in every comment you leave, and others will follow suit. Future maintainers will be grateful too: they can look back at the history, understand how the project evolved, and trace why decisions were made. You are leaving breadcrumbs for your future self and fellow travellers.

## Scale your communications alongside your community

As your project matures and your community grows, issues and pull requests will no longer be enough. You will probably have gained users and collaborators who don't feel at home on GitHub. And not all conversations will be about code and technical matters—community members will want to seek support, exchange tips, get to know each other, or just hang out.

Provide them with alternative venues and designate specific roles for each. For example, here are the communication channels we use for [movement](https://movement.neuroinformatics.dev):

|  | Platform | Come here to |
|---|----------|---------------|
| {fas}`comments` | [Zulip](https://neuroinformatics.zulipchat.com/#narrow/stream/406001-Movement) | Ask general questions, seek user support, chat with `movement` users and developers. |
| {fab}`github` | [GitHub](https://github.com/neuroinformatics-unit/movement) | [Open an issue](https://github.com/neuroinformatics-unit/movement/issues) to report a bug or request a new feature. Open a pull request to contribute code or documentation (see [contributing guide](https://movement.neuroinformatics.dev/dev/community/contributing.html)). Star the [repository](https://github.com/neuroinformatics-unit/movement) if you like `movement`. |
| {fas}`video` | Community Calls | Meet the team and chat about any aspect of `movement` development. [Follow this Zulip topic](https://neuroinformatics.zulipchat.com/#narrow/channel/406001-Movement/topic/Community.20Calls) to receive updates about upcoming calls. These typically run every other Friday from 11:00 to 11:45 (London, U.K. time). |
| {fab}`bluesky` {fab}`mastodon` | Social Media | Follow us on [Bluesky](https://bsky.app/profile/neuroinformatics.dev) and [Mastodon](https://mastodon.online/@neuroinformatics) for project announcements, opportunities and upcoming events. |

_Table copied from [movement's community page](https://movement.neuroinformatics.dev/latest/community/index.html)._

Apart from GitHub and social media, we provide two additional spaces: Zulip and Community Calls.

[Zulip](https://zulip.com) is a chat platform with threaded conversations, similar to [Slack](https://slack.com) or [Discord](https://discord.com). We like it because it offers a generous free tier for open-source projects and keeps conversations organised by topic. Most importantly, it supports 'web-public' channels—anyone can read the conversations without creating an account. If they want to participate, they can log in with an existing account (GitHub, Google, etc.) and start chatting. **No matter which platform you choose, eliminate barriers to entry.** Don't make people create an account—or worse, request permission—just to read conversations. Let them come to you and give them agency.

Community Calls are regular video meetings open to everyone. They are great for putting faces to GitHub handles, building rapport, and having free-form conversations. They are also opportunities to share updates, gather feedback, and brainstorm together. We advertise them ahead of time (with an agenda) and share meeting notes publicly afterwards. It can be hard to know when your project is ready for Community Calls. If unsure, err on the earlier side. When we rolled them out for *movement*, we thought no one would show up—we were pleasantly surprised. **"Nobody cares about my project" is a self-fulfilling prophecy.** Give people a chance to prove you wrong.

As your community grows, managing all these communication channels can become a burden. There are bad actors out there, and you will have to work to keep a high signal-to-noise ratio. **This means moderation**. You need a clear code of conduct—ideally from the very start—and you must enforce it consistently. You may also need governance structures and perhaps a dedicated community manager.

**But if you've reached this point, congratulations: you have a community.** You have succeeded at making people trust your project. You no longer need my advice—the best of luck to you on your open-source journey!

## Takeaway

Write everything down. Make it public by default. Let the magic happen. The magic is people—strangers who become collaborators, collaborators who become friends. Radical openness is not a risk—it's how you find your people.

_This concludes the "Trusted by design" series. See the [introductory blogpost](target-trusted-by-design-intro) for an overview and links to parts 1 and 2._

[^issue-trackers]: There is nothing special about [GitHub issues](https://docs.github.com/en/issues)—[GitLab](https://gitlab.com), [Codeberg](https://codeberg.org), or various project management systems work just as well.

[^merge-request]: [GitLab](https://docs.gitlab.com/user/project/merge_requests/) calls them "merge requests"—a more descriptive term.
