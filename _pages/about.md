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

1. **Multimodal Data Selection:** Studying how data selection strategies should adapt to multimodal corpora with extremely low signal-to-noise ratios.
2. **Specialized Text Data Selection:** Understanding what domain-specific data, such as agentic trajectories and long-context documents, actually contributes to LLM training, and developing principled criteria for selecting examples that provide useful capabilities and learning signals.

<style>
.lifecycle-board {
  margin: 1.5em 0 1.85em;
  padding: 1.15em 1.25em 1.2em;
  background: linear-gradient(180deg, #fafcfe 0%, #f4f8fc 100%);
  border: 1px solid #e2eaf3;
  border-radius: 12px;
}
.lifecycle-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 0.5em;
  margin-bottom: 1em;
}
.lifecycle-title {
  color: #1e293b;
  font-size: 0.78em;
  font-weight: 750;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}
.lifecycle-subtitle {
  color: #64748b;
  font-size: 0.75em;
}
.lifecycle-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 0.75em;
  align-items: stretch;
}
.stage-card {
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 10px;
  padding: 0.85em 0.9em;
  box-shadow: 0 1px 3px rgba(15, 23, 42, 0.03);
}
.stage-card:not(:last-child)::after {
  content: "→";
  position: absolute;
  right: -0.62em;
  top: 50%;
  transform: translateY(-50%);
  width: 1.1em;
  height: 1.1em;
  border-radius: 50%;
  background: #ffffff;
  border: 1px solid #cbd5e1;
  color: #64748b;
  font-size: 0.72em;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 2;
}
.stage-card.active {
  background: linear-gradient(180deg, #eff6ff 0%, #ffffff 100%);
  border-color: #93c5fd;
  box-shadow: 0 3px 10px rgba(25, 118, 210, 0.08);
}
.stage-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.4em;
  margin-bottom: 0.55em;
}
.stage-name {
  color: #0f172a;
  font-size: 0.88em;
  font-weight: 750;
}
.stage-card.active .stage-name {
  color: #1976d2;
}
.stage-step {
  font-size: 0.65em;
  font-weight: 700;
  color: #64748b;
  background: #f1f5f9;
  padding: 0.15em 0.5em;
  border-radius: 999px;
}
.stage-card.active .stage-step {
  color: #1976d2;
  background: #dbeafe;
}
.stage-papers {
  display: flex;
  flex-direction: column;
  gap: 0.4em;
}
.stage-paper {
  font-size: 0.76em;
  line-height: 1.4;
  color: #475569;
  padding-left: 0.55em;
  border-left: 2px solid #cbd5e1;
}
.stage-card.active .stage-paper {
  border-left-color: #1976d2;
}
.stage-paper strong {
  color: #1e293b;
}
.stage-venue {
  margin-top: 0.65em;
  padding-top: 0.45em;
  border-top: 1px dashed #e2e8f0;
  color: #94a3b8;
  font-size: 0.66em;
  font-weight: 650;
  letter-spacing: 0.03em;
}
.stage-card.active .stage-venue {
  color: #1976d2;
}
@media (max-width: 720px) {
  .lifecycle-grid {
    grid-template-columns: 1fr;
    gap: 0.65em;
  }
  .stage-card:not(:last-child)::after {
    content: "↓";
    right: auto;
    left: 50%;
    top: auto;
    bottom: -0.68em;
    transform: translateX(-50%);
  }
}
</style>

<div class="lifecycle-board" aria-label="Research across the LLM training lifecycle" markdown="0">
  <div class="lifecycle-header">
    <span class="lifecycle-title">Research Across the LLM Training Lifecycle</span>
    <span class="lifecycle-subtitle">From earlier stage-specific selection to multimodal &amp; specialized data</span>
  </div>
  <div class="lifecycle-grid">
    <div class="stage-card">
      <div>
        <div class="stage-top">
          <span class="stage-name">Pre-training</span>
          <span class="stage-step">Stage 1</span>
        </div>
        <div class="stage-papers">
          <div class="stage-paper"><strong>DoGraph</strong> · Stable training</div>
          <div class="stage-paper"><strong>D<sup>3</sup></strong> · Sample ordering</div>
        </div>
      </div>
      <div class="stage-venue">ACL 2026 · ICML 2026</div>
    </div>
    <div class="stage-card">
      <div>
        <div class="stage-top">
          <span class="stage-name">Annealing</span>
          <span class="stage-step">Stage 2</span>
        </div>
        <div class="stage-papers">
          <div class="stage-paper"><strong>DirEct</strong> · Principled sample selection</div>
        </div>
      </div>
      <div class="stage-venue">ICML 2026 Spotlight</div>
    </div>
    <div class="stage-card">
      <div>
        <div class="stage-top">
          <span class="stage-name">SFT</span>
          <span class="stage-step">Stage 3</span>
        </div>
        <div class="stage-papers">
          <div class="stage-paper"><strong>HardPT</strong> · Hard-sample tuning</div>
          <div class="stage-paper"><strong>CUBE</strong> · Reasoning quality assessment</div>
        </div>
      </div>
      <div class="stage-venue">ACL 2023 · ICLR 2027 Under Review</div>
    </div>
    <div class="stage-card active">
      <div>
        <div class="stage-top">
          <span class="stage-name">Current Focus</span>
          <span class="stage-step">Ongoing</span>
        </div>
        <div class="stage-papers">
          <div class="stage-paper"><strong>Multimodal</strong> · Cross-modal selection</div>
          <div class="stage-paper"><strong>Specialized Text</strong> · Long-context &amp; agentic</div>
        </div>
      </div>
      <div class="stage-venue">Full-Lifecycle Quality</div>
    </div>
  </div>
</div>

My work has been published at venues including **NeurIPS 2026**, **ICML 2026** (one paper selected as <span style="background-color: #fff3e0; color: #e65100; padding: 2px 8px; border-radius: 4px; font-weight: bold;">🏆 Spotlight</span>), **ACL 2026**, **ACL 2023**, **ACL 2025**, **ICAIF 2025**, and **ICASSP 2026** (<span style="background-color: #fff3e0; color: #e65100; padding: 2px 8px; border-radius: 4px; font-weight: bold;">🏆 Oral</span>). I also serve as a reviewer for leading conferences such as **NeurIPS**, **ICLR**, and **ICML** (selected as <span style="background-color: #fff3e0; color: #e65100; padding: 2px 8px; border-radius: 4px; font-weight: bold;">🏆 Gold Reviewer</span>).

<!-- <hr style="border: 2px solid #ccc; margin: 2em 0;"> -->

<style>
.publication-showcase {
  display: grid;
  gap: 1rem;
  margin: 1rem 0 1.7rem;
}
.publication-card {
  display: grid;
  grid-template-columns: minmax(260px, 0.95fr) minmax(0, 1.15fr);
  overflow: hidden;
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 14px;
  box-shadow: 0 3px 14px rgba(15, 23, 42, 0.05);
  transition: transform 0.18s ease, box-shadow 0.18s ease;
}
.publication-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(15, 23, 42, 0.09);
}
.publication-card__media {
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 0.55rem;
  min-height: 215px;
  margin: 0;
  padding: 1rem;
  background: linear-gradient(145deg, #f8fafc 0%, #eef4f9 100%);
  border-right: 1px solid #e2e8f0;
}
.publication-card__media img {
  display: block;
  width: 100%;
  max-height: 255px;
  object-fit: contain;
  transition: transform 0.18s ease;
}
.publication-card:hover .publication-card__media img {
  transform: scale(1.012);
}
.publication-card__media figcaption {
  color: #64748b;
  font-size: 0.69em;
  line-height: 1.35;
  text-align: center;
}
.publication-card__body {
  align-self: center;
  padding: 1.05rem 1.15rem 1.1rem;
}
.publication-card__tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.38rem;
  margin-bottom: 0.65rem;
}
.publication-tag {
  padding: 0.18rem 0.52rem;
  border-radius: 999px;
  font-size: 0.65em;
  font-weight: 750;
  line-height: 1.35;
}
.publication-tag--published {
  color: #b42318;
  background: #ffebe9;
}
.publication-tag--review {
  color: #175cd3;
  background: #eaf2ff;
}
.publication-tag--rank {
  color: #475467;
  background: #f2f4f7;
}
.publication-card__body h3 {
  margin: 0 0 0.42rem;
  color: #172033;
  font-size: 0.98em;
  line-height: 1.38;
}
.publication-card__authors {
  margin: 0 0 0.55rem;
  color: #667085;
  font-size: 0.76em;
  line-height: 1.45;
}
.publication-card__summary {
  margin: 0;
  color: #475467;
  font-size: 0.79em;
  line-height: 1.58;
}
.publication-card__links {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  margin-top: 0.72rem;
}
.publication-card__links a {
  color: #1976d2;
  font-size: 0.73em;
  font-weight: 700;
  text-decoration: none;
}
.publication-card__links a:hover {
  text-decoration: underline;
}
.publication-notes {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 0.75rem;
  margin: 0.9rem 0 1.7rem;
}
.publication-note {
  padding: 0.9rem 1rem;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-left: 3px solid #93c5fd;
  border-radius: 10px;
}
.publication-note h3 {
  margin: 0.48rem 0 0.34rem;
  color: #27364b;
  font-size: 0.84em;
  line-height: 1.4;
}
.publication-note p {
  margin: 0;
  color: #667085;
  font-size: 0.73em;
  line-height: 1.5;
}
.publication-note .publication-card__links {
  margin-top: 0.5rem;
}
@media (max-width: 760px) {
  .publication-card {
    grid-template-columns: 1fr;
  }
  .publication-card__media {
    min-height: 0;
    border-right: 0;
    border-bottom: 1px solid #e2e8f0;
  }
  .publication-card__media img {
    max-height: 230px;
  }
  .publication-notes {
    grid-template-columns: 1fr;
  }
}
</style>

## 📝 Selected Publications (Data Strategy)

<div class="publication-showcase" aria-label="Selected data strategy publications">
  <article class="publication-card">
    <figure class="publication-card__media">
      <a href="https://arxiv.org/abs/2605.31164" target="_blank" rel="noopener">
        <img src="{{ '/static/publication-figures/d3.webp' | relative_url }}" alt="D3 influence-aware data scheduling framework" loading="lazy">
      </a>
      <figcaption>Figure 1. Influence-aware scheduling from pairwise batch interactions to a learned training order.</figcaption>
    </figure>
    <div class="publication-card__body">
      <div class="publication-card__tags">
        <span class="publication-tag publication-tag--published">ICML 2026</span>
        <span class="publication-tag publication-tag--rank">CCF A · CORE A*</span>
      </div>
      <h3>D<sup>3</sup>: Dynamic Directional Graph-Constrained Data Scheduling for LLM Training</h3>
      <p class="publication-card__authors"><strong>Yuanjian Xu</strong>, et al. · MSRA</p>
      <p class="publication-card__summary">D<sup>3</sup> models gradient and curvature interactions between micro-batches as a directional graph, then solves for a training order that improves the optimization trajectory.</p>
      <div class="publication-card__links">
        <a href="https://arxiv.org/abs/2605.31164" target="_blank" rel="noopener"><i class="fas fa-file-pdf"></i> Paper</a>
        <a href="https://github.com/xuyj233/D3" target="_blank" rel="noopener"><i class="fab fa-github"></i> Code</a>
      </div>
    </div>
  </article>

  <article class="publication-card">
    <figure class="publication-card__media">
      <a href="https://arxiv.org/abs/2605.31175" target="_blank" rel="noopener">
        <img src="{{ '/static/publication-figures/direct.webp' | relative_url }}" alt="Geometric comparison of stable training and annealing" loading="lazy">
      </a>
      <figcaption>Figure 1. Annealing suppresses transverse noise while preserving the useful descent signal.</figcaption>
    </figure>
    <div class="publication-card__body">
      <div class="publication-card__tags">
        <span class="publication-tag publication-tag--published">ICML 2026 Spotlight 🏆</span>
        <span class="publication-tag publication-tag--rank">CCF A · CORE A*</span>
      </div>
      <h3>Towards Efficient LLMs Annealing with Principled Sample Selection</h3>
      <p class="publication-card__authors"><strong>Yuanjian Xu</strong>, et al. · MSRA</p>
      <p class="publication-card__summary">DirEct characterizes the geometry of LLM annealing and selects samples that reduce sharp-direction noise while strengthening progress along the low-curvature valley.</p>
      <div class="publication-card__links">
        <a href="https://arxiv.org/abs/2605.31175" target="_blank" rel="noopener"><i class="fas fa-file-pdf"></i> Paper</a>
        <a href="https://github.com/xuyj233/Direct" target="_blank" rel="noopener"><i class="fab fa-github"></i> Code</a>
      </div>
    </div>
  </article>

  <article class="publication-card">
    <figure class="publication-card__media">
      <a href="https://aclanthology.org/2026.acl-short.28/" target="_blank" rel="noopener">
        <img src="{{ '/static/publication-figures/dograph.webp' | relative_url }}" alt="PCA projections of domain gradients across training epochs" loading="lazy">
      </a>
      <figcaption>Figure 1. Domain-specific gradient clusters gradually overlap as training proceeds.</figcaption>
    </figure>
    <div class="publication-card__body">
      <div class="publication-card__tags">
        <span class="publication-tag publication-tag--published">ACL 2026</span>
        <span class="publication-tag publication-tag--rank">CCF A · CORE A*</span>
      </div>
      <h3>Rethinking Data Mixing from the Perspective of Large Language Models</h3>
      <p class="publication-card__authors"><strong>Yuanjian Xu</strong>, et al.</p>
      <p class="publication-card__summary">The paper connects domain distributions with gradient dynamics. DoGraph uses these relationships to optimize data mixing and explain how domain weighting affects generalization.</p>
      <div class="publication-card__links">
        <a href="https://aclanthology.org/2026.acl-short.28/" target="_blank" rel="noopener"><i class="fas fa-file-pdf"></i> Paper</a>
      </div>
    </div>
  </article>

  <article class="publication-card">
    <figure class="publication-card__media">
      <a href="https://aclanthology.org/2023.acl-long.690/" target="_blank" rel="noopener">
        <img src="{{ '/static/publication-figures/hardpt.webp' | relative_url }}" alt="HardPT sample stratification and adaptive contrastive learning architecture" loading="lazy">
      </a>
      <figcaption>Figure 1. HardPT separates easy, hard, and misleading samples, then constructs contrastive supervision.</figcaption>
    </figure>
    <div class="publication-card__body">
      <div class="publication-card__tags">
        <span class="publication-tag publication-tag--published">ACL 2023</span>
        <span class="publication-tag publication-tag--rank">CCF A · CORE A*</span>
      </div>
      <h3>Hard Sample Aware Prompt-Tuning</h3>
      <p class="publication-card__authors"><strong>Yuanjian Xu</strong>, et al. · THU AIR</p>
      <p class="publication-card__summary">HardPT identifies examples that provide useful difficulty and builds adaptive contrastive batches so prompt-tuning focuses on informative hard samples.</p>
      <div class="publication-card__links">
        <a href="https://aclanthology.org/2023.acl-long.690/" target="_blank" rel="noopener"><i class="fas fa-file-pdf"></i> Paper</a>
      </div>
    </div>
  </article>

  <article class="publication-card">
    <figure class="publication-card__media">
      <a href="https://github.com/xuyj233/data_strategy_survey" target="_blank" rel="noopener">
        <img src="{{ '/static/publication-figures/survey.webp' | relative_url }}" alt="Landscape of data strategies across the LLM training lifecycle" loading="lazy">
      </a>
      <figcaption>Survey overview. The landscape connects pretraining and post-training data strategies across the LLM lifecycle.</figcaption>
    </figure>
    <div class="publication-card__body">
      <div class="publication-card__tags">
        <span class="publication-tag publication-tag--review">Under Review at ACL 2027 · Survey</span>
        <span class="publication-tag publication-tag--rank">CCF A · CORE A*</span>
      </div>
      <h3>Data Strategy in Action: Identifying High-Quality Corpora Across the LLM Training Lifecycle</h3>
      <p class="publication-card__authors"><strong>Yuanjian Xu</strong>, et al.</p>
      <p class="publication-card__summary">This survey organizes data strategies by training stage and decision granularity, showing how quality criteria and selection policies evolve across the full LLM training lifecycle.</p>
      <div class="publication-card__links">
        <a href="https://github.com/xuyj233/data_strategy_survey" target="_blank" rel="noopener"><i class="fab fa-github"></i> Survey Resources</a>
      </div>
    </div>
  </article>

  <article class="publication-card">
    <figure class="publication-card__media">
      <img src="{{ '/static/publication-figures/cube.webp' | relative_url }}" alt="CUBE geometric signatures illustrated with Rubik's cube trajectories" loading="lazy">
      <figcaption>Method overview. Directness, update scale, and early settling describe the internal geometry of reasoning.</figcaption>
    </figure>
    <div class="publication-card__body">
      <div class="publication-card__tags">
        <span class="publication-tag publication-tag--review">Under Review at ICLR 2027</span>
        <span class="publication-tag publication-tag--rank">CCF A · CORE A*</span>
      </div>
      <h3>CUBE: Benchmarking Sample Reasoning Quality from Internal Geometric Dynamics in LLMs</h3>
      <p class="publication-card__authors"><strong>Yuanjian Xu</strong>, et al. · Tencent Hunyuan</p>
      <p class="publication-card__summary">CUBE evaluates reasoning samples through layerwise geometric dynamics, measuring whether internal trajectories are direct, substantive, and convergent.</p>
    </div>
  </article>
</div>

<div class="publication-notes" aria-label="Additional selected data strategy publications">
  <article class="publication-note">
    <span class="publication-tag publication-tag--published">NeurIPS 2026</span>
    <h3>Rethinking Knowledge Distillation for Diffusion Language Models</h3>
    <p>Yuxuan Sun, <strong>Yuanjian Xu</strong>, et al. We study why classical distillation fails for diffusion language models and develop a more effective off-policy and on-policy framework.</p>
    <div class="publication-card__links">
      <a href="https://neurips.cc/virtual/2026/poster/152596" target="_blank" rel="noopener"><i class="fas fa-file-alt"></i> Abstract</a>
    </div>
  </article>
  <article class="publication-note">
    <span class="publication-tag publication-tag--review">Under Review at ICLR 2027</span>
    <h3>Structured Reasoning for Large Language Models</h3>
    <p>Jinyi Han, Zixiang Di, Zishang Jiang, Ying Liao, Jianing Hao, <strong>Yuanjian Xu</strong>, Yanghua Xiao. We study quality assessment for structured chain-of-thought supervision.</p>
  </article>
</div>

## 📝 Selected Publications (Corpora & Benchmarks)

<div class="publication-showcase" aria-label="Selected corpora and benchmark publications">
  <article class="publication-card">
    <figure class="publication-card__media">
      <a href="https://aclanthology.org/2026.findings-acl.1198/" target="_blank" rel="noopener">
        <img src="{{ '/static/publication-figures/bizcompass.webp' | relative_url }}" alt="BizCompass benchmark construction pipeline" loading="lazy">
      </a>
      <figcaption>Figure 1. BizCompass turns business documents into validated, high-quality reasoning questions.</figcaption>
    </figure>
    <div class="publication-card__body">
      <div class="publication-card__tags">
        <span class="publication-tag publication-tag--published">ACL 2026</span>
        <span class="publication-tag publication-tag--rank">CCF A · CORE A*</span>
      </div>
      <h3>BizCompass: Benchmarking the Reasoning Capabilities of LLMs in Business Knowledge and Applications</h3>
      <p class="publication-card__authors"><strong>Yuanjian Xu</strong>, et al.</p>
      <p class="publication-card__summary">BizCompass provides a construction and validation pipeline for evaluating LLM reasoning across business knowledge and application scenarios.</p>
      <div class="publication-card__links">
        <a href="https://aclanthology.org/2026.findings-acl.1198/" target="_blank" rel="noopener"><i class="fas fa-file-pdf"></i> Paper</a>
        <a href="https://github.com/CatherineHao/BizCompass" target="_blank" rel="noopener"><i class="fab fa-github"></i> Code</a>
      </div>
    </div>
  </article>

  <article class="publication-card">
    <figure class="publication-card__media">
      <a href="https://aclanthology.org/2025.findings-acl.489/" target="_blank" rel="noopener">
        <img src="{{ '/static/publication-figures/finripple.webp' | relative_url }}" alt="FinRipple knowledge graph construction, injection, and market alignment framework" loading="lazy">
      </a>
      <figcaption>Figure 2. FinRipple connects time-varying knowledge graphs, instruction tuning, and market alignment.</figcaption>
    </figure>
    <div class="publication-card__body">
      <div class="publication-card__tags">
        <span class="publication-tag publication-tag--published">ACL 2025</span>
        <span class="publication-tag publication-tag--rank">CCF A · CORE A*</span>
      </div>
      <h3>FinRipple: Aligning Large Language Models with Financial Market for Event Ripple Effect Awareness</h3>
      <p class="publication-card__authors"><strong>Yuanjian Xu</strong>, et al.</p>
      <p class="publication-card__summary">FinRipple defines event ripple effect prediction and aligns LLMs with dynamic market structure through knowledge graph injection and market-feedback optimization.</p>
      <div class="publication-card__links">
        <a href="https://aclanthology.org/2025.findings-acl.489/" target="_blank" rel="noopener"><i class="fas fa-file-pdf"></i> Paper</a>
        <a href="https://github.com/CatherineHao/FinRipple" target="_blank" rel="noopener"><i class="fab fa-github"></i> Code</a>
      </div>
    </div>
  </article>

  <article class="publication-card">
    <figure class="publication-card__media">
      <a href="https://arxiv.org/abs/2608.04828" target="_blank" rel="noopener">
        <img src="{{ '/static/publication-figures/skilluse.webp' | relative_url }}" alt="Composition and domain coverage of the Skill-Use benchmark" loading="lazy">
      </a>
      <figcaption>Figure 1. Skill-Use covers 79 skills across nine domains with rubric-based agent evaluation.</figcaption>
    </figure>
    <div class="publication-card__body">
      <div class="publication-card__tags">
        <span class="publication-tag publication-tag--review">Under Review at ACL 2027</span>
        <span class="publication-tag publication-tag--rank">CCF A · CORE A*</span>
      </div>
      <h3>Skill-Use: Can LLMs Actually Use Skills in Agentic Harnesses?</h3>
      <p class="publication-card__authors">Jinyi Han*, <strong>Yuanjian Xu*</strong>, et al. · Equal contribution · Tencent Hunyuan</p>
      <p class="publication-card__summary">Skill-Use evaluates whether LLM agents can recognize, invoke, and correctly apply reusable skills, rather than merely solving tasks from parametric knowledge.</p>
      <div class="publication-card__links">
        <a href="https://arxiv.org/abs/2608.04828" target="_blank" rel="noopener"><i class="fas fa-file-pdf"></i> Paper</a>
        <a href="https://github.com/JinyiHan99/Skill-Use-Bench" target="_blank" rel="noopener"><i class="fab fa-github"></i> Code</a>
      </div>
    </div>
  </article>
</div>

<div class="publication-notes" aria-label="Additional selected benchmark publications">
  <article class="publication-note">
    <span class="publication-tag publication-tag--review">Under Review at ACL 2027</span>
    <h3>Can LLMs Stay Robust in Noisy Agentic Environments?</h3>
    <p><strong>Yuanjian Xu</strong>, et al. We evaluate how agentic systems behave when observations and interaction signals are noisy.</p>
  </article>
  <article class="publication-note">
    <span class="publication-tag publication-tag--review">Under Review at ACL 2027</span>
    <h3>Bridging Foundational and Agentic Capabilities of LLMs</h3>
    <p>Wei Guo, <strong>Yuanjian Xu</strong>, et al. We study how foundational language capabilities relate to performance on agentic tasks.</p>
  </article>
</div>

</div>
</div>

<div id="publications" class="content-section">

<div markdown="1">
<span class='anchor' id='-publications'></span>



## Other Papers

- [<span style="background-color: #ffebee; color: #c62828; padding: 2px 8px; border-radius: 4px; font-weight: bold;">ICASSP 2026 Oral 🏆</span>] **Yuanjian Xu**, et al. *HGAN-SDEs: Learning Neural Stochastic Differential Equations with Hermite-Guided Adversarial Training* [<a href="https://arxiv.org/abs/2512.20272" style="color: #1976d2;"><i class="fas fa-file-pdf"></i> Paper</a>]. <span style="color: #d32f2f; font-weight: bold;">[CCF B]</span> <span style="color: #d32f2f; font-weight: bold;">[CORE A]</span>

- [<span style="background-color: #ffebee; color: #c62828; padding: 2px 8px; border-radius: 4px; font-weight: bold;">ICAIF 2025</span>] **Yuanjian Xu**, et al. *LENS: Large Pre-trained Transformer for Exploring Financial Time Series Regularities* [<a href="https://arxiv.org/abs/2408.10111" style="color: #1976d2;"><i class="fas fa-file-pdf"></i> Paper</a>]. <span style="color: #7b7b7b; font-style: italic;">(Leading conference for AI in Finance)</span>

- [<span style="background-color: #e3f2fd; color: #1565c0; padding: 2px 8px; border-radius: 4px; font-weight: bold;">Under Review at AAAI 2027</span>] **Yuanjian Xu**, et al. *Rethinking Neural SDEs under Shifting Data-Generating Processes*. <span style="color: #d32f2f; font-weight: bold;">[CCF A]</span>
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
