import os

pages = [
    ("unaligned-generative-baseline.md", "The Unaligned Generative Baseline Era", "A detailed look into the pre-2022 era where models were optimized purely on next-token prediction without alignment.", "flowchart TD\n    A[Raw Web Data] --> B[Next Token Prediction]\n    B --> C[Unaligned Output]"),
    ("multi-model-actor-critic.md", "The Multi-Model Actor-Critic Era", "Exploring the ~2022-2023 era of Classic RLHF and Proximal Policy Optimization.", "flowchart TD\n    A[Prompt] --> B[Base Model]\n    A --> C[Reward Model]\n    B --> D[Output]\n    D --> C\n    C -->|Reward| B"),
    ("direct-mathematical-reparameterization.md", "The Direct Mathematical Reparameterization Revolution", "Deep dive into Direct Preference Optimization (DPO).", "flowchart LR\n    A[Chosen/Rejected Data] --> B[Implicit Reward via Policy]\n    B --> C[Binary Cross Entropy Loss]\n    C --> D[Aligned Model]"),
    ("verifiable-on-policy-reasoning.md", "The Verifiable On-Policy Reasoning Era", "Analysis of modern System 2 hidden thinking token traces.", "flowchart TD\n    A[Prompt] --> B[Hidden Reasoning Trace]\n    B --> C[Self-Correction]\n    C --> D[Final Verified Output]"),
    ("standard-dpo.md", "Standard DPO (Bradley-Terry Formulation)", "Detailed mechanics of the Bradley-Terry Formulation in DPO.", "flowchart LR\n    A[Policy Logits] --> B[Odds Ratio]\n    B --> C[DPO Loss]"),
    ("kahneman-tversky-optimization.md", "Kahneman-Tversky Optimization (KTO)", "Applying Prospect Theory to model alignment.", "flowchart TD\n    A[Unpaired Data] --> B[Desirable/Undesirable Tag]\n    B --> C[KTO Utility Mapping]\n    C --> D[Policy Update]"),
    ("odds-ratio-preference.md", "Odds Ratio Preference Optimization (ORPO)", "Unified loss calculation without a reference model.", "flowchart TD\n    A[SFT Phase] --> B[Odds Ratio Tracking]\n    B --> C[Unified ORPO Loss]\n    C --> D[Aligned Weights without Ref Model]"),
    ("rlaif.md", "Reinforcement Learning from AI Feedback (RLAIF)", "Using an AI Constitution to tag preference data.", "flowchart TD\n    A[Model Outputs] --> B[AI Evaluator with Constitution]\n    B --> C[Preference Scores]\n    C --> D[Reward Model Training]"),
    ("symmetric-kl-divergence.md", "Symmetric KL-Divergence Constraints", "Anchoring token drift to prevent model collapse.", "flowchart LR\n    A[Active Policy] --> B[KL Divergence Penalty]\n    C[Frozen Reference Model] --> B\n    B --> D[Stable Optimization]"),
    ("fully-sharded-parameter-storage.md", "Fully Sharded Parameter Storage (FSDP)", "Slashing VRAM overheads via sharding.", "flowchart TD\n    A[Model Parameters] --> B[Shard across GPUs]\n    B --> C[All-Gather Primitive]\n    C --> D[Compute Forward/Backward]"),
    ("likelihood-saturation.md", "The Likelihood Saturation Wall", "Addressing capability collapse through Sparse Autoencoders.", "flowchart TD\n    A[Over-optimized Policy] --> B[Sparse Autoencoder]\n    B --> C[Feature Steering Vectors]\n    C --> D[Restored Capability]"),
    ("sparse-gradient-stagnation.md", "The Sparse Gradient Stagnation Wall", "Warm-start curriculum for compiler-verified environments.", "flowchart TD\n    A[Zero Gradient Stagnation] --> B[Supervised Warm-Start]\n    B --> C[Synthetic Reasoning Traces]\n    C --> D[Autonomous RL Loop]"),
    ("conversational-persona.md", "Conversational Persona Alignment", "Formatting and persona calibration for LLMs.", "flowchart LR\n    A[Raw Model] --> B[Formatting Preferences]\n    B --> C[Structured Output Generation]"),
    ("safety-guardrail-hardening.md", "Safety Guardrail Hardening", "Securing endpoints against jailbreaks.", "flowchart TD\n    A[Adversarial Prompts] --> B[Safety Tuned Model]\n    B --> C[Refusal / Safe Output]"),
    ("autonomous-software-development.md", "Autonomous Software Development", "Closed-loop search for coding models.", "flowchart TD\n    A[Coding Ticket] --> B[Generate Patch]\n    B --> C[Run Unit Tests]\n    C -->|Fail| B\n    C -->|Pass| D[Final Commit]")
]

for filename, title, desc, mermaid in pages:
    content = f"# {title}\n\n{desc}\n\n## Diagram\n\n```mermaid\n{mermaid}\n```\n\n[Back to README](README.md)\n"
    with open(filename, "w") as f:
        f.write(content)

print("Pages created.")
