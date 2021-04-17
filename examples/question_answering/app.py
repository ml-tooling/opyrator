from pydantic import BaseModel, Field
from transformers import pipeline

from opyrator.components import outputs

MODEL_NAME = "deepset/roberta-base-squad2"
# Load model
nlp = pipeline("question-answering", model=MODEL_NAME, tokenizer=MODEL_NAME)


class QuestionAnsweringInput(BaseModel):
    context: str = Field(
        ...,
        description="A string that contains the answer to the question.",
        example="My name is Sarah and I live in London",
        max_length=1000,
    )
    question: str = Field(
        ...,
        description="The question as a string that has an answer within context.",
        example="Where do I live?",
        max_length=140,
    )
    number_of_answers: int = Field(
        2, ge=1, description="The number of answers to return"
    )


def question_answering(input: QuestionAnsweringInput) -> outputs.ClassificationOutput:
    """Question answering based on a text used as context."""

    results = nlp(
        {"question": input.question, "context": input.context},
        topk=input.number_of_answers,
    )

    return outputs.ClassificationOutput(
        __root__=[
            outputs.ScoredLabel(label=result["answer"], score=result["score"])
            for result in results
        ]
    )
