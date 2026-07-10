# The Multi-Model Actor-Critic Era

Exploring the ~2022-2023 era of Classic RLHF and Proximal Policy Optimization.

## Diagram

```mermaid
flowchart TD
    A[Prompt] --> B[Base Model]
    A --> C[Reward Model]
    B --> D[Output]
    D --> C
    C -->|Reward| B
```

[Back to README](README.md)
