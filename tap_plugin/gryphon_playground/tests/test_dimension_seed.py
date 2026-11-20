"""The plugin's dimension seed declares every key the corpus stamps that nobody else declares.

Core refuses an undeclared dimension key and never mints one (aws-build Q48a), so a fixture or
scenario that stamps a key with no Dimension node fails to import. tap.playground belongs to
grid_fixtures and tap.graph to core; this seed declares the rest. Pure JSON: no database.
"""

from __future__ import annotations

import json
import tomllib
from pathlib import Path
from typing import Any

PLUGIN_ROOT = Path(__file__).resolve().parent.parent
SEED = PLUGIN_ROOT / "grift" / "dimension.grift.json"
# Keys other packages own: grid_fixtures declares tap.playground, core declares tap.graph and tap.meta.
OWNED_ELSEWHERE = {"tap.playground", "tap.graph", "tap.meta"}
ZONE_ID = "01a1d37f-27ca-73b0-a4c3-77493aee2e19"


def _stamped_keys() -> set[str]:
    keys: set[str] = set()

    def walk(obj: Any) -> None:
        if isinstance(obj, dict):
            for name, value in obj.items():
                if name == "dimensions" and isinstance(value, dict):
                    keys.update(value)
                walk(value)
        elif isinstance(obj, list):
            for item in obj:
                walk(item)

    for path in [*PLUGIN_ROOT.glob("fixtures/*.json"), *PLUGIN_ROOT.glob("scenarios/*.json")]:
        walk(json.loads(path.read_text(encoding="utf-8")))
    return keys


def _declared() -> dict[str, str]:
    document = json.loads(SEED.read_text(encoding="utf-8"))
    return {
        node["entity"]["name"]: node["entity"]["entity_id"]
        for batch in document["batches"]
        for node in batch["nodes"]
        if node["entity"]["entity_type"] == "dimension"
    }


def test_every_stamped_key_is_declared_here_or_by_its_owner() -> None:
    missing = _stamped_keys() - OWNED_ELSEWHERE - set(_declared())
    assert not missing, f"undeclared dimension keys in the corpus: {sorted(missing)}"


def test_the_seed_declares_nothing_another_package_owns() -> None:
    assert not set(_declared()) & OWNED_ELSEWHERE


def test_zone_keeps_its_fixed_id() -> None:
    assert _declared()["zone"] == ZONE_ID


def test_the_seed_is_declared_in_the_manifest() -> None:
    manifest = tomllib.loads((PLUGIN_ROOT / "tap-plugin.toml").read_text(encoding="utf-8"))
    assert manifest["grift"]["dimension"] == "grift/dimension.grift.json"


def test_every_batch_carries_the_edges_key_the_schema_requires() -> None:
    document = json.loads(SEED.read_text(encoding="utf-8"))
    assert all("edges" in batch for batch in document["batches"])
