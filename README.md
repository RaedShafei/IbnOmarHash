# Ibn Omar Hash Algorithm (Python 2.7)

This project runs the custom "Ibn Omar Hash Algorithm" using a Flask API in a Python 2.7 Docker environment.

## 🐳 Running Locally with Docker

```bash
docker build -t ibn-omar-hash .
docker run -p 5000:5000 ibn-omar-hash
```

## 🌐 Deployment (Fly.io)

### Step 1: Install Fly CLI
[https://fly.io/docs/hands-on/install-flyctl/](https://fly.io/docs/hands-on/install-flyctl/)

### Step 2: Launch App
```bash
fly launch
```

### Step 3: Deploy
```bash
fly deploy
```

## 📮 API Usage

**POST** `/hash`

Request Body:
```json
{ "text": "hello world" }
```

Response:
```json
{ "hash": "0x..." }
```

## Author

Developed by Raed O. Shafei  
🔗 [https://github.com/RaedShafei](https://github.com/RaedShafei)
