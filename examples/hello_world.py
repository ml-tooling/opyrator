import time

from pydantic import BaseModel


class Input(BaseModel):
    message: str
    wait: int


class Output(BaseModel):
    message: str


def hello_world(input: Input) -> Output:
    """Echo the provided `message` after a configurable `wait` time."""
    time.sleep(input.wait)
    return Output(message=input.message)
