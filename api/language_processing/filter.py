import math
import nltk
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

def filter_list(word_list):
    return_size = math.floor(len(word_list) * 0.2)
    new_list = []
    # We only want these parts of speech
    desired_pos = {"ADV", "ADJ", "VERB", "NOUN", "NUM"}
    # remove undesired parts of speech and stop words
    for word in word_list:
        if word[1] in desired_pos and word[0] not in stop_words:
            new_list.append(word)

    return new_list[0:return_size]

### for testing purposes
# def main():
#     words = {("cat", "NOUN"), ("dog", "NOUN"), ("the", "ADP"), ("although", "ADP"), ("mousey", "ADJ"), ("run", "VERB")}
    
#     print(words)
#     words = filter(words)
#     print(words)


# main()







