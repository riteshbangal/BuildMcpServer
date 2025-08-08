
# Build MCP Server – Deployment Runbook

This document provides step-by-step instructions for building, containerizing, deploying, and accessing the **Build MCP Server** in a Kubernetes cluster.

---

## **1. Prerequisites**

* Docker installed and configured
* Kubernetes cluster with `kubectl` access
* Docker Hub account and repository (`314201/build-mcp-server`)
* MCP server code (`main.py`, `requirements.txt`, `Dockerfile`)

---

## **2. Prepare Requirements File**

Create `requirements.txt`:

```txt
fastmcp>=2.11.0
mcp[cli]>=1.12.3
mcp-server>=0.1.4
requests>=2.32.4
typer>=0.16.0
pyyaml>=6.0.2
```

---

## **3. Dockerfile**

Example `Dockerfile`:

```dockerfile
FROM python:3.12-slim

# Install uv
RUN pip install --no-cache-dir uv

WORKDIR /app

# Copy files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose app port
EXPOSE 3000

# Run MCP server
CMD ["uv", "run", "main.py"]
```

---

## **4. Build and Push the Image**

```bash
docker build -t 314201/build-mcp-server:latest .
docker push 314201/build-mcp-server:latest
```

---

## **5. Kubernetes Secret for API Key**

```bash
kubectl create secret generic mcp-server-secrets \
  --from-literal=api_key=12345-abcde-67890-fghij
```

---

## **6. Kubernetes Deployment & Service**

Create `build-mcp-server.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: build-mcp-server
  labels:
    app: build-mcp-server
spec:
  replicas: 1
  selector:
    matchLabels:
      app: build-mcp-server
  template:
    metadata:
      labels:
        app: build-mcp-server
    spec:
      containers:
        - name: build-mcp-server
          image: 314201/build-mcp-server:latest
          imagePullPolicy: Always
          ports:
            - containerPort: 3000
          env:
            - name: API_KEY
              valueFrom:
                secretKeyRef:
                  name: mcp-server-secrets
                  key: api_key
---
apiVersion: v1
kind: Service
metadata:
  name: build-mcp-server-service
spec:
  type: ClusterIP
  selector:
    app: build-mcp-server
  ports:
    - protocol: TCP
      port: 3000
      targetPort: 3000
```

Apply it:

```bash
kubectl apply -f build-mcp-server.yaml
```

---

## **7. Port Forward to Access Locally**

```bash
kubectl port-forward service/build-mcp-server-service 3000:3000
```

---

## **8. Test the MCP Server**

```bash
curl -H "Authorization: Bearer 12345-abcde-67890-fghij" \
     http://localhost:3000/tools/health
```

Expected Response:

```json
{
  "status": "ok",
  "message": "MCP Server is running smoothly."
}
```

---

## **9. Useful Commands**

* **Check Pods**

  ```bash
  kubectl get pods
  ```
* **Check Logs**

  ```bash
  kubectl logs <pod-name>
  ```
* **Delete Deployment**

  ```bash
  kubectl delete -f build-mcp-server.yaml
  ```

---

## **10. Security Notes**

* Never hardcode API keys in source code.
* Always store sensitive values in Kubernetes secrets.
* Restrict port-forwarding and access in production environments.

