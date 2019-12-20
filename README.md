# gcp_class

### [建構可擴充的彈性應用程式](https://cloud.google.com/solutions/scalable-and-resilient-apps?hl=zh-TW)
#### [部署範例解決方案](https://cloud.google.com/solutions/scalable-and-resilient-apps?hl=zh-TW#deploying_the_example_solution)
* ![安裝開機載入軟體](images/instance-stack.png)
<pre>
此開機指令碼將會：

安裝 Chef 用戶端。
下載一個名為 node.json 的特殊 Chef 檔案。此檔案可告知 Chef 要為此執行個體執行何種設定。
執行 Chef 並任其處理詳細的設定作業。
</pre>
#### 完整指令碼 (下載 node.json)
<pre>
#! /bin/bash

# Install Chef
curl -L https://www.opscode.com/chef/install.sh | bash

# Download node.json (runlist)
curl -L https://github.com/googlecloudplatform/... > /tmp/node.json

# Run Chef
chef-solo -j /tmp/node.json -r https://github.com/googlecloudplatform/...
</pre>
#### 取得資料庫密碼
<pre>
curl "http:/metadata.google.internal/computeMetadata/v1/instance/attributes/dbpassword" -H "Metadata-Flavor: Google"
</pre>
