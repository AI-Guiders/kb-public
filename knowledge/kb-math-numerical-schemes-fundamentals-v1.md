# Numerical Schemes Fundamentals v1

**Purpose:** capture essential ideas for finite difference schemes for ODEs/PDEs (stability, consistency, convergence) as a reference for simulation/CA work.

---

## Consistency, stability, convergence

- **Fact:** For linear problems, Lax–Richtmyer theory states that (under appropriate conditions) a consistent and stable numerical scheme converges to the true solution.
- **Heuristic:** when designing or choosing schemes, check *both* local approximation error (consistency) and some form of stability estimate; never assume that a low truncation error alone guarantees a good scheme.
- **First adoption task:** for the first heat-equation scheme, compute the local truncation error and perform a simple stability analysis (or cite a known result) before using it as a reference.
- **Success criterion:** scheme choice is justified by a short argument covering consistency and stability, not only by implementation convenience.
- **Confidence:** medium
- *Source:* LeVeque — *Finite Difference Methods for ODEs and PDEs* (Ch. 1–3).

---

## CFL and explicit schemes

- **Fact:** Explicit time-stepping schemes for diffusion and wave equations are subject to Courant–Friedrichs–Lewy (CFL)–type stability conditions relating time step \(\Delta t\) to spatial step \(\Delta x, \Delta y\).
- **Heuristic:** always treat \(\Delta t\) as a derived quantity from spatial resolution and stability constraints for explicit schemes; for performance reasons, choose the largest safe \(\Delta t\), but never exceed CFL limits.
- **First adoption task:** derive or look up the CFL condition for the chosen 2D heat equation scheme (e.g. FTCS) and encode it as a guardrail in the configuration validator.
- **Success criterion:** no production or R&D run is executed with \(\Delta t\) violating the known CFL bounds for the scheme.
- **Confidence:** high
- *Source:* LeVeque — *Finite Difference Methods for ODEs and PDEs* (chapters on diffusion/advection stability).

---

## Spatial discretisation: finite differences

- **Fact:** Standard finite difference approximations (forward/backward/central) provide first- or second-order accurate approximations to derivatives on uniform grids.
- **Heuristic:** start with simple, well-known stencils (e.g. 3-point first derivative, 5-point Laplacian) to avoid mixing inconsistent approximations in early experiments.
- **First adoption task:** explicitly document which finite difference stencils are used in the equation-to-ca-cuda pipeline (order, formula) and keep them centralised in code.
- **Success criterion:** all derivative approximations in the prototype can be traced back to a small, documented set of stencils.
- **Confidence:** high
- *Source:* LeVeque — *Finite Difference Methods for ODEs and PDEs*; standard numerical analysis texts.

---

## Error measurement and refinement

- **Fact:** Error norms (L1/L2/L∞) and grid refinement studies (halving \(\Delta x\), adjusting \(\Delta t\)) are standard tools for verifying convergence and order of a scheme.
- **Heuristic:** always back up new schemes with at least a basic grid-refinement experiment instead of relying on visual inspection of plots.
- **First adoption task:** for the 2D heat-equation reference case, run a small grid-refinement study (e.g. 32×32, 64×64, 128×128) and estimate observed order of convergence.
- **Success criterion:** observed error behaviour matches theoretical order within reasonable tolerance.
- **Confidence:** medium
- *Source:* LeVeque — *Finite Difference Methods for ODEs and PDEs* (appendices on error norms and convergence).

---

## Link to CA-style rules

- **Fact:** Local finite difference stencils can be interpreted as neighbourhood-based update rules, which aligns naturally with cellular automata style updates.
- **Heuristic:** keep the mapping "stencil → CA rule" explicit: each CA update rule should be traceable back to a known finite difference approximation and its stability properties.
- **First adoption task:** in the rule compiler design, include a table or documentation mapping each CA neighbourhood pattern to its underlying stencil and scheme type (e.g. FTCS for heat).
- **Success criterion:** when debugging or extending CA rules, it is always clear which numerical scheme and assumptions they implement.
- **Confidence:** medium
- *Source:* LeVeque — *Finite Difference Methods for ODEs and PDEs* + internal R&D design for equation-to-ca-cuda (2026-03-10).