from __future__ import annotations

import importlib.metadata

import snakesay_alv as m


def test_version():
    assert importlib.metadata.version("snakesay_alv") == m.__version__
