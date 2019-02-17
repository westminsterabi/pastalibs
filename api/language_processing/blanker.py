import json

def construct_paragraph(data):
    # helper function for blanker
    paragraph = ""
    for item in data:
        dictword = item['text']['content']
        paragraph = paragraph + dictword + " "
    return paragraph

def blanker(jdata, list):
    data = json.loads(jdata)
    pos_data = ['']*len(list)
    count = 0
    for word in list:
        for item in data:
            dictitem = item['text']['content']
            if(dictitem == word):
                item['text']['content'] = "_____"
                pos_data[count] = item['partOfSpeech']['tag']
        count = count + 1
    para = construct_paragraph(data)
    jpos_data = {
        'data':
            {'part_of_speech': pos_data,
             'text': para},
    }
    return json.dumps(data), jpos_data



# ## for testing purposes
# def main():
#     tks = [
#            {
#                "text": {
#                    "content": "The"
#                },
#                "part_of_speech": {
#                    "tag": "X"
#                },
#            },
#            {
#                "text": {
#                    "content": "The"
#                },
#                "part_of_speech": {
#                    "tag": "X"
#                },
#            },
#            {
#                "text": {
#                    "content": "at"
#                },
#                "part_of_speech": {
#                    "tag": "X"
#                },
#            },
#            {
#                "text": {
#                    "content": "blah"
#                    },
#                "part_of_speech": {
#                    "tag": "X"
#                },
#            },
#            {
#                "text": {
#                    "content": "the"
#                    },
#                "part_of_speech": {
#                    "tag": "X"
#                },
#            },
#            {
#                "text": {
#                    "content": "At"
#                    },
#                "part_of_speech": {
#                    "tag": "X"
#                },
#            },
#            {
#                "text": {
#                    "content": "one"
#                    },
#                "part_of_speech": {
#                    "tag": "X"
#                },
#            },
#            {
#                "text": {
#                    "content": "two"
#                    },
#                "part_of_speech": {
#                    "tag": "NUM"
#                },
#            },
#            {
#                "text": {
#                    "content": "three"
#                    },
#                "part_of_speech": {
#                    "tag": "X"
#                },
#            },
#            {
#                "text": {
#                    "content": "four"
#                    },
#                "part_of_speech": {
#                    "tag": "X"
#                },
#            },
#            {
#                "text": {
#                    "content": "five"
#                    },
#                "part_of_speech": {
#                    "tag": "NUM"
#                },
#            },
#            {
#                "text": {
#                    "content": "six"
#                    },
#                "part_of_speech": {
#                    "tag": "X"
#                },
#            },
#            {
#                "text": {
#                    "content": "seven"
#                    },
#                "part_of_speech": {
#                    "tag": "X"
#                },
#            },
#            {
#                "text": {
#                    "content": "eight"
#                    },
#                "part_of_speech": {
#                    "tag": "X"
#                },
#            },
#            {
#                "text": {
#                    "content": "nine"
#                    },
#                "part_of_speech": {
#                    "tag": "NOUN"
#                },
#            },
#            {
#                "text": {
#                    "content": "ten"
#                    },
#                "part_of_speech": {
#                    "tag": "X"
#                },
#            }
#
#         ]
#     tks = json.dumps(tks)
#     words = ["The", "five", "nine"]
#     data, jdata = blanker(tks, words)
#
#
#
# main()
