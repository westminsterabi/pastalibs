# go through words in returned JSON file
# insert word into hash_map, with count 1
# increment count if already there

class HMap:
    # initializes an HMap
    # map is the map
    def __init__(self, tokens):
        self.map = {}
        self.orig_len = 0
        # go through JSON outputs and insert into map, increment original length
        for token in tokens:
            self.insert(token["text"]["content"])
            self.orig_len += 1

    # inserts key if it doesn't exist and increments the count by 1
    def insert(self, key):
        key = key.lower()
        if key not in self.map:
            self.map[key] = 1
        else:
            self.map[key] += 1
    # returns a list of the least frequently appearing words in the text
    # number of words returned is 20% of the original string length
    def least_freq_percent_total(self):
        least_freq = {}
        size = self.orig_len * 0.2
        for key, value in sorted(self.map.items(), key=lambda (k,v): (v,k)):
            print "%s: %s" % (key, value)

    def least_freq_percent_unique(self):
        return -1




def main():
    tks = [
            {
                "text": { 
                    "content": "The" 
                },
            },
            {
                "text": {
                    "content": "The"
                },
            },
            {
                "text": {
                    "content": "at"
                },
            },
            {
                "text": {
                    "content": "blah"
                    },
            },
            {
                "text": {
                    "content": "the"
                    },
            },
            {
                "text": {
                    "content": "At"
                    },
            }
         ]
    my_map = HMap(tks)
    #for key in my_map.map:
        #print "(", key, ", ", my_map.map[key], ")"
    my_map.least_freq_percent_total()


main()




