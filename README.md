Computer Modern avar2
=====================

An experimental new version of Computer Modern as a parametric variable font.

[TOC]


How this project started
------------------------

I have been working with David Berlow and Santiago Orozco (FontBureau) on the production of the first avar2 variable fonts since 2022. During one of our weekly meetings, David said that there was space for us to bring in personal side-projects; that it was important to have fun projects to rest our minds from large, long projects such as [RobotoDelta](#) and [AmstelvarA2](#).

We talked about other possible use cases for the latest variable font technology: things we could do to demonstrate the new capabilities of the format. David invited us to look at our own culture and background for inspiration.

Santiago, inspired by a research trip he did to a certain region of Mexico, came up with idea to design a variable color font for the Maya script, with an animation axis to bring the glyphs to life. (??) [But this is a story for Santiago to tell one day, maybe.]

I thought a bit about my own roots and foundations as a typeface designer. During my days as a student, I have seen how many of my font designing colleagues in Brazil directed their attention to vernacular writing, or typography for indigenous languages, for example, in an attempt to create work that is more relevant to the local context. I was not so much into that; my modernist design education directed my view towards the universal aspects of type, technological innovation, and digital tools. My graduation project was a parametric bitmap font system, and the research I did for that project is what defined my identity as a typeface designer and laid the foundations for the work I do today.

Before the conversation about personal projects, we had briefly talked about the annual ATypI Conference; if we would be presenting any of our current projects there. This year’s conference would take place in Stanford and Sharjah; and I knew that Stanford University was an important place for digital typography, being the home of Donald Knuth (creator of Metafont) and Charles Bigelow (designer of Lucida). So I had this information in the back of my mind before thinking about the personal project.

Putting the two together, I got the idea to make an OpenType avar2 revival of Computer Modern – Donald Knuth’s pioneering parametric typeface, designed with his own Metafont system in the late 1970s, before PostScript was available. The more I thought about it, the more I found it made sense. I think David liked the idea too, because I got green light to work on it next to AmstelvarA2. This was in November or December of 2025.


Why Computer Modern avar2
-------------------------

Here are the main reasons why I think a parametric variable version of Computer Modern makes sense:

### There is room for improvement

From a professional typeface design and font engineering point of view, the available PostScript digital versions of Computer Modern are not very good.

Contour quality is poor. The typeface was not drawn in beziers, the beziers are the result of an automatic conversion of the original Metafont sources into PostScript.

Rounding errors, wobbly curves, (look back into main problems of AMS Fonts)

### The mother of all parametric fonts

...

### Measure current technology

Computer Modern, in its original form as a Metafont + TeX creation, has been the Holy Grail of parametric typeface design. Can we reach the same level of finesse with the current technology? Based on our work on RobotoDelta and AmstelvarA2, I think we can. Sucessfully recreating Computer Modern as an avar2 would be a poetic and convincing way to demonstrate that.

### Sharpen our tools and processes


...

### Documentation and demo

While working on AmstelvarA2, we were still figuring things out. Now that the tools and the workflow have been developed, and have been tested in practice, we can begin documenting our method and process. But now AmstelvarA2 has become too big and complex to serve as an example for beginners. We need a new simpler project which we can document from the beginning, step by step.


Which Computer Modern?
----------------------

There are many versions of Computer Modern available.

These are the ones I’ve looked at:

- AMS Fonts (Standard PostScript version)
- Computer Modern Unicode
- New Computer Modern

[explain the main differences between versions]

After looking at the files I chose to use the AMS versions as our starting point.


Computer Modern homework
------------------------

- The Concept of Metafont
- The Computer Modern book
- ...


Project team
------------

Gustavo Ferreira, design and production
İbrahim Kaçtıoğlu, production assistance
David Berlow, design advice

[AMS Fonts]: http://www.ams.org/arc/resources/amsfonts-about.html
