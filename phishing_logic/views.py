from django.shortcuts import render
from django.http import HttpResponse
from .models import phishing as PhishingModel
import joblib
import os
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


def phishing(request):
    """Main page view for phishing detection."""
    return render(request, 'phishing.html')


def prediction(request):
    """Handle URL prediction requests with error handling."""
    context = {'a': ''}
    
    if request.method == 'POST':
        try:
            # Get URL from POST request
            url = request.POST.get('urls', '').strip()
            
            if not url:
                context['a'] = "Error: Please enter a valid URL"
                return render(request, 'phishing.html', context)
            
            # Load model from models directory (prefers model.sav, falls back to finalmodel.sav)
            models_dir = Path(__file__).resolve().parent.parent / 'models'
            candidate_models = [models_dir / 'model.sav', models_dir / 'finalmodel.sav']
            model_path = next((p for p in candidate_models if p.exists()), None)
            
            if not model_path:
                logger.error(f"Model file not found in {models_dir}")
                context['a'] = "Error: ML model not found. Please ensure model.sav exists in the models folder."
                return render(request, 'phishing.html', context)
            
            # Load and run prediction
            model = joblib.load(model_path)
            result = model.predict([url])
            
            # Save to database
            try:
                phishing_entry = PhishingModel(URLphish=url)
                phishing_entry.save()
            except Exception as db_error:
                logger.warning(f"Could not save to database: {db_error}")
            
            # Determine result message
            if result[0] == "good":
                context['a'] = " Legitimate Site"
            else:
                context['a'] = " Phishing Site"
                
        except FileNotFoundError:
            logger.error("Model file not found")
            context['a'] = "Error: ML model file not found"
        except Exception as e:
            logger.error(f"Prediction error: {str(e)}")
            context['a'] = f"Error: Unable to analyze URL. {str(e)}"
    
    return render(request, 'phishing.html', context)
