# MathVerse 🔥: Does Your Multi-modal LLM Truly See the Diagrams in Visual Math Problems?

![MathQA](https://img.shields.io/badge/Task-MathQA-red) 
![Mathematical Reasoning](https://img.shields.io/badge/Task-Mathematical_Reasoning-red) 
![Multi-Modal](https://img.shields.io/badge/Task-Multi--Modal-red) 

![ChatGPT](https://img.shields.io/badge/Model-ChatGPT-green) 
![GPT-4](https://img.shields.io/badge/Model-GPT--4-green) 
![GPT-4V](https://img.shields.io/badge/Model-GPT--4V-green)
![Gemini](https://img.shields.io/badge/Model-Gemini-green)

Official repository for the paper "[MathVerse: Does Your Multi-modal LLM Truly See the Diagrams in Visual Math Problems?]()".

🌟 For more details, please refer to the project page with dataset exploration and visualization tools: [https://mathverse.github.io/](https://mathverse.github.io/).


[[🌐 Webpage](https://mathverse.github.io/)] [[📖 Paper]()] [[🤗 Huggingface Dataset]()] [[🏆 Leaderboard](https://mathverse.github.io/#leaderboard)] [[🔍 Visualization](https://mathvista.github.io/#visualization)]


## 💥 News

- **[2024.03.22]** 🚀 We release the [arXiv paper]() and some data samples in the [visualizer]().

## 📌 ToDo

- The *testmini* set of MathVerse will be released at [🤗 Huggingface] in a week.
- Coming soon: *CoT Evaluation results*, evaluation tools, and the entire MathVerse dataset

## 👀 About MathVerse

The capabilities of Multi-modal Large Language Models (MLLMs) in visual math problem-solving remain insufficiently evaluated and understood. We investigate current benchmarks to incorporate excessive visual content within textual questions, which potentially assist MLLMs in deducing answers without truly interpreting the input diagrams.

<p align="center">
    <img src="figs/fig1.png" width="70%"> <br>
</p>

To this end, we introduce **MathVerse**, an all-around visual math benchmark designed for an equitable and in-depth evaluation of MLLMs. We meticulously collect 2,612 high-quality, multi-subject math problems with diagrams from publicly available sources. Each problem is then transformed by human annotators into **six distinct versions**, each offering varying degrees of information content in multi-modality, contributing to **15K** test samples in total. This approach allows MathVerse to comprehensively assess ***whether and how much MLLMs can truly understand the visual diagrams for mathematical reasoning.*** 

<p align="center">
    <img src="figs/fig2.png" width="70%"> <br>
    Six different versions of each problem in <b>MathVerse</b> transformed by expert annotators.
</p>

In addition, we propose a **Chain-of-Thought (CoT) Evaluation strategy** for a fine-grained assessment of the output answers. Rather than naively judging True or False, we employ GPT-4(V) to adaptively extract crucial reasoning steps, and then score each step with detailed error analysis, which can reveal the intermediate CoT reasoning quality by MLLMs.

<p align="center">
    <img src="figs/fig3.png" width="70%"> <br>
    The two phases of the CoT evaluation strategy.
</p>

## 🏆 Leaderboard

### Contributing the Leaderboard

🚨🚨 The leaderboard is continuously being updated. 
