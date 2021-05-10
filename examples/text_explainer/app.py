from enum import Enum
from pathlib import Path
from typing import Dict, Union

import eli5
from joblib import dump, load
from pydantic import BaseModel, Field
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegressionCV
from sklearn.pipeline import make_pipeline

cached_model_name = "./newsdata_model.joblib"
cached_vec_name = "./newsdata_vec.joblib"

categories = ["comp.graphics", "sci.med", "misc.forsale", "sci.electronics"]
twenty_train = fetch_20newsgroups(
    subset="train", categories=categories, shuffle=True, random_state=42
)
twenty_test = fetch_20newsgroups(
    subset="test", categories=categories, shuffle=True, random_state=42
)


# Preprocessing logic
def preprocess(data: str) -> str:
    return str(data).replace("\n", " ").replace("\r", "").strip()


vec = CountVectorizer()
if not Path(cached_model_name).exists():
    print("Quickly train model (that can take up to a few minutes): ...")
    clf = LogisticRegressionCV(solver="liblinear", max_iter=1000)
    pipe = make_pipeline(vec, clf)
    pipe.fit([preprocess(item) for item in twenty_train.data], twenty_train.target)
    dump(clf, cached_model_name)
    dump(vec, cached_vec_name)
    print("Finished training!")
else:
    clf = load(cached_model_name)
    vec = load(cached_vec_name)


class OutputFormat(str, Enum):
    HTML = "html"
    JSON = "json"


class Input(BaseModel):
    text: str = Field(
        ...,
        title="Text Input",
        description="The input text that should be classified and explained",
    )
    number_of_output_labels: int = 5
    output_format: OutputFormat = Field(
        OutputFormat.HTML, description="Select the output format of the returned value."
    )


class Output(BaseModel):
    explanation: Union[str, Dict]

    def render_output_ui(self, streamlit, input) -> None:  # type: ignore
        # Replace line breaks (\n) as linebreaks between HTML tags, for example
        # <th>foo</th>

        # <th>bar</th>

        # instead of

        # <th>foo</th>
        # <th>bar</th>

        # lead to an error in the streamlit HTML parsing.
        if type(self.explanation) == str and input.output_format == OutputFormat.HTML:
            streamlit.write(self.explanation.replace("\n", ""), unsafe_allow_html=True)
        else:
            streamlit.write(self.explanation)


def explain(input: Input) -> Output:
    """Classifies the input text (based on a sample news corpus) and returns an explanation using eli5. Try for example `Opyrator example to compute the classification`."""

    explanation = eli5.explain_prediction(
        clf,
        input.text,
        vec=vec,
        top=10,
        top_targets=input.number_of_output_labels,
        target_names=twenty_test.target_names,
    )

    if input.output_format == OutputFormat.JSON:
        explanation = eli5.formatters.as_dict.format_as_dict(explanation)
    elif input.output_format == OutputFormat.HTML:
        explanation = explanation._repr_html_()

    return Output(explanation=explanation)
