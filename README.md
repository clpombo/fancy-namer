# FancyNamer

Generate memorable, human-readable random names for tools, services, agents, experiments, containers, and software systems.

Examples:

- `academic_ability_of_Acropolis`
- `abrasive_Algorithm_of_Aegean`
- `able_scheduler_of_Adriatic`

---

# Features

- Human-readable random name generation
- Deterministic generation using seeds
- Multiple naming modes
- Tool-specific naming
- Lightweight and dependency-free
- Typed Python API
- Extensible architecture

---

# Installation

## From PyPI

```bash
pip install fancy-namer
```

## From source

```bash
git clone https://github.com/<your-username>/fancy-namer.git

cd fancy-namer

pip install -e .
```

---

# Quick Start

## Standard names

```python
from fancy_namer import FancyNamer

namer = FancyNamer()

print(namer.generate_name())
```

Example output:

```text
able_achievement_of_Aconcagua
```

---

## Computer science names

```python
from fancy_namer import FancyNamer

namer = FancyNamer(
    name_type=FancyNamer.NameType.COMPUTER_SCIENCE
)

print(namer.generate_name())
```

Example output:

```text
abrasive_Algorithm_of_Aegean
```

---

## Tool names

```python
from fancy_namer import FancyNamer

namer = FancyNamer(
    name_type=FancyNamer.NameType.TOOL,
    tool_name="scheduler"
)

print(namer.generate_name())
```

Example output:

```text
academic_scheduler_of_Adriatic
```

---

# Deterministic Generation

Providing a seed guarantees reproducible output.

```python
from fancy_namer import FancyNamer

namer = FancyNamer(random_seed=42)

print(namer.generate_name())
```

Running this multiple times produces the same sequence.

---

# API

## FancyNamer

### Constructor

```python
FancyNamer(
    name_type=FancyNamer.NameType.STANDARD,
    tool_name=None,
    random_seed=None,
)
```

### Parameters

| Parameter | Type | Description |
|---|---|---|
| `name_type` | `FancyNamer.NameType` | Naming strategy |
| `tool_name` | `str \| None` | Tool name used when `TOOL` mode is selected |
| `random_seed` | `int \| None` | Seed for deterministic generation |

---

# Name Types

| Name Type | Description |
|---|---|
| `STANDARD` | Uses general nouns |
| `COMPUTER_SCIENCE` | Uses computer science terminology |
| `TOOL` | Uses a user-provided tool name |

---

# Example Outputs

## STANDARD

```text
abandoned_actor_of_Adriatic
acceptable_acorn_of_Aegean
academic_account_of_Acropolis
```

## COMPUTER_SCIENCE

```text
able_API_of_AlabasterBay
abrasive_Algorithm_of_Aconcagua
academic_Authentication_of_Aegean
```

## TOOL

```text
acceptable_scheduler_of_Adriatic
academic_compiler_of_Acropolis
abrasive_router_of_AlabasterBay
```

---

# Project Structure

```text
fancy-namer/
├── README.md
├── pyproject.toml
├── LICENSE
├── fancy_namer/
│    ├── __init__.py
│    ├── namer.py
│    ├── enums.py
│    ├── exceptions.py
│    └── data/
└── tests/
```

---

# Development

## Install development dependencies

```bash
pip install -e .[dev]
```

---

## Run tests

```bash
pytest
```

---

## Lint

```bash
ruff check .
```

---

## Format

```bash
ruff format .
```

---

# Future Roadmap

Planned features include:

- Guaranteed uniqueness mode
- Template-based name generation
- Additional naming categories
- CLI support
- Configurable vocabularies
- Kubernetes-safe slugs
- Plugin architecture
- Internationalization support

---

# Contributing

Contributions, ideas, and vocabulary expansions are welcome.

Typical contributions include:

- New adjective/noun sets
- Additional categories
- Performance improvements
- CLI enhancements
- Documentation updates
- Test coverage improvements

---

# License

MIT License

---

# Motivation

Many generated identifiers are difficult for humans to read or remember.

FancyNamer focuses on generating identifiers that are:

- readable
- memorable
- deterministic when needed
- suitable for infrastructure and developer tooling

This makes generated names easier to use in logs, dashboards, debugging sessions, containers, experiments, and distributed systems.