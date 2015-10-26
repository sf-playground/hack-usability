txt = "("
x, y = 10, 100

font("Hack")
fontSize(100)
text(txt, (x, y))

width, height = textSize(txt)

stroke(1, 0, 0)
for metric in (0, fontDescender(), fontAscender(), fontXHeight(), fontCapHeight()):
    line((x, y + metric), (x + width, y + metric))
