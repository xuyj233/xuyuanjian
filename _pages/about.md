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

I am currently a third-year Ph.D. candidate at the Hong Kong University of Science and Technology (HKUST), supervised by <span style="color: #1976d2;">@Prof. Guang Zhang</span> from HKUST-GZ and <span style="color: #1976d2;">@Dr. Zhong Li</span> from MSRA.

My past research has focused on **sample selection and sample quality assessment across the full LLM training lifecycle**. Recently, I have been exploring two directions:

<style>
.focus-directions {
  margin: 1.15em 0 1.45em;
}
.direction-item {
  display: grid;
  grid-template-columns: 3.3em 1fr;
  gap: 0.9em;
  align-items: start;
  padding: 0.9em 0;
}
.direction-item + .direction-item {
  border-top: 1px solid #edf1f5;
}
.direction-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 2.75em;
  height: 2.75em;
  border-radius: 50%;
  color: #1976d2;
  background: #eaf3fc;
  font-size: 0.95em;
}
.direction-item:nth-child(2) .direction-icon {
  color: #7b1fa2;
  background: #f3eaf7;
}
.direction-title {
  margin-bottom: 0.25em;
  color: #263238;
  font-size: 0.96em;
  font-weight: 750;
}
.direction-description {
  color: #546e7a;
  font-size: 0.86em;
  line-height: 1.58;
}
.direction-signals {
  display: flex;
  flex-wrap: wrap;
  gap: 0.7em;
  margin-top: 0.48em;
  color: #78909c;
  font-size: 0.7em;
  font-weight: 650;
}
.direction-signals span {
  white-space: nowrap;
}
.direction-signals i {
  width: 1.2em;
  color: #1976d2;
  text-align: center;
}
.direction-item:nth-child(2) .direction-signals i {
  color: #8e24aa;
}
@media (max-width: 640px) {
  .direction-item {
    grid-template-columns: 2.8em 1fr;
    gap: 0.65em;
  }
  .direction-icon {
    width: 2.35em;
    height: 2.35em;
  }
}
</style>

<div class="focus-directions" markdown="0">
  <div class="direction-item">
    <div class="direction-icon"><i class="fas fa-images" aria-hidden="true"></i></div>
    <div>
      <div class="direction-title">Multimodal Data Selection</div>
      <div class="direction-description">Identifying high-quality samples by evaluating alignment, complementarity, and informativeness across text, images, and other modalities.</div>
      <div class="direction-signals">
        <span><i class="fas fa-link"></i>Cross-modal alignment</span>
        <span><i class="fas fa-puzzle-piece"></i>Complementarity</span>
        <span><i class="fas fa-chart-line"></i>Informativeness</span>
      </div>
    </div>
  </div>
  <div class="direction-item">
    <div class="direction-icon"><i class="fas fa-robot" aria-hidden="true"></i></div>
    <div>
      <div class="direction-title">Specialized Text Data Selection</div>
      <div class="direction-description">Developing quality criteria for long-context and agentic data. For agentic data, I study what interaction trajectories teach language models and which examples provide genuinely useful learning signals.</div>
      <div class="direction-signals">
        <span><i class="fas fa-route"></i>Planning</span>
        <span><i class="fas fa-tools"></i>Tool use</span>
        <span><i class="fas fa-comment-dots"></i>Feedback</span>
        <span><i class="fas fa-redo-alt"></i>Error recovery</span>
      </div>
    </div>
  </div>
</div>

<style>
.research-thread {
  margin: 1.6em 0 1.8em;
  padding: 1.1em 0 1.25em;
  border-top: 1px solid #e3eaf1;
  border-bottom: 1px solid #e3eaf1;
}
.thread-heading {
  margin-bottom: 1.15em;
  color: #455a64;
  font-size: 0.76em;
  font-weight: 750;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}
.thread-track {
  position: relative;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1em;
}
.thread-track::before {
  content: "";
  position: absolute;
  top: 0.5em;
  left: 0.55em;
  right: 0.55em;
  height: 2px;
  background: linear-gradient(90deg, #b0bec5 0%, #78909c 58%, #1976d2 100%);
}
.thread-track::after {
  content: "";
  position: absolute;
  top: 0.22em;
  right: 0;
  width: 0;
  height: 0;
  border-top: 0.34em solid transparent;
  border-bottom: 0.34em solid transparent;
  border-left: 0.5em solid #1976d2;
}
.thread-step {
  position: relative;
  padding-top: 1.65em;
}
.thread-dot {
  position: absolute;
  top: 0;
  left: 0.18em;
  width: 1.05em;
  height: 1.05em;
  border: 3px solid #fff;
  border-radius: 50%;
  background: #78909c;
  box-shadow: 0 0 0 2px #78909c;
}
.thread-step.current .thread-dot {
  background: #1976d2;
  box-shadow: 0 0 0 2px #1976d2, 0 0 0 6px #e3f2fd;
}
.thread-work {
  color: #263238;
  font-size: 0.88em;
  font-weight: 750;
  line-height: 1.35;
}
.thread-topic {
  margin-top: 0.18em;
  color: #607d8b;
  font-size: 0.76em;
  line-height: 1.4;
}
.thread-venue {
  margin-top: 0.35em;
  color: #90a4ae;
  font-size: 0.65em;
  font-weight: 650;
  letter-spacing: 0.03em;
}
.thread-step.current .thread-work,
.thread-step.current .thread-venue {
  color: #1976d2;
}
@media (max-width: 640px) {
  .thread-track {
    grid-template-columns: 1fr;
    gap: 0;
    padding-left: 1.85em;
  }
  .thread-track::before {
    top: 0.55em;
    bottom: 0.55em;
    left: 0.48em;
    right: auto;
    width: 2px;
    height: auto;
    background: linear-gradient(180deg, #b0bec5 0%, #78909c 58%, #1976d2 100%);
  }
  .thread-track::after {
    top: auto;
    right: auto;
    bottom: 0;
    left: 0.18em;
    transform: rotate(90deg);
  }
  .thread-step {
    padding: 0 0 1.15em;
  }
  .thread-step:last-child {
    padding-bottom: 0;
  }
  .thread-dot {
    top: 0.12em;
    left: -1.85em;
  }
}
</style>

<div class="research-thread" aria-label="Connection between previous work and current research" markdown="0">
  <div class="thread-heading">A continuous research thread</div>
  <div class="thread-track">
    <div class="thread-step">
      <span class="thread-dot"></span>
      <div class="thread-work">HardPT</div>
      <div class="thread-topic">Hard-sample identification</div>
      <div class="thread-venue">ACL 2023</div>
    </div>
    <div class="thread-step">
      <span class="thread-dot"></span>
      <div class="thread-work">DoGraph · DirEct</div>
      <div class="thread-topic">Domain &amp; sample selection</div>
      <div class="thread-venue">ACL · ICML 2026</div>
    </div>
    <div class="thread-step">
      <span class="thread-dot"></span>
      <div class="thread-work">D<sup>3</sup></div>
      <div class="thread-topic">Training-order optimization</div>
      <div class="thread-venue">ICML 2026</div>
    </div>
    <div class="thread-step current">
      <span class="thread-dot"></span>
      <div class="thread-work">Current Focus</div>
      <div class="thread-topic">Multimodal &amp; specialized data</div>
      <div class="thread-venue">ONGOING</div>
    </div>
  </div>
</div>

My work has been published at venues including **NeurIPS 2026**, **ICML 2026** (one paper selected as <span style="background-color: #fff3e0; color: #e65100; padding: 2px 8px; border-radius: 4px; font-weight: bold;">🏆 Spotlight</span>), **ACL 2026**, **ACL 2023**, **ACL 2025**, **ICAIF 2025**, and **ICASSP 2026** (<span style="background-color: #fff3e0; color: #e65100; padding: 2px 8px; border-radius: 4px; font-weight: bold;">🏆 Oral</span>). I also serve as a reviewer for leading conferences such as **NeurIPS**, **ICLR**, and **ICML** (selected as <span style="background-color: #fff3e0; color: #e65100; padding: 2px 8px; border-radius: 4px; font-weight: bold;">🏆 Gold Reviewer</span>).

<!-- <hr style="border: 2px solid #ccc; margin: 2em 0;"> -->

## 📝 Selected Publications

- [<span style="background-color: #ffebee; color: #c62828; padding: 2px 8px; border-radius: 4px; font-weight: bold;">ICML 2026</span>] **Yuanjian Xu**, et al. *D<sup>3</sup>: Dynamic Directional Graph-Constrained Data Scheduling for LLM Training* [<a href="https://arxiv.org/abs/2605.31164" style="color: #1976d2;"><i class="fas fa-file-pdf"></i> Paper</a>] [<a href="https://github.com/xuyj233/D3" style="color: #1976d2;"><i class="fab fa-github"></i> Code</a>]. <span style="color: #d32f2f; font-weight: bold;">[CCF A]</span> <span style="color: #d32f2f; font-weight: bold;">[CORE A*]</span> <span style="color: #7b7b7b; font-style: italic;">(@ MSRA)</span>  
  <div style="background-color: #f8f9fa; border-left: 3px solid #388e3c; padding: 0.8em 1em; margin: 0.5em 0 1em 1.5em; font-size: 0.85em; color: #555; line-height: 1.5;">
  <strong style="color: #388e3c;">✓ Key Contribution:</strong> We explain why training order matters in LLM optimization and propose a data scheduling framework grounded in gradient interactions, where training dependencies are modeled as a graph that explicitly constrains valid training orders.
  </div>

- [<span style="background-color: #ffebee; color: #c62828; padding: 2px 8px; border-radius: 4px; font-weight: bold;">ICML 2026 Spotlight 🏆</span>] **Yuanjian Xu**, et al. *Towards Efficient LLMs Annealing with Principled Sample Selection* [<a href="https://arxiv.org/abs/2605.31175" style="color: #1976d2;"><i class="fas fa-file-pdf"></i> Paper</a>] [<a href="https://github.com/xuyj233/Direct" style="color: #1976d2;"><i class="fab fa-github"></i> Code</a>]. <span style="color: #d32f2f; font-weight: bold;">[CCF A]</span> <span style="color: #d32f2f; font-weight: bold;">[CORE A*]</span> <span style="color: #7b7b7b; font-style: italic;">(@ MSRA)</span>  
  <div style="background-color: #f8f9fa; border-left: 3px solid #388e3c; padding: 0.8em 1em; margin: 0.5em 0 1em 1.5em; font-size: 0.85em; color: #555; line-height: 1.5;">
  <strong style="color: #388e3c;">✓ Key Contribution:</strong> We provide a theoretical characterization of steady-state properties in LLM annealing and formulate sample selection as an optimization problem, achieving SOTA results across multiple model scales.
  </div>

- [<span style="background-color: #ffebee; color: #c62828; padding: 2px 8px; border-radius: 4px; font-weight: bold;">ACL 2026</span>] **Yuanjian Xu**, et al. *Rethinking Data Mixing from the Perspective of Large Language Model* [<a href="https://aclanthology.org/2026.acl-short.28/" style="color: #1976d2;"><i class="fas fa-file-pdf"></i> Paper</a>]. <span style="color: #d32f2f; font-weight: bold;">[CCF A]</span> <span style="color: #d32f2f; font-weight: bold;">[CORE A*]</span>  
  <div style="background-color: #f8f9fa; border-left: 3px solid #388e3c; padding: 0.8em 1em; margin: 0.5em 0 1em 1.5em; font-size: 0.85em; color: #555; line-height: 1.5;">
  <strong style="color: #388e3c;">✓ Key Contribution:</strong> We establish formal connections between gradient dynamics and domain distributions, and introduce DoGraph, a graph-constrained optimization framework for data mixing that clarifies how domain weighting influences LLM generalization.
  </div>

- [<span style="background-color: #ffebee; color: #c62828; padding: 2px 8px; border-radius: 4px; font-weight: bold;">ACL 2023</span>] **Yuanjian Xu**, et al. *Hard Sample Aware Prompt-Tuning* [<a href="https://aclanthology.org/2023.acl-long.690/" style="color: #1976d2;"><i class="fas fa-file-pdf"></i> Paper</a>]. <span style="color: #d32f2f; font-weight: bold;">[CCF A]</span> <span style="color: #d32f2f; font-weight: bold;">[CORE A*]</span> <span style="color: #7b7b7b; font-style: italic;">(@ THU AIR)</span>  
  <div style="background-color: #f8f9fa; border-left: 3px solid #388e3c; padding: 0.8em 1em; margin: 0.5em 0 1em 1.5em; font-size: 0.85em; color: #555; line-height: 1.5;">
  <strong style="color: #388e3c;">✓ Key Contribution:</strong> We introduce a hard sample aware mechanism for prompt-tuning that dynamically adjusts learning focus on difficult samples, improving model performance on challenging instances.
  </div>

- [<span style="background-color: #ffebee; color: #c62828; padding: 2px 8px; border-radius: 4px; font-weight: bold;">NeurIPS 2026</span>] Yuxuan Sun, **Yuanjian Xu**, et al. *Rethinking Knowledge Distillation for Diffusion Language Models* [<a href="https://openreview.net/forum?id=RwFzh7uPPD" style="color: #1976d2;"><i class="fas fa-file-pdf"></i> Paper</a>]. <span style="color: #d32f2f; font-weight: bold;">[CCF A]</span> <span style="color: #d32f2f; font-weight: bold;">[CORE A*]</span> <span style="color: #7b7b7b; font-style: italic;">(@ MSRA)</span>  
  <div style="background-color: #f8f9fa; border-left: 3px solid #388e3c; padding: 0.8em 1em; margin: 0.5em 0 1em 1.5em; font-size: 0.85em; color: #555; line-height: 1.5;">
  <strong style="color: #388e3c;">✓ Key Contribution:</strong> We investigate sample selection for knowledge distillation in diffusion language models, providing a principled perspective on choosing informative training samples for effective distillation.
  </div>

- [<span style="background-color: #e3f2fd; color: #1565c0; padding: 2px 8px; border-radius: 4px; font-weight: bold;">Under Review at ACL 2027 · Survey</span>] **Yuanjian Xu**, et al. *Data Strategy in Action: Identifying High-Quality Corpora Across the LLM Training Lifecycle*. <span style="color: #d32f2f; font-weight: bold;">[CCF A]</span> <span style="color: #d32f2f; font-weight: bold;">[CORE A*]</span>  
  <div style="background-color: #f8f9fa; border-left: 3px solid #388e3c; padding: 0.8em 1em; margin: 0.5em 0 1em 1.5em; font-size: 0.85em; color: #555; line-height: 1.5;">
  <strong style="color: #388e3c;">✓ Key Contribution:</strong> We survey data strategies for identifying high-quality corpora across the full LLM training lifecycle, organizing the field around how data quality requirements evolve across training stages.
  </div>

</div>
</div>

<div id="publications" class="content-section">

<div markdown="1">
<span class='anchor' id='-publications'></span>



## Other Publications

- [<span style="background-color: #ffebee; color: #c62828; padding: 2px 8px; border-radius: 4px; font-weight: bold;">ACL 2026</span>] **Yuanjian Xu**, et al. *BizCompass: Benchmarking the Reasoning Capabilities of LLMs in Business Knowledge and Applications* [<a href="https://aclanthology.org/2026.findings-acl.1198/" style="color: #1976d2;"><i class="fas fa-file-pdf"></i> Paper</a>] [<a href="https://github.com/CatherineHao/BizCompass" style="color: #1976d2;"><i class="fab fa-github"></i> Code</a>]. <span style="color: #d32f2f; font-weight: bold;">[CCF A]</span> <span style="color: #d32f2f; font-weight: bold;">[CORE A*]</span>

- [<span style="background-color: #ffebee; color: #c62828; padding: 2px 8px; border-radius: 4px; font-weight: bold;">ACL 2025</span>] **Yuanjian Xu**, et al. *FinRipple: Aligning Large Language Models with Financial Market for Event Ripple Effect Awareness* [<a href="https://aclanthology.org/2025.findings-acl.489/" style="color: #1976d2;"><i class="fas fa-file-pdf"></i> Paper</a>] [<a href="https://github.com/CatherineHao/FinRipple" style="color: #1976d2;"><i class="fab fa-github"></i> Code</a>]. <span style="color: #d32f2f; font-weight: bold;">[CCF A]</span> <span style="color: #d32f2f; font-weight: bold;">[CORE A*]</span>

- [<span style="background-color: #ffebee; color: #c62828; padding: 2px 8px; border-radius: 4px; font-weight: bold;">ICASSP 2026 Oral 🏆</span>] **Yuanjian Xu**, et al. *HGAN-SDEs: Learning Neural Stochastic Differential Equations with Hermite-Guided Adversarial Training* [<a href="https://arxiv.org/abs/2512.20272" style="color: #1976d2;"><i class="fas fa-file-pdf"></i> Paper</a>]. <span style="color: #d32f2f; font-weight: bold;">[CCF B]</span> <span style="color: #d32f2f; font-weight: bold;">[CORE A]</span>

- [<span style="background-color: #ffebee; color: #c62828; padding: 2px 8px; border-radius: 4px; font-weight: bold;">ICAIF 2025</span>] **Yuanjian Xu**, et al. *LENS: Large Pre-trained Transformer for Exploring Financial Time Series Regularities* [<a href="https://arxiv.org/abs/2408.10111" style="color: #1976d2;"><i class="fas fa-file-pdf"></i> Paper</a>]. <span style="color: #7b7b7b; font-style: italic;">(Leading conference for AI in Finance)</span>

## Under Review

- [<span style="background-color: #ffebee; color: #c62828; padding: 2px 8px; border-radius: 4px; font-weight: bold;">Technical Report @ Tencent Hunyuan</span>] Jinyi Han*, **Yuanjian Xu***, et al. *Skill-Use: Can LLMs Actually Use Skills in Agentic Harnesses?* [<a href="https://arxiv.org/abs/2608.04828" style="color: #1976d2;"><i class="fas fa-file-pdf"></i> Paper</a>] [<a href="https://github.com/JinyiHan99/Skill-Use-Bench" style="color: #1976d2;"><i class="fab fa-github"></i> Code</a>]. <span style="color: #d32f2f; font-weight: bold;">[CCF A]</span> <span style="color: #7b7b7b; font-style: italic;">(under review at AAAI 2027, equal contribution)</span>

- [<span style="background-color: #e3f2fd; color: #1565c0; padding: 2px 8px; border-radius: 4px; font-weight: bold;">Under Review at AAAI 2027</span>] **Yuanjian Xu**, et al. *Rethinking Neural SDEs under Shifting Data-Generating Processes*. <span style="color: #d32f2f; font-weight: bold;">[CCF A]</span>

## In Progress

- [<span style="background-color: #fffde7; color: #f57f17; padding: 2px 8px; border-radius: 4px; font-weight: bold;">🚧 Target ICLR 2027</span>] **Yuanjian Xu**, et al. *Benchmarking Sample Reasoning Quality from Internal Geometric Dynamics in LLMs*. <span style="color: #d32f2f; font-weight: bold;">[CCF A]</span> <span style="color: #7b7b7b; font-style: italic;">(@ Tencent Hunyuan)</span>

- [<span style="background-color: #fffde7; color: #f57f17; padding: 2px 8px; border-radius: 4px; font-weight: bold;">🚧 Target ACL 2027</span>] **Yuanjian Xu**, et al. *The WoW: A Large-Scale World Knowledge Corpus for Full-Lifecycle LLM Training*. <span style="color: #d32f2f; font-weight: bold;">[CCF A]</span>
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
<p style="margin: 0.65em 0 0 0; color: #444; line-height: 1.65;">Working on quality assessment for unlabeled samples and the design of frontier agentic benchmarks.</p>
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
