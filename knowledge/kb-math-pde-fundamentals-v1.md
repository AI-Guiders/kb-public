# PDE Fundamentals v1

**Purpose:** concise reference for basic partial differential equations (PDEs) relevant to simulation (heat/wave/Poisson) and well-posed initial/boundary value problems.

---

## Core linear PDE classes

- **Fact:** Many classical PDE models in physics and engineering fall into three main linear types: elliptic (e.g. Poisson), parabolic (e.g. heat), and hyperbolic (e.g. wave).
- **Heuristic:** when formulating or reading a PDE, first classify it (elliptic / parabolic / hyperbolic) — this strongly constrains appropriate boundary conditions, numerical schemes, and expectations about solution behaviour.
- **First adoption task:** for each new PDE problem in R&D, explicitly label its type in the problem spec (e.g. "2D heat (parabolic)", "Poisson (elliptic)", "1D wave (hyperbolic)").
- **Success criterion:** no PDE is treated as a generic "equation" in design docs; type is always stated.
- **Confidence:** high
- *Source:* L.C. Evans — *Partial Differential Equations* (2nd ed., AMS, 2010) + Shearer & Levy — *Partial Differential Equations* (Princeton, 2015).

---

## Canonical examples

- **Heat equation (parabolic):**
  - Form: \( u_t = \alpha \Delta u + f(x,t) \) in a domain \(\Omega \subset \mathbb{R}^n\).
  - Models diffusion / heat conduction; typical numerics use explicit or implicit time-stepping plus finite differences / finite elements in space.
- **Wave equation (hyperbolic):**
  - Form: \( u_{tt} = c^2 \Delta u + f(x,t) \).
  - Models vibrations / waves; energy conservation and finite propagation speed are key invariants.
- **Poisson / Laplace (elliptic):**
  - Form: \( -\Delta u = f(x) \) (Poisson) or \( \Delta u = 0 \) (Laplace).
  - Steady-state / potential problems; solutions are typically smooth inside the domain and controlled by boundary data.

- **Heuristic:** for early R&D, standardise on these three as reference problems for validation and regression tests.
- **First adoption task:** define at least one canonical test case for each of heat, wave, and Poisson in 1D/2D (domain, IC/BC, analytic or high-quality reference solution).
- **Success criterion:** new numerical schemes and CA rules are always tested against at least one canonical problem before being used in more complex settings.
- **Confidence:** high
- *Source:* LeVeque — *Finite Difference Methods for Ordinary and Partial Differential Equations* (SIAM, 2007).

---

## Initial and boundary value problems

- **Fact:** For parabolic and hyperbolic PDEs, one typically specifies an **initial condition** (IC) at \(t=0\) plus boundary conditions (BCs) on \(\partial \Omega\); for elliptic equations, only BCs on \(\partial \Omega\) are specified.
- **Heuristic:** always keep IC and BCs explicit and separate in problem specs; do not overload "source term" or coefficients to hide boundary effects.
- **First adoption task:** in the equation→CA IR, make IC and BC separate top-level fields, each with explicit type tags (Dirichlet / Neumann / mixed / periodic) and parameters.
- **Success criterion:** problem configs are unambiguous about which data belong to IC vs BC, and numerical code does not guess or infer them from context.
- **Confidence:** high
- *Source:* Shearer & Levy — *Partial Differential Equations: An Introduction to Theory and Applications* (Princeton, 2015).

---

## Boundary condition types

- **Dirichlet BC:** prescribe the value of the solution on the boundary (e.g. fixed temperature).
- **Neumann BC:** prescribe the normal derivative (e.g. insulated/no-flux boundary in heat problems).
- **Robin / mixed BC:** linear combination of value and normal derivative.
- **Periodic BC:** identify opposite sides of the domain; often best for avoiding artificial reflections.

- **Heuristic:** choose BC type based on the physical meaning first, then on numerical convenience; when in doubt, start with simpler BCs (Dirichlet/Neumann) for validation before moving to more realistic mixed/periodic cases.
- **First adoption task:** for each canonical test problem, document the BC type per side (e.g. left/right Dirichlet, top/bottom Neumann) and why it makes sense physically.
- **Success criterion:** BC choices can be explained in one sentence of physical reasoning; no "because it was easier to code" defaults in core tests.
- **Confidence:** medium
- *Source:* standard PDE texts (Evans; Shearer & Levy).

---

## Well-posedness (at a high level)

- **Fact:** Well-posed problems (in the sense of Hadamard) require existence, uniqueness, and continuous dependence of the solution on input data; many pathological PDE/BC combinations violate one of these.
- **Heuristic:** for R&D prototypes, stick to well-known well-posed setups (classical heat/wave/Poisson test problems) and treat exotic boundary or domain configurations as *experiments*, not baselines.
- **First adoption task:** when defining a new problem type, check a trusted PDE text (Evans / Shearer & Levy) to see whether the chosen IC/BC/domain combination is standard and well-posed.
- **Success criterion:** no core regression tests rely on intentionally ill-posed PDE setups.
- **Confidence:** medium
- *Source:* Evans — *Partial Differential Equations* (2nd ed.).