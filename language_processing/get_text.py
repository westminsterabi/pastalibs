import json



# Gets cleaned up text with API call and converts to string
def get_data():
    # grab and load JSON
    # TODO: replace with API call
    json_text = "[{\"Text\": \"Here is some sample text that we can work with\"}]"
    data = json.loads(json_text)

    # Grab text string out of data
    text_string = data[0]["Text"]
    return text_string

def main():
    get_data()

if __name__=="__main__":
    main()
