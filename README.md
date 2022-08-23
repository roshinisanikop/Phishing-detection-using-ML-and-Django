# Phishing-detection-using-ML-and-Django


Detects if the url entered/pasted on to the site is a phishing site or legitimate site. 

An attempt to bring awareness to Cyber Phishing Attacks and prevent phishing attacks. 

### Project Summary: 

  -Data Preprocessing involved gathering relevant tokens from the URLs dataset using RegexpTokenizer() method from the nltk method.
  
  -Yielded root words using Snowball which was then passed to a CountVectorizer function for further data cleaning. 
  
  -Implemented various ML algorithms like Decision Tree, Random Forest, and Logistic Regression on a unique dataset of which Logistic Regression proved to provide the    best accuracy of 96.19%.
  
  -Deployed the model using Django Framework.
  
  ## How to run it?
  Firstly, you'll need a virtual environment to run this. 
  
  Why do we need a virtual environment?
  
  A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them. 
  
  So make sure to do this step by step in the console:
  
    - pip install virtualenv
    
    - cd env
    
    - cd scripts
    
    - ./activate
    
    - ### Install dependencies required:
    
      pip install
      
      - wordcloud (Word Cloud is a data visualization technique used for representing text data in which the size of each word indicates its frequency or importance.)
      
      - seaborn 
      
      - nltk (very important, this is how your url is broken down into tokens)
      
      - sklearn
      
      - pandas
      
      - db-sqlite3
      
    - run classification.py 
    
      - python classification.py
      
    - pip install django
    
    - and then finally to get your localhost/ server running
    
      - py manage.py runserver
      
  For views.py - Feel free to use either of the models - finalmodel.sav or model.sav.
  
  The model tests URLs that are unlisted on the dataset correctly as well. 
  
  
      

