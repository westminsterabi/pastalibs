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
    libs = GenerateLibs("What the fuck did you just fucking say about me, you little bitch? \
    I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in \
    numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in \
    gorilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me \
    but just another target. I will wipe you the fuck out with precision the likes of which has \
    never been seen before on this Earth, mark my fucking words. You think you can get away with \
    saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my \
    secret network of spies across the USA and your IP is being traced right now so you better \
    prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call \
    your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over \
    seven hundred ways, and that's just with my bare hands. Not only am I extensively trained in \
    unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and \
    I will use it to its full extent to wipe your miserable ass off the face of the continent,\
    you little shit. If only you could have known what unholy retribution your little 'clever'\
     comment was about to bring down upon you, maybe you would have held your fucking tongue. \
     But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. \
     I will shit fury all over you and you will drown in it. You're fucking dead, kiddo.")

    scav_bothers_me = "SCAV bothers me. I'm fine with nerds having fun in an overindulgent \
    nerdfest. What really bothers me is the amount of importance this university puts on such a \
    meaningless endeavor. People pretend like this is some celebration of creativity and \
    intellectual originality. No. Wake up. You are not doing anything more significant than \
    those weird geeks with Japanese fetishes who show up at anime conventions in droves \
    having paid hundreds of dollars to create the most accurate Chun Li costume.When you are \
    at a rich private school that gentrified an entire community of low-income African Americans \
    and eradicated an entire culture of jazz and arts under the name of urban renewal, when \
    that school is currently celebrating a swanky new art center that purports to engage a \
    variety of cultures while cutting its trauma program so that all the gunshot victims in \
    the South Side die on the ambulance ride to Northwestern, you have an obligation to do \
    something meaningful and relevant. UChicago not only is an Ivory Tower and a sheltered \
    and privileged bubble; it celebrates being one. There is a reason this school has so many \
    Nobel laureates and yet very little social relevance."

    second_libs = GenerateLibs(scav_bothers_me)
    pretty_printer = pprint.PrettyPrinter()
    pretty_printer.pprint(libs.frequencies)
    pretty_printer.pprint(second_libs.frequencies)
