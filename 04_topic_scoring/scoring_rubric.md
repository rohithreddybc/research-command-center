# Scoring rubric

For each topic, score 1–5 on each factor below.

Factors:
- A Trend strength
- B Audience size
- C Gap clarity
- D Reusability
- E Bench/dataset potential
- F Tool potential
- G Survey/taxonomy potential
- H Venue availability
- I Speed to submission
- J No-APC likelihood
- K Profile fit
- L NIW value
- M EB-1A value
- N Career/FAANG
- O Crowded risk
- P Weak-novelty risk
- Q Private-data dependency
- R IP/employer risk
- S Verifiability ease
- T Collab dependency
- U Reproducibility
- V Public-artifact potential
- W Ethics/legal
- X Reviewer interest

Composites:

```
CitationPotential = 1.5*A + 1.5*B + 2*C + 1.5*D + X
ExecFeasibility   = 2*I + 1.5*K + 1.5*S + U - 1.5*Q - 1.5*T
ImmigrationValue  = 1.5*L + 1.5*M + 1.2*V + 0.5*D
CareerValue       = 1.5*N + V + 0.5*F + 0.5*D
PublicationPath   = 1.5*H + 1.5*J + I - P
RiskPenalty       = O + P + 1.5*Q + 2*R + 0.5*W + 0.5*T

Overall = 0.30*CitationPotential
        + 0.20*ExecFeasibility
        + 0.20*ImmigrationValue
        + 0.10*CareerValue
        + 0.20*PublicationPath
        - 0.40*RiskPenalty
```

All scores PRELIMINARY until evidence-based scoring runs in `scripts/05_score_topics.py`.
