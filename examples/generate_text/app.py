from pydantic import BaseModel, Field
from transformers import pipeline

MODEL_NAME = "distilgpt2"
# Load model
nlp = pipeline("text-generation", model=MODEL_NAME, tokenizer=MODEL_NAME)


class TextGenerationInput(BaseModel):
    text: str = Field(
        ...,
        title="Text Input",
        description="The input text to use as basis to generate text.",
        max_length=1000,
    )
    temperature: float = Field(
        1.0,
        gt=0.0,
        multiple_of=0.001,
        description="The value used to module the next token probabilities.",
    )
    max_length: int = Field(
        30,
        ge=5,
        le=100,
        description="The maximum length of the sequence to be generated.",
    )
    repetition_penalty: float = Field(
        1.0,
        ge=0.0,
        le=1.0,
        description="The parameter for repetition penalty. 1.0 means no penalty.",
    )
    top_k: int = Field(
        50,
        ge=0,
        description="The number of highest probability vocabulary tokens to keep for top-k-filtering.",
    )
    do_sample: bool = Field(
        False,
        description="Whether or not to use sampling ; use greedy decoding otherwise.",
    )


class TextGenerationOutput(BaseModel):
    generated_text: str = Field(...)


def generate_text(input: TextGenerationInput) -> TextGenerationOutput:
    """Generate text based on a given prompt."""

    res = nlp(
        input.text,
        temperature=input.temperature,
        max_length=input.max_length,
        repetition_penalty=input.repetition_penalty,
        top_k=input.top_k,
    )
    return TextGenerationOutput(generated_text=res[0]["generated_text"])
