---
title: In conversation with Gregory Becker
date: '2025-11-25'
description: 'In this conversation we speak with Gregory Becker, a core developer of Spack: a build from source package manager.'
categories:
- In conversation with
tags:
- Spack
banner: wp-content/uploads/2025/02/P_20250107_145539-1440x500.jpg
---

# In conversation with Gregory Becker

*November 25, 2025*

![Profile picture of Gregory Becker](wp-content/uploads/2025/11/Gregory-Becker-Profile-Photo-Square.png){ .align-right }

*In this conversation we speak with [Gregory Becker](https://spack.io/greg-becker-profile/) from Lawrence Livermore National Laboratory in the US, a core developer of [Spack](https://spack.io): a build from source package manager. Spack is used extensively by ACCESS-NRI and is essential for building and deploying ACCESS models on systems such as NCI’s Gadi supercomputer.*

#### Where did you grow up, and how did you come to be a Spack developer?

I grew up in Austin, Texas, and went to college at Williams College in Massachusetts. I started my degree thinking I would study maths and philosophy. But I ended up studying maths and computer science.

During my junior year of college, I asked one of my college professors which alumni I should contact that do the kind of computer science I was interested in. He gave me about ten names and email addresses, and I called and emailed all of them. One of them was [Todd Gamblin](https://people.llnl.gov/gamblin2) (creator of Spack), who gave me an internship.

After the internship I started a job at [Lawrence Livermore National Laboratory](https://www.llnl.gov), where I had been interning. I began working on Spack in August of 2015. That November, the [initial Spack paper](https://doi.org/10.1145/2807591.2807623) was released, and the usership exploded. I’ve been working on Spack ever since.

#### What is Spack, and why is it important?

For people that work with scientific software, everyone has had the experience of trying to get the software to build on their system, or to build with their tool that they need to integrate with it. This can turn into a nightmare, involving weeks of fighting obscure compiler errors, missing symbols, or all sorts of other problems.

Having something that can do a lot of that for you is a game changer. As an end user it’s great: you can push a button and get it working. But it’s not just about having a push button for installing the software that you need.

The package recipes in Spack also serve a dual purpose as a repository of knowledge for all the weird tips and tricks that people have come up with to make the package build in all sorts of contexts.

#### What excites you about Spack?

From a technical standpoint, the thing I am most excited about is work on the concretizer. This is the internal algorithm that takes a user’s specification of what they want to install and turns it into a concrete build plan.

The concretizer algorithm is written in [Answer Set Programming](https://en.wikipedia.org/wiki/Answer_set_programming), which is an interesting sort of logical programming language. It turns your brain inside out a little bit working with it. I am really enjoying the process of replacing the previous concretization solver that was written in Python and wasn’t up to the task. For the past six years we’ve been using and improving this new solver to make it as performant as possible.

#### What do you like to do outside of work?

My main hobby is rock climbing. I mostly do it in the gym just due to the constraints of time. But I live in northern California now, which is a great place to climb outdoors as well.

#### Do you have a fun fact about yourself?

I’ve never drank a full cup of coffee in my life. I don’t have anything against coffee (besides the flavour), it’s just never been part of my life to caffeinate in that way.

**Categories:** [In conversation with](https://www.access-nri.org.au/category/in-conversation-with/)

**Tags:** [Spack](tag/spack.md)
