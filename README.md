# airflow-cloud-sql-proxy-sample
This project is created to demonstrate how to export the data from Cloud SQL to GCS. And this is implemented as per the article https://wecode.wepay.com/posts/bigquery-wepay and the yaml files are from  https://github.com/GoogleCloudPlatform/cloudsql-proxy/blob/master/Kubernetes.md

## Steps to create the Cloud SQL export to GCS from Google composer

1) First login on to GKE cluster 
![alt text](https://github.com/porumamilla/airflow-cloud-sql-proxy-sample/blob/master/images/Screen%20Shot%202019-05-17%20at%203.02.35%20PM.png) 

2) Create the credentials from Service account json file </br>
kubectl create secret generic service-account-token --from-file=credentials.json=./service-account.json

3) Clone the project in CloudShell and under root of this project you can find the file sqlproxy-deployment.yaml and deploy it using the following command <br/>kubectl apply -f sqlproxy-deployment.yaml

4) Under root of this project you can find the file sqlproxy-services.yaml and deploy it using the following command <br/>kubectl apply -f sqlproxy-services.yaml

5) Once the you deploy the service for SQL proxy please run the following command to get the Cluster IP <br/> kubectl get services <br/> You will see something like "sqlproxy-service-database1   ClusterIP   xx.xx.xxx.xxx". Note down this ip so that we can use this in Composer connections

6) Configure the My SQL connection like the following and the copy the Cluster IP into the Host field
![alt text](https://github.com/porumamilla/airflow-cloud-sql-proxy-sample/blob/master/images/Screen%20Shot%202019-05-17%20at%203.24.23%20PM.png) 

7) Configure the GCP connection like the following. Please enter your GCP project ID and serice account JSON string 
![alt text](https://github.com/porumamilla/airflow-cloud-sql-proxy-sample/blob/master/images/Screen%20Shot%202019-05-17%20at%203.28.28%20PM.png) 

8) Once you have successfully configured the above steps and please copy the dag file from dag folder in this project to airflow dag folder. 

## CloudSQL table used in dag 
Following supplier table is used in Cloud SQL for this demo

| Field           | Type         | Null | Key | Default | Extra |
|-----------------|--------------|------|-----|---------|-------|
| id              | int(11)      | NO   | PRI | NULL    |       |
| name            | varchar(255) | YES  |     | NULL    |       |
| ship_to_address | varchar(255) | YES  |     | NULL    |       |
| bill_to_address | varchar(255) | YES  |     | NULL    |       |

