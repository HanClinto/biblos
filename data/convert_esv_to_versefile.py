import xml.etree.ElementTree as ET

input_file = 'esv.xml'
output_file = 'engwebp_esv.xml'

# Convert input file that looks like:
# <bible>
# <b n="Genesis">
# 	<c n="1">
#		<v n="1">In the beginning, God created the heavens and the earth.</v>
#		<v n="2">The earth was without form and void, and darkness was over the face of the deep. And the Spirit of God was hovering over the face of the waters.</v>
#		<v n="3">And God said, "Let there be light," and there was light.</v>

# To output file that looks like:
# <verseFile>
#  <v b="GEN" c="1" v="1">In the beginning, God created the heavens and the earth.</v>
#  <v b="GEN" c="1" v="2">The earth was without form and void, and darkness was over the face of the deep. And the Spirit of God was hovering over the face of the waters.</v>
#  <v b="GEN" c="1" v="3">And God said, "Let there be light," and there was light.</v>

tree = ET.parse(input_file)

root = tree.getroot()

verseFile = ET.Element('verseFile')

for book in root.findall('b'):
    book_name = book.attrib['n']
    for chapter in book.findall('c'):
        chapter_num = chapter.attrib['n']
        for verse in chapter.findall('v'):
            verse_num = verse.attrib['n']
            verse_text = verse.text
            vf_element = ET.SubElement(verseFile, 'v')
            vf_element.set('b', book_name)
            vf_element.set('c', chapter_num)
            vf_element.set('v', verse_num)
            vf_element.text = verse_text

tree = ET.ElementTree(verseFile)
# Output the file with one element per line
ET.indent(tree, '  ')
tree.write(output_file, encoding='utf-8', xml_declaration=True )


