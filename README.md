## 460degrees Technical Challenge :

IaaS Approch : 
===============
- Write, Plan, and Create Infrastructure as Code
- Provision of AWS EC2 instance as an application server.
- ec2.tf is main terraform file which inclueds all the resources for the application server.
- terraform.tfvars is the variable file which includes the supporting variable for the TF file. 
- Please update the AWS access key and secret and other parameters as required.

How to Run Terraform:
=====================
- Install terraform depending upon your OS : https://www.terraform.io/downloads.html
- Install terraform and initialise it in working directory, using cmd : terraform init
- Run terraform plan : The execution plan shows what Terraform will do when you call apply. This lets you avoid any surprises when Terraform manipulates infrastructure.
- Run terraform apply : When you apply the execution plan, it will ask for your confirmation before starting its operations.

Dockerize an application:
=========================
- Install docker on application server.
- Build : To build our application in a Docker container, we need to create a Dockerfile. A Dockerfile contains the instructions to build your application in a container. 
- Run : Run the container and make the application available on port 80 using below command : 
     ##### sudo docker run -it -p 80:5002 460degree


