from myhelper.listener import Listener
from myhelper.speaker import Speaker
from myhelper.gpt_model import GPTModel
from myhelper.utils import answer, speak

from threading import Thread


if __name__ == "__main__":
    SHOW_QUESTIONS = True
    SHOW_ANSWER = True

    listener = Listener()
    speaker = Speaker(first=True)
    gpt_model = GPTModel()

    speaker("Tout est chargé correctement, on peut commencer")
    del speaker

    try:
        while True:
            question = listener()
            # for now, we assume everything I say is a question waiting to be answered
            question += "?"
            if SHOW_QUESTIONS:
                print(f"QUESTION : {question}")
            response = []
            spoken = []
            threading_gpt = Thread(target=answer, args=[gpt_model, question, response])
            threading_speaker = Thread(target=speak, args=[response, spoken])
            threading_gpt.start()
            threading_speaker.start()

            threading_gpt.join()
            threading_speaker.join()
            if SHOW_ANSWER:
                print(f"REPONSE : {''.join(response)}")
    except KeyboardInterrupt:
        print("\nDone")
