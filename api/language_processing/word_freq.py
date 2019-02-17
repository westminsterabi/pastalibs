# go through words in returned JSON file
# insert word into hash_map, with count 1
# increment count if already there

class HMap:
    # initializes an HMap
    # map is the map
    def __init__(self, tokens):
        self.map = {}
        # go through JSON outputs and insert into map, increment original length
        for token in tokens:
            self.insert(token["text"]["content"])

    # inserts key if it doesn't exist and increments the count by 1
    def insert(self, key):
        key = key.lower()
        if key not in self.map:
            self.map[key] = 1
        else:
            self.map[key] += 1
    # returns a list of the least frequently appearing words in the text
    # number of words returned is 20% of the number of unique words
    def least_freq(self):
        least_freq = []
        size = len(self.map) * 0.2
        i = 0
        for key, value in sorted(self.map.items(), key=lambda (k,v): (v,k)):
            if (i > size):
                break
            least_freq.append(key)
            i += 1

        return least_freq

### for testing purposes
#def main():
#    tks = [
#            {
#                "text": { 
#                    "content": "The" 
#                },
#            },
#            {
#                "text": {
#                    "content": "The"
#                },
#            },
#            {
#                "text": {
#                    "content": "at"
#                },
#            },
#            {
#                "text": {
#                    "content": "blah"
#                    },
#            },
#            {
#                "text": {
#                    "content": "the"
#                    },
#            },
#            {
#                "text": {
#                    "content": "At"
#                    },
#            },
#            {
#                "text": {
#                    "content": "one"
#                    },
#            },
#            {
#                "text": {
#                    "content": "two"
#                    },
#            },
#            {
#                "text": {
#                    "content": "three"
#                    },
#            },
#            {
#                "text": {
#                    "content": "four"
#                    },
#            },
#            {
#                "text": {
#                    "content": "five"
#                    },
#            },
#            {
#                "text": {
#                    "content": "six"
#                    },
#            },
#            {
#                "text": {
#                    "content": "seven"
#                    },
#            },
#            {
#                "text": {
#                    "content": "eight"
#                    },
#            },
#            {
#                "text": {
#                    "content": "nine"
#                    },
#            },
#            {
#                "text": {
#                    "content": "ten"
#                    },
#            }
            
#         ]
#    my_map = HMap(tks)
#    #for key in my_map.map:
#        #print "(", key, ", ", my_map.map[key], ")"
#    least_freq = my_map.least_freq()


#main()




