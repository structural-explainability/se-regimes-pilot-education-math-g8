# se-regimes stress report

**Regimes:** 9 **Families:** 3 **Cases:** 6 **Passed:** 6 **Failed:** 0

## Rule matrix

_Declared responses from the regime registry (se-regimes): theory-level assertions, not empirically validated._
_Populated from registry regardless of case coverage._

| regime  | BF  | decomposition | nor_reorg |
| ------- | --- | ------------- | --------- |
| `OBL`   | INH | INH           | INH       |
| `OCC`   | INH | INH           | INH       |
| `REC`   | INH | INH           | INH       |
| `ENR-L` | PRS | INH           | INH       |
| `ENR-I` | BRK | INH           | INH       |
| `CTX-E` | INH | PRS           | INH       |
| `CTX-S` | INH | BRK           | INH       |
| `NOR-C` | INH | INH           | PRS       |
| `NOR-S` | INH | INH           | BRK       |

Legend for rule matrix:

- PRS = Preserves identity. The transformation does not change identity under the regime.
- BRK = Breaks identity. The transformation produces a distinct identity under the regime.
- INH = Inherits identity.
  The transformation does not operate on the identity criteria tracked by the regime;
  identity is carried forward without a PRS/BRK determination at this layer.

## Case coverage matrix

_Which regime x family pairs have at least one stress-test case._

| regime  | BF  | decomposition | nor_reorg |
| ------- | --- | ------------- | --------- |
| `OBL`   | -   | -             | -         |
| `OCC`   | -   | -             | -         |
| `REC`   | -   | -             | -         |
| `ENR-L` | ✓   | -             | -         |
| `ENR-I` | ✓   | -             | -         |
| `CTX-E` | -   | ✓             | -         |
| `CTX-S` | -   | ✓             | -         |
| `NOR-C` | -   | -             | ✓         |
| `NOR-S` | -   | -             | ✓         |

## All cases

| id                      | domain              | regime  | expected            | source | result |
| ----------------------- | ------------------- | ------- | ------------------- | ------ | ------ |
| `edu-math-g8-enr-l-001` | `education.math.g8` | `ENR-L` | `BF:PRS`            | -      | ✓      |
| `edu-math-g8-enr-i-001` | `education.math.g8` | `ENR-I` | `BF:BRK`            | -      | ✓      |
| `edu-math-g8-ctx-e-001` | `education.math.g8` | `CTX-E` | `decomposition:PRS` | -      | ✓      |
| `edu-math-g8-ctx-s-001` | `education.math.g8` | `CTX-S` | `decomposition:BRK` | -      | ✓      |
| `edu-math-g8-nor-c-001` | `education.math.g8` | `NOR-C` | `nor_reorg:PRS`     | -      | ✓      |
| `edu-math-g8-nor-s-001` | `education.math.g8` | `NOR-S` | `nor_reorg:BRK`     | -      | ✓      |
