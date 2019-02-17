import pprint
from language_processing import process_text, word_freq

class GenerateLibs(object):
    def __init__(self, text):
        self.raw_text = text
        self.tokens = self.gen_tokens()
        self.frequencies = self.get_freq()

    def gen_tokens(self):
        return process_text.syntax_text(self.raw_text)

    def get_freq(self):
        return word_freq.HMap(self.tokens).least_freq()


if __name__ == '__main__':
    libs = GenerateLibs("What the fuck did you just fucking say about me")
    pretty_printer = pprint.PrettyPrinter()
    pretty_printer.pprint(libs.frequencies)