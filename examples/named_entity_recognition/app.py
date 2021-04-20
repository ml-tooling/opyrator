from enum import Enum
from typing import List, Set

import spacy
from pydantic import BaseModel, Field

# Load Model
nlp = spacy.load("en_core_web_sm")


class Entity(str, Enum):
    ORG = "ORG"
    PERSON = "PERSON"
    TIME = "TIME"
    DATE = "DATE"
    GPE = "GPE"
    MONEY = "MONEY"


class TextInput(BaseModel):
    text: str = Field(
        ..., example="Apple is looking at buying U.K. startup for $1 billion"
    )
    entity_types: Set[Entity] = Field(
        ..., description="Selected entity types to discover on the text."
    )


class NamedEntity(BaseModel):
    text: str
    start_char: int
    end_char: int
    label: Entity


class NamedEntitiesOutput(BaseModel):
    __root__: List[NamedEntity]

    def render_output_ui(self, streamlit, input) -> None:  # type: ignore
        """Custom output UI.

        If this method is implmeneted, it will be used instead of the default Output UI renderer.
        """
        from annotated_text import annotated_text

        TYPE_TO_COLOR = {
            Entity.ORG: "#8ef",
            Entity.PERSON: "#faa",
            Entity.TIME: "#afa",
            Entity.DATE: "#ABEBC6",
            Entity.GPE: "#FF7F50",
            Entity.MONEY: "#6495ED",
        }

        text_parts = []
        last_index = 0
        for item in sorted(self.__root__, key=lambda x: x.start_char):
            text_part = input.text[last_index : item.start_char]
            if text_part:
                text_parts.append(text_part)
            text_parts.append(
                (
                    input.text[item.start_char : item.end_char],
                    item.label.value,
                    TYPE_TO_COLOR[item.label],
                )
            )
            last_index = item.end_char

        text_part = input.text[last_index : len(input.text)]
        if text_part:
            text_parts.append(text_part)
        annotated_text(*text_parts)


def named_entity_recognition(input: TextInput) -> NamedEntitiesOutput:
    doc = nlp(input.text)
    results = []
    for ent in doc.ents:
        try:
            entity_type = Entity(ent.label_)
            if entity_type in input.entity_types:
                results.append(
                    NamedEntity(
                        text=ent.text,
                        start_char=ent.start_char,
                        end_char=ent.end_char,
                        label=entity_type,
                    )
                )
        except ValueError:
            continue

    return NamedEntitiesOutput(__root__=results)
