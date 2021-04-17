import os
import urllib.request

import fasttext

from opyrator.tasks.text_classification import (
    TextClassificationInput,
    TextClassificationOutput,
)

PRETRAINED_MODEL_PATH = "./lid.176.ftz"

# Download model if it does not exist
if not os.path.exists(PRETRAINED_MODEL_PATH):
    urllib.request.urlretrieve(
        "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.ftz",
        PRETRAINED_MODEL_PATH,
    )

# Load Model
model = fasttext.load_model(PRETRAINED_MODEL_PATH)


def detect_language(input: TextClassificationInput) -> TextClassificationOutput:
    """Detect the language of a given text via a Fasttext model."""

    predictions = model.predict([input.inputs], k=5)

    scored_labels = [
        {"label": scored_label[0].replace("__label__", ""), "score": scored_label[1]}
        for scored_label in zip(predictions[0][0], predictions[1][0])
    ]

    return TextClassificationOutput.parse_obj(scored_labels)
