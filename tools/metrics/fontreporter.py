#!/usr/bin/env python

import fontforge
import os
import sys


def main(font_paths):
    try:
        import fontforge
        import psMat
    except ImportError:
        sys.stderr.write('The required FontForge modules could not be loaded.\n\n')

        if sys.version_info.major > 2:
            sys.stderr.write('FontForge only supports Python 2. Please run this script with the Python 2 executable - e.g. "python2 {0}"\n'.format(sys.argv[0]))
        else:
            sys.stderr.write('You need FontForge with Python bindings for this script to work.\n')

        sys.exit(1)

    for fontpath in font_paths:
        try:
            font = fontforge.open(fontpath)
        except EnvironmentError:
            sys.stderr.write("Error opening the requested font file.")
            sys.exit(1)

        # Font Name Tables
        familyname = font.familyname    # PostScript font family name
        fullname = font.fullname        # PostScript font name
        fondname = font.fondname        # Mac fond name
        fontname = font.fontname        # PostScript font name (subfont name in CID keyed fonts)
        copyright = font.copyright      # Copyright description
        version = font.version          # Font release version
        encoding = font.encoding        # Font encoding
        number_glyphs = len(font)       # number of glyphs
        is_cid = font.is_cid            # Is CID keyed font?


        # Font Type
        is_truetype = font.is_quadratic

        # Font Metrics
        em_size = font.em
        ymin = -font.descent
        ymax = font.ascent
        capheight = font.capHeight
        xheight = font.xHeight
        italic_angle = font.italicangle
        underlinepos = font.upos          # position of underline relative to baseline
        underlinesize = font.uwidth       # width of underline
        weight = font.weight              # Weight string, see os2_weight for numeric weight

        hasvmetrics = font.hasvmetrics
        cleartype_optimized = font.head_optimized_for_cleartype


        # sfnt Name Tables
        sfnt = font.sfnt_names
        # for item in sfnt:
        #     print(item[1] + " : " + item[2])

        # hhea
        hhea_ascent = font.hhea_ascent
        hhea_descent = font.hhea_descent
        hhea_linegap = font.hhea_linegap
        horizontal_baseline = font.horizontalBaseline

        # OS/2
        os2_typoascent = font.os2_typoascent
        os2_typoascent_add = font.os2_typoascent_add
        os2_typodescent = font.os2_typodescent
        os2_typodescent_add = font.os2_typodescent_add
        os2_typolinegap = font.os2_typolinegap

        os2_winascent = font.os2_winascent
        os2_windescent = font.os2_windescent

        os2_panose = font.os2_panose
        os2_strikepos = font.os2_strikeypos
        os2_strikesize = font.os2_strikeysize
        ### subscripts
        os2_subxoffset = font.os2_subxoff
        os2_subxsize = font.os2_subxsize
        os2_subyoffset = font.os2_subyoff
        os2_subysize = font.os2_subysize
        ### superscripts
        os2_supxoffset = font.os2_supxoff
        os2_supxsize = font.os2_supxsize
        os2_supyoffset = font.os2_supyoff
        os2_supysize = font.os2_supysize
        ### Weight & Width
        os2_weight = font.os2_weight           # key available at http://www.microsoft.com/typography/otspec/os2.htm#wtc
        os2_width = font.os2_width             # key available at http://www.microsoft.com/typography/otspec/os2.htm#wdc
        ### Heights
        os2_capheight = font.os2_capheight
        os2_xheight = font.os2_xheight

        # gasp tables
        gasp = font.gasp

        # TrueType instruction programs
        num_funcdefs = font.maxp_FDEFs             # The number of function definitions used by the tt program
        num_instrdefs = font.maxp_IDEFs            # The number of instruction definitions used by the tt program
        max_stackdepth = font.maxp_maxStackDepth   # The maximum stack depth used by the tt program
        max_storelocs = font.maxp_storageCnt       # The number of storage locations used by the tt program
        num_twilight = font.maxp_twilightPtCnt     # The number of points in the twilight zone of the tt program
        num_zones = font.maxp_zones                # The number of zones used in the tt program

        # Unicode Ranges
        uniranges = font.os2_unicoderanges

        # Errors
        load_state = font.loadState


        # Test for Presence of Glyphs by Hex Position

        # print(font.findEncodingSlot(0x031))


        # Font Dimensions, Find Largest Bounding Box Dimensions

        font_dimensions = {
                'xmin'  :    0,
                'ymin'  :    -font.descent,
                'xmax'  :    0,
                'ymax'  :    font.ascent,
                'width' :    0,
                'height':    0,
        }

        # Find the largest char width and height
        #
        # 0x00-0x17f is the Latin Extended-A range
        # 0x2500-0x2600 is the box drawing range
        for glyph in range(0x00, 0x17f) + range(0x2500, 0x2600):
            try:
                (xmin, ymin, xmax, ymax) = font[glyph].boundingBox()
            except TypeError:
                continue

            if font_dimensions['width'] == 0:
                font_dimensions['width'] = font[glyph].width

            if ymin < font_dimensions['ymin']: font_dimensions['ymin'] = ymin
            if ymax > font_dimensions['ymax']: font_dimensions['ymax'] = ymax
            if xmax > font_dimensions['xmax']: font_dimensions['xmax'] = xmax

        font_dimensions['height'] = abs(font_dimensions['ymin']) + font_dimensions['ymax']

        print(font_dimensions['xmin'])
        print(font_dimensions['xmax'])
        print(font_dimensions['ymin'])
        print(font_dimensions['ymax'])
        print(font_dimensions['width'])
        print(font_dimensions['height'])



        # Reporting
        # print(familyname)
        # print(fullname)
        # print(fondname)
        # print(fontname)
        # print(em_size)
        # print(ymin)
        # print(ymax)
        # print(capheight)
        # print(encoding)
        # print(uniranges)





if __name__ == '__main__':
    main(sys.argv[1:])

