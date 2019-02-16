#!/usr/bin/env python
# code from https://cloud.google.com/natural-language/docs/analyzing-syntax

import argparse
import os
import six
from google.cloud import language
from google.cloud.language import types
from google.cloud.language import enums
from google.cloud import storage

# for local testing
credential_path = "pastalibs-uncommon2019-6cc325ad8dbc.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

def syntax_text(text):
    # [START language_syntax_text]
    client = language.LanguageServiceClient()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    # Instantiates a plain text document.
    # [START language_python_migration_syntax_text]
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects syntax in the document. You can also analyze HTML with:
    #   document.type == enums.Document.Type.HTML
    tokens = client.analyze_syntax(document).tokens

    return tokens

    # [END language_python_migration_syntax_text]
    # [END language_syntax_text]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="takes input text and returns syntax")
    parser.add_argument("--text", help="input text")
    args = parser.parse_args()
<<<<<<< HEAD
    tokens = syntax_text(args.text)
    print(tokens)
=======
    syntax_text(args.text)

>>>>>>> d53764fd3a1345b0c66481193b98dfbbc5594c21
