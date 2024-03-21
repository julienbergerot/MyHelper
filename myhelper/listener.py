from typing import Any

import sounddevice as sd
import queue
import ast


from vosk import Model, KaldiRecognizer


class Listener:
    def __init__(self, lang: str = "fr") -> None:
        self.q = queue.Queue()
        self.model = Model(lang=lang)
        self.device_info = sd.query_devices(0, "input")
        self.samplerate = int(self.device_info["default_samplerate"])

        print(f"{self.__class__.__name__} loaded")

    def callback(self, indata: Any, frames: Any, time: Any, status: Any) -> None:
        """This is called (from a separate thread) for each audio block."""
        self.q.put(bytes(indata))

    def __call__(self) -> None:
        with sd.RawInputStream(
            samplerate=self.samplerate,
            blocksize=8000,
            device=0,
            dtype="int16",
            channels=1,
            callback=self.callback,
        ):
            rec = KaldiRecognizer(self.model, self.samplerate)
            while True:
                data = self.q.get()
                if rec.AcceptWaveform(data):
                    res = ast.literal_eval(rec.Result())["text"]
                    if res == "":
                        continue
                    return res


if __name__ == "__main__":
    listener = Listener()
    print(listener())
