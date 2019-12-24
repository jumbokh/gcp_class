### Google-speech-text 測試
#### 啟用 API
<pre>
https://cloud.google.com/speech-to-text/docs/quickstart-protocol?_ga=2.234802334.-1824209114.1577068850
</pre>
#### 建立憑證
<pre>
https://cloud.google.com/docs/authentication/getting-started#auth-cloud-implicit-python
</pre>
#### create authkey:
#### API和服務==>憑證==>建立憑證==>服務帳戶金鑰
#### ==>新增服務帳戶=> 服務名(自取)、角色:project->擁有者

#### 選擇/建立專案，如: Google-speech-test-01
 
#### Linux:
<pre>
  export GOOGLE_APPLICATION_CREDENTIALS="/home/jumbo/src/gcp/Google-ML-Class-31e15d26a06d.json"
  pip3 install google-cloud-storage==1.23.0
</pre>

#### 安裝SDK
<pre>
  curl https://sdk.cloud.google.com | bash
  gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS
  gcloud auth application-default login
  gcloud auth application-default print-access-token
  gcloud auth application-default print-access-token > token
  export ACCESS_TOKEN=`cat token`
</pre>

####  To generate an access token for other uses, run:
####    gcloud auth application-default print-access-token
  
#### 建立 sync-request.json
<pre>
nano sync-reqest.json
輸入:

{
  "config": {
      "encoding":"FLAC",
      "sampleRateHertz": 16000,
      "languageCode": "en-US",
      "enableWordTimeOffsets": false
  },
  "audio": {
      "uri":"gs://cloud-samples-tests/speech/brooklyn.flac"
  }
}
</pre>
#### 測試:

<pre>
curl -s -H "Content-Type: application/json" \
    -H "Authorization: Bearer $ACCESS_TOKEN" \
    https://speech.googleapis.com/v1/speech:recognize \
    -d @sync-request.json
</pre>
#### 或是:
<pre>
curl -s -H "Content-Type: application/json" \
    -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
    https://speech.googleapis.com/v1/speech:recognize \
    -d @sync-request.json
</pre>
#### Windows:
##### 先下載安裝 curl，並在windows path 中, 增加 curl 指令位置
#####  curl 官網: https://curl.haxx.se/windows/
<pre>
gcloud auth application-default print-access-token > token.json
set ACCESS_TOKEN=[PATH].json
curl -s -H "Content-Type: application/json" -H "Authorization: Bearer $ACCESS_TOKEN https://speech.googleapis.com/v1/speech:recognize -d @sync-request.json
</pre>

#### 錯誤一: 未啟用API
<pre>
{
  "error": {
    "code": 403,
    "message": "Cloud Speech-to-Text API has not been used in project 432046692542 before or it is disabled. Enable it by visiting https://console.developers.google.com/apis/api/speech.googleapis.com/overview?project=432046692542 then retry. If you enabled this API recently, wait a few minutes for the action to propagate to our systems and retry.",
    "status": "PERMISSION_DENIED",
    "details": [
      {
        "@type": "type.googleapis.com/google.rpc.Help",
        "links": [
          {
            "description": "Google developers console API activation",
            "url": "https://console.developers.google.com/apis/api/speech.googleapis.com/overview?project=432046692542"
          }
        ]
      }
    ]
  }
}
jumbo@RPi4:~/src/gcp$

</pre>

#### 正確回應:
<pre>
jumbo@RPi4:~/src/gcp$ curl -s -H "Content-Type: application/json" \
>     -H "Authorization: Bearer $ACCESS_TOKEN" \
>     https://speech.googleapis.com/v1/speech:recognize \
>     -d @sync-request.json
{
  "results": [
    {
      "alternatives": [
        {
          "transcript": "how old is the Brooklyn Bridge",
          "confidence": 0.98314303
        }
      ]
    }
  ]
}
jumbo@RPi4:~/src/gcp$
</pre>
  
  
  
  
