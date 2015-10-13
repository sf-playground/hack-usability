# [PROPOSAL] The Grid

At a size of `12px` it appears that fifteen years of typeface evolution has evolved into the auto-hinting somehwat neatly aligning the glyphs of Hack to our smallest, realistic unit of measurement: the pixel. In other words, at a size of 12px, the box a glyph is rendered in is `7px` wide and `12px` and the stroke-width of the characters is practically equal to `1px`. Common sense dictates that we should use this somehow. Therefor, I propose the following:

---

**The Grid** is an abstract binary (black and white) representation of a particular glyph at 12px. It is the simplified shape of the glyph, without hinting, subpixel rendering, different environment. It is simply the basic shape of the glyph, the shape that needs to recognizable and distinguisable _on its own_.

This binary format is easily (automatically) and objectively testible against all other glyphs. We could go as far as to say that the validity of the design of a glyph (at 12px) can be based on this simplified model underneath. And in the case of glyphs that look similar (such as the i, 1, l, |, I example) the grid view can be used to mathematically calculated how similar they actually are in their base shape. We could even automate this process and calculate the overlap between the abstract grid-view and the rendered letter as a form of custom CI testing.

---

Up till now, this has only been a mental exercise (seemed like a good idea), so the examples below might not yet live up to what's conceptually promised above.

Image 1:
- The boxes are 7x12px
- The grey area represents the x-height/body of a glyph
- The red horizontal line is the base line
- The shapes in red are outlined glyphs (without hinting) in Illustrator. I've manually positioned them to match the pixel grid.
- The black pixels are purely usability.
- The green pixels are added for identity.

![](https://github.com/sf-playground/hack-usability/raw/master/images/example-1.png)

Image 2:
- Compare the actual hinted and subpixel anti-aliased output at 12px.

![](https://github.com/sf-playground/hack-usability/raw/master/images/example-2.png)

Preliminary conclusions:
- The lowercase `i` is by far the best aligned character in this set.
- You can clearly see how the AA makes letters 'blurry'.
- You can also see how the tops of the `1` and the `l` are too similar when rendered. This could either be solved by removing the identity part of the `l` or by angling the nose of the `1` down more to create more distinction. If you would compare the pure pixel versions of the `1` and `l` you could draw the conclusion that they are indeed perhaps too similar.
