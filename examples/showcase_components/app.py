import datetime
from enum import Enum
from typing import Dict, List, Optional, Set

from pydantic import BaseModel, Field, SecretStr

from opyrator.components.types import FileContent


class SelectionValue(str, Enum):
    FOO = "foo"
    BAR = "bar"


class OtherData(BaseModel):
    text: str
    integer: int


class ShowcaseModel(BaseModel):
    short_text: str = Field(..., max_length=60, description="Short text property")
    password: SecretStr = Field(..., description="Password text property")
    long_text: str = Field(..., description="Unlimited text property")
    integer_in_range: int = Field(
        20,
        ge=10,
        lt=30,
        multiple_of=2,
        description="Number property with a limited range. Optional because of default value.",
    )
    positive_integer: int = Field(
        ..., ge=0, multiple_of=10, description="Positive integer with step count of 10."
    )
    float_number: float = Field(0.001)
    date: Optional[datetime.date] = Field(
        datetime.date.today(),
        description="Date property. Optional because of default value.",
    )
    time: Optional[datetime.time] = Field(
        datetime.datetime.now().time(),
        description="Time property. Optional because of default value.",
    )
    string_list: List[str] = Field(
        ..., max_items=20, description="List of string values"
    )
    int_list: List[int] = Field(..., description="List of int values")
    boolean: bool = Field(
        False,
        description="Boolean property. Optional because of default value.",
    )
    file_list: Optional[List[FileContent]] = Field(
        None,
        description="A list of files. Optional property.",
    )
    single_file: Optional[FileContent] = Field(
        None,
        description="A single file. Optional property.",
    )
    string_dict: Dict[str, str] = Field(
        ..., description="Dict property with string values"
    )
    float_dict: Dict[str, float] = Field(
        ..., description="Dict property with float values"
    )
    single_selection: SelectionValue = Field(
        ..., description="Only select a single item from a set."
    )
    multi_selection: Set[SelectionValue] = Field(
        ..., description="Allows multiple items from a set."
    )
    single_object: OtherData = Field(
        ...,
        description="Another object embedded into this model.",
    )
    object_list: List[OtherData] = Field(
        ...,
        description="A list of objects embedded into this model.",
    )


def showcase_components(input: ShowcaseModel) -> ShowcaseModel:
    """Showcase of a variety of differnt property types and how they are shown in the UI.

    This function only returns the input data.
    """
    return input
