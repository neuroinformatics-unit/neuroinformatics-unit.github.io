---
blogpost: true
date: 22 September 2023
author: Laura Porta
location: London, UK
category: Blog
language: English
image: 1
---

# What is all the stuff the NIU keep going on about? CI? linting? What's a ruff, is it black?
*Author: Laura Porta*  
A cooking analogy to explain the importance of CI and linting.  

<img src="../_static/blog_images/intro_to_linting_and_ci/cookies.jpg" width="100%"/>

## Why should I care?
If you've ever followed a complex recipe, you'll understand the need for careful steps and checks. For developers, CI and linting are similar tools. They ensure our "recipes" (code) turn out just right.

## What is CI?
CI stands for Continuous Integration. Think of it as a kitchen assistant who keeps tasting the soup at every stage, ensuring it's always delicious.

### How does CI work?
CI is a process that **runs** automatically every time you make a change to your code. It checks that your code is working as expected, and alerts you if there are any problems. Every time you push a change to your codebase on GitHub, CI (your cooking assistant) can install your package, run your tests, and check your code for errors as if it were a user interacting with your software.

### If I don't use CI, what could go wrong?
Imagine baking a cake. If you don't taste-test as you go, you might end up with a salty dessert. Without CI, small errors in code can create big problems later. 

## What about linting?
Linting is like having a baking mentor who guides you on techniques, ensuring your cake rises perfectly every time. It points out potential issues in your recipe (code) so you can fix them before baking.

### How does linting work?
Linting is a process that checks your code for errors, bugs, and stylistic issues. It's like a **spell-checker** for code. Usually, you run it before committing your changes. It helps you maintain a consistent style and avoid errors, but differently from CI, it doesn't run your code.

### What if I don't use linting?
Without linting, you might not notice that your cake recipe (code) is missing a key ingredient. Linting helps you spot errors before they cause problems.

### How can I automate linting? Use pre-commit hooks
Pre-commit hooks are scripts that run before you commit your changes. They can be used to run linting automatically, so you don't have to remember to do it yourself. Tools like `black`, `mypy`, `ruff` can be called. They respectively check your code for style, type errors, and security issues.
You can install the NIU pre-commit tools by using our cookiecutter template.

### What is the difference between `ruff` and `black`?
`black` is a tool that checks your code for style issues. It's like a baking mentor who ensures your cake is always perfectly risen. 
`ruff` is an extremely fast Python linter that like a Swiss army knife, can be used to check for style and type errors. It's like a 5-star Michelin chef who ensures your cake is perfectly risen, and that you didn't accidentally add salt instead of sugar.

## What's a cookiecutter template?
A cookiecutter template is a tool that helps you create a new project. It's like having a kitchen with all the tools you need to bake a cake. You can use it to create a new project with all the NIU tools already set up. You can find it [here](https://github.com/neuroinformatics-unit/python-cookiecutter).

