from enum import Enum
from tempfile import NamedTemporaryFile

import fasttext
from pydantic import BaseModel, Field

from opyrator.components.types import FileContent


class Model(str, Enum):
    SKIPGRAM = "skipgram"
    CBOW = "cbow"


class LossFunction(str, Enum):
    NS = "ns"
    HS = "hs"
    SOFTMAX = "softmax"
    OVA = "ova"


class WordVectorTrainingInput(BaseModel):
    text: str = Field(
        ...,
        description="The text to use for training the word vector model.",
        min_length=10,
        max_length=5000,
    )
    model: Model = Field(
        Model.SKIPGRAM,
        title="Select Model Type",
        description="Model for computing word representations",
    )
    learning_rate: float = Field(0.05, gt=0.0, le=1)
    dimension: int = Field(50, ge=10, le=100, description="Size of word vectors.")
    epoch: int = Field(5, ge=1, le=20)
    min_count: int = Field(1, ge=1, description="Minimal number of word occurrences.")
    loss_function: LossFunction = Field(LossFunction.NS, title="Loss Function")

    # def render_output_ui(self, streamlit):
    #     import umap
    #     import umap.plot
    #     from sklearn.datasets import load_digits

    #     digits = load_digits()

    #     mapper = umap.UMAP().fit(digits.data)
    #     p = umap.plot.interactive(mapper, labels=digits.target)
    #     streamlit.bokeh_chart(p, use_container_width=True)


class WordVectorTrainingOutput(BaseModel):
    vector_file: FileContent

    def render_output_ui(self, streamlit) -> None:  # type: ignore
        streamlit.markdown(
            f'<a href="data:application/octet-stream;base64,{self.vector_file}" download="model.vec"><input type="button" value="Download Trained Vectors"></a>',
            unsafe_allow_html=True,
        )


def train_word_vectors(input: WordVectorTrainingInput) -> WordVectorTrainingOutput:
    """Trains word vectors via [FastText](https://fasttext.cc) based on a provided text."""

    with NamedTemporaryFile(suffix=".txt", mode="w", encoding="utf-8") as f:
        f.write(input.text)
        f.seek(0)

        model = fasttext.train_unsupervised(
            f.name,
            model=input.model.value,
            lr=input.learning_rate,
            dim=input.dimension,
            epoch=input.epoch,
            minCount=input.min_count,
            loss=input.loss_function,
        )

        with NamedTemporaryFile(suffix=".vec", mode="w+b") as vec_file:
            words = model.get_words()
            for word in words:
                vec_file.write(
                    str.encode(
                        word
                        + "".join(" " + str(vi) for vi in model.get_word_vector(word))
                        + "\n"
                    )
                )
            vec_file.seek(0)
            return WordVectorTrainingOutput(vector_file=vec_file.read())
