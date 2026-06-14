# ODE / IDE Fundamentals v1

**Purpose:** compact reference for ordinary differential equations (ODEs), integral equations (IE), and integro-differential equations (IDE) relevant to later CA-based simulation.

---

## ODE basics

- **Fact:** many time-evolution models reduce to systems of ordinary differential equations (ODEs) of the form \(u'(t) = f(t, u(t))\) with initial condition \(u(t_0) = u_0\).
- **Heuristic:** for spatially homogeneous problems or for reduced models of PDEs, it is often simpler and safer to prototype on ODEs first (well-understood stability/accuracy) before moving to full PDE/IDE.
- **First adoption task:** for each new PDE/IDE prototype, design at least one lower-dimensional ODE test problem exercising similar stability/accuracy constraints.
- **Success criterion:** new stepping schemes are validated on ODE analogues before being deployed in more complex PDE/IDE settings.
- **Confidence:** high
- *Source:* standard ODE texts; LeVeque — *Finite Difference Methods for ODEs and PDEs* (Part II).

---

## Integral and integro-differential equations

- **Fact:** many memory and nonlocal effects are naturally modeled by integral and integro-differential equations (Volterra/Fredholm types), where the future state depends on an integral over past states and/or space.
- **Heuristic:** use integral terms to model nonlocal influence explicitly (kernels) instead of trying to encode everything into local PDE coefficients.
- **First adoption task:** define 1–2 canonical Volterra/Fredholm IDE test problems (from textbooks) as references for the nonlocal part of the pipeline.
- **Success criterion:** IDE support in the equation→CA→CUDA stack is always tested against at least these canonical problems.
- **Confidence:** medium
- *Source:* Abdul-Majid Wazwaz — *A First Course in Integral Equations* (2nd ed.); Polyanin & Manzhirov — *Handbook of Integral Equations*.

---

## Volterra vs Fredholm (high level)

- **Volterra equations:** integration limits depend on the independent variable (e.g. from 0 to \(t\)); often model cumulative history or hereditary effects.
- **Fredholm equations:** integration limits are fixed; often used for spatially nonlocal interactions.

- **Heuristic:** for time-history effects, prefer Volterra-type IDEs; for spatial nonlocality at each time step, prefer Fredholm-type kernels.
- **First adoption task:** classify each nonlocal operator in the IR as either time-Volterra, space-Fredholm, or a combination, even if numerically all appear as discrete sums.
- **Success criterion:** IR clearly distinguishes between history-based and spatial nonlocal terms.
- **Confidence:** medium
- *Source:* Wazwaz — *A First Course in Integral Equations*; Volterra — *Theory of Functionals and of Integral and Integro-Differential Equations*.

---

## Discretisation idea (preview)

- **Fact:** many integral / IDE terms can be discretised as weighted sums (convolutions) over time or space, leading naturally to kernel-based updates suitable for CA-style rules.
- **Heuristic:** express nonlocal terms as explicit discrete kernels early in the pipeline (IR), instead of hiding quadrature inside kernels; this keeps the mapping to CA rules transparent.
- **First adoption task:** in the IR for equation-to-ca-cuda, include an explicit `kernel` description (support + weights) for each nonlocal term.
- **Success criterion:** the rule compiler can be implemented purely in terms of local stencils and explicit discrete kernels, without re-deriving integrals from scratch.
- **Confidence:** medium
- *Source:* LeVeque — *Finite Difference Methods for ODEs and PDEs* (sections on integral terms) + Wazwaz IDE examples.
