import os
import urllib.request

import fasttext
from pydantic import BaseModel, Field

from opyrator.components import outputs

PRETRAINED_MODEL_PATH = "./lid.176.ftz"

# Download language detection model if it does not exist
if not os.path.exists(PRETRAINED_MODEL_PATH):
    urllib.request.urlretrieve(
        "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.ftz",
        PRETRAINED_MODEL_PATH,
    )

# Load pretrained language model
model = fasttext.load_model(PRETRAINED_MODEL_PATH)


class TextClassificationInput(BaseModel):
    inputs: str = Field(
        ..., title="Text Input", description="The input text to be classified."
    )


def detect_language(input: TextClassificationInput) -> outputs.ClassificationOutput:
    """Detect the language of a given text via a Fasttext model."""

    # New lines need to be removed -> otherwise there is an error
    predictions = model.predict([input.inputs.replace("\n", " ")], k=5)

    scored_labels = [
        {"label": scored_label[0].replace("__label__", ""), "score": scored_label[1]}
        for scored_label in zip(predictions[0][0], predictions[1][0])
    ]

    return outputs.ClassificationOutput.parse_obj(scored_labels)
