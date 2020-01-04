# analyze-Syntax-gs.py

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# gcs_uri = 'gs://cloud-samples-data/language/president.txt'
gcs_uri = 'gs://nlp-text-1/president.txt'
client = language.LanguageServiceClient()

# Instantiates a plain text document.
document = types.Document(
    gcs_content_uri=gcs_uri,
    type=enums.Document.Type.PLAIN_TEXT)

# Detects syntax in the document. You can also analyze HTML with:
#   document.type == enums.Document.Type.HTML
tokens = client.analyze_syntax(document).tokens

for token in tokens:
    part_of_speech_tag = enums.PartOfSpeech.Tag(token.part_of_speech.tag)
    print(u'{}: {}'.format(part_of_speech_tag.name,
                           token.text.content))