from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

#gcs_uri = 'gs://cloud-samples-data/language/hello.txt'
gcs_uri = 'gs://nlp-text-1/reviews/bladerunner-pos.txt'
client = language.LanguageServiceClient()

# Instantiates a plain text document.
document = types.Document(
    gcs_content_uri=gcs_uri,
    type=enums.Document.Type.PLAIN_TEXT)

# Detects sentiment in the document. You can also analyze HTML with:
#   document.type == enums.Document.Type.HTML
sentiment = client.analyze_sentiment(document).document_sentiment

print('Score: {}'.format(sentiment.score))
print('Magnitude: {}'.format(sentiment.magnitude))