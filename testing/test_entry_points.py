# mypy: allow-untyped-defs
from __future__ import annotations

import importlib.metadata


def test_pytest_entry_points_are_identical():
    dist = importlib.metadata.distribution("ok")
    entry_map = {ep.name: ep for ep in dist.entry_points}
    assert entry_map["ok"].value == entry_map["pytest"].value
