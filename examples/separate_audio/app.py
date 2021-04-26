import os
import subprocess
import sys
from tempfile import NamedTemporaryFile, TemporaryDirectory

from pydantic import BaseModel, Field

from opyrator.components.types import FileContent


class AudioSeparationInput(BaseModel):
    audio_file: FileContent = Field(..., mime_type="audio/mpeg")


class AudioSeparationOutput(BaseModel):
    vocals_file: FileContent = Field(
        ...,
        mime_type="audio/wav",
        description="The vocals (singing voice) extracted from the audio file.",
    )
    accompaniment_file: FileContent = Field(
        ...,
        mime_type="audio/wav",
        description="The non-voice parts etracted from the audio file.",
    )


def separate_audio(input: AudioSeparationInput) -> AudioSeparationOutput:
    """Separation of a music file to vocals (singing voice) and accompaniment.

    To try it out, you can use this example audio file: [audio_example.mp3](https://github.com/deezer/spleeter/raw/master/audio_example.mp3).
    """

    with NamedTemporaryFile(suffix=".mp3", mode="w+b") as audio_file:
        audio_file.write(input.audio_file.as_bytes())
        audio_file.seek(0)
        with TemporaryDirectory() as tmp_dir:

            subprocess.run(
                sys.executable
                + ' -m spleeter separate -p spleeter:2stems --filename_format "{instrument}.{codec}" -o '
                + f"{tmp_dir} {audio_file.name}",
                shell=True,
            )

            vocals_file = None

            with open(os.path.join(tmp_dir, "vocals.wav"), "rb") as f:
                vocals_file = f.read()

            accompaniment_file = None
            with open(os.path.join(tmp_dir, "accompaniment.wav"), "rb") as f:
                accompaniment_file = f.read()

            return AudioSeparationOutput(
                vocals_file=vocals_file, accompaniment_file=accompaniment_file
            )
