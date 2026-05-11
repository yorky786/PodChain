# PodChain

**PodChain** is a controlled workflow system built from small execution units called **pods**.

🏗️ **Featured:** 
- [The PodChain Factory Model](docs/FACTORY_MODEL.md) — *Industrial-grade workflow architecture.*
- [Anatomy of a Pod](docs/ANATOMY.md) — *Detailed technical blueprint of the execution node.*
- [Strategic Implementation](docs/USE_CASES.md) — *When to use PodChain (and when not to).*

> **Note:** PodChain does not replace AI. It controls AI by placing work inside fixed pods, artifact handoffs, validation gates, and receipts.

## Core Principle
**No pass, no ignition.**

Each pod performs one job, creates an artifact, writes a receipt, and only allows the next pod to run if validation passes.

## Features
- **Isolation:** Each pod is an independent unit of execution.
- **Verification:** Mandatory validation gates before any state change.
- **Auditability:** Immutable receipts generated for every execution.
- **Control:** Fixed handoffs between execution units.

## Quick Start
```bash
python -m podchain.runner run pod website_builder --input examples/website_builder/input.yaml
```

## Structure
- `podchain/`: Core engine.
- `templates/`: Blueprints for pods, inputs, and receipts.
- `docs/`: 
  - [The Concept](docs/CONCEPT.md): Why PodChain exists.
  - [The Pod](docs/THE_POD.md): The "No Brain" philosophy (Contract, Worker, Gatekeeper).
  - [Architecture](docs/ARCHITECTURE.md): System layers and execution flow.
- `examples/`: Reference implementations.

## License
Apache License 2.0

---
Created by **Amit Bhatia**.
