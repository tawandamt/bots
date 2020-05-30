from flask import Flask, request
import wikipedia
import emoji
from googletrans import Translator
import warnings

import requests
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').strip().lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    in1 = incoming_msg
    if 'start' in incoming_msg:
        msg.body("Hello I 'am Jojo, your virtual assistant, powered by AI, designed for your learning.\n\n"
                "Type *search* and i will search information from the web for you or *learn* to access our virtual class")
        msg.body((emoji.emojize(":zipper-mouth_face:")))
        responded = True

    elif 'search' in incoming_msg:
        msg.body("Use T1 as a prefix to any search item, use the format below\n\n"
                 "examples: T1 computer printer or T1 4th industrial revolution\n"
                 "*Note* the search function use AI be specific to get a correct answer avoid using  one word phraises")
        responded = True

    elif 'media' in incoming_msg:
        try:
            message1 = incoming_msg[5:]
            page = wikipedia.page(message1)
            url = page.images[0]
            msg.media(url)

        except Exception:
            url = 'Eish, cant find anything. Be more specific on what you are looking for, add a word or two?'
        msg.body(url)
        responded = True



    elif 'dictionary' in incoming_msg:
        message1 = incoming_msg[10:]
        dict = vb.meaning(message1)
        msg.body(dict)
        responded = True

    elif 'isizulu' in incoming_msg:
        message1 = incoming_msg[7:]
        translator = Translator()
        result = translator.translate(message1, src='en', dest='zu')
        msg.body(result.text)
        responded = True

    elif 'english' in incoming_msg:
        message1 = incoming_msg[7:]
        translator = Translator()
        result = translator.translate(message1, src='zu', dest='en')
        msg.body(result.text)
        responded = True

    elif 'shona' in incoming_msg:
        message1 = incoming_msg[5:]
        translator = Translator()
        result = translator.translate(message1, src='en', dest='sn')
        msg.body(result.text)
        responded = True

    elif 'xhosa' in incoming_msg:
        message1 = incoming_msg[5:]
        translator = Translator()
        result = translator.translate(message1, src='en', dest='sn')
        msg.body(result.text)
        responded = True

    elif 't1' in incoming_msg:

        #      answer = wikipedia.summary(message1, sentences=2)
        #        if len(answer)==0:
        #          answer = 'Request was not found using wiki. Be more specific?'
        #      else:
        #          if len(answer) > 1500:
        #              answer = answer[0:1500] + "..."
        #      msg.body(answer)
        #   msg.media(url)

        try:
            message1 = incoming_msg[2:]
            answer = wikipedia.summary(message1, sentences=2)

        except Exception:
            answer = 'Eish, cant find anything. Be more specific on what you are looking for, add a word or two?'

        msg.body(answer)
        responded = True

    elif 'learn' in incoming_msg:
        msg.body(emoji.emojize(":file_folder:"))
        msg.body("*<<<course: Masonry L2>>>* \n\n"
                 "Select a *number* next to a *Topic* you want\n\n"
                  

                 "Topic 1: Introduction and background\n"
                 "Topic 2: Setting out masonry walls\n"
                 "Topic 3: Basic construction of masonry walls\n"
                 "Topic 4: Advanced construction of masonry walls\n"
                 "<<<<                                 >>>>")
        #msg.body(body)
        return str(resp)

    if '1' == in1:
        msg.body(emoji.emojize(":pencil:"))
        msg.body("*Topic 1: Introduction and background*\n\n"
                 "*1.1*:>Briefly describe the history of bricks and blocks\n"
                 "*1.2*:>Define terminology used in masonry. \n"
                 "*1.3*:>List standard wall thicknesses \n"
                 "*1.4*:>Describe solid and hollow masonry units\n"
                 "*1.5*:>Distinguish between bricks and blocks. \n"
                 "*1.6*:>old terms. \n"
                 "*1.7*:>Activity 1. \n"
                 )


    elif '1.1' == in1:
        msg.body("*Briefly describe the history of bricks and blocks*\n\n")
        msg.body("\n\n")
        msg.body(emoji.emojize("\n\n:telescope:"))
        msg.body("Bricks dated 10,000 years old were found in the Middle East, and the earliest mention of brick making was found in the Bible, Exodus 1:14; 5:4-19. "
                 "These records showed the Israelites made bricks for their Egyptian rulers with earth and straw. "
                 "Examples of the civilizations who used mud brick are the ancient Egyptians and the Indus Valley Civilization, where it was used exclusively."
                 "In particular, it is evident from the ruins of Buhen, Mohenjo-daro and Harappa."
                 "The first sun-dried bricks were made in Mesopotamia (what is now Iraq), in the ancient city of Ur in about 4000 BC, although the arch used for drying the bricks was not actually found."
                 " In Sumerian times offerings of food and drink were presented to “the Bone god”, who was “represented in the ritual by the first brick”. More recently, mortar for the foundations of the Hagia Sophia in Istanbul was mixed with accompanied by prayers, placed between every 12 bricks."
                 "The Romans made use of fired bricks, and the Roman legions, which operated mobile kilns, introduced bricks to many parts of the empire. Roman bricks are often stamped with the mark of the legion that supervised their production. The use of bricks in southern and western Germany, for example, can be traced back to traditions already described by the Roman architect Vitruviuse made without the heat of sun and soon became popular in cooler climates."
                )

    elif '1.2' == in1:

        msg.body("*Define terminology used in masonry.*\n\n"
                 "*Control joints*\n"
                 "Defines a control as a joint designed to permit relative movement of sections pf a masonry structure or wall to occur without impairing the functional integrity of the masonry structure or wall"
                 "Clay bricks used to expand over years and so its important to make sure that a wall would have eough space  to get bigger otherwise it would crack, that is why we have control joints.\n\n"
                 "*Wall ties*\n"
                 "SANS 2001:CM1 says a wall tie is a mechanical fastener which connects leaves of masonry to each other materials.\n\n"
                 "*Crimp wires*\n"
                 "SANS 2001:CM1 says that crimp wire ties shall be provided in collar-jointed walls at vertical and horizontal centers that do not exceed 450mm.\n"
                 "*Brickforce*\n"
                 "SANS 2001:CM1 describes brickforrce as :'A light welded stell fabric that comprises two hard-drawn wires of diameter not less than 2.8mm and not greater than 3.55mm, held apart by either perpendicular (ladder-type) or diagonal truss-type cross wires.")

    elif '1.3' == in1:
        msg.body("*List standard wall thicknesses*\n\n"
                 "A wall can carry a part of a roof, or another structure of a building if its at least 140mm wide.SANS 10400 lists two more sizes 190mm and 230 mm for structural walls"
                 "Cavity walls may also be structural.SANS 10400 says that 90 mm masonry units may be used if the roof is not made of concrete"
                 "For a heavy roof, such as a concrete slab, the leaves have to be at least 110mm thick.\n\n"
                 "*Modular Units*"
                 "SANS 10400 says that walls have to have a minimum thickness of 90mm, 0r 190mm, depending on where the wall is build and what weight it carries.")


    elif '1.4' == in1:
        msg.body("*Describe solid and hollow masonry units.*\n\n"
                 "*Solid*\n"
                 "Most clay bricks are solid or they had small holes(called cores) in them. The cores were there to make sure the brick did not slide around on the wet mortar.\n"
                 "*Hollow*"
                 "Many solid units had a slight holow on one or either side.It also stopped the brick from sliding around on the mortar that hollow is called a frog.\n"
                 )

    elif '1.5' == in1:
        msg.body("*Distinguish between bricks and blocks*\n\n"
                 "*A Block*\n"
                 "A block is an masonry unit which has a length between 300 and 650mm or a width between 130 and 300 mm or a height between 120 and 300mm.\n"
                 "*A Brick*\n"
                 "A brick is any masonry unit which is not a block.\n")


    elif '1.7' == in1:
        msg.body("*Activity 1:*\n\n"
                 "*Learning activity*"
                 "1. Write a paragraph on why a control joint is necessary and explain why we should not put a piece of steel in the control joint.\n"
                  "2. Why do you think brickforce wall ties and crimp ties are used today if buildings thata are hundreds of years od did not have anything like that?.\n"
                 )
    else:
        if not responded:
            msg.body('Sorry I did not get you correctly, type the word *start* to restart.')
            msg.body('Enter the *numbers* as indicated if you were in the virtual class ')
    return str(resp)

    msg.body(reply)
    return str(resp)


if __name__ == '__main__':
    app.run()