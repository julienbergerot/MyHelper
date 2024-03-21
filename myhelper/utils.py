from myhelper.speaker import Speaker

from typing import List


def answer(model, question: str, response: List[str]) -> None:
    for str in model(question):
        response.append(str)

    response.append("DONE")


def speak(response: List[str], spoken: List[str]) -> None:
    while len(response) == 0 or response[-1] != "DONE":
        total = "".join(response)
        already = "".join(spoken)
        remaining = total[len(already) :]
        to_say = ".".join(remaining.split(".")[:-1])
        if to_say == 0:
            continue
        spoken.append(to_say)
        speaker = Speaker()
        speaker(to_say)
        del speaker

    # Speak for the rest
    total = "".join(response[:-1])
    already = "".join(spoken)
    remaining = total[len(already) :]
    speaker = Speaker()
    speaker(remaining)
    del speaker
