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

# Detects sentiment in the document. You can also analyze HTML with:
#   document.type == enums.Document.Type.HTML
entities = client.analyze_entities(document).entities

for entity in entities:
    entity_type = enums.Entity.Type(entity.type)
    print('=' * 20)
    print(u'{:<16}: {}'.format('name', entity.name))
    print(u'{:<16}: {}'.format('type', entity_type.name))
    print(u'{:<16}: {}'.format('salience', entity.salience))
    print(u'{:<16}: {}'.format('wikipedia_url',
          entity.metadata.get('wikipedia_url', '-')))
    print(u'{:<16}: {}'.format('mid', entity.metadata.get('mid', '-')))