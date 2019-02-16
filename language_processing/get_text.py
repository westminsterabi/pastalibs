import json

# Gets cleaned up text with API call and converts to string
def get_data():
    return -1

# Extracts cleaned up text and returns as string
def convert_data(data):
    data_string = data[0]["Text"]
    return data_string

def main():
    filename = "json_sample.json"
    file = open(filename, "r")
    data = json.load(file)
    convert_data(data)

if __name__=="__main__":
    main()
