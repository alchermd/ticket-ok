- Author: John Alcher Doloiras <johnalcherdoloiras@gmail.com>
- Changelog:
    - 01/16/2023 - ADR created and accepted

---

# Tech Stack

## Status

Accepted on 01/16/2023

## Context

**Ticket OK** is planned as a web application (see [v0.0.1 requirements](../requirements/v0.0.1.md)), thus a web
application tech stack is warranted for development to commence.

## Decision

As a heavy user of [Django](https://djangoproject.com/), I've decided to not reinvent the wheel and use the familiar
framework for **Ticket OK**. My experience, combined with
Django's [core strengths](https://www.djangoproject.com/start/overview/), makes it a good choice for a web-focused
application like **Ticket OK**. To keep things simple, I'll also use [PostgreSQL](https://www.postgresql.org/) as the
persistent storage given its popularity among the Django community. I'll start off
with [Django Templates](https://docs.djangoproject.com/en/4.1/topics/templates/) on the frontend and revisit in the
future if a JavaScript frontend for an SPA is warranted.

The current Django version is [4.1](https://docs.djangoproject.com/en/4.1/), and I'll try to keep the version updated as
the project progresses.

## Consequences

Committing to a framework this early could lead to difficulties in swapping to another framework in the future. But I
believe the chances of that happening is close to none.