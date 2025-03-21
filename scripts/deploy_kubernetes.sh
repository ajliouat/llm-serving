#!/bin/bash

# Apply Kubernetes configurations
kubectl apply -f deployments/kubernetes/deployment.yaml
kubectl apply -f deployments/kubernetes/service.yaml
kubectl apply -f deployments/kubernetes/autoscaler.yaml

echo "Deployment complete!"