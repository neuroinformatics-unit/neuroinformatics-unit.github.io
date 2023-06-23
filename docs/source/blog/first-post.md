---
blogpost: true
date: Jan 01, 2023
author: Neuroinformatics Unit
location: World
category: Manual
language: English
---

# Why and How to Translate Scientific Script from MATLAB to Python: A Comprehensive Guide

## Rationale
In the realm of scientific project development, scientists often find themselves drafting quick, succinct scripts to navigate a myriad of computational challenges. From orchestrating experimental setups to analyzing complex data, these tasks necessitate a programming language that's both versatile and accessible. Historically, MATLAB has been the go-to choice for many such endeavours due to its capacity to facilitate script creation and craft user-friendly interfaces.

According to the 2022 StackOverflow survey, MATLAB is still used by approximately 4.5% of professionals in academia. However, the landscape is experiencing a steady shift towards other languages, with Python taking a lion's share of 41.6% in the same survey.

Although MATLAB has served scientists faithfully for years, its execution is tied down by its proprietary nature, creating significant limitations. Firstly, the software license can be costly, especially for small institutions or individual researchers. Moreover, the closed-source nature of MATLAB can hamper flexibility and customization.

On the other hand, Python, an open-source alternative, is increasingly gaining popularity in the academic world. The reasons behind this trend are multifold. Python's open-source nature implies it's freely available to everyone, which democratizes access. It also provides a robust platform for integrating unit tests into the codebase, promoting a healthier and more reliable code ecosystem. Python's object-oriented programming (OOP) support allows for code reusability and modularity, making code maintenance easier and more efficient.

Given these advantages, there's a rising demand for transitioning from MATLAB to Python, and we're here to guide you through the process of porting your code efficiently.
## Getting started
When attempting such a translation, you may encounter two main types of MATLAB code: 1. "Dirty" scripts, and 2. Well-structured pieces of software.

Regardless of the code type, it's crucial first to understand the objectives of the original MATLAB script. Sketch out how Python tools might achieve the same results given identical inputs and goals. Drafting a schema or flowchart can prove incredibly helpful in visualizing this translation process.

## Navigating the original codebase

### Using the debugger
Next, delve into the original MATLAB codebase to grasp its real implementation. A debugger can assist in this exploration, helping you follow the sequence of method calls, inspect parameter inputs, and evaluate their outputs. 

### Static analysis
You may encounter scenarios where the code you aim to rewrite relies heavily on custom scripts or specific combinations of outdated packages. These dependencies might restrict the execution of the code to the original developer's machine. In such cases, static code analysis becomes an invaluable tool, coupled with a thorough exploration of method documentation and dialogue with the original code's developers and users when possible.

### Dependency analyser
For sprawling codebases, a dependency analyzer can elucidate the connections between different files and functions, helping you chart a course through the complexity.


## Plan and write your code
As you undertake the translation from MATLAB to Python, your initial focus should be on designing the overall architecture, identifying key input-output relationships, and planning how to develop these in Python. This process is less about replicating individual methods and more about maintaining functionality at a higher level. Therefore, although it will be useful to use AI assistants such as GitHub Copilot to understand individual lines of code, it won't be sufficient to structure the architecture of your Python codebase.

Python's extensive ecosystem offers ample opportunities for performance optimization and code efficiency. For instance, libraries such as NumPy and Cython can considerably speed up your code, while Python's approach to vectorization can help reduce the need for lengthy loops commonly seen in MATLAB. 

Remember, translating MATLAB scripts verbatim might be tempting, but Python's strength lies in its flexibility and its extensive library ecosystem. Embrace Python’s strengths by looking for opportunities to optimize and streamline your code. 

Finally, ensure the validity and efficiency of your Python script by performing comparative testing with the MATLAB version. Libraries like MATLAB Engine API for Python can facilitate this by calling MATLAB functions directly from Python, providing a valuable benchmark for your Python code.


## Conclusion

In conclusion, translating MATLAB scripts to Python is more than a simple conversion process. It presents an opportunity to optimize, streamline, and refine the codebase. While Python may require more verbose code for some operations, the advantages of open-source access, testing frameworks, object-oriented programming, and a powerful suite of libraries more than compensate.

The task may appear daunting, especially for large or complex codebases, but a thoughtful approach—understanding the original script's objectives, planning the Python equivalent, leveraging Python's strengths, and verifying through comparative testing—can ensure a successful translation.

Remember, the goal is not just to replicate functionality, but to create a Python codebase that is robust, efficient, and poised for future development. With careful planning and strategic execution, you can unlock Python's full potential and advance your scientific projects to new heights.



