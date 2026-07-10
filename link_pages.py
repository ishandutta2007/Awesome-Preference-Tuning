import sys

path = r'C:\Users\ishan\Documents\Projects\Awesome-Preference-Tuning\README.md'
with open(path, 'r', encoding='utf8') as f:
    c = f.read()

replacements = [
    ('| **The Unaligned Generative Baseline Era (Pre-2022)** |', '| [**The Unaligned Generative Baseline Era (Pre-2022)**](unaligned-generative-baseline.md) |'),
    ('| **The Multi-Model Actor-Critic Era (Classic RLHF / PPO, ~2022–2023)** |', '| [**The Multi-Model Actor-Critic Era (Classic RLHF / PPO, ~2022–2023)**](multi-model-actor-critic.md) |'),
    ('| **The Direct Mathematical Reparameterization Revolution (DPO, 2023–2024)** |', '| [**The Direct Mathematical Reparameterization Revolution (DPO, 2023–2024)**](direct-mathematical-reparameterization.md) |'),
    ('| **The Verifiable On-Policy Reasoning & Test-Time Search Era (~2025–Present)** |', '| [**The Verifiable On-Policy Reasoning & Test-Time Search Era (~2025–Present)**](verifiable-on-policy-reasoning.md) |'),
    ('| **A. Standard DPO (Bradley-Terry Formulation)** |', '| [**A. Standard DPO (Bradley-Terry Formulation)**](standard-dpo.md) |'),
    ('| **B. Kahneman-Tversky Optimization (KTO)** |', '| [**B. Kahneman-Tversky Optimization (KTO)**](kahneman-tversky-optimization.md) |'),
    ('| **C. Odds Ratio Preference Optimization (ORPO)** |', '| [**C. Odds Ratio Preference Optimization (ORPO)**](odds-ratio-preference.md) |'),
    ('| **D. Reinforcement Learning from AI Feedback (RLAIF / Constitutional AI)** |', '| [**D. Reinforcement Learning from AI Feedback (RLAIF / Constitutional AI)**](rlaif.md) |'),
    ('| **Symmetric KL-Divergence Constraints** |', '| [**Symmetric KL-Divergence Constraints**](symmetric-kl-divergence.md) |'),
    ('| **Fully Sharded Parameter Storage (FSDP Tuning)** |', '| [**Fully Sharded Parameter Storage (FSDP Tuning)**](fully-sharded-parameter-storage.md) |'),
    ('| **The Likelihood Saturation and Capability Collapse Wall (The Alignment Tax)** |', '| [**The Likelihood Saturation and Capability Collapse Wall (The Alignment Tax)**](likelihood-saturation.md) |'),
    ('| **The Sparse Gradient Stagnation Wall** |', '| [**The Sparse Gradient Stagnation Wall**](sparse-gradient-stagnation.md) |'),
    ('| **Conversational Persona and Formatting Alignment for LLMs** |', '| [**Conversational Persona and Formatting Alignment for LLMs**](conversational-persona.md) |'),
    ('| **Safety Guardrail Hardening and Red-Teaming Defense** |', '| [**Safety Guardrail Hardening and Red-Teaming Defense**](safety-guardrail-hardening.md) |'),
    ('| **Autonomous Software Development & Sandbox Repository Maintenance** |', '| [**Autonomous Software Development & Sandbox Repository Maintenance**](autonomous-software-development.md) |')
]

for old, new in replacements:
    c = c.replace(old, new)

with open(path, 'w', encoding='utf8') as f:
    f.write(c)

print("Replaced links.")
