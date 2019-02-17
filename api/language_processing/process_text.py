#!/usr/bin/env python
# code from https://cloud.google.com/natural-language/docs/analyzing-syntax

import argparse
import os
import six
import pprint
from google.cloud import language
from google.cloud.language import types
from google.cloud.language import enums
from google.cloud import storage
from google.protobuf.json_format import MessageToDict

# for local testing
credential_path = "/Users/abihunter/pastalibs/api/language_processing/pastalibs-uncommon2019-fb268eb00254.json"
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
    tokenized = client.analyze_syntax(document).tokens
    tokens = [MessageToDict(token) for token in tokenized]
    return tokens

    # [END language_python_migration_syntax_text]
    # [END language_syntax_text]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="takes input text and returns syntax")
    parser.add_argument("--text", help="input text")
    args = parser.parse_args()
    tokens = syntax_text(args.text)
    pretty_printer = pprint.PrettyPrinter()
    for token in tokens:
        pretty_printer.pprint(token)
