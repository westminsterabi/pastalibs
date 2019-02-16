# go through words in returned JSON file
# insert word into hash_map, with count 1
# increment count if already there


def make_map(tokens):
    hmap = {}
    
    # go through JSON outputs and insert
    for token in tokens:
        print(token)

def insert(key, hmap):
    if key not in hmap:
        hmap[key] = 1
    else:
        hmap[key] += 1



def main():
    tks = [
            {
                "text": { 
                    "content": "The", 
                    "beginOffset": 4
                },
                "partOfSpeech": {
                    "tag": "DET",}, 
                "dependencyEdge": {
                    "headTokenIndex": 2,
                    "label": "DET"
                    },
                "lemma": "The"
            },
            {
                "text": {
                    "content": "only",
                    "beginOffset": 8
                    },
                "partOfSpeech": {
                    "tag": "ADJ",
                    },
                "dependencyEdge": {
                    "headTokenIndex": 2,
                    "label": "AMOD"
                    },
                "lemma": "only"
            }
         ]
    make_map(tks)


main()




