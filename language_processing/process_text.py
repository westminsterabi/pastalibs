#!/usr/bin/env python
# code from https://cloud.google.com/natural-language/docs/analyzing-syntax

import argparse
import os
import six
from google.cloud import language
from google.cloud.language import types
from google.cloud.language import enums

credential_path = "/Users/amyhuang/Downloads/pastalibs-uncommon2019-6cc325ad8dbc.json"
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

    """
    # part-of-speech tags from enums.PartOfSpeech.Tag
    pos_tag = ('UNKNOWN', 'ADJ', 'ADP', 'ADV', 'CONJ', 'DET', 'NOUN', 'NUM',
               'PRON', 'PRT', 'PUNCT', 'VERB', 'X', 'AFFIX')

    for token in tokens:
        print(u'{}: {}: {}'.format(token.part_of_speech.tag,
                                   pos_tag[token.part_of_speech.tag],
                                   token.text.content))
    """
    # print(tokens)
    return tokens

    # [END language_python_migration_syntax_text]
    # [END language_syntax_text]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="takes input text and returns syntax")
    parser.add_argument("--text", help="input text")
    args = parser.parse_args()
    syntax_text(args.text)