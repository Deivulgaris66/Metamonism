![Framework Version](https://img.shields.io/badge/version-v1.1_hybrid-blue) ![License](https://img.shields.io/badge/license-CC_BY_4.0-green) ![Status](https://img.shields.io/badge/status-active_development-yellow)
# Metamonism Project: Ontological Framework (v1.1 - Hybrid Structure)

![Framework Status](https://img.shields.io/badge/status-v1.1_structured-blue)
![License](https://img.shields.io/badge/license-CC_BY_4.0-blue)

## 🎯 Purpose & Dual-Channel Architecture

This repository is the **canonical source** for the Metamonism ontological framework. It implements a **dual-channel architecture**:

*   **H-channel** (`ARTICLES/H/`): Contains human-readable abstracts, metadata, and direct links to the canonical publications. Full articles (PDFs) are published on external, versioned platforms like Zenodo or PhilPapers and are referenced via immutable **DOIs**.
*   **M-channel** (`ARTICLES/M/`): Contains machine-readable specifications (YAML/JSON-LD) of the same articles. These files are optimized for AI indexing, programmatic access, and contain **explicit semantic links** to the foundational `CORE/` and the disciplinary models in `ONTODYNAMICS/`.

**Both channels are semantically equivalent and maintained in parallel.** The M-channel acts as the structured, queryable interface to the knowledge expressed in the H-channel.
## 🏗️ Repository Structure (Hybrid)
```
Metamonism/
├── ARTICLES/                    # BRIDGE: Parallel H and M versions
│   ├── H/                      # Human-readable channel
│   │   └── 01_Foundation/      # Article 1: "Metamonism as Foundation..."
│   │       ├── README.md       # Abstract, DOI link, context
│   │       └── meta.yaml       # Publication metadata
│   │
│   └── M/                      # Machine-readable channel
│       └── 01_Foundation/      # M-specification of Article 1
│           ├── README.md       # Structured summary
│           ├── specification.yaml # Core claims, arguments, links
│           └── references.yaml # Explicit links to CORE & ONTODYNAMICS
│
├── ONTODYNAMICS/                # KNOWLEDGE BASE: Thematic disciplinary models
│   ├── PHYSICS/                 # World 1: Physics
│   │   ├── manifest.yaml
│   │   ├── quantum_mechanics.yaml
│   │   └── thermodynamics.yaml
│   ├── COSMOLOGY/               # World 2: Cosmology
│   │   ├── manifest.yaml
│   │   ├── redshift.yaml
│   │   └── large_scale.yaml
│   └── CHEMISTRY/               # World 3: Chemistry
│       ├── manifest.yaml
│       └── bonding.yaml
│
├── CORE/                        # FOUNDATION: Immutable axioms & definitions
│   ├── axioms.yaml
│   ├── definitions.yaml
│   ├── operators.yaml
│   └── core_v1.0.md
│
├── KNOWLEDGE_GRAPH/             # SEMANTIC NETWORK (Auto-generated)
│   ├── README.md
│   ├── global_relations.jsonld
│   └── cross_reference.csv
│
└── CONTRIBUTING.md              # Contribution guidelines
```
### 📊 Knowledge Graph (Auto-Generated)

The `KNOWLEDGE_GRAPH/` directory is designed to contain **automatically generated semantic mappings** of all relationships within the framework.
*   **Source Data:** Relationships are declared within `ARTICLES/M/` specification files (in `references.yaml`) and `ONTODYNAMICS/` model manifests.
*   **Current Status:** The graph is **manually curated** during the development phase (v1.1). The placeholder files explain the intended structure.
*   **Future State:** Automation for generating `global_relations.jsonld` and `cross_reference.csv` from source files is **planned for a future version**.
*   **⚠️ Important:** Files in this directory should not be edited directly once automation is implemented; all edits should be made in the source specifications (`ARTICLES/M/`).

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
*   ## 🚀 Getting Started

### For Researchers & Philosophers
1.  Browse `ARTICLES/H/` to find article abstracts and publication metadata.
2.  Follow the **DOI link** in the article's `meta.yaml` to access the canonical, peer-reviewed PDF (e.g., on Zenodo).
3.  To explore the formal structure and connections of an idea, navigate to its parallel `ARTICLES/M/` specification.

### For Developers, Data Scientists & AI
This repository is structured as a machine-readable knowledge base.
```bash
# Example: Clone and inspect the core axioms
git clone https://github.com/Deivulgaris66/Metamonisn.git
cat Metamonism/CORE/axioms.yaml

# The primary entry points for parsing are:
# 1. CORE/axioms.yaml
# 2. ARTICLES/M/ (for the latest structured claims)
# 3. The manifest files in ONTODYNAMICS/*/manifest.yaml
```

### For Contributors
Please read the [`CONTRIBUTING.md`](./CONTRIBUTING.md) guide thoroughly. It explains the workflow for:
*   Proposing new or refined models in `ONTODYNAMICS/`.
*   Creating new machine specifications (M-versions) in `ARTICLES/M/`.
*   Suggesting changes to the immutable `CORE/`, which requires careful versioning.

---
**Ontology Architect:** Andrii Myshko (Metamonist)  
**Structure Version:** 1.1 (Hybrid)  
**Last Updated:** 2024-03-21  
**Contact:** Please use [GitHub Issues](https://github.com/Deivulgaris66/Metamonisn/issues) for discussion.
