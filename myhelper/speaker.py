import pyttsx3


class Speaker:
    def __init__(self, first: bool = False) -> None:
        self.engine = pyttsx3.init()
        if first:
            print(f"{self.__class__.__name__} loaded")

    def __call__(self, text: str) -> None:
        self.engine.say(text)
        self.engine.runAndWait()


if __name__ == "__main__":
    speaker = Speaker(first=True)
    texts = [
        "Bonjour, je m'appelle Julien",
        "Comment on fait un poulet curry?",
        "Au revoir, on se retrouve demain à la plage",
    ]
    for text in texts:
        speaker(text)
