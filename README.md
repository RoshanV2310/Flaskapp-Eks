eksctl create cluster --name=flask --region=ap-south-1 --zones=ap-south-1a,ap-south-1b --node-type=t3a.medium --nodes=1 --nodes-min=1 --nodes-max=2 --node-volume-size=10 --ssh-access --ssh-public-key=eks --managed --asg-access --node-private-networking=true --vpc-cidr=10.0.0.0/16 --nodegroup-name=flask


eksctl utils associate-iam-oidc-provider --region ap-south-1 --cluster flask --approve

eksctl get iamidentitymapping --cluster=flask --region=ap-south-1


aws eks update-kubeconfig --region a-south-1 --name flask-app

********************************************************************************************************************************


# Download IAM Policy

## Download latest

curl -o iam_policy.json https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/main/docs/install/iam_policy.json

## Verify latest

ls -lrta

******************************************************************************

# Create IAM Policy using policy downloaded

aws iam create-policy --policy-name AWSLoadBalancerControllerIAMPolicy --policy-document file://iam_policy.json

"Arn": "arn:aws:iam::339713074691:policy/AWSLoadBalancerControllerIAMPolicy",


***********************************************************************************

Create IAM role using Eksctl

eksctl create iamserviceaccount --cluster=flask-app --namespace=kube-system --name=aws-load-balancer-controller --role-name AmazonEKSLoadBalancerControllerRole --attach-policy-arn=arn:aws:iam::992382511089:policy/AWSLoadBalancerControllerIAMPolicy --approve



****************************************************************************************************************************************

helm repo add eks https://aws.github.io/eks-charts

helm repo update 

helm install aws-load-balancer-controller eks/aws-load-balancer-controller -n kube-system --set clusterName=flask --set serviceAccount.create=false --set serviceAccount.name=aws-load-balancer-controller

*******************************************************************************************************************************************************************

By default and for convenience, the Kubernetes control plane will allocate a port from a range (default: 30000-32767)



Flask App with MySQL Docker Setup

This is a simple Flask app that interacts with a MySQL database. The app allows users to submit messages, which are then stored in the database

DataBase

CREATE SCHEMA IF NOT EXISTS mydb;

use mydb;

CREATE TABLE IF NOT EXISTS messages (id INT AUTO_INCREMENT PRIMARY KEY,first_name VARCHAR(255) NOT NULL,last_name VARCHAR(255) NOT NULL,message TEXT NOT NULL);

SHOW TABLES;

SELECT * FROM messages;
