### 建立自己的 image
#### 以 Debian 為例
#### show available images
<pre>
gcloud compute images list
</pre>
<pre>

gcloud compute instances create "instance-2" \
 --zone "asia-east1-b" \
 --machine-type "n1-standard-1" \
 --subnet "default" \
 --maintenance-policy "MIGRATE" \
 --image "debain-10-buster-v20191210" \
 --image-project "debian-cloud" \
 --boot-disk-size "10G" \
 --boot-disk-type "pd-standard" \
 --boot-disk-device-name "instance-2"
</pre>
<pre>
 gcloud compute ssh instance-2 --zone asia-east1-b
 
 sudo su -
 apt-get update -y && apt-get install ngix -y
 runlevel
 </pre>
 #### 確定 ngix 再重開時可以自動執行
 <pre>
 ls -l /etc/rc5.d/
 reboot
 </pre>
 #### 設定該主機刪除時，把硬碟留下來
 <pre>
 gcloud compute instances set-disk-auto-delete instance-2 \
  --no-auto-delete \
  --disk instance-2 \
  --zone asia-east1-b
 </pre>
 #### 刪除主機，然後透過該硬碟製作 image
 <pre>
 gcloud compute instances delete instance-2 --zone asia-east1-b -q
 </pre>
 #### 接下來針對卸載的硬碟製作 image
 <pre>
 gcloud compute images create myimage --source-disk instance-2 \
  --source-disk-zone asia-east1-b
 </pre>
 ### 建立 instance template
 <pre>
 gcloud compute instance-templates create "instance-template-1" \
 --machine-type "n1-standard-1" \
 --network "default" \
 --image "myimage" \
 --tags "http-server","https-server" \
 --boot-disk-size "10" \
 --boot-disk-type "pd-standard" \
 --boot-disk-device-name "instance-template-1"
 </pre>
 ### 建立 instance group
 <pre>
 gcloud compute instance-groups managed create "instance-group-1" \
 --zone "asia-east1-b" \
 --cool-down-period "60" \
 --max-num-replicas "10" \
 --min-num-eplicas "1" \
 --target-cpu-utilization "0.6"
 </pre>
