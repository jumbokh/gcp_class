# analyze-Entity-Sentiment-gs.py
import sys
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# gcs_uri = 'gs://cloud-samples-data/language/president.txt'
gcs_uri = 'gs://nlp-text-1/president.txt'

client = language.LanguageServiceClient()

document = types.Document(
    gcs_content_uri=gcs_uri,
    type=enums.Document.Type.PLAIN_TEXT)

# Detect and send native Python encoding to receive correct word offsets.
encoding = enums.EncodingType.UTF32
if sys.maxunicode == 65535:
    encoding = enums.EncodingType.UTF16

result = client.analyze_entity_sentiment(document, encoding)

for entity in result.entities:
    print(u'Name: "{}"'.format(entity.name))
    for mention in entity.mentions:
        print(u'  Begin Offset : {}'.format(mention.text.begin_offset))
        print(u'  Content : {}'.format(mention.text.content))
        print(u'  Magnitude : {}'.format(mention.sentiment.magnitude))
        print(u'  Sentiment : {}'.format(mention.sentiment.score))
        print(u'  Type : {}'.format(mention.type))
    print(u'Salience: {}'.format(entity.salience))
    print(u'Sentiment: {}\n'.format(entity.sentiment))