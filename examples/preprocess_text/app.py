import re
from enum import Enum
from typing import Set

import nltk
from pydantic import BaseModel, Field

try:
    EN_STOP_WORDS = set(nltk.corpus.stopwords.words("english"))
except LookupError:
    nltk.download("stopwords")
    EN_STOP_WORDS = set(nltk.corpus.stopwords.words("english"))


class PreprocessingStep(str, Enum):
    REMOVE_SPECIAL_CHARACTERS = "remove-special-characters"
    REMOVE_SINGLE_CHARACTERS = "remove-single-characters"
    CLEAN_MULTIPLE_SPACES = "clean-multiple-spaces"
    LOWERCASE = "lowercase"
    REMOVE_STOP_WORDS = "remove-stop-words"


class TextPreprocessingInput(BaseModel):
    text: str
    preprocessing_steps: Set[PreprocessingStep] = Field(
        ..., description="Preprocessing steps to apply on the text."
    )


class TextProcessingOutput(BaseModel):
    preprocessed_text: str = Field(...)


def preprocess_text(input: TextPreprocessingInput) -> TextProcessingOutput:
    """Clean up text data based on selected preprocessing steps."""

    text = input.text

    if PreprocessingStep.REMOVE_SPECIAL_CHARACTERS in input.preprocessing_steps:
        text = re.sub(r"\W", " ", text)

    if PreprocessingStep.REMOVE_SINGLE_CHARACTERS in input.preprocessing_steps:
        text = re.sub(r"\s+[a-zA-Z]\s+", " ", text)

    if PreprocessingStep.CLEAN_MULTIPLE_SPACES in input.preprocessing_steps:
        text = re.sub(r"\s+", " ", text, flags=re.I)

    if PreprocessingStep.LOWERCASE in input.preprocessing_steps:
        text = text.lower()

    if PreprocessingStep.REMOVE_STOP_WORDS in input.preprocessing_steps:
        tokens = text.split()
        tokens = [word for word in tokens if word not in EN_STOP_WORDS]
        text = " ".join(tokens)

    return TextProcessingOutput(preprocessed_text=text)
