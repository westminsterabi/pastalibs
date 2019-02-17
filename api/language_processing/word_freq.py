class HMap:
    # initializes an HMap
    # map is the map
    def __init__(self, tokens):
        self.map = {}
        # go through JSON outputs and insert into map, increment original length
        for token in tokens:
            self.insert((token["text"]["content"], token["partOfSpeech"]["tag"]))

    # inserts key if it doesn't exist and increments the count by 1
    def insert(self, key):
        key = (key[0].lower(), key[1])
        if key not in self.map:
            self.map[key] = 1
        else:
            self.map[key] += 1
    # returns a list of the least frequently appearing words in the text
    def least_freq(self):
        least_freq = []
        for key, value in sorted(self.map.items(), key=lambda tup: (tup[1],tup[0])):
            least_freq.append(key)

        return least_freq

def create_word_list(tks):
    hmap = HMap(tks)
    word_list = hmap.least_freq()
    return word_list
    

### for testing purposes
# def main():
#     tks = [
#             {
#                 "text": { 
#                     "content": "The" 
#                 },
#                 "part_of_speech": {
#                     "tag": "ADP"
#                 },
#             },
#             {
#                 "text": {
#                     "content": "the"
#                 },
#                 "part_of_speech": {
#                     "tag": "ADP"
#                 },
#             },
#             {
#                 "text": {
#                     "content": "The"
#                 },
#                 "part_of_speech": {
#                     "tag": "ADP"
#                 },
#             },
#             {
#                 "text": {
#                     "content": "vat"
#                 },
#                 "part_of_speech": {
#                     "tag": "Noun"
#                 },
#             },
#          ]
#     my_map = HMap(tks)
#     for key in my_map.map:
#         print "(", key, ", ", my_map.map[key], ")"
#     least_freq = my_map.least_freq()


# main()




