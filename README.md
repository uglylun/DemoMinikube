# DemoMinikube
An end to end Demo for Minikube

### build a image for return systime
> cd app
> docker build -t demon:v0.1 .

### apply resource with terraform (not used since being given an virtual server)
> terraform init
> terraform apply 

### YAML for minikube to run an app, including ingress-rule,  namespace, service, ingress controller
> YAML

### this project is still not compeleted, todo list is below
 - github action setting to trigger image build and push to docker harbor when there is a commit or merge to main branch (not hard)
 - minikube ingress controller setting for public access (meet trouble for network)
 - auto deploy system app when images pushed to docker harbor, need to link webhook with kubernes api(a bit complex)
