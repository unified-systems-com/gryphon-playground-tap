"""A runner sibling found while pinning bare-dimension equality snapshots."""

from tap_plugin.gryphon_playground.gridkin.runner import redact_registry_scan


def test_registry_redaction_preserves_nonliteral_json_parameters():
    capture = (
        'SELECT id FROM tap_entity WHERE "tap_entity"."entity_type" IN (%s, %s) '
        'AND ("tap_entity"."dimensions" -> %s) = %s\n'
        "-- params: ['batch', 'search', 'tap.playground', Jsonb('gridkin')]"
    )
    redacted = redact_registry_scan(capture, frozenset({"batch", "search"}))
    assert "<entity-type-registry>" in redacted
    assert "Jsonb('gridkin')" in redacted
