# Phishing Detection (ML + Django)

Detects if a submitted URL is phishing or legitimate using a trained ML model.

## Project Summary
- Tokenize URLs with `nltk.RegexpTokenizer`, stem with Snowball, vectorize with `CountVectorizer`.
- Trained multiple models; Logistic Regression reached ~96% accuracy.
- Served via Django with a simple form UI and DB logging of checked URLs.

## Quickstart
```bash
# 1) Create and activate venv
python3 -m venv .venv
source .venv/bin/activate   # on Windows: .venv\Scripts\activate

# 2) Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 3) Set required environment
export SECRET_KEY="replace-me"   # required
export DEBUG="True"              # optional, defaults to False

# 4) Migrate database
python manage.py migrate

# 5) (Optional) Re-run feature extraction / demo
python classification.py

# 6) Run dev server
python manage.py runserver
```

Key paths
- Django project: [config](config)
- Django app: [phishing_logic](phishing_logic)
- Template: [phishing_logic/templates/phishing.html](phishing_logic/templates/phishing.html)
- Static assets: [phishing_logic/statics](phishing_logic/statics)
- Model file: `model.sav` (or `finalmodel.sav`) in repo root

## Production and Deployment
- Collect static: `python manage.py collectstatic --noinput`
- Never commit secrets; `SECRET_KEY` must come from environment.
- Deploy to Google App Engine: see [deployment.md](deployment.md).

## Notes
- SQLite is fine for demo.
- Whitenoise serves static files in production.
  
  
      

