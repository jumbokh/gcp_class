#$ gsutil cp -r gs://automl-vision-prj-vcm./download_dir
from google.cloud import automl

# TODO(developer): Uncomment and set the following variables
project_id = 'automl-vision-prj'
model_id = 'SOngNewChu_vision_20200103091353'

client = automl.AutoMlClient()
# Get the full path of the model.
model_full_id = client.model_path(project_id, 'us-central1', model_id)
response = client.undeploy_model(model_full_id)

print(u'Model undeployment finished. {}'.format(response.result()))