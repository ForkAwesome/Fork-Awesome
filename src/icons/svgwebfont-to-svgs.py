# Turn a SVG webfont to a series of font files
# Inspired by http://helpfulsheep.com/2015-03-25-converting-svg-fonts-to-svg/

import sys

def get_glyph_value(line, start_text):
    end_text ='"'
    start_index = line.find(start_text)
    end_index = line.find(end_text, start_index + len(start_text))
    if start_index < 0 or end_index < 0:
        return
    return line[start_index + len(start_text):end_index]

def get_glyph_name(line):
    name = get_glyph_value(line, start_text = 'glyph-name="')
    name = name.replace('_', '-')
    return name

def get_glyph_unicode(line):
    unicode_char = get_glyph_value(line, start_text = 'unicode="&#x')
    if unicode_char:
        return '0x' + unicode_char[:-1].zfill(4).upper()

if len(sys.argv) < 2:
    print 'Usage: python {} webfont-file.svg destination-folder'.format(sys.argv[0])
    sys.exit()

file = open(sys.argv[1], 'r')
folder = sys.argv[2]
line = file.readline()

while line:
    if '<glyph' in line:
            name = get_glyph_name(line)
            unicode_char = get_glyph_unicode(line)

            if unicode_char:
                filename = './' + folder + '/' + unicode_char + '_' + name + '.svg'
                with open(filename, 'w') as w:
                    w.write('<?xml version="1.0" standalone="no"?>\n')
                    w.write('<svg width="1536px" height="1536px" version="1.1" xmlns="http://www.w3.org/2000/svg">\n')
                    w.write(line.replace('<glyph', '<path transform="scale(1, -1) translate(0, -1536)"') + '\n')

                    nextLine = file.readline()
                    while '/>' not in nextLine:
                        w.write(nextLine)
                        nextLine = file.readline()
                    w.write(nextLine)
                    w.write('</svg>')

    line = file.readline()

file.close()
