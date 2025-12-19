---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<div id="about-me" class="content-section active" markdown="1">
<span class='anchor' id='about-me'></span>

# 👋 A Brief Introduction

I am currently pursuing a Ph.D. degree at the Hong Kong University of Science and Technology (HKUST), now in my third year, supervised by <span style="color: #1976d2;">@Prof. Guang Zhang</span> from HKUST-GZ and <span style="color: #1976d2;">@Dr. Li Zhong</span> from Microsoft Research Asia (MSRA).

My research interests focus on **Data-Centric AI**, **generative model theory**, and **interpretability**. I am also interested in applied research that can generate practical value, such as **Fintech** and other domains.

My work has been published at venues including **ACL 2023**, **ACL 2025**, and **ICAIF**, with additional manuscripts under review at **ICLR**, **ACL Rolling Review (ARR)**, and **ICASSP**. I also serve as a reviewer for leading conferences such as **NeurIPS**, **ICLR**, and **AAAI**.

# 🔥 News
- *2025.10*: &nbsp;😊 Two papers received **all positive reviews** in the October  **ACL ARR** cycle!
- *2025*: &nbsp;🎉🎉 Two papers accepted at **ACL 2025** and **ICAIF 2025**!
- *2023*: &nbsp;🎉🎉 Paper accepted at **ACL 2023**!

<!-- <hr style="border: 2px solid #ccc; margin: 2em 0;"> -->

# 📝 Published Papers

- **Yuanjian Xu** and Guang Zhang*. *FinRipple: Aligning Large Language Models with Financial Market for Event Ripple Effect Awareness* [<a href="#" style="color: #1976d2;"><i class="fas fa-file-pdf"></i> Paper</a>] [<a href="#" style="color: #1976d2;"><i class="fab fa-github"></i> Code</a>]. **ACL 2025** <span style="color: #d32f2f; font-weight: bold;">[CCF A, CORE A*]</span>  
  <div style="background-color: #f8f9fa; border-left: 3px solid #388e3c; padding: 0.8em 1em; margin: 0.5em 0 1em 1.5em; font-size: 0.85em; color: #555; line-height: 1.5;">
  <strong style="color: #388e3c;">✓ Key Contribution:</strong> We propose FinRipple to align LLMs with financial markets by modeling event ripple effects, enabling better understanding of how financial events propagate and impact market dynamics.
  </div>

- **Yuanjian Xu** and Zaiqing Nie*. *Hard Sample Aware Prompt-Tuning* [<a href="#" style="color: #1976d2;"><i class="fas fa-file-pdf"></i> Paper</a>] [<a href="#" style="color: #1976d2;"><i class="fab fa-github"></i> Code</a>]. **ACL 2023** <span style="color: #d32f2f; font-weight: bold;">[CCF A, CORE A*]</span>  
  <div style="background-color: #f8f9fa; border-left: 3px solid #388e3c; padding: 0.8em 1em; margin: 0.5em 0 1em 1.5em; font-size: 0.85em; color: #555; line-height: 1.5;">
  <strong style="color: #388e3c;">✓ Key Contribution:</strong> We introduce a hard sample aware mechanism for prompt-tuning that dynamically adjusts learning focus on difficult samples, improving model performance on challenging instances.
  </div>

- **Yuanjian Xu** and Guang Zhang*. *LENS: Large Pre-trained Transformer for Exploring Financial Time Series Regularities* [<a href="#" style="color: #1976d2;"><i class="fas fa-file-pdf"></i> Paper</a>] [<a href="#" style="color: #1976d2;"><i class="fab fa-github"></i> Code</a>]. **ICAIF 2025** <span style="color: #7b7b7b; font-style: italic;">(Leading conference for AI in Finance)</span>  
  <div style="background-color: #f8f9fa; border-left: 3px solid #388e3c; padding: 0.8em 1em; margin: 0.5em 0 1em 1.5em; font-size: 0.85em; color: #555; line-height: 1.5;">
  <strong style="color: #388e3c;">✓ Key Contribution:</strong> We present LENS, a large-scale pre-trained Transformer that captures inherent regularities in financial time series, achieving superior performance in financial forecasting tasks.
  </div>


- Jianing Hao†, Yuhe Wu†, **Yuanjian Xu†** and Guang Zhang*. *BizCompass: Benchmarking the Reasoning Capabilities of LLMs in Business Knowledge and Applications*. <span style="background-color: #e3f2fd; color: #1976d2; padding: 2px 8px; border-radius: 4px; font-weight: bold;">ACL ARR (Oct 2025)</span> <span style="color: #d32f2f; font-weight: bold;">[CCF A, CORE A*]</span> <span style="background-color: #c8e6c9; color: #2e7d32; padding: 2px 8px; border-radius: 4px; font-weight: bold;">✓ All Positive Reviews</span> <span style="color: #666; font-size: 0.9em;">(† Equal Contribution)</span>  
  <div style="background-color: #f8f9fa; border-left: 3px solid #1976d2; padding: 0.8em 1em; margin: 0.5em 0 1em 1.5em; font-size: 0.85em; color: #555; line-height: 1.5;">
  <strong style="color: #1976d2;">🔑 Key Idea:</strong> We introduce BizCompass, a dual-axis benchmark connecting theoretical foundations (finance, economics, statistics, OR) with practical business applications (analyst, trader, consultant), revealing how theoretical knowledge translates into real-world business performance.
  </div>

- **Yuanjian Xu** and Guang Zhang*. *Rethinking Data Mixing from the Perspective of Large Language Model*. <span style="background-color: #e3f2fd; color: #1976d2; padding: 2px 8px; border-radius: 4px; font-weight: bold;">ACL ARR (Oct 2025)</span> <span style="color: #d32f2f; font-weight: bold;">[CCF A, CORE A*]</span> <span style="background-color: #c8e6c9; color: #2e7d32; padding: 2px 8px; border-radius: 4px; font-weight: bold;">✓ All Positive Reviews</span>  
  <div style="background-color: #f8f9fa; border-left: 3px solid #1976d2; padding: 0.8em 1em; margin: 0.5em 0 1em 1.5em; font-size: 0.85em; color: #555; line-height: 1.5;">
  <strong style="color: #1976d2;">🔑 Key Idea:</strong> We establish formal connections between gradient dynamics and domain distributions, and introduce DoGraph, a graph-constrained optimization framework for data mixing that clarifies how domain weighting influences LLM generalization.
  </div>

- **Yuanjian Xu** and Guang Zhang*. *HGAN-SDEs: Learning Neural Stochastic Differential Equations with Hermite-Guided Adversarial Training*. <span style="background-color: #e3f2fd; color: #1976d2; padding: 2px 8px; border-radius: 4px; font-weight: bold;">ICASSP 2026</span> <span style="color: #d32f2f; font-weight: bold;">[CCF B, CORE A]</span> <span style="background-color: #c8e6c9; color: #2e7d32; padding: 2px 8px; border-radius: 4px; font-weight: bold;">✓ All Positive Reviews</span>  
  <div style="background-color: #f8f9fa; border-left: 3px solid #1976d2; padding: 0.8em 1em; margin: 0.5em 0 1em 1.5em; font-size: 0.85em; color: #555; line-height: 1.5;">
  <strong style="color: #1976d2;">🔑 Key Idea:</strong> We introduce HGAN-SDEs, leveraging Neural Hermite functions to construct an expressive yet lightweight discriminator for Neural SDEs, achieving reduced computational complexity and improved training stability with theoretical guarantees.
  </div>

> <span style="color: #2e7d32; font-weight: bold;">📌 Note:</span> Papers with <span style="background-color: #c8e6c9; color: #2e7d32; padding: 2px 8px; border-radius: 4px; font-weight: bold;">✓ All Positive Reviews</span> badges are currently under review and have received positive feedback from all reviewers, indicating a high likelihood of acceptance.

</div>

<div id="publications" class="content-section" markdown="1">
<span class='anchor' id='-publications'></span>



## Under Review

- **Yuanjian Xu** and Guang Zhang*. *State Aware Neural Stochastic Differential Equations for Multi-Modal Dynamics*. <span style="background-color: #e3f2fd; color: #1976d2; padding: 2px 8px; border-radius: 4px; font-weight: bold;">ICLR 2026</span>

- **Yuanjian Xu** and Guang Zhang*. *Mitigating Discretization Bias in Neural Stochastic Differential Equations via Inference-Time Dropout*. <span style="background-color: #e3f2fd; color: #1976d2; padding: 2px 8px; border-radius: 4px; font-weight: bold;">ICLR 2026</span>

---

## In Preparation

- **Yuanjian Xu**, et al. *LLM Agents Evolution with Advantage Tree Guidance*. <span style="color: #888;">Target:</span> **ACL** <span style="color: #d32f2f; font-weight: bold;">[CCF A]</span>  
  <div style="background-color: #f8f9fa; border-left: 3px solid #1976d2; padding: 0.8em 1em; margin: 0.5em 0 1em 1.5em; font-size: 0.85em; color: #555; line-height: 1.5;">
  <strong style="color: #1976d2;">🔑 Key Idea:</strong> We propose a tree-structured approach to decompose agent component contributions and reduce estimation bias by adaptively adjusting sampling frequency, achieving improved convergence in multi-agent systems.
  </div>

- **Yuanjian Xu**, et al. *Neural Causal Process*. <span style="color: #888;">Target:</span> **ICML** <span style="color: #d32f2f; font-weight: bold;">[CCF A]</span>  
  <div style="background-color: #f8f9fa; border-left: 3px solid #1976d2; padding: 0.8em 1em; margin: 0.5em 0 1em 1.5em; font-size: 0.85em; color: #555; line-height: 1.5;">
  <strong style="color: #1976d2;">🔑 Key Idea:</strong> We introduce Neural Graph Process to jointly model the co-evolution of graph structure, node attributes, and edge attributes using neural SDEs, addressing the limitation that existing methods only model structural or attribute changes in isolation.
  </div>

- **Yuanjian Xu**, et al. *Information Aggregation under Model Capacity Constraints: A Unified View of Tokenization, Patching, and Motifs*. <span style="color: #888;">Target:</span> **ICML** <span style="color: #d32f2f; font-weight: bold;">[CCF A, CORE A*]</span>  
  <div style="background-color: #f8f9fa; border-left: 3px solid #1976d2; padding: 0.8em 1em; margin: 0.5em 0 1em 1.5em; font-size: 0.85em; color: #555; line-height: 1.5;">
  <strong style="color: #1976d2;">🔑 Key Idea:</strong> We formalize how information aggregation (tokenization, patching, motifs) induces a trade-off with model capacity, and propose a framework to evaluate aggregation schemes using low-capacity models, enabling principled comparison with reduced computation.
  </div>

- **Yuanjian Xu**, et al. *Training Data Order Matters in Large Language Model Optimization*. <span style="color: #888;">Target:</span> **ICML** <span style="color: #d32f2f; font-weight: bold;">[CCF A, CORE A*]</span>  
  <div style="background-color: #f8f9fa; border-left: 3px solid #1976d2; padding: 0.8em 1em; margin: 0.5em 0 1em 1.5em; font-size: 0.85em; color: #555; line-height: 1.5;">
  <strong style="color: #1976d2;">🔑 Key Idea:</strong> We explain why training order matters in LLM optimization and propose a data scheduling framework grounded in gradient interactions, where training dependencies are modeled as a graph that explicitly constrains valid training orders.
  </div>

- **Yuanjian Xu**, et al. *Data Matters Late: Towards Principled Sample Selection for the Annealing Phase of LLM Pre-Training*. <span style="color: #888;">Target:</span> **ICML** <span style="color: #d32f2f; font-weight: bold;">[CCF A, CORE A*]</span>  
  <div style="background-color: #f8f9fa; border-left: 3px solid #1976d2; padding: 0.8em 1em; margin: 0.5em 0 1em 1.5em; font-size: 0.85em; color: #555; line-height: 1.5;">
  <strong style="color: #1976d2;">🔑 Key Idea:</strong> We provide a theoretical characterization of steady-state properties in LLM annealing and formulate sample selection as an optimization problem, achieving SOTA results across multiple model scales.
  </div>

- **Yuanjian Xu**, et al. *A Unified Framework for Time-Series Foundation Model Pretraining*. <span style="color: #888;">Target:</span> **JMLR** <span style="color: #d32f2f; font-weight: bold;">[CCF A]</span>

- **Yuanjian Xu**, et al. *A Comprehensive Survey on Data Curriculum and Scheduling Strategies in Deep Learning*. <span style="color: #888;">Target:</span> **IJCAI Survey** <span style="color: #d32f2f; font-weight: bold;">[CCF A]</span>

- **Yuanjian Xu**, et al. *A Systematic Survey of Multi-Agent Learning, Collaboration, and Decision-Making*. <span style="color: #888;">Target:</span> **IJCAI Survey** <span style="color: #d32f2f; font-weight: bold;">[CCF A]</span>
</div>

<div id="experience" class="content-section" markdown="1">
<span class='anchor' id='experience'></span>



## 🎓 Education

I am currently pursuing a Ph.D. in Fintech at the **Hong Kong University of Science and Technology**. I received my Master's degree in Computer Science from **Peking University**, and my Bachelor's degree in Computer Science from **Nankai University**.

---

## 🎓 Academic Research

I have conducted research at leading academic institutions, including **Microsoft Research Asia (MSRA)**, **Tsinghua University's Institute for AI Industry Research (AIR)**, and **Hong Kong University of Science and Technology**.

---

## 💼 Industry Research

At **OpenCSG**, a startup company focusing on open-source AI community development, I led an algorithm team consisting of **2 Ph.D. students** (<span style="font-family: 'Courier New', monospace; color: #1976d2;">@Jianing Hao</span> from HKUST(GZ), <span style="font-family: 'Courier New', monospace; color: #1976d2;">@Tianze Sun</span> from HIT) and **2 master students** (<span style="font-family: 'Georgia', serif; color: #7b1fa2;">@Changwei Xu</span> from HKU, <span style="font-family: 'Georgia', serif; color: #7b1fa2;">@Han Ding</span> from Beihang University). I have also gained research experience at **HuaTai Securities**, where I worked as a research intern and participated in quantitative research.

---

## 🏆 Honors and Awards
- *2023--Present* Full Ph.D. Scholarship, Hong Kong University of Science and Technology
- *2021* Award for Excellent Academic Excellence, Peking University (Certificate No.: H2021000170320)
- *2021* Air Star Plan, Tsinghua University, Institute for AI Industry Research (AIR)
</div>
