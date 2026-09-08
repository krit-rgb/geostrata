# 3D ULPIN Contract Status

## Source-defined contracts

The project reference defines the following handoff concepts:

1. Site Data Package
2. Classified Segment Package
3. Validated Polyhedron Package
4. Discrepancy Report
5. Review Decision
6. LADM record
7. ULPIN format
8. REST API contract

## Current implementation status

| Contract | Implementation | Status |
|---|---|---|
| Site Data Package | contracts/site-data-package.json | Draft |
| Classified Segment Package | contracts/classified-segment-package.json | Draft |
| Validated Polyhedron Package | contracts/validated-polyhedron-package.json | Draft |
| Discrepancy Report | contracts/discrepancy-report.json | Draft |
| Review Decision | contracts/review-decision.json | Draft |
| LADM Record | contracts/ladm-record.json | Pending team confirmation |
| ULPIN Format | contracts/ulpin-format.json | Pending team confirmation |
| REST API | contracts/api/openapi.yaml | Draft |

## Important unresolved decisions

### LADM

The source requires a LADM-compliant record, but does not specify the
exact LADM classes, attributes, or mapping.

Member 4/database owner must confirm the final mapping.

### ULPIN

The source defines the conceptual structure:

- Parent ULPIN: immutable 14-digit identifier based on surface-footprint centroid.
- Child ULPIN: identifies a floor/unit using a vertical locator and a hash
  derived from the exact 3D volume.

The exact encoding, hashing algorithm, and final string construction
are not specified in the source documents.

These must be agreed before implementing ULPIN generation.

### Classified segment geometry

The source states that points/regions receive AI labels and confidence
values, but does not specify the exact JSON representation of those
points/regions.

This must be confirmed with Member 2.

### Validated polyhedron geometry

The source requires exact closed 3D solids, but does not specify whether
the JSON contract should contain vertices/faces directly or reference
an external mesh representation.

This must be confirmed with Member 3.