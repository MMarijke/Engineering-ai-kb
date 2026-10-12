---
title: Robotics
tags: [robotics]
status: growing
updated: 2026-10-10
---

# Robotics

> **Scope** — How machines sense, decide and move in the physical world: system architecture, the geometry of motion, estimating state from noisy sensors, and planning collision-free paths.

## Visual summary

```mermaid
flowchart LR
    SENSE["Sensing<br/>IMU, encoders, LiDAR, camera"] --> EST["State estimation<br/>Kalman, particle, SLAM"]
    EST --> PLAN["Planning<br/>A*, RRT, trajectory optimization"]
    PLAN --> CTRL["Control<br/>PID, LQR, MPC"]
    CTRL --> ACT["Actuation<br/>motors, joints"]
    ACT --> WORLD(("Physical<br/>world"))
    WORLD --> SENSE
    KIN["Kinematics<br/>geometry of the body"] -.-> PLAN
    KIN -.-> CTRL
```

## Notes

| Note | Status | One-line summary |
|---|---|---|
| [Sense-plan-act architecture](sense-plan-act.md) | growing | The standard layered view of a robot, its sensors, and ROS 2 vocabulary |
| [Kinematics](kinematics.md) | growing | Forward and inverse kinematics, the Jacobian and singularities, with runnable code |
| [State estimation](state-estimation.md) | growing | Kalman filter, particle filter and the structure of SLAM |
| [Motion planning](motion-planning.md) | growing | Configuration space, A*, sampling-based planners and when to use each |

## Suggested reading order

Architecture → Kinematics → State estimation → Motion planning, then dip into [Control systems](../control-systems/index.md) for the layer that turns plans into motor commands.

## Related topics

- [Control systems](../control-systems/index.md) — closing the loop around actuators.
- [Electronics](../electronics/index.md) — sensors, motor drivers and buses.
- [AI](../ai/index.md) — learned perception and policies.
- [Mathematics](../mathematics/index.md) — linear algebra and probability throughout.
