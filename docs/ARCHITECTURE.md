# PodChain Architecture

The system consists of three main layers:

1. **The Runner:** Responsible for loading pod definitions, executing logic, and managing the lifecycle.
2. **The Validator:** Responsible for checking artifacts against rules defined in the pod template.
3. **The Ledger:** A collection of receipts that form the audit trail (the "Chain").

## System Diagram

```mermaid
graph TD
    classDef runner fill:#2B2D42,stroke:#8D99AE,stroke-width:2px,color:#EDF2F4,border-radius:5px
    classDef pod fill:#8D99AE,stroke:#2B2D42,stroke-width:2px,color:#2B2D42,border-radius:5px
    classDef validator fill:#EF233C,stroke:#2B2D42,stroke-width:2px,color:#EDF2F4,border-radius:5px
    classDef artifact fill:#EDF2F4,stroke:#D90429,stroke-width:2px,color:#2B2D42,border-radius:5px
    classDef receipt fill:#2B2D42,stroke:#EF233C,stroke-width:2px,color:#EDF2F4,border-radius:5px

    Runner((PodChain<br/>Runner)):::runner

    subgraph The Chain
        P1[Pod 1]:::pod
        P2[Pod 2]:::pod
        P3[Pod 3]:::pod
    end

    Runner -->|1. Loads & Orchestrates| P1
    Runner -->|Loads| P2
    Runner -->|Loads| P3

    P1 -->|2. Generates| A1[Artifact 1]:::artifact
    A1 --> V1{Validator}:::validator
    V1 -->|3. PASS| R1[Receipt 1]:::receipt
    R1 -.->|4. Unlocks Ignition| P2

    P2 -->|Generates| A2[Artifact 2]:::artifact
    A2 --> V2{Validator}:::validator
    V2 -->|FAIL| E[Execution Blocked]:::validator
```

## Execution Flow
1. **Load:** Runner reads `pod.yaml` and `input.yaml`.
2. **Pre-flight:** Validator checks if dependencies (previous artifacts) are valid.
3. **Execute:** The pod's `run.py` is invoked.
4. **Post-flight:** Validator inspects the new artifact.
5. **Finalize:** Runner writes `receipt.json`.
