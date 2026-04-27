# se-regimes stress report

**Regimes:** 9 **Families:** 3 **Cases:** 27 **Passed:** 27 **Failed:** 0

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
- INH = No split pressure established.
  The transformation does not operate on the identity criteria tracked by the regime;
  no PRS/BRK determination is made at this layer.

## Case coverage matrix

_Which regime x family pairs have at least one stress-test case._

| regime  | BF  | decomposition | nor_reorg |
| ------- | --- | ------------- | --------- |
| `OBL`   | ✓   | ✓             | ✓         |
| `OCC`   | ✓   | ✓             | ✓         |
| `REC`   | ✓   | ✓             | ✓         |
| `ENR-L` | ✓   | ✓             | ✓         |
| `ENR-I` | ✓   | ✓             | ✓         |
| `CTX-E` | ✓   | ✓             | ✓         |
| `CTX-S` | ✓   | ✓             | ✓         |
| `NOR-C` | ✓   | ✓             | ✓         |
| `NOR-S` | ✓   | ✓             | ✓         |

## All cases

| id                             | domain              | regime  | expected            | source | result |
| ------------------------------ | ------------------- | ------- | ------------------- | ------ | ------ |
| `edu-math-g8-enr-l-001`        | `education.math.g8` | `ENR-L` | `BF:PRS`            | -      | ✓      |
| `edu-math-g8-enr-i-001`        | `education.math.g8` | `ENR-I` | `BF:BRK`            | -      | ✓      |
| `edu-math-g8-ctx-e-001`        | `education.math.g8` | `CTX-E` | `decomposition:PRS` | -      | ✓      |
| `edu-math-g8-ctx-s-001`        | `education.math.g8` | `CTX-S` | `decomposition:BRK` | -      | ✓      |
| `edu-math-g8-nor-c-001`        | `education.math.g8` | `NOR-C` | `nor_reorg:PRS`     | -      | ✓      |
| `edu-math-g8-nor-s-001`        | `education.math.g8` | `NOR-S` | `nor_reorg:BRK`     | -      | ✓      |
| `edu-math-g8-obl-bf-001`       | `education.math.g8` | `OBL`   | `BF:INH`            | -      | ✓      |
| `edu-math-g8-obl-decomp-001`   | `education.math.g8` | `OBL`   | `decomposition:INH` | -      | ✓      |
| `edu-math-g8-obl-nor-001`      | `education.math.g8` | `OBL`   | `nor_reorg:INH`     | -      | ✓      |
| `edu-math-g8-occ-bf-001`       | `education.math.g8` | `OCC`   | `BF:INH`            | -      | ✓      |
| `edu-math-g8-occ-decomp-001`   | `education.math.g8` | `OCC`   | `decomposition:INH` | -      | ✓      |
| `edu-math-g8-occ-nor-001`      | `education.math.g8` | `OCC`   | `nor_reorg:INH`     | -      | ✓      |
| `edu-math-g8-rec-bf-001`       | `education.math.g8` | `REC`   | `BF:INH`            | -      | ✓      |
| `edu-math-g8-rec-decomp-001`   | `education.math.g8` | `REC`   | `decomposition:INH` | -      | ✓      |
| `edu-math-g8-rec-nor-001`      | `education.math.g8` | `REC`   | `nor_reorg:INH`     | -      | ✓      |
| `edu-math-g8-enr-l-decomp-neg` | `education.math.g8` | `ENR-L` | `decomposition:INH` | -      | ✓      |
| `edu-math-g8-enr-l-nor-neg`    | `education.math.g8` | `ENR-L` | `nor_reorg:INH`     | -      | ✓      |
| `edu-math-g8-enr-i-decomp-neg` | `education.math.g8` | `ENR-I` | `decomposition:INH` | -      | ✓      |
| `edu-math-g8-enr-i-nor-neg`    | `education.math.g8` | `ENR-I` | `nor_reorg:INH`     | -      | ✓      |
| `edu-math-g8-ctx-e-bf-neg`     | `education.math.g8` | `CTX-E` | `BF:INH`            | -      | ✓      |
| `edu-math-g8-ctx-e-nor-neg`    | `education.math.g8` | `CTX-E` | `nor_reorg:INH`     | -      | ✓      |
| `edu-math-g8-ctx-s-bf-neg`     | `education.math.g8` | `CTX-S` | `BF:INH`            | -      | ✓      |
| `edu-math-g8-ctx-s-nor-neg`    | `education.math.g8` | `CTX-S` | `nor_reorg:INH`     | -      | ✓      |
| `edu-math-g8-nor-c-bf-neg`     | `education.math.g8` | `NOR-C` | `BF:INH`            | -      | ✓      |
| `edu-math-g8-nor-c-decomp-neg` | `education.math.g8` | `NOR-C` | `decomposition:INH` | -      | ✓      |
| `edu-math-g8-nor-s-bf-neg`     | `education.math.g8` | `NOR-S` | `BF:INH`            | -      | ✓      |
| `edu-math-g8-nor-s-decomp-neg` | `education.math.g8` | `NOR-S` | `decomposition:INH` | -      | ✓      |
