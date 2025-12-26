# Deploying to Google Cloud Platform

## Prerequisites
1. Install Google Cloud SDK: https://cloud.google.com/sdk/docs/install
2. Create a Google Cloud project
3. Enable billing for your project

## Deployment Steps

### 1. Initialize Google Cloud
```bash
# Login to Google Cloud
gcloud auth login

# Set your project ID
gcloud config set project YOUR_PROJECT_ID

# Enable App Engine
gcloud app create --region=us-central
```

### 2. Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### 3. Deploy to App Engine
```bash
gcloud app deploy
```

### 4. View Your App
```bash
gcloud app browse
```

## Important Notes

- **Model File**: Make sure `model.sav` is in the project root
- **Database**: Currently using SQLite (fine for demo, consider Cloud SQL for production)
- **Secret Key**: Set environment variable in App Engine for production
- **Debug Mode**: Disabled in production automatically

## Environment Variables (Optional)

To set environment variables in App Engine, edit `app.yaml`:
```yaml
env_variables:
  SECRET_KEY: 'your-super-secret-key-here'
  DEBUG: 'False'
```

## Costs
- App Engine Standard: ~$0.05/hour when active
- Free tier: 28 instance hours/day

## Troubleshooting

View logs:
```bash
gcloud app logs tail -s default
```

Check app status:
```bash
gcloud app describe
```
