(licensing-target)=
# Software licensing

## Disclaimer
**This document was not written by lawyers, and does not represent legal advice.**

This guide was written by the [Neuroinformatics Unit](https://neuroinformatics.dev/) to help researchers at the [Sainsbury Wellcome Centre (SWC)](https://www.sainsburywellcome.org/web/) and [Gatsby Computational Neuroscience Unit (GCNU)](https://www.ucl.ac.uk/gatsby/gatsby-computational-neuroscience-unit) at [University College London (UCL)](https://www.ucl.ac.uk/) choose a license for their software.
It does not represent official guidance by SWC, GCNU or UCL.
In particular this is not advice about intellectual property, but rather the practicalities of adding a license to your software.
For more information, SWC/GCNU researchers should consult the SWC/GCNU and UCL documentation about intellectual property or contact [UCL Business](https://www.uclb.com/) if you think your software may have commercial potential (before release).

## Summary
**Unless your software has commercial potential or depends upon other software with a restrictive license, we recommend you use [The 3-Clause BSD License (BSD-3-Clause)](https://opensource.org/licenses/BSD-3-Clause).**

## Why license your software?
There are many reasons to release your software openly such as a funder/publisher requirement, to collaborate with others or simply in the spirit of open science. However, if your software is not licensed then nobody outside your employer’s organisation can (legally) use it.

To allow others to use your software, you must explicitly choose a license to detail what they can, and cannot do with your software. Typically, this license is included with your software in a file, such as `LICENSE.txt`.

## Choosing a license
Intellectual property (IP) law is complex, and the open source software (OSS) license selection reflects this. However, there are many useful resources to help you pick a license such as [choosealicense.com](https://choosealicense.com/) and [tldrlegal.com](https://tldrlegal.com/).

It is often tempting to write your own license, perhaps only allowing academic use. Unless you are an IP lawyer, please use one of the existing, well-established licenses. This way others can understand what they can use your software for, without seeking their own legal advice.

## To choose a license:
1. Ensure you have permission to license the software yourself. In most cases this decision will be up to your research group leader or department head.
2. Obtain permission from any other contributors. If any part of the software was developed at a different institute (either by yourself, or a collaborator) ensure you have written permission. Ensure you choose a license in accordance with the requirements of any other institution and their funders. Adding or changing a license when external collaborators are involved is tricky. This can be avoided by choosing a license before commencing work.
3. If you think your software has commercial potential contact your institutional IP or tech transfer team (e.g. [UCL Business](https://www.uclb.com/)) before releasing your code.
4. Ensure you follow the requirements of the funders and the institutes in which you work. For SWC/GCNU researchers, at the time of writing, UCL, Gatsby and Wellcome do not have a formal OSS licensing policy.
5. Check the licenses of any other software on which yours depends and ensure you release your software in accordance with these.
6. Consider the licenses used by other software in the field. It may be easier to contribute to a larger ecosystem of tools if the licenses are compatible.
7. If you have specific license requirements, consult a guide such as [choosealicense.com](https://choosealicense.com/). **Otherwise …**
8. **If you want a simple license that allows for virtually unrestricted use of your software, but with a liability disclaimer, use [The 3-Clause BSD License (BSD-3-Clause)](https://opensource.org/licenses/BSD-3-Clause).**

## Adding a license
In most cases, adding a license is as simple as copying the license text into a file named `LICENSE.txt` or similar and including this with your software. If you have a GitHub repository, adding a new file named `LICENSE.txt` from the web interface will produce a button “Choose a license template” which will allow you to choose from a list.

## Frequently asked questions

### Can I change the license later?
You can, but the earlier versions will still be licensed under the original terms. This is why it’s important to carefully consider the license from the outset.

### How do I know when my code is ready to release?
If you’ve followed the above steps, then it’s ready to release. There will always be bugs, and the best way to find these are to allow others to read your code and use your software.

### If my code depends on another library with a more restrictive license (e.g. GPL), does this affect how I license my software?

If it is installed separately, and you simply call the library (e.g. using a Python package) then you can choose a license for your software as normal. If you bundle the third party code with your library or link against it, this may affect the license you can use. In these cases, check the terms of the specific license as the GPL family (e.g. GPL, LGPL, AGPL) may vary.

### I have included code from others within my repository (e.g. a DL model), how does this affect licensing?
Firstly, you should ensure that the license for your code is compatible with the included code (e.g. by using a [license compatibility checking tool](https://joinup.ec.europa.eu/collection/eupl/solution/joinup-licensing-assistant/jla-compatibility-checker)). You should also adhere to any terms of the third party license and it is good practice to always include a copy of this license with the third party code.

## Acknowledgements
This document was adapted from the excellent [Imperial OSS license document](https://www.imperial.ac.uk/research-and-innovation/support-for-staff/scholarly-communication/research-data-management/sharing-data/research-software/).
