# Biblos Data Back-End

This code is responsible for processing Bible text into a Chroma database.

It intakes Bible text in Verse Per Line (VPL) format and outputs a SQLite database of verse embeddings.

To do this, it groups verses from each chapter together, then breaks them up to try to limit the amount of tokens in each document.  It then embeds each document with some metadata about the verse.

## VPL Format

This script parses `v` tags from an XML document, assuming one verse per tag.

Example:
```
<verseFile>
  <v b="GEN" c="1" v="1">In the beginning, God created the heavens and the earth. </v>
  <v b="GEN" c="1" v="2">The earth was formless and empty. Darkness was on the surface of the deep and God’s Spirit was hovering over the surface of the waters. </v>
  <v b="GEN" c="1" v="3">God said, “Let there be light,” and there was light. </v>
```

