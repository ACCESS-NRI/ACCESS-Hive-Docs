---
title: Jemma Jeffree’s Internship Experience
date: '2025-10-03'
description: We speak with Jemma Jeffree about her experience doing a PhD internship at ACCESS-NRI, which focused on improving ACCESS-CM3.
categories:
- In conversation with
tags:
- ACCESS-CM3
- Internship
banner: wp-content/uploads/2022/03/Unsplash-Raychel-Sanner-Storm-1440x500.jpg
---

# Jemma Jeffree’s Internship Experience

*October 3, 2025*

![](wp-content/uploads/2025/10/Jemma_Jeffree-264x300.png)

Recent ACCESS-NRI PhD intern, Jemma Jeffree

In this conversation we speak with [Jemma Jeffree](https://earthsciences.anu.edu.au/people/jemma-jeffree) about her experience doing a PhD internship at ACCESS-NRI, which focused on improving ACCESS-CM3.

#### Tell me a bit about yourself, your career so far, and why you decided to do a PhD.

I’ve wanted to do science for as long as I can remember. My interests changed between different STEM areas throughout high school, until at some point I met ENSO (El Niño Southern Oscillation). It didn’t click the first time I was taught this topic, but once I actually understood the concept it captured me in a way that nothing else had previously.

When I started my Honours year, nobody at the Australian National University (ANU) was working with ENSO in the way I wanted to. My Honours project measured deep ocean currents using satellite data – so still climate science, but taking a year away from ENSO. Then, at the start of my PhD, my current supervisor (with a background aligned with my research interest in ENSO) moved to ANU, so I stayed here to work with her.

#### What was it about ENSO that drew you in?

It keeps moving.

I like working with lots of data, particularly spatial data. Climate science is inherently 4-dimensional (3 spatial dimensions + time), and allows you to work with huge datasets that are continually being updated. You can make theories, and then test them as more observations come to light. It’s also interesting because the findings and impacts are directly relevant to people.

ENSO is always bouncing backwards and forwards between an El Niño and a La Niña state, so you can’t study it as a static system. You have to understand it as that oscillating system, and explore how the backwards and forwards might change so you can predict it. That complexity called to me.

#### Why did you decide to do an internship at ACCESS-NRI?

I needed a break from my PhD. The paper that I was working on, which will form the first chapter of my PhD, was stressing me out. It felt like a lot of pressure from other people’s expectations to write, coupled with feeling like I didn’t know what I was doing or how to finish the paper. The internship at ACEESS-NRI was a circuit-breaker, giving me a chance to step away from that paper that was occupying all my time and gain some perspective.

The internship also gave me an opportunity to work on the technical skills that I had abandoned for the previous year when I had been focused on writing. Programming has been an important part of my life since early high-school. My dad has a computer science degree, which invariably impacted the conversations we had, and I did a two-week summer school on informatics and algorithms at the end of high school. So, one of the reasons that climate science called to me was the hands-on code writing.

Coding is fun because you need to understand what you want to do well enough to break it down into the smallest possible constituent tasks. Computers are spectacularly stupid; they can’t interpolate between your instructions if you miss something. I love writing code and working with computers, and that wasn’t as big of a part of my PhD as I would have liked it to be. ACCESS-NRI gave me a chance to focus on model development and the more technical side of climate science.

#### What did you do during your internship at ACCESS-NRI?

I did a lot of small things, but there were two major projects that I worked on.

The main one was looking at ACCESS-CM3, which is of the models we’re building for CMIP7, and trying to fix the radiation balance. I had hoped we could improve the ENSO in ACCESS-CM3, but the model was not yet at a point where the background climate state was valid. The net radiation balance was too high, so the model absorbed too much solar radiation and warmed way too fast. My job was to work out why the model was wrong. (In the end, the solution involved reading some documentation from the UK Met Office’s web page and copying a few minor parameter changes.)

The other project I worked on involved improving the python tools for analysing large data sets such as climate models. There was a bug in the way one library was calculating variance, such that in situations with very low variance and large means (ie, deep ocean salinity) it was producing noisy and unrealistic answers. I rewrote the algorithm to be more computationally stable in those situations, and these changes have been incorporated into the package.

![](wp-content/uploads/2025/10/Jemma-Jeffree-Training-Day-1024x683.jpg)

Jemma Jeffree helping to facilitate a session at the ACCESS Training Day 2025. *Photo credit: Harshula Jayasuriya*

#### How did your experience as an ACCESS-NRI intern compare to what you initially expected?

I had even more freedom than I anticipated. Noone really seemed to mind what I did as long as the micro-projects I chose and areas I explored were in a vaguely ACCESS-NRI space.

It was really nice just to work on things that I had been abandoning for a while. I identified the problem with flox a while ago and knew roughly how to fix it, but I never felt like I had the permission to work on it because I needed to be doing PhD stuff and writing my paper. It was fantastic at ACCESS-NRI to be able to go and dig into the internals of this python package and understand more about the infrastructure that underpins climate science.

#### What advice would you give to other PhD students considering an internship at ACCESS-NRI?

Have some fun, take the time to explore, and keep your options open. What the internship really gave me was an opportunity to explore stuff that I care about without pressure or anything needing to come from it. But, it’s also great as a CV item or to develop skills working with climate models, and a lot of fun.

#### What does the future look like to you from here?

I still need to finish my PhD and finish the paper I was writing before I started at ACCESS-NRI.

I’d like to keep being involved in the development of packages like the one I updated during my internship, although I don’t know how much time I’ll be able to set aside for that.

I am also invested in helping to set up a link between the community and ACCESS-NRI to evaluate ACCESS-CM3. There’s lots of community members who are really interested in being involved with developing new climate models, but they don’t know the best way to interact with the ACCESS-NRI development teams. It took several months of me being here to understand how ACCESS-NRI works, and I would like to make that bridge easier.

**Categories:** [In conversation with](https://www.access-nri.org.au/category/in-conversation-with/)

**Tags:** [ACCESS-CM3](tag/access-cm3.md), [Internship](tag/internship.md)
