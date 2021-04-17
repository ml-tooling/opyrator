from pydantic import BaseModel, Field

from opyrator.components import outputs


class TextClassificationInput(BaseModel):
    inputs: str = Field(
        ..., title="Text Input", description="The input text to be classified."
    )


class TextClassificationOutput(outputs.ClassificationOutput):
    pass
