import io

import numpy as np
from ISR.models import RDN
from PIL import Image
from pydantic import BaseModel, Field

from opyrator.components.types import FileContent

# Load pretrained model
rdn_model = RDN(weights="psnr-small")


class ImageSuperResolutionInput(BaseModel):
    image_file: FileContent = Field(..., mime_type="image/png")


class ImageSuperResolutionOutput(BaseModel):
    upscaled_image_file: FileContent = Field(
        ...,
        mime_type="image/png",
        description="Upscaled image via super resolution model.",
    )


def image_super_resolution(
    input: ImageSuperResolutionInput,
) -> ImageSuperResolutionOutput:
    """Upscale and improve the quality of low resolution images.

    This opyrator uses the [image-super-resolution](https://github.com/idealo/image-super-resolution) library.

    To try it out, you can use this [example image](https://github.com/idealo/image-super-resolution/raw/master/data/input/sample/baboon.png).
    """

    upscaled_image = Image.fromarray(
        rdn_model.predict(np.array(Image.open(io.BytesIO(input.image_file.as_bytes()))))
    )

    img_byte_array = io.BytesIO()
    upscaled_image.save(img_byte_array, format="PNG")
    return ImageSuperResolutionOutput(upscaled_image_file=img_byte_array.getvalue())
