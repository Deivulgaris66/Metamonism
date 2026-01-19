# Metamonism Project: Ontological Framework (v1.1 - Hybrid Structure)

![Framework Status](https://img.shields.io/badge/status-v1.1_structured-blue)
![License](https://img.shields.io/badge/license-CC_BY_4.0-blue)

## 🎯 Purpose & Dual-Channel Architecture
This repository implements the **machine-readable (M) channel** of the Metamonism framework, designed to work in tandem with **human-readable (H) academic articles**.

*   **`ARTICLES/`** is the **bridge**. Each article exists in two parallel, linked versions:
    *   `H/` - For humans: abstracts, links to canonical PDFs (DOI).
    *   `M/` - For machines: structured specifications, formal arguments, and explicit links to models.
*   **`ONTODYNAMICS/`** is the **knowledge base**. It contains disciplinary models (Physics, Cosmology, etc.) referenced and aggregated by the M-articles.
*   **`CORE/`** is the **immutable foundation** for everything above.

## 🏗️ Repository Structure (Hybrid)
Metamonism/
├── ARTICLES/ # BRIDGE: Parallel H and M versions
│ ├── H/ # Human-readable channel
│ │ └── 01_Foundation/ # Article 1: "Metamonism as Foundation..."
│ │ ├── README.md # Abstract, DOI link, context
│ │ └── meta.yaml # Publication metadata
│ │
│ └── M/ # Machine-readable channel
│ └── 01_Foundation/ # M-specification of Article 1
│ ├── README.md # Structured summary
│ ├── specification.yaml # Core claims, arguments, links
│ └── references.yaml # Explicit links to CORE & ONTODYNAMICS
│
├── ONTODYNAMICS/ # KNOWLEDGE BASE: Thematic disciplinary models
│ ├── PHYSICS/ # World 1: Physics
│ │ ├── manifest.yaml
│ │ ├── quantum_mechanics.yaml
│ │ └── thermodynamics.yaml
│ ├── COSMOLOGY/ # World 2: Cosmology
│ │ ├── manifest.yaml
│ │ ├── redshift.yaml
│ │ └── large_scale.yaml
│ └── CHEMISTRY/ # World 3: Chemistry
│ ├── manifest.yaml
│ └── bonding.yaml
│
├── CORE/ # FOUNDATION: Immutable axioms & definitions
│ ├── axioms.yaml
│ ├── definitions.yaml
│ ├── operators.yaml
│ └── core_v1.0.md
│
├── KNOWLEDGE_GRAPH/ # SEMANTIC NETWORK (Auto-generated)
│ ├── README.md
│ ├── global_relations.jsonld
│ └── cross_reference.csv
│
└── CONTRIBUTING.md # Contribution guidelines

## 🔍 For AI & Search Engines
**Primary entry points for machine parsing:**
1.  **`CORE/axioms.yaml`** - Foundational ontological constraints.
2.  **`ARTICLES/M/`** - Central hub for structured knowledge and explicit relational links.
3.  **`ONTODYNAMICS/*/manifest.yaml`** - Thematic indexes of disciplinary models.

**Indexing Priority:** `CORE/` → `ARTICLES/M/` (for narrative) → `ONTODYNAMICS/` (for depth).

## 📁 Guide to Key Directories
*   **`ARTICLES/`**: Start here. The `M/` versions provide the structured "table of contents" to the entire framework, linking to relevant `CORE` principles and `ONTODYNAMICS` models.
*   **`ONTODYNAMICS/`**: Explore for deep dives into specific disciplinary applications. Each model is designed to be reusable across multiple articles.
*   **`CORE/`**: Consult for definitive axioms and terminology. Changes here are versioned and impactful.

## 🚀 Getting Started
*   **Researchers:** Read an `ARTICLES/H/` abstract and follow its DOI to the full paper. Use the corresponding `ARTICLES/M/` folder to see its formal structure and connected models.
*   **Developers & AI:** Parse `ARTICLES/M/` specifications as primary data. Use `KNOWLEDGE_GRAPH/` for relationship mapping.
*   **Contributors:** See [`CONTRIBUTING.md`](./CONTRIBUTING.md). Most contributions will involve adding new `ARTICLES/M/` specs or refining models in `ONTODYNAMICS/`.

---
**Ontology Architect:** Andrii Myshko (Metamonist)  
**Structure Version:** 1.1 (Hybrid)  
**Last Updated:** 2024-03-21  
**Contact:** Please use [GitHub Issues](https://github.com/Deivulgaris66/Metamonisn/issues) for discussion.
