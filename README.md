# Vector Lessons (FreeCodeCamp Companion)

This repo expands FreeCodeCamp’s introductory vector lesson into a narrated walkthrough (`vectors_edu.py`) and a lean sandbox (`vectors_space.py`). Start here if you want to match FCC’s pacing while getting extra context on higher-dimensional vectors, operator overloading, and memory tricks in Python.

## Highlights
- Explains how `vectors_edu.py` extends FCC’s “Intro to Vectors” challenge with commentary, extra dimensions, and memory tips, while `vectors_space.py` sticks to the essentials for quick experiments.
- Shows the FCC progression: foundational `R2Vector`, inheritance into `R3Vector`, `R4Vector`, `R5Vector` with `__slots__`, and `R6Vector` utilities—the commentary mirrors how FCC scaffolds new ideas.
- Clarifies how to run each script, what to expect, and how to use the verbose printouts as checkpoints while you learn.
- Suggests FCC-friendly practice tasks: reproduce tests, plug in your own values, add new vector types, write unit tests, or drop the walkthrough into a notebook.
- Links directly to FCC material and the Python docs so you can keep exploring.
- Catalogs every method (norms, string helpers, arithmetic overloads, attribute inspectors) so you can see exactly which Python data-model tools each lesson section reinforces.

## Why This Exists
- Mirror the structure of FCC’s vector challenges while removing the “black box” feeling.
- Give you runnable snippets that match the way FCC introduces new ideas (start in 2D, then generalize).
- Encourage you to explore beyond FCC by showing how to add dimensions, overload operators, and inspect objects.

## Files at a Glance
| File | Purpose |
| --- | --- |
| `vectors_edu.py` | The narrated walkthrough. Starts with the FCC-style `R2Vector` and layers in `R3Vector`, `R4Vector`, `R5Vector` (with `__slots__`), and `R6Vector`. Every method is explained: norms, `__str__`, `__repr__`, addition, subtraction, scalar and dot products. |
| `vectors_space.py` | The “just the vectors” version. Keeps the FCC feel—keyword-only constructors, `norm` property, and operator overloads—without the extended commentary so you can tweak it freely. |

## Run the Examples
```bash
python vectors_edu.py   # guided tour with prints and explanations
python vectors_space.py # concise demo of the same operations
```
Python 3.8+ is enough; everything stays in the standard library.

Running `vectors_edu.py` prints checkpoints that align with FCC’s lesson beats—norm calculations, readable string output, inheritance demos, slot-based memory savings, and an attribute inspection via `R6Vector.show_attr`.

## Learning Path (Follows FCC Flow)
1. Start with `R2Vector` to see the exact logic that FCC outlines (component storage, Euclidean norm).
2. Step into `__str__` and `__repr__` to understand why FCC uses friendly string output in their tests.
3. Watch `R3Vector` and `R4Vector` inherit from `R2Vector`—the same “build on earlier lessons” pattern FCC uses.
4. Hit `R5Vector` to see why `__slots__` matters when FCC talks about memory or performance trade-offs.
5. Use `R6Vector.show_attr` to learn how to introspect objects even when `__dict__` is unavailable—handy for debugging your FCC submissions.

## Advanced Techniques Inside
- **Keyword-only constructors** (`*` in `__init__`) mirror FCC’s style and force readable, explicit arguments as vectors gain dimensions.
- **`vars()` and attribute dictionaries** let a single norm implementation scale gracefully from 2D to 6D, underscoring how Python stores instance state.
- **Operator overloading** (`__add__`, `__sub__`, `__mul__`) demonstrates both scalar multiplication and dot products, plus the importance of returning `NotImplemented`.
- **`__slots__` vs `__dict__`** in `R5Vector`/`R6Vector` show tangible memory savings and why some attributes disappear from `__dict__`.
- **Static utility methods** such as `R6Vector.show_attr` combine `__dict__` and slotted attributes so you can inspect any instance, even when slots hide the usual dictionary.
- **Readable representations** (`__str__`, `__repr__`, f-string `!r` usage) illustrate why FCC tests rely on human-friendly output and how to supply it.
- **Lean reimplementation in `vectors_space.py`** swaps the narrated prints for a property-based `norm`, giving you a quick playground for experimenting with the overloaded operators.

## Method Reference
| Class & Method | Concept Reinforced |
| --- | --- |
| `R2Vector.__init__` | Keyword-only arguments, attribute setup |
| `R2Vector.norm()` | Dimension-agnostic Euclidean norm via `vars()` |
| `R2Vector.__str__`, `__repr__` | Human-friendly vs. constructor-style output |
| `R3Vector.__init__` | `super()` and extending base classes |
| `R4Vector.__init__` | Reusing parent setup while adding new axes |
| `R5Vector.__slots__` | Memory optimization, slot-only storage |
| `R5Vector.__add__`, `__sub__`, `__mul__` | `NotImplemented`, scalar multiply, dot product |
| `R6Vector.show_attr()` | Static helpers for slotted introspection |
| `vectors_space.R2Vector.norm` (property) | Property decorators and derived values |

## Practice Ideas (FCC-Friendly)
1. Rewrite the FreeCodeCamp vector tests using these classes, verifying that your `norm`, `__str__`, and arithmetic match expectation.
2. Create an `R7Vector` or `ComplexVector` that reuses the helper logic—notice how little code changes.
3. Extend `__mul__` with cross products in 3D, then compare with FCC’s optional challenges.
4. Drop the code into a Jupyter notebook, cell-by-cell, to annotate your own notes next to the console output.
5. Write unit tests (e.g., `unittest` or `pytest`) that mimic FCC’s test runner, then adjust the classes until the tests give you green bars.

## Keep Exploring
- FreeCodeCamp curriculum: search “Scientific Computing with Python – Vectors” for the original challenge.
- Python docs: [Data model](https://docs.python.org/3/reference/datamodel.html) (dunder methods) and [Classes](https://docs.python.org/3/tutorial/classes.html#inheritance).
- Optional deep dive: *Fluent Python* (special methods & operator overloading).

Use the narrated file as your FCC companion while learning the concepts, then graduate to the lean version when you’re ready to tinker or submit solutions.
