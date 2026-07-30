# Deployment Guide

Panduan deployment aplikasi AI Product Promotion Editor ke berbagai platform.

## Table of Contents

- [Local Development](#local-development)
- [Docker Deployment](#docker-deployment)
- [Heroku Deployment](#heroku-deployment)
- [AWS Deployment](#aws-deployment)
- [Google Cloud Platform](#google-cloud-platform)
- [Azure Deployment](#azure-deployment)
- [VPS/Server Deployment](#vpsserver-deployment)

---

## Local Development

### Setup

```bash
# Clone repository
git clone https://github.com/fadhlurrahmana/solid-doodle.git
cd solid-doodle

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run development server
python app.py
```

### Environment Variables

Create `.env` file (optional):
```
FLASK_ENV=development
FLASK_DEBUG=1
MAX_CONTENT_LENGTH=16777216
```

---

## Docker Deployment

### Build and Run

```bash
# Build image
docker build -t promo-editor .

# Run container
docker run -d -p 5000:5000 \
  -v $(pwd)/uploads:/app/uploads \
  -v $(pwd)/outputs:/app/outputs \
  --name promo-editor \
  promo-editor

# Check logs
docker logs -f promo-editor

# Stop container
docker stop promo-editor
```

### Docker Compose

```bash
# Start services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Production Docker Build

Update `Dockerfile` for production:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create non-root user
RUN useradd -m -u 1000 appuser && \
    chown -R appuser:appuser /app
USER appuser

RUN mkdir -p uploads outputs

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "app:app"]
```

Add gunicorn to requirements.txt:
```
gunicorn==21.2.0
```

---

## Heroku Deployment

### Prerequisites
- Heroku account
- Heroku CLI installed

### Steps

1. **Create Heroku app**
```bash
heroku create your-app-name
```

2. **Add buildpacks**
```bash
heroku buildpacks:add --index 1 heroku/python
```

3. **Create Procfile**
```
web: gunicorn app:app
```

4. **Create runtime.txt**
```
python-3.11.0
```

5. **Deploy**
```bash
git add .
git commit -m "Prepare for Heroku deployment"
git push heroku main
```

6. **Scale web dyno**
```bash
heroku ps:scale web=1
```

7. **Open app**
```bash
heroku open
```

### Heroku Configuration

```bash
# Set environment variables
heroku config:set FLASK_ENV=production

# Add temporary file storage (ephemeral)
# Consider using S3 for persistent storage

# View logs
heroku logs --tail
```

---

## AWS Deployment

### EC2 Deployment

1. **Launch EC2 Instance**
   - Ubuntu 22.04 LTS
   - t2.medium or larger (for image processing)
   - Security group: Allow ports 22, 80, 443

2. **Connect and Setup**
```bash
ssh -i your-key.pem ubuntu@your-ec2-ip

# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and dependencies
sudo apt install python3-pip python3-venv nginx -y

# Clone repository
git clone https://github.com/fadhlurrahmana/solid-doodle.git
cd solid-doodle

# Setup virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn
```

3. **Configure Nginx**
```bash
sudo nano /etc/nginx/sites-available/promo-editor
```

Add:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        
        # Handle large file uploads
        client_max_body_size 20M;
    }
}
```

```bash
# Enable site
sudo ln -s /etc/nginx/sites-available/promo-editor /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

4. **Create Systemd Service**
```bash
sudo nano /etc/systemd/system/promo-editor.service
```

Add:
```ini
[Unit]
Description=Promo Editor Web Application
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/solid-doodle
Environment="PATH=/home/ubuntu/solid-doodle/venv/bin"
ExecStart=/home/ubuntu/solid-doodle/venv/bin/gunicorn --workers 4 --bind 127.0.0.1:5000 app:app

[Install]
WantedBy=multi-user.target
```

```bash
# Start service
sudo systemctl start promo-editor
sudo systemctl enable promo-editor
sudo systemctl status promo-editor
```

5. **SSL with Let's Encrypt**
```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d your-domain.com
```

### AWS Elastic Beanstalk

1. **Install EB CLI**
```bash
pip install awsebcli
```

2. **Initialize EB**
```bash
eb init -p python-3.11 promo-editor --region us-east-1
```

3. **Create environment**
```bash
eb create promo-editor-env
```

4. **Deploy**
```bash
eb deploy
```

5. **Open app**
```bash
eb open
```

---

## Google Cloud Platform

### App Engine Deployment

1. **Create app.yaml**
```yaml
runtime: python311

instance_class: F2

env_variables:
  FLASK_ENV: production

handlers:
  - url: /static
    static_dir: static

  - url: /.*
    script: auto
```

2. **Deploy**
```bash
gcloud app deploy

# View in browser
gcloud app browse
```

### Cloud Run Deployment

1. **Build container**
```bash
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/promo-editor
```

2. **Deploy to Cloud Run**
```bash
gcloud run deploy promo-editor \
  --image gcr.io/YOUR_PROJECT_ID/promo-editor \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --memory 2Gi
```

---

## Azure Deployment

### Azure App Service

1. **Create Web App**
```bash
az webapp up --name your-app-name --resource-group your-rg --runtime "PYTHON:3.11"
```

2. **Configure deployment**
```bash
az webapp config appsettings set \
  --resource-group your-rg \
  --name your-app-name \
  --settings FLASK_ENV=production
```

3. **Deploy code**
```bash
az webapp deployment source config-local-git \
  --resource-group your-rg \
  --name your-app-name

git remote add azure <deployment-url>
git push azure main
```

---

## VPS/Server Deployment

### DigitalOcean, Linode, Vultr, etc.

Follow similar steps to AWS EC2 deployment:

1. Create droplet/instance with Ubuntu 22.04
2. Install Python, pip, nginx
3. Clone repository and setup
4. Configure nginx as reverse proxy
5. Setup systemd service
6. Configure SSL with Let's Encrypt

### Using Docker on VPS

```bash
# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Clone and run
git clone https://github.com/fadhlurrahmana/solid-doodle.git
cd solid-doodle
docker-compose up -d
```

---

## Production Checklist

- [ ] Set FLASK_ENV=production
- [ ] Disable debug mode
- [ ] Use production-grade WSGI server (gunicorn, uWSGI)
- [ ] Configure reverse proxy (nginx, Apache)
- [ ] Set up SSL/TLS certificates
- [ ] Configure firewall rules
- [ ] Set up monitoring and logging
- [ ] Configure automatic backups
- [ ] Implement rate limiting
- [ ] Add authentication if needed
- [ ] Set up CDN for static files
- [ ] Configure error tracking (Sentry)
- [ ] Set resource limits
- [ ] Plan for scaling
- [ ] Document deployment process

---

## Performance Optimization

### Nginx Configuration

```nginx
# Enable gzip compression
gzip on;
gzip_vary on;
gzip_min_length 1024;
gzip_types text/css text/javascript application/javascript application/json;

# Cache static files
location /static/ {
    expires 1y;
    add_header Cache-Control "public, immutable";
}

# Increase timeouts for processing
proxy_connect_timeout 300;
proxy_send_timeout 300;
proxy_read_timeout 300;
```

### Gunicorn Workers

```bash
# Calculate optimal workers: (2 x CPU cores) + 1
gunicorn --workers 5 --worker-class sync --bind 0.0.0.0:5000 app:app
```

### Redis Caching (Optional)

Add Redis for caching processed results:

```python
import redis
cache = redis.Redis(host='localhost', port=6379, db=0)
```

---

## Monitoring

### Setup Logging

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
```

### Health Check Endpoint

Add to app.py:

```python
@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy'}), 200
```

### Monitoring Tools

- **Application**: New Relic, Datadog, or AppDynamics
- **Server**: Prometheus + Grafana
- **Logs**: ELK Stack (Elasticsearch, Logstash, Kibana)
- **Uptime**: UptimeRobot, Pingdom

---

## Backup Strategy

```bash
# Backup uploads and outputs
tar -czf backup-$(date +%Y%m%d).tar.gz uploads/ outputs/

# Backup to S3 (if using AWS)
aws s3 cp backup-$(date +%Y%m%d).tar.gz s3://your-backup-bucket/
```

---

## Troubleshooting

### Common Issues

1. **Out of Memory**
   - Increase server RAM
   - Optimize image processing
   - Add swap space

2. **Slow Processing**
   - Use faster CPU
   - Optimize image resizing
   - Add caching

3. **Upload Failures**
   - Check nginx client_max_body_size
   - Verify Flask MAX_CONTENT_LENGTH
   - Check disk space

---

## Support

For deployment issues:
- Check application logs
- Review nginx error logs
- Consult platform documentation
- Open GitHub issue for help
