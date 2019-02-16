# go through words in returned JSON file
# insert word into hash_map, with count 1
# increment count if already there

class HMap:
    def __init__(self):
        self.map = {}

    def insert(self, key):
        if key not in self.map:
            self.map[key] = 1
        else:
            self.map[key] += 1


def make_map(tokens):
    hmap = HMap()

    # go through JSON outputs and insert
    for token in tokens:
        hmap.insert(token["text"]["content"])

    return hmap



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
                    "content": "The",
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
    my_map = make_map(tks)
    for key in my_map.map:
        print "(", key, ", ", my_map.map[key], ")"


main()




