# Hack; usability vs. identity

A programmer's typeface is an important part of the development toolset, and one that tends to divide developers into strongly held allegiances in much the same way that text editors do.  The appeal of any given typeface for source is the result of a complex combination of subjective and objective factors.  The former include the shapes, rhythm, and spacing of the face - design decisions that combine to produce its identity.  The primary objective factor is its usability, a feature that determines its usefulness in a body of source code text presented to the viewer.  We cannot hope to create an identity that appeals to all users, this is a fixed feature of the design and one that generates a spectrum of responses from those who view the typeface.  We can modify the design in order to optimize its usability in source code.  This is our primary development objective for the Hack typeface.

This document defines and lays out our approach to the usability of the Hack typeface. Our aim is to develop a set of guidelines which allow us to objectively specify and measure the usability of these fonts across diverse font rendering environments, and compare this face with other commonly used source code typefaces. We acknowledge that this will not be a perfect tool and that our decisions about usability may not be uniformly acceptable to developers who consider the instrument. However, we strongly believe that a novel typeface development approach that includes a user-centric design focus, transparency in the design process, and an open and active discussion with the developer community will result in a useful development tool.

The identity of Hack is a rather subjective enigma that lies somewhere between lead designer @chrissimpkins' gut feelings, and the design concept of _form follows function_, or in our terms `($usability >= @identity) === true`.

The introduction above leads to an imperfect solution for a broad target audience, and it intentionally leaves perfection out of the equation. To fill that void, we are working in parallel on a solution that will allow you to generate a derivative version of Hack (with alternate glyphs) specific to your needs. So perhaps utopia after all?

## Primary focus of development

To guide the effort we put towards creating Hack, we use the following assumptions to narrow down infinity to something graspable:

1. Hack is a typeface primarily used for _source code_.
2. Hack is not limited to a specific platform.
3. Hack is used with a type-size between _8px_ and _14px_
4. Hack is used with a line-height between _100%_ and _150%_.
5. Hack aims to be an acceptible typeface for source code even _without_ syntax highlighting.
6. Hack is optimized for and tested with the most common programming languages and uses; Javascript, Python, Ruby, Java, PHP, Markdown, CSS, HTML and C/C++.

This does not mean that issues that fall outside of these parameters are ignored. Any valid use-case that helps us improve the overall usability of Hack is welcomed with open brackets.

## Metrics (in lieu of a better title)

Hinting suggests that _12px_ is the 'ideal' size for Hack, because that is where the stroke-width in the design (with roots dating back to about 2000) is closest to 1px, and thus fits best to the pixel grid on the screen. The corresponding x-height at that size is _7px_ with a glyph width of _7px_ as well. At _14px_ this area is _8p x 8px_.

## [PROPOSAL] How to deal with usability (issues)?

Let's take [#120](https://github.com/chrissimpkins/Hack/issues/120) as an example; "I think curly braces can be more curly, parentheses be more round, and ends of square brackets can extend horizontally".

At a first glance, this seems a matter of opinion, perhaps a matter of identity. But it is also an opportunity to take another look at those characters. The most important thing to 'read' from the issue report is that the issue is not necessarily that the curly aren't round enough. To use a medical metaphor: the user merely mentions symptoms.

1. The first step is the context where these symptoms occur. Ideally we'd be able to exactly replicate the conditions under which the user experiences the issue, but for practical purposes we can usually settle for a screenshot.
2. In this case the user reports three issues: curly braces, parentheses, and square brackets. Treat each as its own issue.
3. Make an inventory of the different semantic contexts of that character, and ideally expand this beyond the language the user is using. What are the different ways that for instance parentheses are used? Not only to group things, but they also provide a way of nesting groups. They allow a sort of sidebar within normal text. They are used in smileys. Is there a space between the character and what it groups? And how differs that per language? What are the defaults? Is the roundness intended to group the x-height, capitals, punctuation, etc? Are the parentheses intended to provide room to the contents, or to hug them tight? What characters are they usually next to? And how do other typefaces do it?

Just from these three points, you can (over time) create an objective profile and make a rational decision whether parentheses are round enough, are positioned correctly, etc.

It is important to note that there is no single optimal solution. But a good way to visually value a solution is to look at it by squinting. The dossiers that originate this way will forever be dynamic, and will keep growing. Things simply change. But it is good to keep track of as much of it as possible. If only to close annoying issues ;)
