- Author: John Alcher Doloiras <johnalcherdoloiras@gmail.com>
- Changelog:
    - 01/16/2023 - ADR created and accepted

---

# Dev Tooling

## Status

Accepted on 01/16/2023

## Context

Enforcing a consistent code style is a must for modern projects that is expected to be worked on by multiple people. On
the same vein, having a static typing analysis tool could offset a lot of the "disadvantages" of a dynamic language like
Python.

## Decision

I've decided to use the [pre-commit framework](https://github.com/pre-commit) and [mypy](https://mypy-lang.org/) to
enforce style consistency and static analysis, respectively. I've been a long time user of pre-commit and have used it
for all of my projects that I know will pass the prototyping phase. I've used type hints for quite some time as well,
but this would be the firs time I'll enforce it via a mypy pre-commit hook.

## Consequences

Given that this is the first time that I'll be using the mypy pre-commit hook, I could experience a bit of a hiccup
along the way.