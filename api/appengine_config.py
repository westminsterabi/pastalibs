# appengine_config.py
from google.appengine.ext import vendor
import nltk

# Add any libraries install in the "lib" folder.
vendor.add('lib')
nltk.download('stopwords')