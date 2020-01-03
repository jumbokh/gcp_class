
## Cloud AutoML Vision: AutoML Vision API Tutorial
## [網址](https://cloud.google.com/vision/automl/docs/tutorial)
#### 下載憑證，並設定環境變數
<pre>
set GOOGLE_APPLICATION_CREDENTIALS=D:\mydoc\EDU\gcp_class\automl-vision-prj-f912a7d555cf.json
</pre>
#### 增加服務帳戶，設定角色，並同意 服務帳戶 存取你的 Google雲端服務專案資源
<pre>
gcloud auth login
gcloud projects add-iam-policy-binding automl-vision-prj --member="user:jumbokh@gmail.com" --role="roles/automl.admin" 
gcloud projects add-iam-policy-binding automl-vision-prj --member=serviceAccount:Cloud-AutoML-prj  --role="roles/automl.editor" 
gcloud projects add-iam-policy-binding automl-vision-prj --member="serviceAccount:custom-vision@appspot.gserviceaccount.com"  --role="roles/storage.admin"
</pre>
#### 安裝客戶端 library
<pre>
pip install --upgrade google-cloud-automl
</pre>
#### 設定環境變數
<pre>
set PROJECT_ID="automl-vision-prj"
set REGION_NAME="us-central1"
</pre>
#### 新增 Google Cloud Storage bucket
* bucket 名稱必須為: $PROJECT_ID-vcm
<pre>
gsutil mb -p $PROJECT_ID -c regional -l $REGION_NAME gs://$PROJECT_ID-vcm/
</pre>
#### 複製資料集至你的 Google Cloud Storage bucket
<pre>
gsutil -m cp -R gs://cloud-ml-data/img/flower_photos/  gs://$PROJECT_ID-vcm/img/
</pre>
#### 資料集必須為每個影像檔案準備清單檔及標示資料，詳: [如何準備你的資料集](https://cloud.google.com/vision/automl/docs/prepare)
<pre>
gsutil cat gs://$PROJECT_ID-vcm/img/flower_photos/all_data.csv | sed "s:cloud-ml-data:$PROJECT_ID-vcm:" > all_data.csv
</pre>
#### 然後複製你的 .csv 檔案至 bucket
<pre>
gsutil cp all_data.csv gs://$PROJECT_ID-vcm/csv/
</pre>
#### 複製以下程式:
* [automl_vision_dataset.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/vision/automl/automl_vision_dataset.py)
* [automl_vision_model.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/vision/automl/automl_vision_model.py)
* [automl_vision_predict.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/vision/automl/automl_vision_predict.py)
#### 執行步驟:
##### STEP 1. 建立資料集
<pre>
python automl_vision_dataset.py create_dataset "flowers" "False"
</pre>
##### 回復資訊:
<pre>
Dataset name: projects/216065747626/locations/us-central1/datasets/ICN7372141011130533778
Dataset id: ICN7372141011130533778
Dataset display name: flowers
Image classification dataset specification:
       classification_type: MULTICLASS
Dataset example count: 0
Dataset create time:
       seconds: 1530251987
       nanos: 216586000
</pre>
##### STEP 2.匯入影像至資料集
<pre>
python automl_vision_dataset.py import_data $DATASET_ID "gs://$PROJECT_ID-vcm/csv/all_data.csv" {Python}

mvn compile exec:java -Dexec.mainClass="com.google.cloud.vision.samples.automl.DatasetApi" -Dexec.args="import_data $DATASET_ID gs://$PROJECT_ID-vcm/csv/all_data.csv" {Java}

node automlVisionDataset.js import-data $DATASET_ID "gs://$PROJECT_ID-vcm/csv/all_data.csv" {Node.js}
</pre>
##### 回復資訊:
<pre>
Processing import...
Dataset imported.
</pre>
##### STEP 3. 建模 (注意免費 node hour數)
<pre>
python automl_vision_model.py create_model $DATASET_ID "flowers_model" "1" {Python}

mvn compile exec:java -Dexec.mainClass="com.google.cloud.vision.samples.automl.ModelApi" -Dexec.args="create_model $DATASET_ID flowers_model 1" {Java}

node automlVisionModel.js create-model $DATASET_ID "flowers_model" "1" {Node.js}
</pre>
#### 在布置完後，馬上測試預測， 可以再跑一次建模，測試完後請記得刪除布置
<pre>
Training operation name: projects/216065747626/locations/us-central1/operations/ICN3007727620979824033
Training started...
Model name: projects/216065747626/locations/us-central1/models/ICN7683346839371803263
Model id: ICN7683346839371803263
Model display name: flowers_model
Image classification model metadata:
Training budget: 1
Training cost: 1
Stop reason:
Base model id:
Model create time:
        seconds: 1529649600
        nanos: 966000000
Model deployment state: deployed
</pre>
##### STEP 4. 評估模組
<pre>
python automl_vision_model.py display_evaluation $MODEL_ID {Python}

mvn compile exec:java -Dexec.mainClass="com.google.cloud.vision.samples.automl.ModelApi" -Dexec.args="display_evaluation $MODEL_ID" {Java}

node automlVisionModel.js display-evaluation $MODEL_ID {Node.js}
</pre>
##### 回復資訊:
<pre>
Precision and recall are based on a score threshold of 0.5
Model Precision: 96.3%
Model Recall: 95.7%
Model F1 score: 96.0%
Model Precision@1: 96.33%
Model Recall@1: 95.74%
Model F1 score@1: 96.04%
</pre>
##### STEP 5. 使用建好的模組進行預測
<pre>
python automl_vision_predict.py predict $MODEL_ID "resources/test.png" "0.7" {Python}

mvn compile exec:java -Dexec.mainClass="com.google.cloud.vision.samples.automl.PredictionApi" -Dexec.args="predict $MODEL_ID resources/test.png 0.7" {Java}

node automlVisionPredict.js predict $MODEL_ID "resources/test.png" "0.7" {Node.js}
</pre>
##### 回復資訊:
<pre>
Prediction results:
Predicted class name: dandelion
Predicted class score: 0.9702693223953247
</pre>
#### STEP 6. 刪除模組
<pre>
python automl_vision_model.py delete_model $MODEL_ID {Python}

mvn compile exec:java -Dexec.mainClass="com.google.cloud.vision.samples.automl.ModelApi" -Dexec.args="delete_model $MODEL_ID" {Java}

node automlVisionModel.js delete-model $MODEL_ID {Node.js}
</pre>
##### 回復資訊:
<pre>
Model deleted.
</pre>
