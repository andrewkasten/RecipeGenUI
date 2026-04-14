#!/bin/bash
set -e

# Create backend directory structure
mkdir -p backend/apps
touch backend/apps/__init__.py

# Create frontend before starting containers so npm ci has package-lock.json
npm create vite@latest frontend -- --template react-ts
(cd frontend && npm install)

# Build images
docker compose -f docker-compose.dev.yml build --no-cache

# Run startproject before starting services so gunicorn can find config.wsgi
docker compose -f docker-compose.dev.yml run --rm api django-admin startproject config .

# Create apps
docker compose -f docker-compose.dev.yml run --rm api python manage.py startapp ai_api apps/ai_api
docker compose -f docker-compose.dev.yml run --rm api python manage.py startapp gendata apps/gendata

# Fix app name in apps.py files (startapp sets name to 'ai_api' instead of 'apps.ai_api')
docker compose -f docker-compose.dev.yml run --rm api python << 'EOF'
import os

for app in ['ai_api', 'gendata']:
    path = f'apps/{app}/apps.py'
    with open(path, 'r') as f:
        content = f.read()
    content = content.replace(f"name = '{app}'", f"name = 'apps.{app}'")
    with open(path, 'w') as f:
        f.write(content)
EOF

# Update settings.py to include new apps and PostgreSQL config
docker compose -f docker-compose.dev.yml run --rm api python << 'EOF'
import re

with open('config/settings.py', 'r') as f:
    content = f.read()

# Add apps
content = content.replace(
    "'django.contrib.staticfiles',",
    "'django.contrib.staticfiles',\n    'apps.ai_api',\n    'apps.gendata',"
)

# Add os import if not present
if 'import os' not in content:
    content = 'import os\n' + content

# Replace default SQLite DATABASES with PostgreSQL
content = re.sub(
    r"DATABASES = \{.*?^\}",
    """DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DB_NAME", "config"),
        'USER': os.getenv("DB_USER", "postgres"),
        'PASSWORD': os.getenv("DB_PASS", "postgres"),
        "HOST": os.getenv("DB_HOST", "db"),
        "PORT": os.getenv("DB_PORT", "5432"),
    }
}""",
    content,
    flags=re.DOTALL | re.MULTILINE
)

with open('config/settings.py', 'w') as f:
    f.write(content)
EOF

# Generate requirements.txt in backend directory
docker compose -f docker-compose.dev.yml run --rm api pip freeze > backend/requirements.txt

# Start all services now that config exists
docker compose -f docker-compose.dev.yml up -d

npm install zod

echo "✓ Django project and React app created successfully"
echo "✓ Backend: backend/"
echo "✓ Frontend: frontend/"
echo "✓ Requirements: backend/requirements.txt"
echo "✓ Services running: frontend (5173), api (8000), db (5432)"
