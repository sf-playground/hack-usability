## Hack; usability vs. identity

A programmer's typeface is one of his most important tools. It is therefor not without reason that so many of us are constantly on the look out for a typeface that just _feels better_. This 'perfect grip' is a delicate balance between usability and identity.

This document will be an outline of the usability aspects of this project. Our aim is to develop a set of guidelines which allows us to objectively specify and measure Hack's usability; in comparison to other typefaces, but also within different environments. We acknowledge that perfection in such a diverse context is impossible. However, we strongly believe that transparency in the design process, and an open and active discussion with the community, will result in a solid tool.

The identity of Hack is a rather subjective enigma that lies somewhere between lead designer @chrissimpkins' gut feelings, and the design concept of _form follows function_, or in our terms `($usability >= @identity) === true`.

The introduction above leads to an imperfect solution for a broad target audience, and it intentionally leaves perfection out of the equation. To fill that void, we are working in parallel on a solution that will allow you to generate a derivative version of Hack (with alternate glyphs) specific to your needs. So perhaps utopia after all?

## Primary focus of development

To guide the effort we put towards creating Hack, we use the following assumptions to narrow down infinity to something graspable:

1. Hack is a typeface primarily used for _source code_.
2. Hack is not limited to a specific platform.
3. Hack is used with a type-size between _8px_ and _14px_.
4. Hack is used with a line-height between _100%_ and _150%_.
5. Hack aims to be an acceptible typeface for source code even _without_ syntax highlighting.
6. Hack is optimized for and tested with the most common programming languages and uses; Javascript, Python, Ruby, Java, PHP, Markdown, CSS, HTML and C/C++.

This does not mean that issues that fall outside of these parameters are ignored. Any valid use-case that helps us improve the overall usability of Hack is welcomed with open brackets.

## [PROPOSAL] How to deal with usability (issues)?

Let's take [#120](https://github.com/chrissimpkins/Hack/issues/120) as an example; "I think curly braces can be more curly, parentheses be more round, and ends of square brackets can extend horizontally".

At a first glance, this seems a matter of opinion, perhaps a matter of identity. But it is also an opportunity to take another look at those characters. The most important thing to 'read' from the issue report is that the issue is not necessarily that the curly aren't round enough. To use a medical metaphor: the user merely mentions symptoms.

1. The first step is the context where these symptoms occur. Ideally we'd be able to exactly replicate the conditions under which the user experiences the issue, but for practical purposes we can usually settle for a screenshot.
2. In this case the user reports three issues: curly braces, parentheses, and square brackets. Treat each as its own issue.
3. Make an inventory of the different semantic contexts of that character, and ideally expand this beyond the language the user is using. What are the different ways that for instance parentheses are used? Not only to group things, but they also provide a way of nesting groups. They allow a sort of sidebar within normal text. They are used in smileys. Is there a space between the character and what it groups? And how differs that per language? What are the defaults? Is the roundness intended to group the x-height, capitals, punctuation, etc? Are the parentheses intended to provide room to the contents, or to hug them tight? What characters are they usually next to? And how do other typefaces do it?

Just from these three points, you can (over time) create an objective profile and make a rational decision whether parentheses are round enough, are positioned correctly, etc.

It is important to note that there is no single optimal solution. But a good way to visually value a solution is to look at it by squinting. The dossiers that originate this way will forever be dynamic, and will keep growing. Things simply change. But it is good to keep track of as much of it as possible. If only to close annoying issues ;)
