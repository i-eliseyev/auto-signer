import dataclasses

from PIL.PngImagePlugin import PngImageFile


@dataclasses.dataclass
class SignData:
    image: PngImageFile
    original_filename: str