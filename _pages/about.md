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

## 👋 A Brief Introduction

I am currently a third-year Ph.D. candidate at the Hong Kong University of Science and Technology (HKUST), supervised by <span style="color: #1976d2;">@Prof. Guang Zhang</span> from HKUST-GZ and <span style="color: #1976d2;">@Dr. Zhong Li</span> from MSRA. I am currently doing research at **Tencent Hunyuan** as a **Qing Yun Program** intern.

My research revolves around **Data-centric Machine Learning**, with a primary focus on LLMs. Specifically, my work has systematically investigated four dimensions — **data selection, curriculum, representation, and orchestration** — organized around the following research questions:

<style>
.rq-map { margin: 1.5em 0 1.75em 0; }
.rq-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 0.9em; align-items: stretch; }
.rq-hub {
  grid-column: 1 / -1; justify-self: center; width: min(80%, 400px);
  position: relative; z-index: 5; text-align: center; margin: -1.2em 0;
  background: linear-gradient(135deg, #64b5f6 0%, #2196f3 100%);
  color: #fff; border-radius: 14px; padding: 0.6em 1.1em;
  box-shadow: 0 4px 16px rgba(33,150,243,0.32); border: 3px solid #fff;
}
.rq-hub .rq-hub-title { font-size: 0.86em; font-weight: 700; letter-spacing: 0.2px; }
.rq-hub-sub { display: flex; flex-wrap: wrap; justify-content: center; gap: 0.25em 0.6em; margin-top: 0.3em; }
.rq-hub-item { display: inline-flex; align-items: center; gap: 0.3em; font-size: 0.66em; font-weight: 600; }
.rq-hub-tag {
  font-size: 0.9em; font-weight: 700; letter-spacing: 0.2px;
  background: rgba(255,255,255,0.28); color: #fff;
  padding: 0px 7px; border-radius: 20px;
}
.rq-card {
  position: relative; background: #fff; border: 1px solid #eceff1;
  border-radius: 12px; padding: 1em 1.1em 0.9em 1.1em;
  box-shadow: 0 2px 10px rgba(0,0,0,0.06);
  transition: transform 0.18s ease, box-shadow 0.18s ease;
  border-top: 4px solid var(--rq-color);
}
.rq-card:hover { transform: translateY(-4px); box-shadow: 0 8px 22px rgba(0,0,0,0.12); }
.rq-head { display: flex; align-items: center; gap: 0.5em; margin-bottom: 0.45em; }
.rq-badge {
  flex-shrink: 0; font-size: 0.72em; font-weight: 700; color: #fff;
  background: var(--rq-color); padding: 3px 9px; border-radius: 20px;
}
.rq-topic { font-size: 0.9em; font-weight: 700; color: #263238; }
.rq-q { font-size: 0.86em; font-style: italic; color: #546e7a; line-height: 1.45; margin-bottom: 0.6em; }
.rq-tags { display: flex; flex-wrap: wrap; gap: 0.35em; margin-bottom: 0.55em; }
.rq-tag {
  font-size: 0.72em; font-weight: 600; color: var(--rq-color);
  background: var(--rq-soft); padding: 2px 8px; border-radius: 5px;
}
.rq-affil { display: flex; flex-wrap: wrap; gap: 0.3em; }
.rq-affil-tag {
  display: inline-flex; align-items: center; gap: 0.2em;
  font-size: 0.68em; font-weight: 600; color: #607d8b;
  background: #eceff1; padding: 2px 7px; border-radius: 4px;
}
@media (max-width: 640px) {
  .rq-grid { grid-template-columns: 1fr; gap: 0.9em; }
  .rq-hub { width: auto; margin: 0; border-radius: 14px; padding: 0.75em 1em; }
  .rq-hub .rq-hub-title { font-size: 0.95em; }
  .rq-hub-item { font-size: 0.72em; }
}
</style>

<div class="rq-map" markdown="0">
<div class="rq-grid">
<div class="rq-card" style="--rq-color:#1976d2; --rq-soft:#e3f2fd;">
<div class="rq-head"><span class="rq-badge">RQ1</span><span class="rq-topic">Data Selection</span></div>
<div class="rq-q">On which data should the model be trained?</div>
<div class="rq-tags"><span class="rq-tag">HardPT · ACL 2023</span><span class="rq-tag">DoGraph · ACL 2026</span><span class="rq-tag">DirEct · ICML 2026</span></div>
<div class="rq-affil"><span class="rq-affil-tag">🏛 Microsoft</span><span class="rq-affil-tag">🏛 Tsinghua AIR</span></div>
</div>
<div class="rq-card" style="--rq-color:#388e3c; --rq-soft:#e8f5e9;">
<div class="rq-head"><span class="rq-badge">RQ2</span><span class="rq-topic">Data Curriculum</span></div>
<div class="rq-q">In what order should the training data be scheduled?</div>
<div class="rq-tags"><span class="rq-tag">D<sup>3</sup> · ICML 2026</span></div>
<div class="rq-affil"><span class="rq-affil-tag">🏛 Microsoft</span></div>
</div>
<div class="rq-hub">
<div class="rq-hub-title">🧭 Data-Centric Machine Learning</div>
<div class="rq-hub-sub">
<span class="rq-hub-item">Chinese FineWeb-Edu <span class="rq-hub-tag">Dataset</span></span>
<span class="rq-hub-item">BizCompass · ACL 2026 <span class="rq-hub-tag">Benchmark</span></span>
<span class="rq-hub-item">From Tokens to Intelligence <span class="rq-hub-tag">Survey</span></span>
</div>
</div>
<div class="rq-card" style="--rq-color:#8e24aa; --rq-soft:#f3e5f5;">
<div class="rq-head"><span class="rq-badge">RQ3</span><span class="rq-topic">Data Representation</span></div>
<div class="rq-q">How should complex data characteristics be addressed?</div>
<div class="rq-tags"><span class="rq-tag">LENS · ICAIF 2025</span><span class="rq-tag">HGAN-SDEs · ICASSP 2026</span><span class="rq-tag">MM-NSDEs · AAAI 2026</span><span class="rq-tag">HF Pretraining · Product</span></div>
<div class="rq-affil"><span class="rq-affil-tag">🏛 JoinQuant</span><span class="rq-affil-tag">🏛 HKUST</span></div>
</div>
<div class="rq-card" style="--rq-color:#e65100; --rq-soft:#fff3e0;">
<div class="rq-head"><span class="rq-badge">RQ4</span><span class="rq-topic">Data Orchestration</span></div>
<div class="rq-q">How can we organize heterogeneous data in a more elegant way?</div>
<div class="rq-tags"><span class="rq-tag">FinRipple · ACL 2025</span><span class="rq-tag">Meituan Nutrition KG · Product</span></div>
<div class="rq-affil"><span class="rq-affil-tag">🏛 Tsinghua AIR</span><span class="rq-affil-tag">🏛 HKUST</span></div>
</div>
</div>
</div>

My work has been published at venues including **ICML 2026** (one paper selected as <span style="background-color: #fff3e0; color: #e65100; padding: 2px 8px; border-radius: 4px; font-weight: bold;">🏆 Spotlight</span>), **ACL 2026**, **ACL 2023**, **ACL 2025**, **ICAIF 2025**, and **ICASSP 2026** (<span style="background-color: #fff3e0; color: #e65100; padding: 2px 8px; border-radius: 4px; font-weight: bold;">🏆 Oral</span>). I also serve as a reviewer for leading conferences such as **NeurIPS**, **ICLR**, and **ICML** (selected as <span style="background-color: #fff3e0; color: #e65100; padding: 2px 8px; border-radius: 4px; font-weight: bold;">🏆 Gold Reviewer</span>).

<!-- <hr style="border: 2px solid #ccc; margin: 2em 0;"> -->

## 📝 Selected Papers (First Author)

- [<span style="background-color: #ffebee; color: #c62828; padding: 2px 8px; border-radius: 4px; font-weight: bold;">ICML 2026</span>] **Yuanjian Xu**, et al. *D<sup>3</sup>: Dynamic Directional Graph-Constrained Data Scheduling for LLM Training*. <span style="color: #d32f2f; font-weight: bold;">[CCF A]</span> <span style="color: #d32f2f; font-weight: bold;">[CORE A*]</span> <span style="color: #7b7b7b; font-style: italic;">(@ MSRA)</span>  
  <div style="background-color: #f8f9fa; border-left: 3px solid #388e3c; padding: 0.8em 1em; margin: 0.5em 0 1em 1.5em; font-size: 0.85em; color: #555; line-height: 1.5;">
  <strong style="color: #388e3c;">✓ Key Contribution:</strong> We explain why training order matters in LLM optimization and propose a data scheduling framework grounded in gradient interactions, where training dependencies are modeled as a graph that explicitly constrains valid training orders.
  </div>

- [<span style="background-color: #ffebee; color: #c62828; padding: 2px 8px; border-radius: 4px; font-weight: bold;">ICML 2026 Spotlight 🏆</span>] **Yuanjian Xu**, et al. *Towards Efficient LLMs Annealing with Principled Sample Selection*. <span style="color: #d32f2f; font-weight: bold;">[CCF A]</span> <span style="color: #d32f2f; font-weight: bold;">[CORE A*]</span> <span style="color: #7b7b7b; font-style: italic;">(@ MSRA)</span>  
  <div style="background-color: #f8f9fa; border-left: 3px solid #388e3c; padding: 0.8em 1em; margin: 0.5em 0 1em 1.5em; font-size: 0.85em; color: #555; line-height: 1.5;">
  <strong style="color: #388e3c;">✓ Key Contribution:</strong> We provide a theoretical characterization of steady-state properties in LLM annealing and formulate sample selection as an optimization problem, achieving SOTA results across multiple model scales.
  </div>

- [<span style="background-color: #ffebee; color: #c62828; padding: 2px 8px; border-radius: 4px; font-weight: bold;">ACL 2026</span>] **Yuanjian Xu**, et al. *BizCompass: Benchmarking the Reasoning Capabilities of LLMs in Business Knowledge and Applications*. <span style="color: #d32f2f; font-weight: bold;">[CCF A]</span> <span style="color: #d32f2f; font-weight: bold;">[CORE A*]</span>  
  <div style="background-color: #f8f9fa; border-left: 3px solid #388e3c; padding: 0.8em 1em; margin: 0.5em 0 1em 1.5em; font-size: 0.85em; color: #555; line-height: 1.5;">
  <strong style="color: #388e3c;">✓ Key Contribution:</strong> We introduce BizCompass, a dual-axis benchmark connecting theoretical foundations (finance, economics, statistics, OR) with practical business applications (analyst, trader, consultant), revealing how theoretical knowledge translates into real-world business performance.
  </div>

- [<span style="background-color: #ffebee; color: #c62828; padding: 2px 8px; border-radius: 4px; font-weight: bold;">ACL 2026</span>] **Yuanjian Xu**, et al. *Rethinking Data Mixing from the Perspective of Large Language Model*. <span style="color: #d32f2f; font-weight: bold;">[CCF A]</span> <span style="color: #d32f2f; font-weight: bold;">[CORE A*]</span>  
  <div style="background-color: #f8f9fa; border-left: 3px solid #388e3c; padding: 0.8em 1em; margin: 0.5em 0 1em 1.5em; font-size: 0.85em; color: #555; line-height: 1.5;">
  <strong style="color: #388e3c;">✓ Key Contribution:</strong> We establish formal connections between gradient dynamics and domain distributions, and introduce DoGraph, a graph-constrained optimization framework for data mixing that clarifies how domain weighting influences LLM generalization.
  </div>

- [<span style="background-color: #ffebee; color: #c62828; padding: 2px 8px; border-radius: 4px; font-weight: bold;">ACL 2025</span>] **Yuanjian Xu**, et al. *FinRipple: Aligning Large Language Models with Financial Market for Event Ripple Effect Awareness* [<a href="#" style="color: #1976d2;"><i class="fas fa-file-pdf"></i> Paper</a>] [<a href="#" style="color: #1976d2;"><i class="fab fa-github"></i> Code</a>]. <span style="color: #d32f2f; font-weight: bold;">[CCF A]</span> <span style="color: #d32f2f; font-weight: bold;">[CORE A*]</span>  
  <div style="background-color: #f8f9fa; border-left: 3px solid #388e3c; padding: 0.8em 1em; margin: 0.5em 0 1em 1.5em; font-size: 0.85em; color: #555; line-height: 1.5;">
  <strong style="color: #388e3c;">✓ Key Contribution:</strong> We propose FinRipple to align LLMs with financial markets by modeling event ripple effects, enabling better understanding of how financial events propagate and impact market dynamics.
  </div>

- [<span style="background-color: #ffebee; color: #c62828; padding: 2px 8px; border-radius: 4px; font-weight: bold;">ACL 2023</span>] **Yuanjian Xu**, et al. *Hard Sample Aware Prompt-Tuning* [<a href="#" style="color: #1976d2;"><i class="fas fa-file-pdf"></i> Paper</a>] [<a href="#" style="color: #1976d2;"><i class="fab fa-github"></i> Code</a>]. <span style="color: #d32f2f; font-weight: bold;">[CCF A]</span> <span style="color: #d32f2f; font-weight: bold;">[CORE A*]</span> <span style="color: #7b7b7b; font-style: italic;">(@ THU AIR)</span>  
  <div style="background-color: #f8f9fa; border-left: 3px solid #388e3c; padding: 0.8em 1em; margin: 0.5em 0 1em 1.5em; font-size: 0.85em; color: #555; line-height: 1.5;">
  <strong style="color: #388e3c;">✓ Key Contribution:</strong> We introduce a hard sample aware mechanism for prompt-tuning that dynamically adjusts learning focus on difficult samples, improving model performance on challenging instances.
  </div>

- [<span style="background-color: #ffebee; color: #c62828; padding: 2px 8px; border-radius: 4px; font-weight: bold;">ICASSP 2026 Oral 🏆</span>] **Yuanjian Xu**, et al. *HGAN-SDEs: Learning Neural Stochastic Differential Equations with Hermite-Guided Adversarial Training* [<a href="#" style="color: #1976d2;"><i class="fas fa-file-pdf"></i> Paper</a>] [<a href="#" style="color: #1976d2;"><i class="fab fa-github"></i> Code</a>]. <span style="color: #d32f2f; font-weight: bold;">[CCF B]</span> <span style="color: #d32f2f; font-weight: bold;">[CORE A]</span>  
  <div style="background-color: #f8f9fa; border-left: 3px solid #388e3c; padding: 0.8em 1em; margin: 0.5em 0 1em 1.5em; font-size: 0.85em; color: #555; line-height: 1.5;">
  <strong style="color: #388e3c;">✓ Key Contribution:</strong> We introduce HGAN-SDEs, leveraging Neural Hermite functions to construct an expressive yet lightweight discriminator for Neural SDEs, achieving reduced computational complexity and improved training stability with theoretical guarantees.
  </div>

- [<span style="background-color: #ffebee; color: #c62828; padding: 2px 8px; border-radius: 4px; font-weight: bold;">ICAIF 2025</span>] **Yuanjian Xu**, et al. *LENS: Large Pre-trained Transformer for Exploring Financial Time Series Regularities* [<a href="#" style="color: #1976d2;"><i class="fas fa-file-pdf"></i> Paper</a>] [<a href="#" style="color: #1976d2;"><i class="fab fa-github"></i> Code</a>]. <span style="color: #7b7b7b; font-style: italic;">(Leading conference for AI in Finance)</span>  
  <div style="background-color: #f8f9fa; border-left: 3px solid #388e3c; padding: 0.8em 1em; margin: 0.5em 0 1em 1.5em; font-size: 0.85em; color: #555; line-height: 1.5;">
  <strong style="color: #388e3c;">✓ Key Contribution:</strong> We present LENS, a large-scale pre-trained Transformer that captures inherent regularities in financial time series, achieving superior performance in financial forecasting tasks.
  </div>

</div>
</div>

<div id="publications" class="content-section">

<div markdown="1">
<span class='anchor' id='-publications'></span>



## 📮 Papers in Submission 

- [<span style="background-color: #e3f2fd; color: #1565c0; padding: 2px 8px; border-radius: 4px; font-weight: bold;">Under Review at AAAI 2027</span>] Jinyi Han, **Yuanjian Xu**, et al. *Skill-Use: Can LLMs Actually Use Skills in Agentic Harnesses?* <span style="color: #d32f2f; font-weight: bold;">[CCF A]</span> <span style="color: #7b7b7b; font-style: italic;">(@ Tencent Hunyuan)</span>

- [<span style="background-color: #e3f2fd; color: #1565c0; padding: 2px 8px; border-radius: 4px; font-weight: bold;">Under Review at AAAI 2027</span>] **Yuanjian Xu**, et al. *Rethinking Neural SDEs under Shifting Data-Generating Processes*. <span style="color: #d32f2f; font-weight: bold;">[CCF A]</span>

- [<span style="background-color: #e3f2fd; color: #1565c0; padding: 2px 8px; border-radius: 4px; font-weight: bold;">Under Review at NeurIPS 2026</span>] Yuxuan Sun, **Yuanjian Xu**, et al. *Rethinking Knowledge Distillation for Diffusion Language Models*. <span style="color: #d32f2f; font-weight: bold;">[CCF A]</span> <span style="color: #d32f2f; font-weight: bold;">[CORE A*]</span> <span style="background-color: #e8f5e9; color: #2e7d32; padding: 2px 8px; border-radius: 4px; font-weight: bold;">All Positive Reviews</span> <span style="color: #7b7b7b; font-style: italic;">(@ MSRA)</span>

## 🔬 Papers in Progress

- [<span style="background-color: #fffde7; color: #f57f17; padding: 2px 8px; border-radius: 4px; font-weight: bold;">🚧 Target ICLR 2027</span>] **Yuanjian Xu**, et al. *Identifying Knowledge Gaps via the Manifold Geometry of Soft Prompts*. <span style="color: #d32f2f; font-weight: bold;">[CCF A]</span> <span style="color: #7b7b7b; font-style: italic;">(@ Tencent Hunyuan)</span>

- [<span style="background-color: #fffde7; color: #f57f17; padding: 2px 8px; border-radius: 4px; font-weight: bold;">🚧 Target ICLR 2027</span>] **Yuanjian Xu**, et al. *Benchmarking Sample Reasoning Quality from Internal Geometric Dynamics in LLMs*. <span style="color: #d32f2f; font-weight: bold;">[CCF A]</span> <span style="color: #7b7b7b; font-style: italic;">(@ Tencent Hunyuan)</span>

- [<span style="background-color: #fffde7; color: #f57f17; padding: 2px 8px; border-radius: 4px; font-weight: bold;">🚧 Target ICLR 2027</span>] **Yuanjian Xu**, et al. *Towards Principled Long-Text Data Selection with Attention Head Functional Specialization*. <span style="color: #d32f2f; font-weight: bold;">[CCF A]</span>

- [<span style="background-color: #fffde7; color: #f57f17; padding: 2px 8px; border-radius: 4px; font-weight: bold;">🚧 Target ACL 2027</span>] **Yuanjian Xu**, et al. *The WoW: A Large-Scale World Knowledge Corpus for Full-Lifecycle LLM Training*. <span style="color: #d32f2f; font-weight: bold;">[CCF A]</span>

- [<span style="background-color: #fffde7; color: #f57f17; padding: 2px 8px; border-radius: 4px; font-weight: bold;">🚧 Survey</span>] **Yuanjian Xu**, et al. *From Tokens to Intelligence: A Survey on Data Selection for Large Language Models*.
</div>
</div>

<div id="experience" class="content-section">

<div markdown="1">
<span class='anchor' id='experience'></span>

## 🎓 Education

I am currently pursuing a Ph.D. in Fintech at the **Hong Kong University of Science and Technology**. I received my Master's degree in Computer Science from **Peking University**, and my Bachelor's degree in Computer Science from **Nankai University**.



## 🔬 Academic Activities

- Teaching Assistant, **Advanced Statistics** (FTEC 5030), HKUST



## 💼 Internship

<div style="display: flex; align-items: flex-start; gap: 1em; margin-bottom: 1.3em;">
<img src="{{ '/static/logos/tencent.png' | relative_url }}" alt="Tencent" style="width: 46px; height: 46px; border-radius: 8px; object-fit: contain; flex-shrink: 0; margin-top: 0.2em;">
<div style="flex: 1; min-width: 0;">
<div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 0.5em; border-bottom: 1px solid #e0e0e0; padding-bottom: 0.35em;">
<strong>Tencent Hunyuan</strong>
<span style="color: #555; font-size: 0.95em;">Top Talent Research Intern</span>
</div>
<p style="margin: 0.65em 0 0 0; color: #444; line-height: 1.65;">Currently working as a <strong>Qing Yun Program</strong> research intern in foundation model research.</p>
</div>
</div>

<div style="display: flex; align-items: flex-start; gap: 1em; margin-bottom: 1.3em;">
<img src="{{ '/static/logos/tsinghua.png' | relative_url }}" alt="Tsinghua University" style="width: 46px; height: 46px; border-radius: 8px; object-fit: contain; flex-shrink: 0; margin-top: 0.2em;">
<div style="flex: 1; min-width: 0;">
<div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 0.5em; border-bottom: 1px solid #e0e0e0; padding-bottom: 0.35em;">
<strong>AIR, Tsinghua University</strong>
<span style="color: #555; font-size: 0.95em;">Research Intern</span>
</div>
<p style="margin: 0.65em 0 0 0; color: #444; line-height: 1.65;">Worked under the supervision of <span style="color: #1976d2;">Prof. Zaiqing Nie</span>. Contributed to the <em>Meituan Nutrition Knowledge Graph</em> construction. Investigated <em>hard sample problems</em> in NLP and proposed <em>HardPT</em>, published at <em>ACL 2023</em>.</p>
</div>
</div>

<div style="display: flex; align-items: flex-start; gap: 1em; margin-bottom: 1.3em;">
<img src="{{ '/static/logos/microsoft.svg' | relative_url }}" alt="Microsoft Research Asia" style="width: 46px; height: 46px; border-radius: 8px; object-fit: contain; flex-shrink: 0; margin-top: 0.2em;">
<div style="flex: 1; min-width: 0;">
<div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 0.5em; border-bottom: 1px solid #e0e0e0; padding-bottom: 0.35em;">
<strong>Microsoft Research Asia (MSRA)</strong>
<span style="color: #555; font-size: 0.95em;">Research Intern</span>
</div>
<p style="margin: 0.65em 0 0 0; color: #444; line-height: 1.65;">Worked under the supervision of <span style="color: #1976d2;">Dr. Zhong Li</span>. Focused on <em>data selection</em> and <em>training order optimization for large language models</em>. Proposed the <em>D<sup>3</sup></em> method and an <em>annealing training framework</em>, both accepted at <em>ICML 2026</em> (annealing work as Spotlight).</p>
</div>
</div>

<div style="display: flex; align-items: flex-start; gap: 1em; margin-bottom: 0.5em;">
<img src="{{ '/static/logos/joinquant.png' | relative_url }}" alt="JoinQuant" style="width: 46px; height: 46px; border-radius: 8px; object-fit: contain; flex-shrink: 0; margin-top: 0.2em;">
<div style="flex: 1; min-width: 0;">
<div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 0.5em; border-bottom: 1px solid #e0e0e0; padding-bottom: 0.35em;">
<strong>Joinquant (Billion-scale quantitative fund)</strong>
<span style="color: #555; font-size: 0.95em;">Research Intern</span>
</div>
<p style="margin: 0.65em 0 0 0; color: #444; line-height: 1.65;">Worked under the supervision of PM Ruixiao. Developed <em>tick-level generative and representation models</em> for <em>high-frequency trading</em>. Addressed key challenges including <em>non-equally spaced data</em> and <em>market randomness</em>.</p>
</div>
</div>



## 🏆 Honors and Awards
- *2026* **Top 10% Intern**, Microsoft Research Asia (MSRA)
- *2023--Present* Full Ph.D. Scholarship, Hong Kong University of Science and Technology
- *2021* Award for Excellent Academic Excellence, Peking University (Certificate No.: H2021000170320)
- *2021* Air Star Plan, Tsinghua University, Institute for AI Industry Research (AIR)

</div>
</div>
