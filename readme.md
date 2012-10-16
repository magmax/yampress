# YAMPRESS

Build your presentations easily and fast!

## Idea ##

I liked very much the idea of [impress.js](http://bartaz.github.com/impress.js), but it is very hard to implement for every presentation.

One of the advantages of impress.js is that you can deploy it everywhere. You only needs a browser that can be found in almost every computer: chrome or firefox. So... Why to depend on PDF?


With this idea in my brain I'm trying to build a language, based on YAML, easy to understand, that allows me to build pretty impress.js slides.

## An example ##

This example is currently working:

	---
	title: This is the title of the presentation
	style: css/impress.css
	---
	title: This is the title of the first slide
	content: And this is the content for the slide XD
	---
	title: This is the title of the second slide
	content: And this is the content for the second slide!!!
	---
	This is the fouth slide, without any title.
	In the future, it should contain the same title than the previous slide :D
	---
	title: Lists
	content:
	  - first item
	  - second item
	  - third item

Easy enough?

You can see some real examples:
* basic example: [code](examples/basic.iml) [view](http://www.magmax.org/yampress/basic.html)

## In some days... ###

In some days I want to have this:

	---
	title: Wish list
	style: css/impress.css
	---
	title: Support for columns
	content:
	-
	  - first item in column 1
	  - second item
	-
	  - third item in column 2
	  - fouth item
	---
	title: Pictures go in fixed positions
	content:
	images: [image1.png, image2.png]
	---
	title: Support for background pictures
	background-image: image.png
	content: Text is over the image
	---
	title: Support for background colors:
	background-color: #ff0000
	content: Text over the color!
	---
	title: Support for markdown text:
	content: So we will have *italic* and **bold** text
	---
	title: Support for transitions
	effect: slide-right


Yes, you are right: I'm going to loose a lot of power. But I think  that it is going to be enough easy to think about it...

Another point is to generate an optional index, being able to set sections, sub-sections and so on.


## In the future, maybe... ##

The idea is to generate [Beamer](http://es.wikipedia.org/wiki/Beamer) templates too, so you can share your PDFs. But the first approach is by using *impress.js* in the beginning.

So, the YMI language should be language independant :D


# License #

Yampress code is GPL3. Your designs and slides are yours, so they are MIT. This way you can change it at your convenience.
