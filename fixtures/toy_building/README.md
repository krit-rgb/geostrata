# Toy Building Fixture

This fixture provides deterministic test data for the 3D ULPIN pipeline.

## Cases

### clean

`clean/building.json`

Represents a simple two-floor building without a deliberate discrepancy.

### discrepancy

`discrepancy/building.json`

Contains an official footprint and an intentionally different
observed footprint.

The discrepancy case is intended to exercise:

1. Geometry reconstruction
2. Discrepancy detection
3. Review queue creation
4. Human review decision
5. Final record handling

## Important

This is a synthetic development fixture.

It does not represent a real cadastral record and its CRS,
vertical datum, geometry tolerances, and identifiers are placeholders
for integration testing.