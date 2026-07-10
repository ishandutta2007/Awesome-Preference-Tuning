# Autonomous Software Development

Closed-loop search for coding models.

## Diagram

```mermaid
flowchart TD
    A[Coding Ticket] --> B[Generate Patch]
    B --> C[Run Unit Tests]
    C -->|Fail| B
    C -->|Pass| D[Final Commit]
```

[Back to README](README.md)
