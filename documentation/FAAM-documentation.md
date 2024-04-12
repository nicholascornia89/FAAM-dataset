# FAAM corpus documentation

## CVAT categories

- **handwritten_annotation**: main category to label handwritten annotation regions.
- **clean_image**: this label has been used to indicate an image free from handwritten annotations. It can be used to validate a model for spotting them in larger corpora.
- **printed_annotation**: we have used this label to annotate regions of printed annotations, such has ink stamps of libraries or previous owners.
- **title_frame**: text region including information about the work's title. 
- **part_name**: text region including information about the playing part, such as a specific instrument in orchestral music.
## Filename guideline

We have tried to provide a standardized format for each filename of the corpus, according to the following scheme:

```
institution-composer-title-identifier-format-page_number
```

- **institution (3 characters)**: referring to the **abbreviation**  id of each holding institution. For a detailed list of digital libraries, see the [metadata](../metadata) section. 
- **composer (5 characters)**: surname of the main author of the work. If the surname is shorter than 5 character we have used the first name initials.
- **title (7 characters)**: a free-form string, including initials of the title with opus or catalogue numbers when possible.
- **identifier**: library identifier, corresponding with the **FAAM-ID** naming the object in the [raw-images](../raw-images) section. 
- **format (2 characters)**: illustrate the score format of the image according to the following abbreviations:
	- **pt** (Part Score): A voice is embedded in one single staff, usually a melodic instrument.
	- **ps** (Polyphonic Score): A score for one instrument that uses more than one staff for embedding its voices, like a keyboard or a harp.
	- **fs** (Full Score): a combination of several voices and staves in one system, like a song or an orchestral score.
	- **mt** (Music Treatise): combination of text and music
- **page_number (5 digits)**: note that each format has its own numeric order.
