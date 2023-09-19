import json

from bioimageio.core._internal.utils import files
from bioimageio.core._io import load_description as load_description
from bioimageio.core._io import load_description_and_validate as load_description_and_validate
from bioimageio.core._io import read_description as read_description
from bioimageio.core._io import read_description_and_validate as read_description_and_validate
from bioimageio.core._io import resolve_source as resolve_source
from bioimageio.core._io import write_description as write_description
from bioimageio.core._io import write_package as write_package

with files("bioimageio.core").joinpath("VERSION").open("r", encoding="utf-8") as f:
    __version__: str = json.load(f)["version"]
    assert isinstance(__version__, str)

#  __version__ = json.loads((pathlib.Path(__file__).parent / "VERSION").read_text())["version"]
# from .prediction import predict_image, predict_images, predict_with_padding, predict_with_tiling
# from .prediction_pipeline import create_prediction_pipeline
# from .resource_io import (
#     export_resource_package,
#     load_raw_resource_description,
#     load_resource_description,
#     save_raw_resource_description,
#     serialize_raw_resource_description,
# )
# from .resource_tests import check_input_shape, check_output_shape, test_resource

# __all__ = [
#     "check_input_shape",
#     "check_output_shape",
#     "create_prediction_pipeline",
#     "export_resource_package",
#     "load_raw_resource_description",
#     "load_resource_description",
#     "predict_image",
#     "predict_images",
#     "predict_with_padding",
#     "predict_with_tiling",
#     "save_raw_resource_description",
#     "serialize_raw_resource_description",
#     "test_resource",
