# Research

## [PROPOSAL] How to deal with usability (issues)?

Let's take [#120](https://github.com/chrissimpkins/Hack/issues/120) as an example; "I think curly braces can be more curly, parentheses be more round, and ends of square brackets can extend horizontally".

At a first glance, this seems a matter of opinion, perhaps a matter of identity. But it is also an opportunity to take another look at those characters. The most important thing to 'read' from the issue report is that the issue is not necessarily that the curly aren't round enough. To use a medical metaphor: the user merely mentions symptoms.

1. The first step is the context where these symptoms occur. Ideally we'd be able to exactly replicate the conditions under which the user experiences the issue, but for practical purposes we can usually settle for a screenshot.
2. In this case the user reports three issues: curly braces, parentheses, and square brackets. Treat each as its own issue.
3. Make an inventory of the different semantic contexts of that character, and ideally expand this beyond the language the user is using. What are the different ways that for instance parentheses are used? Not only to group things, but they also provide a way of nesting groups. They allow a sort of sidebar within normal text. They are used in smileys. Is there a space between the character and what it groups? And how differs that per language? What are the defaults? Is the roundness intended to group the x-height, capitals, punctuation, etc? Are the parentheses intended to provide room to the contents, or to hug them tight? What characters are they usually next to? And how do other typefaces do it?

Just from these three points, you can (over time) create an objective profile and make a rational decision whether parentheses are round enough, are positioned correctly, etc.

It is important to note that there is no single optimal solution. But a good way to visually value a solution is to look at it by squinting. The dossiers that originate this way will forever be dynamic, and will keep growing. Things simply change. But it is good to keep track of as much of it as possible. If only to close annoying issues ;)
