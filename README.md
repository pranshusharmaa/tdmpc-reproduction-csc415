# tdmpc-reproduction-csc415
# TD-MPC Code Reproduction — CSC415 Assignment 1

This repository contains code and results for reproducing experiments from:

TD-MPC: TD Learning for Model Predictive Control

as part of CSC415 — Introduction to Reinforcement Learning.

The goal is to reproduce the main learning behavior of TD-MPC and perform an ablation study by reducing the MPC planning horizon.

---

# Repository Contents

- plot_eval.py — Script to generate evaluation curves from logs
- tdmpc_eval_curves.png — Learning curve comparing baseline and ablation
- README.md — Setup and reproduction instructions

Experiments were conducted using the official TD-MPC implementation:
https://github.com/nicklashansen/tdmpc

---

# Environment Setup

## 1. Clone the official TD-MPC repository

git clone https://github.com/nicklashansen/tdmpc
cd tdmpc


## 2. Create Python environment

Using Conda:

conda create -n tdmpc python=3.8 -y
conda activate tdmpc


## 3. Install dependencies

pip install torch numpy gym matplotlib hydra-core dm-control


Note: numpy<2 may be required for compatibility.

---

# Reproducing Experiments

## Baseline Training

Run TD-MPC on the walker-walk task:

python src/train.py task=walker-walk exp_name=baseline seed=0


This uses default parameters.

---

## Ablation Study — Reduced MPC Horizon

We evaluate robustness of TD-MPC by reducing planning horizon:

python src/train.py task=walker-walk exp_name=abl_horizon5 seed=0 planning.horizon=5


Due to computational constraints, this experiment was run for approximately 300k environment steps.

---

# Generating Evaluation Plot

After training completes:

python plot_eval.py


This parses evaluation logs and generates:

tdmpc_eval_curves.png


---

# Experiment Description

The reproduction evaluates whether TD-MPC maintains stable learning when planning depth is reduced.

Hypothesis:
Reducing the MPC horizon will slightly reduce stability but preserve overall performance due to strong value learning.

Results:
All configurations achieve high returns, demonstrating robustness to moderate reductions in planning horizon.

---

# Notes on Differences from Original Paper

- Experiments run with limited compute
- Single random seed
- Horizon ablation truncated at ~300k steps
- Minor discrepancies expected due to hardware and runtime constraints

---

# Reproducibility Checklist

To reproduce results:

1. Clone TD-MPC repo
2. Install dependencies
3. Run baseline command
4. Run horizon=5 command
5. Run plot_eval.py

---

# AI Usage

ChatGPT was used to assist with debugging environment setup, interpreting logs, and drafting documentation. All experiments were executed and validated manually.

---

# License

For academic use only.
