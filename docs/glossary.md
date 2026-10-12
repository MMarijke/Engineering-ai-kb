---
title: Glossary
tags: [reference]
status: growing
updated: 2026-10-10
---

# Glossary

Short definitions with a pointer to the note that explains each term properly. Keep entries alphabetical; add new ones when a term appears in two or more notes.

| Term | Definition | Where |
|---|---|---|
| Anti-windup | Stopping the integrator from accumulating while the actuator is saturated | [PID control](control-systems/pid-control.md) |
| Attention | Weighted average of values, with weights from query-key similarity | [Transformers](ai/transformers.md) |
| Backpropagation | Chain-rule computation of gradients from the output back to every parameter | [Neural networks](ai/neural-networks-and-backprop.md) |
| Band gap | Energy separating a solid's filled valence band from its empty conduction band | [Quantum & semiconductors](physics/quantum-and-semiconductors.md) |
| Bias-variance trade-off | Test error splits into error from too-simple models and error from over-sensitivity to the sample | [ML fundamentals](ai/machine-learning-fundamentals.md) |
| Bode plot | Gain and phase of a transfer function versus frequency | [Stability](control-systems/stability-and-frequency-response.md) |
| Carnot efficiency | Upper bound $1 - T_c/T_h$ on any heat engine between two temperatures | [Thermodynamics](physics/thermodynamics.md) |
| Condition number | Ratio of largest to smallest singular value; sensitivity of a problem to perturbation | [Linear algebra](mathematics/linear-algebra.md) |
| Configuration space | Space of all robot configurations; obstacles become forbidden regions | [Motion planning](robotics/motion-planning.md) |
| Controllability | Whether inputs can steer the state anywhere | [State space & LQR](control-systems/state-space-and-lqr.md) |
| Cross-entropy | Loss measuring how well a predicted distribution matches the true one | [Probability & statistics](mathematics/probability-and-statistics.md) |
| Delta-v | Total velocity change a spacecraft can produce; the currency of mission design | [Rocket equation](aerospace/rocket-equation-and-staging.md) |
| Eigenvalue / eigenvector | Scalar and direction satisfying $Av = \lambda v$ | [Linear algebra](mathematics/linear-algebra.md) |
| Entropy | Measure of unavailable energy (thermodynamics) or uncertainty (information theory) | [Thermodynamics](physics/thermodynamics.md) |
| Extended Kalman filter | Kalman filter that linearizes nonlinear models at the current estimate | [State estimation](robotics/state-estimation.md) |
| Gain / phase margin | How much extra gain or phase lag a feedback loop tolerates before instability | [Stability](control-systems/stability-and-frequency-response.md) |
| Gradient descent | Iteratively stepping against the gradient to minimize a function | [Calculus & optimization](mathematics/calculus-and-optimization.md) |
| Hohmann transfer | Minimum-delta-v two-burn transfer between coplanar circular orbits | [Orbital mechanics](aerospace/orbital-mechanics.md) |
| Jacobian | Matrix of partial derivatives; maps joint velocities to tip velocity in robotics | [Kinematics](robotics/kinematics.md) |
| Kalman filter | Optimal recursive estimator for linear systems with Gaussian noise | [State estimation](robotics/state-estimation.md) |
| KCL / KVL | Kirchhoff's current and voltage laws: charge and energy conservation in circuits | [Circuit fundamentals](electronics/circuit-fundamentals.md) |
| Lagrangian | $T - V$; basis for deriving equations of motion in any coordinates | [Classical mechanics](physics/classical-mechanics.md) |
| LQR | Optimal state-feedback gain minimizing a quadratic cost | [State space & LQR](control-systems/state-space-and-lqr.md) |
| Mach number | Speed divided by local speed of sound | [Aerodynamics](aerospace/aerodynamics-basics.md) |
| Markov decision process | Framework of states, actions, transitions, rewards and discounting | [Reinforcement learning](ai/reinforcement-learning.md) |
| Maximum likelihood | Choosing parameters that make the observed data most probable | [Probability & statistics](mathematics/probability-and-statistics.md) |
| MOSFET | Voltage-controlled transistor; the building block of CMOS logic | [Quantum & semiconductors](physics/quantum-and-semiconductors.md) |
| Observability | Whether the state can be reconstructed from the outputs | [State space & LQR](control-systems/state-space-and-lqr.md) |
| Overfitting | Fitting noise in the training set so performance on new data suffers | [ML fundamentals](ai/machine-learning-fundamentals.md) |
| PID | Controller combining proportional, integral and derivative action on error | [PID control](control-systems/pid-control.md) |
| Pole | Root of a transfer function's denominator; location determines stability and speed | [Stability](control-systems/stability-and-frequency-response.md) |
| PWM | Pulse-width modulation: approximating an analog level by switching fast | [Microcontrollers & buses](electronics/microcontrollers-and-buses.md) |
| Q-learning | Off-policy temporal-difference algorithm learning action values | [Reinforcement learning](ai/reinforcement-learning.md) |
| Reynolds number | Ratio of inertial to viscous forces in a flow | [Aerodynamics](aerospace/aerodynamics-basics.md) |
| RRT | Rapidly-exploring Random Tree; sampling-based motion planner | [Motion planning](robotics/motion-planning.md) |
| Singular value decomposition | Factorization $A = U\Sigma V^\top$ valid for any matrix | [Linear algebra](mathematics/linear-algebra.md) |
| SLAM | Simultaneous localization and mapping | [State estimation](robotics/state-estimation.md) |
| Specific impulse ($I_{sp}$) | Thrust per unit weight flow of propellant, in seconds | [Rocket equation](aerospace/rocket-equation-and-staging.md) |
| Time constant ($\tau$) | Time for a first-order system to reach 63.2% of its final value | [Circuit fundamentals](electronics/circuit-fundamentals.md) |
| Transformer (neural) | Architecture of attention and MLP blocks in residual stacks | [Transformers](ai/transformers.md) |
| Vis-viva equation | Orbital speed from position and semi-major axis: $v^2 = \mu(2/r - 1/a)$ | [Orbital mechanics](aerospace/orbital-mechanics.md) |
