# TotalSegmentator FastAPI on Azure Container Apps

End-to-end, **zero-touch** pipeline that:

1. **Builds** a Docker image containing **FastAPI + TotalSegmentator**  
2. **Pushes** the image to Azure Container Registry (ACR)  
3. **Deploys** it to **Azure Container Apps (ACA)** on every `git push`

---

### 🚀 Quick start

1. **Clone / fork** this repo  
2. **Create Azure resources once**  
   ```bash
   az group create -n my-resource-group -l eastus
   az acr create -g my-resource-group -n totalsegacr --sku Basic
   az containerapp create \
     -g my-resource-group \
     -n totalseg-app \
     --image totalsegacr.azurecr.io/totalseg-api:latest \
     --environment my-container-env \
     --ingress external \
     --target-port 8000
