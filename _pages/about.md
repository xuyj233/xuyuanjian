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

<div id="about-me" class="content-section active">
<span class='anchor' id='about-me'></span>

<div markdown="1">

# 👋 A Brief Introduction

I am currently pursuing a Ph.D. degree at the Hong Kong University of Science and Technology (HKUST), now in my third year, supervised by <span style="color: #1976d2;">@Prof. Guang Zhang</span> from HKUST-GZ and <span style="color: #1976d2;">@Dr. Zhong Li</span> from Microsoft Research Asia (MSRA).

My research interests focus on **Data-Centric AI**, **generative model theory**, and **interpretability**. I am also interested in applied research that can generate practical value, such as **Fintech** and other domains.

My work has been published at venues including **ACL 2023**, **ACL 2025**, **ICAIF**, and **ICASSP 2026** (oral). Two submissions to **ICML 2026** have received **all positive reviews**; additional manuscripts are under review at **IJCAI 2026**, **ACL**, **ICLR**, and **ACL Rolling Review (ARR)**. I also serve as a reviewer for leading conferences such as **NeurIPS**, **ICLR**, and **AAAI**.

# 🔥 News
- *2026.04*: &nbsp;😊 Two papers submitted to **ICML 2026** received **all positive reviews**!
- *2026.01*: &nbsp;🎉 Paper accepted at **ICASSP 2026** (**oral**)!
- *2025.10*: &nbsp;😊 Two papers received **all positive reviews** in the October  **ACL ARR** cycle!
- *2025*: &nbsp;🎉🎉 Two papers accepted at **ACL 2025** and **ICAIF 2025**!
- *2023*: &nbsp;🎉🎉 Paper accepted at **ACL 2023**!

<!-- <hr style="border: 2px solid #ccc; margin: 2em 0;"> -->

# 📝 Selected Papers

- [<span style="background-color: #e3f2fd; color: #1976d2; padding: 2px 8px; border-radius: 4px; font-weight: bold;">ICML 2026</span>] **Yuanjian Xu**, et al. *D$^{3}$: Dynamic Directional Graph-Constrained Data Scheduling for LLM Training*. <span style="color: #d32f2f; font-weight: bold;">[CCF A]</span> <span style="color: #d32f2f; font-weight: bold;">[CORE A*]</span> <span style="background-color: #c8e6c9; color: #2e7d32; padding: 2px 8px; border-radius: 4px; font-weight: bold;">✓ All Positive Reviews</span>  
  <div style="background-color: #f8f9fa; border-left: 3px solid #1976d2; padding: 0.8em 1em; margin: 0.5em 0 1em 1.5em; font-size: 0.85em; color: #555; line-height: 1.5;">
  <strong style="color: #1976d2;">🔑 Key Idea:</strong> We explain why training order matters in LLM optimization and propose a data scheduling framework grounded in gradient interactions, where training dependencies are modeled as a graph that explicitly constrains valid training orders.
  </div>

- [<span style="background-color: #e3f2fd; color: #1976d2; padding: 2px 8px; border-radius: 4px; font-weight: bold;">ICML 2026</span>] **Yuanjian Xu**, et al. *Towards Efficient LLMs Annealing with Principled Sample Selection*. <span style="color: #d32f2f; font-weight: bold;">[CCF A]</span> <span style="color: #d32f2f; font-weight: bold;">[CORE A*]</span> <span style="background-color: #c8e6c9; color: #2e7d32; padding: 2px 8px; border-radius: 4px; font-weight: bold;">✓ All Positive Reviews</span>  
  <div style="background-color: #f8f9fa; border-left: 3px solid #1976d2; padding: 0.8em 1em; margin: 0.5em 0 1em 1.5em; font-size: 0.85em; color: #555; line-height: 1.5;">
  <strong style="color: #1976d2;">🔑 Key Idea:</strong> We provide a theoretical characterization of steady-state properties in LLM annealing and formulate sample selection as an optimization problem, achieving SOTA results across multiple model scales.
  </div>

- [<span style="background-color: #e3f2fd; color: #1976d2; padding: 2px 8px; border-radius: 4px; font-weight: bold;">ACL 2026</span>] Jianing Hao†, Yuhe Wu†, **Yuanjian Xu†** and Guang Zhang*. *BizCompass: Benchmarking the Reasoning Capabilities of LLMs in Business Knowledge and Applications*. <span style="color: #d32f2f; font-weight: bold;">[CCF A]</span> <span style="color: #d32f2f; font-weight: bold;">[CORE A*]</span> <span style="background-color: #c8e6c9; color: #2e7d32; padding: 2px 8px; border-radius: 4px; font-weight: bold;">✓ All Positive Reviews</span> <span style="color: #666; font-size: 0.9em;">(† Equal Contribution)</span>  
  <div style="background-color: #f8f9fa; border-left: 3px solid #1976d2; padding: 0.8em 1em; margin: 0.5em 0 1em 1.5em; font-size: 0.85em; color: #555; line-height: 1.5;">
  <strong style="color: #1976d2;">🔑 Key Idea:</strong> We introduce BizCompass, a dual-axis benchmark connecting theoretical foundations (finance, economics, statistics, OR) with practical business applications (analyst, trader, consultant), revealing how theoretical knowledge translates into real-world business performance.
  </div>

- [<span style="background-color: #e3f2fd; color: #1976d2; padding: 2px 8px; border-radius: 4px; font-weight: bold;">ACL 2026</span>] **Yuanjian Xu** and Guang Zhang*. *Rethinking Data Mixing from the Perspective of Large Language Model*. <span style="color: #d32f2f; font-weight: bold;">[CCF A]</span> <span style="color: #d32f2f; font-weight: bold;">[CORE A*]</span> <span style="background-color: #c8e6c9; color: #2e7d32; padding: 2px 8px; border-radius: 4px; font-weight: bold;">✓ All Positive Reviews</span>  
  <div style="background-color: #f8f9fa; border-left: 3px solid #1976d2; padding: 0.8em 1em; margin: 0.5em 0 1em 1.5em; font-size: 0.85em; color: #555; line-height: 1.5;">
  <strong style="color: #1976d2;">🔑 Key Idea:</strong> We establish formal connections between gradient dynamics and domain distributions, and introduce DoGraph, a graph-constrained optimization framework for data mixing that clarifies how domain weighting influences LLM generalization.
  </div>

- [<span style="background-color: #e3f2fd; color: #1976d2; padding: 2px 8px; border-radius: 4px; font-weight: bold;">ACL 2025</span>] **Yuanjian Xu** and Guang Zhang*. *FinRipple: Aligning Large Language Models with Financial Market for Event Ripple Effect Awareness* [<a href="#" style="color: #1976d2;"><i class="fas fa-file-pdf"></i> Paper</a>] [<a href="#" style="color: #1976d2;"><i class="fab fa-github"></i> Code</a>]. <span style="color: #d32f2f; font-weight: bold;">[CCF A]</span> <span style="color: #d32f2f; font-weight: bold;">[CORE A*]</span>  
  <div style="background-color: #f8f9fa; border-left: 3px solid #388e3c; padding: 0.8em 1em; margin: 0.5em 0 1em 1.5em; font-size: 0.85em; color: #555; line-height: 1.5;">
  <strong style="color: #388e3c;">✓ Key Contribution:</strong> We propose FinRipple to align LLMs with financial markets by modeling event ripple effects, enabling better understanding of how financial events propagate and impact market dynamics.
  </div>

- [<span style="background-color: #e3f2fd; color: #1976d2; padding: 2px 8px; border-radius: 4px; font-weight: bold;">ACL 2023</span>] **Yuanjian Xu** and Zaiqing Nie*. *Hard Sample Aware Prompt-Tuning* [<a href="#" style="color: #1976d2;"><i class="fas fa-file-pdf"></i> Paper</a>] [<a href="#" style="color: #1976d2;"><i class="fab fa-github"></i> Code</a>]. <span style="color: #d32f2f; font-weight: bold;">[CCF A]</span> <span style="color: #d32f2f; font-weight: bold;">[CORE A*]</span>  
  <div style="background-color: #f8f9fa; border-left: 3px solid #388e3c; padding: 0.8em 1em; margin: 0.5em 0 1em 1.5em; font-size: 0.85em; color: #555; line-height: 1.5;">
  <strong style="color: #388e3c;">✓ Key Contribution:</strong> We introduce a hard sample aware mechanism for prompt-tuning that dynamically adjusts learning focus on difficult samples, improving model performance on challenging instances.
  </div>

- [<span style="background-color: #e3f2fd; color: #1976d2; padding: 2px 8px; border-radius: 4px; font-weight: bold;">ICASSP 2026</span>] **Yuanjian Xu** and Guang Zhang*. *HGAN-SDEs: Learning Neural Stochastic Differential Equations with Hermite-Guided Adversarial Training* [<a href="#" style="color: #1976d2;"><i class="fas fa-file-pdf"></i> Paper</a>] [<a href="#" style="color: #1976d2;"><i class="fab fa-github"></i> Code</a>]. <span style="color: #d32f2f; font-weight: bold;">[CCF B]</span> <span style="color: #d32f2f; font-weight: bold;">[CORE A]</span> <span style="background-color: #fff3e0; color: #e65100; padding: 2px 8px; border-radius: 4px; font-weight: bold;">Oral</span>  
  <div style="background-color: #f8f9fa; border-left: 3px solid #388e3c; padding: 0.8em 1em; margin: 0.5em 0 1em 1.5em; font-size: 0.85em; color: #555; line-height: 1.5;">
  <strong style="color: #388e3c;">✓ Key Contribution:</strong> We introduce HGAN-SDEs, leveraging Neural Hermite functions to construct an expressive yet lightweight discriminator for Neural SDEs, achieving reduced computational complexity and improved training stability with theoretical guarantees.
  </div>

- [<span style="background-color: #e3f2fd; color: #1976d2; padding: 2px 8px; border-radius: 4px; font-weight: bold;">ICAIF 2025</span>] **Yuanjian Xu** and Guang Zhang*. *LENS: Large Pre-trained Transformer for Exploring Financial Time Series Regularities* [<a href="#" style="color: #1976d2;"><i class="fas fa-file-pdf"></i> Paper</a>] [<a href="#" style="color: #1976d2;"><i class="fab fa-github"></i> Code</a>]. <span style="color: #7b7b7b; font-style: italic;">(Leading conference for AI in Finance)</span>  
  <div style="background-color: #f8f9fa; border-left: 3px solid #388e3c; padding: 0.8em 1em; margin: 0.5em 0 1em 1.5em; font-size: 0.85em; color: #555; line-height: 1.5;">
  <strong style="color: #388e3c;">✓ Key Contribution:</strong> We present LENS, a large-scale pre-trained Transformer that captures inherent regularities in financial time series, achieving superior performance in financial forecasting tasks.
  </div>

> <span style="color: #2e7d32; font-weight: bold;">📌 Note:</span> Papers with <span style="background-color: #c8e6c9; color: #2e7d32; padding: 2px 8px; border-radius: 4px; font-weight: bold;">✓ All Positive Reviews</span> badges are currently under review and have received positive feedback from all reviewers, indicating a high likelihood of acceptance.

</div>
</div>

<div id="publications" class="content-section">

<div markdown="1">
<span class='anchor' id='-publications'></span>



## Under Review

- [<span style="background-color: #e3f2fd; color: #1976d2; padding: 2px 8px; border-radius: 4px; font-weight: bold;">ACL 2026</span>] **Yuanjian Xu**, et al. *A$^{4}$: Tree-Based Action Advantage Attribution for LLM Agent Evolution*. <span style="color: #d32f2f; font-weight: bold;">[CCF A]</span>  
  <div style="background-color: #f8f9fa; border-left: 3px solid #1976d2; padding: 0.8em 1em; margin: 0.5em 0 1em 1.5em; font-size: 0.85em; color: #555; line-height: 1.5;">
  <strong style="color: #1976d2;">🔑 Key Idea:</strong> We propose a tree-structured approach to decompose agent component contributions and reduce estimation bias by adaptively adjusting sampling frequency, achieving improved convergence in multi-agent systems.
  </div>

- [<span style="background-color: #e3f2fd; color: #1976d2; padding: 2px 8px; border-radius: 4px; font-weight: bold;">IJCAI 2026 Survey</span>] **Yuanjian Xu**, et al. *A Systematic Survey of Multi-Agent Learning, Collaboration, and Decision-Making*. <span style="color: #d32f2f; font-weight: bold;">[CCF A]</span>

- [<span style="background-color: #e3f2fd; color: #1976d2; padding: 2px 8px; border-radius: 4px; font-weight: bold;">IJCAI 2026</span>] **Yuanjian Xu** and Guang Zhang*. *State Aware Neural Stochastic Differential Equations for Multi-Modal Dynamics*.

</div>
</div>

<div id="experience" class="content-section">

<div markdown="1">
<span class='anchor' id='experience'></span>



## 🎓 Education

I am currently pursuing a Ph.D. in Fintech at the **Hong Kong University of Science and Technology**. I received my Master's degree in Computer Science from **Peking University**, and my Bachelor's degree in Computer Science from **Nankai University**.

---

## 🔬 Academic Activities

**Research Experience:**
- Microsoft Research Asia (MSRA), supervised by <span style="color: #1976d2;">@Dr. Zhong Li</span>
- Tsinghua University's Institute for AI Industry Research (AIR), supervised by <span style="color: #1976d2;">@Prof. Zaiqing Nie</span>

**Teaching Experience:**
- Teaching Assistant, **Advanced Statistics** (FTEC 5030), HKUST

---

## 💼 Internship

<div style="margin-bottom: 1.3em;">
<div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 0.5em; border-bottom: 1px solid #e0e0e0; padding-bottom: 0.35em;">
<strong>AIR, Tsinghua University</strong>
<span style="color: #555; font-size: 0.95em;">Research Intern</span>
</div>
<p style="margin: 0.65em 0 0 0; color: #444; line-height: 1.65;">Worked under the supervision of <span style="color: #1976d2;">Prof. Zaiqing Nie</span>. Contributed to the <em>Meituan Nutrition Knowledge Graph</em> construction. Investigated <em>hard sample problems</em> in NLP and proposed <em>HardPT</em>, published at <em>ACL 2023</em>.</p>
</div>

<div style="margin-bottom: 1.3em;">
<div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 0.5em; border-bottom: 1px solid #e0e0e0; padding-bottom: 0.35em;">
<strong>Microsoft Research Asia (MSRA)</strong>
<span style="color: #555; font-size: 0.95em;">Research Intern</span>
</div>
<p style="margin: 0.65em 0 0 0; color: #444; line-height: 1.65;">Worked under the supervision of <span style="color: #1976d2;">Dr. Zhong Li</span>. Focused on <em>data selection</em> and <em>training order optimization for large language models</em>. Proposed the <em>D<sup>3</sup></em> method and an <em>annealing training framework</em>, both currently under submission.</p>
</div>

<div style="margin-bottom: 0.5em;">
<div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 0.5em; border-bottom: 1px solid #e0e0e0; padding-bottom: 0.35em;">
<strong>Joinquant (Billion-scale quantitative fund)</strong>
<span style="color: #555; font-size: 0.95em;">Research Intern</span>
</div>
<p style="margin: 0.65em 0 0 0; color: #444; line-height: 1.65;">Worked under the supervision of PM Ruixiao. Developed <em>tick-level generative and representation models</em> for <em>high-frequency trading</em>. Addressed key challenges including <em>non-equally spaced data</em> and <em>market randomness</em>.</p>
</div>

---

## 🏆 Honors and Awards
- *2023--Present* Full Ph.D. Scholarship, Hong Kong University of Science and Technology
- *2021* Award for Excellent Academic Excellence, Peking University (Certificate No.: H2021000170320)
- *2021* Air Star Plan, Tsinghua University, Institute for AI Industry Research (AIR)

</div>
</div>
