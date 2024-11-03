ReadMe Commands

Build and Push Docker Image:
Build and push the Docker image to Docker Hub or Amazon ECR.

# Build the Docker image
docker build -t my-vbbu-image:latest .

# Tag the image for Docker Hub
docker tag my-vbbu-image:latest <your-dockerhub-username>/my-vbbu-image:latest

# Push the image to Docker Hub
docker push <your-dockerhub-username>/my-vbbu-image:latest


To deploy Kubernetes manifests:

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f configmap.yaml
kubectl apply -f persistentvolume.yaml
kubectl apply -f persistentvolumeclaim.yaml
kubectl apply -f hpa.yaml
kubectl apply -f networkpolicy.yaml
