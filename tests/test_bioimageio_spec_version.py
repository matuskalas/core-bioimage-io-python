import json
import subprocess
import sys

import pytest
from packaging.version import Version


@pytest.mark.skipif(sys.version_info < (3, 8), reason="requires python 3.8")
@pytest.mark.skipif(pytest.mamba_cmd is None, reason="requires mamba")
def test_bioimageio_spec_version():
    from importlib.metadata import metadata

    # get latest released bioimageio.spec version
    mamba_repoquery = subprocess.run(
        f"{pytest.mamba_cmd} repoquery search -c conda-forge --json bioimageio.spec".split(" "),
        encoding="utf-8",
        capture_output=True,
        check=True,
    )
    full_out = mamba_repoquery.stdout  # full output includes mamba banner
    search = json.loads(full_out[full_out.find("{") :])  # json output starts at '{'
    rmaj, rmin, rpatch, *_ = search["result"]["pkgs"][0]["version"].split(".")
    released = Version(f"{rmaj}.{rmin}.{rpatch}")

    # get currently pinned bioimageio.spec version
    meta = metadata("bioimageio.core")
    req = meta["Requires-Dist"]
    assert req.startswith("bioimageio.spec (==")
    pmaj, pmin, ppatch, *asterisk_and_rest = req[len("bioimageio.spec (==") :].split(".")
    assert asterisk_and_rest[0].startswith(
        "*"
    ), "bioimageio.spec version should be pinned down to patch, e.g. '0.4.9.*'"
    pinned = Version(f"{pmaj}.{pmin}.{ppatch}")

    assert pinned >= released, "bioimageio.spec pinned to an old version!"
