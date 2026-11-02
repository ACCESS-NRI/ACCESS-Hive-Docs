---
title: Reflections on SciPy 2025
date: '2025-07-28'
description: In this event report, ACCESS-NRI staff Dr Charles Turner and Dr Paige Martin reflect on their experiences at the SciPy 2025 conference held during July...
categories:
- News
tags:
- Event report
- Python
banner: wp-content/uploads/2023/12/markus-spiske-unsplash-data-1440x500.jpg
---

# Reflections on SciPy 2025

*July 28, 2025*

*In this event report, ACCESS-NRI staff [Dr Charles Turner](person/charles-turner.md) and [Dr Paige Martin](person/dr-paige-martin.md) reflect on their experiences at the [SciPy 2025 conference](https://www.scipy2025.scipy.org) held during July in Tacoma, Washington (USA).*

Contents:

- [Charles’ reflections](#Charles)
- [Paige’s reflections](#Paige)

# Charles’ reflections { #Charles }

Early in 2025, Paige Martin posted in our work Zulip channel that she was helping to convene the geoscience track at SciPy 2025, in Tacoma, Washington. I’d helped convene the PyConAU science track with her the previous November, and I’d loved the conference. It was a radically different experience to the scientific conferences I was more used to attending. Keen to attend, I hastily banged together an abstract (Paige later told me it was reviewed very favourably) and crossed my fingers.

![](wp-content/uploads/2025/07/IMG_3969-300x225.jpeg)

Paige and Charles ready for their adventure at SciPy 2025. *Photo credit: Paige Martin*

Luckily, the abstract was accepted, and my adventure began. At ACCESS-NRI, we rely pretty heavily on the ‘[Pangeo](https://pangeo.io/) software stack’—a combination of libraries including [Xarray](https://xarray.dev/), [Dask](https://www.dask.org/), and [Intake](https://intake.readthedocs.io/en/latest/)—which are fundamental to how we share and analyse our climate model output. Like all things in software, this stack is constantly evolving, improving and changing, and keeping on top of the direction of travel is crucial to our ability to provide meaningful support to the Australian climate community. And where better to do it than SciPy?

I’m not quite sure which came first— the software or the package—but I do know that the SciPy conference came before [NumPy](https://intake.readthedocs.io/en/latest/) had reached its 1.0 release, all thanks to a keynote talk by Charles R. Harris at the conference this year, where he elucidated a beautiful history of both the conference and the package (as well as, crucially, the dinner menu each year).

Learning about catering at previous conferences was just the tip of the iceberg. The conference was split into 3 parts over 7 days: two days of tutorials, three of the main conference, and two days of sprints. Both Paige and I attended the tutorials, as well as the main conference, and I was lucky enough to attend the first day of the sprints—more on that later.

On the first morning, I spent the morning learning about how NVIDIA are providing open source tooling to make hardware accelerated computation available to the Python community, using packages like [CuPy](https://cupy.dev/) and [Numba](https://numba.pydata.org/). That afternoon, Paige and I attended a tutorial on [Pixi](https://pixi.sh/latest/)—a brand new package manager for Python lead by the creator of [Mamba](https://mamba.readthedocs.io/en/latest/)—which aims to revolutionise python package management, in particular for scientific workflows. We asked an obscene number of questions (I think we caused the tutorial to overrun by at least half an hour) before going for dinner with the guys who led the tutorial. All in all, a very successful fact-finding mission so far!

The next day, still reeling from the jetlag, we attended two more tutorials: one in the morning on new developments in python packaging (this time not Pixi), followed by a walkthrough of some of the new features of [Xarray](https://xarray.dev/) by a group of its core developers. Paige used to work with several of them, and so naturally, we all got talking. After the tutorial was up, we went to a brewery/restaurant just round the corner and continued to discuss tooling. Deepak, an Xarray core developer, told me that evening that some of our Xarray woes could be solved with a relatively simple change to Xarray itself, and encouraged me to have a crack at solving the problem during the sprints. More on that later!

![](wp-content/uploads/2025/07/IMG_6533-300x225.jpeg)

Paige introduces Charles for his session on the ACCESS-NRI Intake Catalogue. *Photo credit: Aimee Barciauskas*

The next morning, it was time for me to present. Paige introduced me to the audience, and in the following half hour, I ran through the [ACCESS-NRI Intake Catalog](https://access-nri-intake-catalog.readthedocs.io/en/latest/): its design, how we use it to distribute model output, and how we support the community. Luckily everything went smoothly – other than a mild projector mishap that looked like I might finish the presentation without slides!

The rest of the main conference flew by: I attended a Birds of a Feather session as a panellist talking about the role of research software engineers, learnt about the newest and most exciting developments in the our software ecosystem (too many to list here, but you can be sure they’ll be coming to you soon!), and got to know a number of the developers who work on these exciting packages. Luckily, Paige seemed to already know absolutely everyone, so I managed to piggyback off her social circles, even going for dinner with her and the whole [Icechunk](https://icechunk.io/en/latest/) team on Thursday night!

By the time Saturday morning rolled around, and it was time for the sprints, I was absolutely fried. After an (un)healthy number of strong coffees and an excellent breakfast, I got to work. I had two goals for the sprints: make the contribution to Xarray that Deepak had suggested and work out whether we could use Pixi to resolve some of our python packaging difficulties. With Deepak’s guidance, and the help of a couple of new friends, we made serious inroads into both with two new open pull requests, and my first contribution to Xarray!

All in all, a successful week!

# Paige’s reflections { #Paige }

![](wp-content/uploads/2025/07/IMG_4009-300x225.jpeg)

Charles and Paige at SciPy 2025 in Tacoma, Washington.

Ever since my first time attending SciPy[\*](#SciPy-note) in 2022, it has been one of my favorite conferences, and this year was no exception! It is the perfect mix of science and open-source software—two of my favorite things. It’s the event that convenes maintainers, contributors, and users of many of the packages that the ACCESS community relies on, including [NumPy](https://numpy.org/), [SciPy](https://scipy.org/) (the Python package that confusingly has the same name as the conference), [Xarray](https://xarray.dev/), [Conda](https://docs.conda.io/en/latest/), [Jupyter](https://jupyter.org/), [scikit-learn](https://scikit-learn.org/stable/), and many others. I will echo what Charles wrote above and add a few tidbits from my own perspective.

SciPy this year was held in Tacoma, Washington, USA from July 7–13. I was honored to be a co-organizer and co-chair of the Earth/Ocean/Geo/Climate/Atmosphere science track for the second year and so I got to help run the talks in our track during the week. We had some extremely high-quality presentations this year, both oral and poster (see below for some highlights).

In addition to being a track co-organizer, I was also invited to help organize and run the Tools Plenary sessions; 30-minute slots just after the plenary speakers present each morning. These Tools Plenary sessions are meant to provide an update on the key packages or communities that are part of the scientific Python ecosystem. The organizing for the Tools Plenaries mostly happens during the week of the conference—not out of laziness, but (1) to determine which package maintainers are present at the conference and (2) to ensure that we invite package developers that may be new on the scene this year. The packages represented at the Tools Plenaries this year include Xarray, AstroPy, Zarr, Scikit-learn, matplotlib, Journal of Open Source Software (JOSS), Pangeo, Jupyter, SciPy (the package), and many others.

![](wp-content/uploads/2025/07/Screen-Shot-2025-07-22-at-4.26.28-PM-300x188.png)

The SciPy 5 singing group who presented ‘Under the Sea-Python’. *Photo credit: Juanita Gomez*

Lastly, I’ll quickly mention that the SciPy 5 singing group reunited again for their third performance at SciPy this year. This is a group I helped start back in 2022 where we reword lyrics to a known song so that it’s about that year’s SciPy conference. It’s a ton of fun, but also tricky since we have to write the song during the week so we can tailor the lyrics to what happens that week. This year we performed “Under the Sea-Python”, and while we wait for the recording to be posted on YouTube, you can find the 2022 song [at this link](https://www.youtube.com/watch?v=yhwXDaaq09s).

Some of the things I learned at the conference include:

- [Pixi](https://pixi.sh/latest/) is a new package manager that looks like it will quickly take the lead as the main package manager as it’s fast (written in the [Rust](https://www.rust-lang.org/) language), relatively easy to use, and is built around creating software environments by project, which makes reproducibility for scientific projects simpler and more straightforward.
- [Polars](https://pola.rs/) is a relatively new package that seems to be taking the place of Pandas for many applications, largely because it’s much faster in many circumstances (core is built in Rust).
- [Xarray](https://xarray.dev/) now can handle flexible indexes. Previously, Xarray was only well-suited for rectilinear data sets, but now it can support curvilinear grids, staggered grids, discrete global grids, and several others (see [this link](https://xarray-indexes.readthedocs.io/) for more details and examples).
- Discrete global grid systems (DGGS) are more complicated than regular map projections but have some key benefits. We can use DGGS with Xarray via [xdggs](https://github.com/xarray-contrib/xdggs).
- [PyOpenSci](https://www.pyopensci.org/) is a community that helps make Python packaging easier for scientists. They are a very welcoming and supportive group and have an agreement with the [Journal of Open Source Software](https://joss.theoj.org/)(JOSS), so if you follow the PyOpenSci guidelines (which includes a peer review), then you can get fast-tracked to publication via JOSS.
- [Cubed](https://cubed-dev.github.io/cubed/) is a relatively new package that provides scalable, out-of-core processing for multi-dimensional arrays (it is a so-called “drop-in replacement” for the [Dask Array](https://docs.dask.org/en/stable/array.html) API). The primary benefit of Cubed over other options is that it has bounded memory, so will let you know before you start a distributed computation if it will run out of memory.
- [VirtualiZarr](https://virtualizarr.readthedocs.io/en/stable/) and [Icechunk](https://icechunk.io/en/latest/) work together to allow non cloud-optimized data storage formats (like netcdf) to be read as virtual Zarr chunks that are very performant on cloud, and are also versioned (like Git for datasets) that allows for multi-player mode (where someone can access and use the data while another person is writing an update of the same dataset). Note that Icechunk is written in Rust, with a thin Python wrapper.
- [Earthmover](https://earthmover.io/) is a start-up that provides a platform for working with multi-dimensional data on the Cloud. They have created “Arraylake”—essentially a Datalake for multi-dimensional datasets that is easily searchable and accessible, while combining the data versioning and transactional nature of VirtualiZarr and Icechunk.
- [Rust](https://www.rust-lang.org/) seems to be the language of choice right now to write core parts of packages, as it is extremely fast (Polars, Pixi, and Icechunk are all written mostly in Rust)
- Some lighthearted history of [NumPy](https://numpy.org/) (courtesy of Charles Harris’s plenary presentation), in addition to the menus that Charles mentioned:
  - NumPy was almost called “Numerix” (Asterix’s educated cousin), but an Australian company already had the name, so they had to choose something else.
  - NumPy chose interoperability over competition: as other packages started developing around the NumPy ecosystem (e.g. JAX, Dask, Xarray, PyTorch), these could have split the community. Instead, NumPy encouraged interoperability. For example, packages like Xarray can wrap NumPy arrays.

In summary, my heart is full after yet another wonderful year of SciPy and I encourage anyone interested in science and software to attend SciPy in the future.

Recordings of the plenary talks, tools plenary sessions, oral presentations and tutorials get posted on YouTube after the conference (see [this link](https://www.youtube.com/@SciPy-Conf/playlists) for some videos from 2023 and 2024 and [this link](https://www.youtube.com/@enthought/playlists) for earlier videos).

<a id="SciPy-note"></a>*\*Not to be confused with* [*SciPy the Python package*](https://scipy.org/) *or* [*Scientific Python*](https://scientific-python.org/) *– the community behind the scientific Python ecosystem.*

**Categories:** [News](category/news.md)

**Tags:** [Event report](tag/event-report.md), [Python](tag/python.md)
