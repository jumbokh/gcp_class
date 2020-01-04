# analyze-Syntax-in.py
import six
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

text = 'President Kennedy spoke at the White House.'

client = language.LanguageServiceClient()

if isinstance(text, six.binary_type):
    text = text.decode('utf-8')

# Instantiates a plain text document.
document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)

# Detects syntax in the document. You can also analyze HTML with:
#   document.type == enums.Document.Type.HTML
tokens = client.analyze_syntax(document).tokens

for token in tokens:
    part_of_speech_tag = enums.PartOfSpeech.Tag(token.part_of_speech.tag)
    print(u'{}: {}'.format(part_of_speech_tag.name,
                           token.text.content))