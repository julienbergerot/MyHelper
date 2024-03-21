from typing import Any, Generator
from ctransformers import AutoModelForCausalLM, AutoTokenizer


class GPTModel:
    def __init__(self, directory: str = "models") -> None:
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path_or_repo_id=directory,
            model_file="mistral-7b-instruct-v0.1.Q3_K_S.gguf",
            model_type="mistral",
            gpu_layers=50,
            temperature=0.7,
            top_p=0.7,
            top_k=50,
            repetition_penalty=1.2,
            context_length=8192,
            max_new_tokens=2048,
        )
        print(f"{self.__class__.__name__} loaded")

    def __call__(self, question: str) -> Generator[str, None, None]:
        for text in self.model(question, stream=True):
            yield text


if __name__ == "__main__":
    model = GPTModel(directory="../models")
    for str in model("Pourquoi le ciel est bleu"):
        print(str, end="", flush=True)
