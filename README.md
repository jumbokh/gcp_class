# gcp_class
##
#### ![課程](images/課程.jpg)
##
* [Google Cloud Platform Pricing Calculator](https://cloud.google.com/products/calculator/?hl=zh-tw#id=9423259f-e423-4c0a-a728-fc4d00574902)
## Python 開發環境建置及 Google Cloud SDK
* [python 開發環境安裝](https://cloud.google.com/python/setup?hl=zh-tw) 或是下載 [Winpython](https://drive.google.com/open?id=1MYVYG6kY5Tj15-nq7RBctVn4oZX15akH)
* [GCP SDK 安裝](https://cloud.google.com/sdk/docs/quickstart-windows?hl=zh-tw)
* [情緒分析教學課程](https://cloud.google.com/natural-language/docs/sentiment-tutorial?hl=zh-tw)
* [內容分類教學課程](https://cloud.google.com/natural-language/docs/classify-text-tutorial?hl=zh-tw)
* [使用 SDK 的 gsutil](https://cloud.google.com/storage/docs/quickstart-gsutil?hl=zh-tw)
* gs://cloud-samples-data/language
* gsutil cp gs://cloud-samples-data/language/* gs://[Your-bucket]
* [AutoML Vision](https://cloud.google.com/vision/automl/docs/create-datasets?hl=zh-TW#create-dataset)
##
* [輕鬆學會 Google TensorFlow 2.0 人工智慧深度學習實作開發](https://github.com/taipeitechmmslab/MMSLAB-TF2)
* [使用 Keras 測試 Cifar-10 圖片資料集](http://yhhuang1966.blogspot.com/2018/04/keras-cifar-10.html)
* [Tensorflow 官網](https://github.com/tensorflow/models)
* [Tensorflow基礎 I -- 安裝](https://fgc.stpi.narl.org.tw/activity/videoDetail/4b1141305d9cd231015d9d07dbe1002a)
##
## Day 5
### Tensorflow: 文字辨識、車牌辨識應用
* [Optical Character Recognition (OCR) Tutorial](https://cloud.google.com/functions/docs/tutorials/ocr?hl=zh-tw#functions-prepare-environment-python)
* [How to serve deep learning models using TensorFlow 2.0 with Cloud Functions](https://cloud.google.com/blog/products/ai-machine-learning/how-to-serve-deep-learning-models-using-tensorflow-2-0-with-cloud-functions?hl=zh-tw)
* [Number plate recognition with Tensorflow](http://matthewearl.github.io/2016/05/06/cnn-anpr/)
### Main Lab
* [End-to-end Machine Learning with Tensorflow on GCP](https://codelabs.developers.google.com/codelabs/end-to-end-ml/index.html?index=..%2F..cloudai#0)
* [Detect text in images](https://cloud.google.com/vision/docs/ocr?hl=zh-tw&apix_params=%7B%22resource%22%3A%7B%22requests%22%3A%5B%7B%22features%22%3A%5B%7B%22type%22%3A%22TEXT_DETECTION%22%7D%5D%2C%22image%22%3A%7B%22source%22%3A%7B%22imageUri%22%3A%22gs%3A%2F%2Fcar-license-01%2Farticleimage_170542.jpg%22%7D%7D%7D%5D%7D%7D)

### 實戰演練
* Q1: 把 image 存下來， 試著放至 storage， 然後傳下來至個人電腦
#### 說明:
#### 已經設置安裝好的 VM 想要保留下來，參照第一天的實作，建立 image， 然後傳到 storage bucket， 
#### 接著在Local端以 gsutil 指令下載， 最後記得把 bucket 中的 image 及 vm中建立的 image 刪除
##
* Q2: face recognition 專案， 可以把它做成第四天實作的第一個 Flask 網頁程式嗎?
##
* Q3: 可以把 GCP VM 的 X11 Display 打開， 以 vnc viewer 在 Local 端顯示嗎?
##
### 參考
* [Exploratory data analysis, feature selection for better ML models](https://cloud.google.com/blog/products/ai-machine-learning/building-ml-models-with-eda-feature-selection)
* [Auto Data Exploration and Feature Recommendation Tool](https://github.com/GoogleCloudPlatform/professional-services/tree/master/tools/ml-auto-eda)
* [Text classification with TensorFlow Hub: Movie reviews](https://www.tensorflow.org/tutorials/keras/text_classification_with_hub)
* [實作基於 tensorflow 和 CNN 的車牌辨識系統](https://github.com/sapphirelin/re-deep-anpr)
* [Batch image annotation offline](https://cloud.google.com/vision/docs/batch?hl=zh-tw)
* [Translating and speaking text from a photo with glossaries](https://cloud.google.com/translate/docs/hybrid-glossaries-tutorial?hl=zh-tw)
* [Using neural networks to build an automatic number plate recognition system](https://github.com/matthewearl/deep-anpr)
##
## Day 4
### Tensorflow: 環境建置、人臉辨識應用
### Face recognition 環境建置
### [python 3.5 升級至 python 3.7](https://exitcode0.net/debian-9-how-to-upgrade-python-3-5-to-python-3-7/)
### [抓圖](https://github.com/jumbokh/gcp_class/tree/master/VISION)
### [安裝 dlib](https://www.pyimagesearch.com/2018/01/22/install-dlib-easy-complete-guide/)
### 或是:
<pre>
sudo apt-get update
sudo apt-get install build-essential cmake
sudo apt-get install libopenblas-dev liblapack-dev 
sudo apt-get install libx11-dev libgtk-3-dev
sudo apt-get install python python-dev python-pip
sudo apt-get install python3 python3-dev python3-pip
pip install numpy
pip install dlib
</pre>
<pre>
sudo apt-get update
sudo apt-get install virtualenv git
virtualenv cv -p python3
source cv/bin/activate
pip install -r requirements.txt
pip install imutils
sudo apt-get install libsm6
sudo apt-get install libxrender1
sudo apt-get install libxext-dev
git clone https://github.com/nikitaa30/Face-Recognition
git clone https://github.com/ageitgey/face_recognition.git
python Face-Recognition/encode_faces.py --dataset dataset --encodings encodings.pickle
python Face-Recognition/recognize_faces_image.py --encodings encodings.pickle --image examples/example_01.png
</pre>
#### [參考](https://github.com/ageitgey/face_recognition/blob/master/README_Simplified_Chinese.md)
#### setup tensorflow in gcp vm
* STEP1. [建立 VM](https://console.cloud.google.com/compute/instances?hl=zh-TW)， 2CPU, 8GB RAM, Debian
* STEP2. 下載並安裝 [putty 終端機](https://the.earth.li/~sgtatham/putty/latest/w64/putty-64bit-0.73-installer.msi)
* STEP3. 檢視 並複製 SSH之 gcloud指令
![SSH](https://github.com/jumbokh/gcp_class/blob/master/images/ssh-vm.png)
* STEP4. 開啟 cmd 視窗，執行剛剛複製之 gcloud 指令 (已事先安裝 GCP SDK，見上方說明)
* STEP5. 進入終端機後安裝環境:
<pre>
sudo apt-get update
sudo apt-get install python3
sudo apt-get install python3-pip
sudo pip3 install tensorflow==2.0.0.b1

</pre>
#### Tensorflow code
##### Hello World! 
##### code1: {[coma-test.py](https://github.com/jumbokh/gcp_class/blob/master/Source/soma-test.py)},  
##### code2: {[nHello.py](https://github.com/jumbokh/gcp_class/blob/master/Source/nHello.py)}
<pre>
# tensorflow 1.x
import tensorflow as tf
msg = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(msg))
##
# tensorflow 2.x
import tensorflow as tf
msg = tf.constant('Hello, TensorFlow!')
tf.print(msg)
</pre>
##
* [Basic](https://nbviewer.jupyter.org/github/jumbokh/gcp_class/blob/master/Source/Basics%20of%20TensorFlow%20Programming-20180809.ipynb) {[source](https://github.com/jumbokh/gcp_class/blob/master/Source/Basics%20of%20TensorFlow%20Programming-20180809.ipynb)}
* [MNIST](https://nbviewer.jupyter.org/github/jumbokh/gcp_class/blob/master/Source/CNN%20with%20TensorFlow%20-%20MNIST%20-%2020181008.ipynb) {[Source](https://github.com/jumbokh/gcp_class/blob/master/Source/CNN%20with%20TensorFlow%20-%20MNIST%20-%2020181008.ipynb)}
* [CIFAR10](https://nbviewer.jupyter.org/github/jumbokh/gcp_class/blob/master/Source/CNN%20with%20TensorFlow%20-%20CIFAR10%20-%2020181026.ipynb) {[Source](https://github.com/jumbokh/gcp_class/blob/master/Source/CNN%20with%20TensorFlow%20-%20CIFAR10%20-%2020181026.ipynb)}
* [Tensorflow 2.0 初學者入門 colab](https://colab.research.google.com/github/tensorflow/docs/blob/master/site/zh-cn/tutorials/quickstart/beginner.ipynb?hl=zh-cn#scrollTo=F7dTAzgHDUh7)
* [针对专业人员的 TensorFlow 2.0 入门](https://colab.research.google.com/github/tensorflow/docs/blob/master/site/zh-cn/tutorials/quickstart/advanced.ipynb?hl=zh-cn)
#### Lab
* [使用 TensorFlow 建立物件偵測應用程式](https://cloud.google.com/solutions/creating-object-detection-application-tensorflow)
<pre>
ln -fs /opt/graph_def/ssd_mobilenet_v1_coco_11_06_2017/frozen_inference_graph.pb /opt/graph_def/frozen_inference_graph.pb
systemctl restart object-detection
systemctl status object-detection
</pre>
* [如何在 TensorFlow 使用深度學習建立臉部辨識一](https://blog.gcp.expert/tensorflow-facial-recognition-1/)
* [IMAGEAI_ObjectDetectionTrain_HoloLens.ipynb](https://github.com/jumbokh/cv_face/blob/master/src/IMAGEAI_ObjectDetectionTrain_HoloLens.ipynb)
* [人臉辨識 -- 使用 Darknet](https://github.com/jumbokh/cv_face/tree/master/opencv/day2)
* [人臉辨識 -- 使用 face recognition](https://github.com/jumbokh/cv_face/tree/master/opencv/day3)
* [TensorFlow Face Recognition: Three Quick Tutorials](https://missinglink.ai/guides/tensorflow/tensorflow-face-recognition-three-quick-tutorials/)
* [Face recognition -- encode](https://github.com/nikitaa30/Face-Recognition)
####
* [Quick Start: Distributed Training on the Oxford-IIIT Pets Dataset on Google Cloud](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/running_pets.md)
### Book
* ![Book](https://img12.360buyimg.com/n1/jfs/t18118/208/806643351/595772/1a32b251/5aab1e84N59164019.jpg)
* [深度学习之TensorFlow—入门、原理与进阶实战](https://www.aianaconda.com/index/CodeOne)
### 參考
* [Tensorflow 2.0 官方教程](https://www.tensorflow.org/tutorials/quickstart/advanced?hl=zh-cn)
* [CUDA ToolKit 10.1 Download](https://developer.nvidia.com/cuda-10.1-download-archive-base)
* [視覺辨識課程](https://github.com/jumbokh/cv_face)
* [人臉辨識(Face recognition) 解析與實作](https://medium.com/life-is-fantistic/%E4%BA%BA%E8%87%89%E8%BE%A8%E8%AD%98-face-recognition-cffcec53a544)
* [如何在 TensorFlow 使用深度學習建立臉部辨識二](https://blog.gcp.expert/tensorflow-facial-recognition-2/)
* [如何在 TensorFlow 使用深度學習建立臉部辨識三](https://blog.gcp.expert/tensorflow-facial-recognition-3/)
* [科技大擂台 與AI對話(熱身賽)](https://fgc.stpi.narl.org.tw/activity/video/techai)
* [Face Recognition with Python, in Under 25 Lines of Code](https://realpython.com/face-recognition-with-python/)

## Day 3
## [講義: Natural Language API](https://github.com/jumbokh/gcp_class/blob/master/NLP/Natural%20Language%20API.pptx)
## [Cloud Vision 電腦視覺實戰](https://github.com/jumbokh/gcp_class/tree/master/VISION)
##
* LAB [Natural Language API 快速入門：使用用戶端程式庫](https://cloud.google.com/natural-language/docs/quickstart-client-libraries?hl=zh-tw)
* [Natural Language](https://cloud.google.com/natural-language/?hl=zh_TW)
##


#### 參考:
* [IMDb 資料集](https://www.imdb.com/)
* [用RNN做情意分析: colab ipynb](https://nbviewer.jupyter.org/github/jumbokh/gcp_class/blob/master/NLP/04_1_%E7%94%A8RNN%E5%81%9A%E6%83%85%E6%84%8F%E5%88%86%E6%9E%90%20%281%29.ipynb)
* [CUDA Driver](https://drive.google.com/open?id=1feB4md3IuopiLIev70rRY9iY-niSKeLz)
* [Deep learning in Computer Vision](http://gg.gg/bcc3t)
* [doc: Cloud Natural Language API](https://cloud.google.com/natural-language/?hl=zh_TW)
* [ppt:朝樂門老師](https://github.com/jumbokh/gcp_class/blob/master/NLP/41%E8%87%AA%E7%84%B6%E8%AF%AD%E8%A8%80%E5%A4%84%E7%90%86.pptx)
* [图书《Python编程：从数据分析到数据科学》的配套资源](https://github.com/LemenChao/PythonFromDAToDS)
* [python code 自然語言處理](https://nbviewer.jupyter.org/github/jumbokh/gcp_class/blob/master/NLP/41.%E8%87%AA%E7%84%B6%E8%AF%AD%E8%A8%80%E5%A4%84%E7%90%86.ipynb)
* [GCP 機器學習(2) – Natural Language API 應用實例](https://blog.gcp.expert/machine-learning-natural-language-api/)
* [Using the Natural Language API with Python](https://codelabs.developers.google.com/codelabs/cloud-natural-language-python3/index.html?index=..%2F..index#0)
* [ppt: 語音聊天機器人](https://github.com/jumbokh/gcp_class/blob/master/NLP/FT700-ch15.ppt)
* [動手玩玩 GOOGLE CLOUD VISION API](https://www.mile.cloud/zh-hant/google-cloud-vision-api/)
##
## Day 2
* [speech to text](https://cloud.google.com/speech-to-text/docs/quickstart-protocol)
* [AI & Machine Learning](https://cloud.google.com/products/ai/?hl=zh-tw#more-ai-resources)
* [Google 機器學習三大服務](https://cloud.google.com/apis/docs/overview)
* [vision API](https://cloud.google.com/vision/?hl=zh-tw&utm_source=google&utm_medium=cpc&utm_campaign=japac-TW-all-zh-dr-bkws-all-super-trial-e-dr-1003987&utm_content=text-ad-none-none-DEV_c-CRE_263273745739-ADGP_Hybrid+%7C+AW+SEM+%7C+BKWS+~+T1+%7C+EXA+%7C+ML+%7C+1:1+%7C+TW+%7C+zh+%7C+Vision+%7C+google+cloud+vision+api+%7C+en-KWID_43700031887751273-kwd-203288731207&userloc_9040321&utm_term=KW_google%20cloud%20vision%20api&gclid=Cj0KCQiAl5zwBRCTARIsAIrukdPS_OnI7B_o8YEV4n--CYIOymZVVFKaFK-fzRH0rh9wIFQ-9RDaiowaAtnVEALw_wcB)
* [NL API](https://cloud.google.com/natural-language/?hl=zh-tw&utm_source=google&utm_medium=cpc&utm_campaign=japac-TW-all-en-dr-bkws-all-all-trial-b-dr-1003987&utm_content=text-ad-none-none-DEV_c-CRE_252375343168-ADGP_Hybrid+%7C+AW+SEM+%7C+BKWS+~+T1+%7C+BMM+%7C+ML+%7C+M:1+%7C+TW+%7C+en+%7C+Language+%7C+API-KWID_43700036898841807-kwd-490168509258&userloc_9040321&utm_term=KW_%2Bgoogle%20%2Bnl%20%2Bapi&gclid=Cj0KCQiAl5zwBRCTARIsAIrukdMj14wWmIR3rHXVslZigPlxh-uQ1kSEu9-tVQ9rJUKmE0XNASDdQ2YaAgUDEALw_wcB)
* [Google 機器學習三大服務：AutoML, Cloud ML Engine, ML API 介紹與比較](https://blog.gcp.expert/google-cloud-automl-ml-engine-ml-api/)
* [Google Cloud Auto ML Prices](https://cloud.google.com/skus/?hl=zh_TW&_ga=2.32958715.-492626677.1577098418&_gac=1.213815654.1577098418.Cj0KCQiA6IHwBRCJARIsALNjViVJF6XIuFJD_Wvf0LluZbusR7aGAK8QYhLihR2ocuZIB8CTVGsgGcoaAgPfEALw_wcB&currency=USD&filter=auto+ml)
* [APIs and Reference](https://cloud.google.com/natural-language/docs/apis)
* [Actions on Google: The developer platform for the Google Assistant.](https://developers.google.com/assistant)
* [Cloud Speech-to-text API 指南](https://cloud.google.com/speech-to-text/docs/how-to)
* [用於Firebase的ML套件](https://firebase.google.com/docs/ml-kit?authuser=0)
* [GCP ML API](https://blog.gcp.expert/google-cloud-automl-ml-engine-ml-api/)
* [範例應用程式](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/speech/cloud-client)
* ![GCP ML API](images/GCP_ML_info.png)
* ![languageCode](images/language-code.JPG)

##
![定價](images/text-speech-price.JPG)
* LAB1: [Good Cloud speech API](https://cloud.google.com/speech-to-text/?hl=zh-tw&utm_source=google&utm_medium=cpc&utm_campaign=japac-TW-all-zh-dr-bkws-all-super-trial-e-dr-1003987&utm_content=text-ad-none-none-DEV_c-CRE_263264846828-ADGP_Hybrid+%7C+AW+SEM+%7C+BKWS+~+T1+%7C+EXA+%7C+ML+%7C+1:1+%7C+TW+%7C+zh+%7C+Speech+%7C+google+cloud+speech+api+%7C+en-KWID_43700031887751063-kwd-203288730727&userloc_9040321&utm_term=KW_google%20cloud%20speech%20api&gclid=CjwKCAiA9JbwBRAAEiwAnWa4Q2L6JNb6JogBial2wAr81VYZ5u4OrRugpr-9YzFBBQZEU33BTpu_OxoC_gwQAvD_BwE)
* LAB1(參考): [Machine Learning(一)：Cloud Speech API 介紹與實作](https://blog.gcp.expert/machine-learning-cloud-speech-api/)
* [金鑰下載](https://cloud.google.com/speech-to-text/docs/reference/libraries)
##
* LAB2:[Cloud speech to text API](https://github.com/jumbokh/gcp_class/blob/master/Google_text-to-speech-API.md)
##
* LAB3:[在 Windows 下使用 Google Assistant](https://github.com/jumbokh/gcp_class/blob/master/Google_Assistant_Win10.md)
* [Your own Raspberry Pi Google Assistant](https://medium.com/@janne.spijkervet/your-own-raspberry-pi-google-assistant-1434be9eac99)
* [How to Get Google Assistant for PC](https://www.lifewire.com/google-assistant-on-windows-4628292)
##
* LAB4: [轉錄短音訊檔案](https://cloud.google.com/speech-to-text/docs/sync-recognize#speech-sync-recognize-python)

##
## Day1
* LAB1: [註冊 Google Cloud Plateform](https://github.com/jumbokh/gcp_class/blob/master/GCP_%E8%A8%BB%E5%86%8A%E5%8F%8A%E5%BB%BA%E7%AB%8B%E5%B0%88%E6%A1%88.pptx)
##
* [[GCP]Google Cloud Platform架站(6) - 外部IP查詢與靜態IP設定](https://robarter.pixnet.net/blog/post/223287133-%5Bgcp%5Dgoogle%E9%9B%B2%E7%AB%AF%E6%9E%B6%E7%AB%99---%E5%A4%96%E9%83%A8ip%E6%9F%A5%E8%A9%A2%E8%88%87%E9%9D%9C%E6%85%8Bip%E8%A8%AD%E5%AE%9A)
* LAB2: [負載平衡](https://github.com/jumbokh/gcp_class/blob/master/Load_balance.md)
* [Creating a Virtual Machine](https://codelabs.developers.google.com/codelabs/cloud-create-a-vm/index.html?index=..%2F..index#0)
##
* LAB3: [FireBase: Get Start](https://codelabs.developers.google.com/codelabs/firebase-get-to-know-web/index.html?index=..%2F..index#0)
        [完成檔](https://github.com/jumbokh/gcp_class/tree/master/Source/firebase-gtk-web-start-wendj1_Done)
* LAB4: [練習題](https://codelabs.developers.google.com/codelabs/firebase-web/index.html?index=..%2F..index#0)
##


## 書籍

* ![機器學習開發神器！Google Cloud Platform 雲端開發應用超入門](images/Flag_F9361.jpg) [連結](https://www.flag.com.tw/books/product/F9361)
* ![Google Cloud平台實作手冊：Google雲端功能一點就通](images/MP21713.jpg) [連結](https://www.books.com.tw/products/0010753986)

## 參考連結

* [懶人包】Google Cloud 基礎教學資源彙集](https://blog.gcp.expert/google-cloud-products-quick-start/)
* [Firebase 是什麼 ? 集 APP 後端開發與分析於一身的強大工具！](https://blog.gcp.expert/firebase-gcp/)
* [Get to Know Cloud Firestore #1](https://www.youtube.com/watch?time_continue=1&v=v_hR4K4auoQ&feature=emb_logo)
* [The 7 Steps of Machine Learning (AI Adventures)](https://www.youtube.com/watch?v=nKW8Ndu7Mjw&feature=emb_logo)
* [From Zero to ML on Google Cloud Platform (Cloud Next '18)](https://www.youtube.com/watch?v=QU7_eU8HzAQ)
##
### Google CodeLab
* [End-to-end Machine Learning with Tensorflow on GCP](https://codelabs.developers.google.com/codelabs/end-to-end-ml/index.html?index=..%2F..cloudai#0)
* [Integrating Machine Learning APIs](https://codelabs.developers.google.com/codelabs/cloud-ml-apis/index.html?index=..%2F..index#0)
* [Get to know Firebase for web](https://codelabs.developers.google.com/codelabs/firebase-get-to-know-web/index.html?index=..%2F..index#0)
* [Using the Vision API with Python](https://codelabs.developers.google.com/codelabs/cloud-vision-api-python/index.html?index=..%2F..cloudai#0)
* [End-to-end Machine Learning with Tensorflow on GCP](https://codelabs.developers.google.com/codelabs/end-to-end-ml/index.html?index=..%2F..cloudai#0)
* [Google Code on GITHUB](https://github.com/googlecodelabs/tools)
* [A sample of the Smart Home device control APIs in Actions on Google](https://github.com/actions-on-google/smart-home-nodejs)
* [Cloud Firestore Web Codelab](https://codelabs.developers.google.com/codelabs/firestore-web/index.html?index=..%2F..index#0)
* [Detect objects in an Image using Firebase MLKit](https://codelabs.developers.google.com/codelabs/mlkit-image-objects-android/index.html?index=..%2F..index#0)
* [Train and deploy on-device image classification model with AutoML Vision in ML Kit](https://codelabs.developers.google.com/codelabs/automl-vision-edge-in-mlkit/index.html?index=..%2F..index#0)
* [Recognize text, facial features, and objects in images with ML Kit for Firebase: Android](https://codelabs.developers.google.com/codelabs/mlkit-android/index.html?index=..%2F..index#0)
##
