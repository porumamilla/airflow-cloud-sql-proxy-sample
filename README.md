# airflow-cloud-sql-proxy-sample
This project is created to demonstrate how to export the data from Cloud SQL to GCS. And this is implemented as per the article https://wecode.wepay.com/posts/bigquery-wepay and the yaml files are from  https://github.com/GoogleCloudPlatform/cloudsql-proxy/blob/master/Kubernetes.md

## Steps to create the Cloud SQL export to GCS from Google composer

1) First login on to GKE cluster 


1) Create the credentials from Service account json file
kubectl create secret generic service-account-token --from-file=credentials.json=./service-account.json

2) 
