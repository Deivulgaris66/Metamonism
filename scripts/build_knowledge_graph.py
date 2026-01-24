#!/usr/bin/env python3
"""
build_knowledge_graph.py v0.1
Minimal ontological compiler: ARTICLES/M → KNOWLEDGE_GRAPH

This is NOT a feature-complete RDF generator.
This is a proof that the contract works mechanically.

Functionality:
1. Load CORE/relations.yaml (canonical relation types)
2. Parse ARTICLES/M/*.yaml (extract semantic_relations)
3. Validate: relation exists in CORE
4. Emit minimal JSON-LD to KNOWLEDGE_GRAPH/global_relations.jsonld
5. Emit CSV to KNOWLEDGE_GRAPH/cross_reference.csv

Version: 0.1 (ontological minimum)
Status: Proof of concept
"""

import yaml
import json
import csv
from pathlib import Path
from typing import List, Dict, Set
import sys

# =============================================================================
# CONFIGURATION
# =============================================================================

CORE_DIR = Path("CORE")
ARTICLES_M_DIR = Path("ARTICLES/M")
KNOWLEDGE_GRAPH_DIR = Path("KNOWLEDGE_GRAPH")

RELATIONS_FILE = CORE_DIR / "relations.yaml"
OUTPUT_JSONLD = KNOWLEDGE_GRAPH_DIR / "global_relations.jsonld"
OUTPUT_CSV = KNOWLEDGE_GRAPH_DIR / "cross_reference.csv"

# =============================================================================
# STEP 1: LOAD CANONICAL RELATIONS
# =============================================================================

def load_canonical_relations() -> Set[str]:
    """Load the set of admissible relation types from CORE/relations.yaml"""
    print("📖 Loading CORE/relations.yaml...")
    
    if not RELATIONS_FILE.exists():
        print(f"❌ ERROR: {RELATIONS_FILE} not found")
        sys.exit(1)
    
    with open(RELATIONS_FILE, 'r', encoding='utf-8') as f:
        relations_data = yaml.safe_load(f)
    
    # Extract relation names from the 'relations' section
    canonical_relations = set(relations_data.get('relations', {}).keys())
    
    print(f"✅ Loaded {len(canonical_relations)} canonical relations:")
    for rel in sorted(canonical_relations):
        print(f"   • {rel}")
    
    return canonical_relations

# =============================================================================
# STEP 2: PARSE ARTICLES/M
# =============================================================================

def parse_articles() -> List[Dict]:
    """Parse all YAML files in ARTICLES/M and extract semantic_relations"""
    print(f"\n📖 Parsing articles in {ARTICLES_M_DIR}...")
    
    if not ARTICLES_M_DIR.exists():
        print(f"⚠️  WARNING: {ARTICLES_M_DIR} does not exist")
        return []
    
    all_relations = []
    article_files = list(ARTICLES_M_DIR.glob("*.yaml"))
    
    if not article_files:
        print(f"⚠️  No .yaml files found in {ARTICLES_M_DIR}")
        return []
    
    for article_file in article_files:
        # Skip template
        if article_file.name == "TEMPLATE.yaml":
            continue
            
        print(f"  📄 Processing {article_file.name}...")
        
        try:
            with open(article_file, 'r', encoding='utf-8') as f:
                article_data = yaml.safe_load(f)
            
            # Extract semantic_relations section
            sem_rels = article_data.get('semantic_relations', [])
            
            if not sem_rels:
                print(f"     ⚠️  No semantic_relations found")
                continue
            
            # Add source file info to each relation
            for rel in sem_rels:
                rel['source_file'] = str(article_file)
                all_relations.append(rel)
            
            print(f"     ✅ Extracted {len(sem_rels)} relations")
            
        except Exception as e:
            print(f"     ❌ ERROR parsing {article_file.name}: {e}")
            continue
    
    print(f"\n✅ Total relations extracted: {len(all_relations)}")
    return all_relations

# =============================================================================
# STEP 3: VALIDATE RELATIONS
# =============================================================================

def validate_relations(relations: List[Dict], canonical_relations: Set[str]) -> List[Dict]:
    """Validate that all relations are in CORE/relations.yaml"""
    print("\n🔍 Validating relations...")
    
    valid_relations = []
    errors = []
    
    for i, rel in enumerate(relations, 1):
        relation_type = rel.get('relation')
        subject = rel.get('subject')
        obj = rel.get('object')
        source = rel.get('source_file', 'unknown')
        
        # Check required fields
        if not all([relation_type, subject, obj]):
            errors.append(f"  ❌ Relation #{i}: Missing required fields (subject/relation/object)")
            continue
        
        # Check if relation exists in canonical set
        if relation_type not in canonical_relations:
            errors.append(
                f"  ❌ Relation #{i}: Unknown relation '{relation_type}'\n"
                f"     Source: {source}\n"
                f"     Must be one of: {', '.join(sorted(canonical_relations))}"
            )
            continue
        
        # If valid, add to valid set
        valid_relations.append(rel)
        print(f"  ✅ {subject} --{relation_type}→ {obj}")
    
    # Report errors
    if errors:
        print(f"\n⚠️  Validation errors found:")
        for error in errors:
            print(error)
    
    print(f"\n✅ Valid relations: {len(valid_relations)}/{len(relations)}")
    
    if errors and len(valid_relations) == 0:
        print("❌ No valid relations found. Aborting.")
        sys.exit(1)
    
    return valid_relations

# =============================================================================
# STEP 4: EMIT JSON-LD
# =============================================================================

def emit_jsonld(relations: List[Dict]):
    """Generate minimal JSON-LD graph"""
    print(f"\n📝 Generating {OUTPUT_JSONLD}...")
    
    # Group relations by subject
    graph_nodes = {}
    
    for rel in relations:
        subject = rel['subject']
        relation = rel['relation']
        obj = rel['object']
        
        if subject not in graph_nodes:
            graph_nodes[subject] = {"@id": subject}
        
        # Add relation as property
        if relation not in graph_nodes[subject]:
            graph_nodes[subject][relation] = []
        
        graph_nodes[subject][relation].append(obj)
    
    # Construct JSON-LD
    jsonld = {
        "@context": {
            "@vocab": "https://metamonism.org/relations/",
            "defines": "https://metamonism.org/relations/defines",
            "derives_from": "https://metamonism.org/relations/derives_from",
            "uses_operator": "https://metamonism.org/relations/uses_operator",
            "contradicts": "https://metamonism.org/relations/contradicts",
            "isomorphic_to": "https://metamonism.org/relations/isomorphic_to",
            "maps_to": "https://metamonism.org/relations/maps_to",
            "refines": "https://metamonism.org/relations/refines",
            "predicts": "https://metamonism.org/relations/predicts",
            "explains": "https://metamonism.org/relations/explains",
            "composes_with": "https://metamonism.org/relations/composes_with"
        },
        "@graph": list(graph_nodes.values())
    }
    
    # Write to file
    KNOWLEDGE_GRAPH_DIR.mkdir(parents=True, exist_ok=True)
    
    with open(OUTPUT_JSONLD, 'w', encoding='utf-8') as f:
        json.dump(jsonld, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Generated {len(graph_nodes)} nodes in JSON-LD")

# =============================================================================
# STEP 5: EMIT CSV
# =============================================================================

def emit_csv(relations: List[Dict]):
    """Generate human-readable cross-reference CSV"""
    print(f"\n📝 Generating {OUTPUT_CSV}...")
    
    KNOWLEDGE_GRAPH_DIR.mkdir(parents=True, exist_ok=True)
    
    with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['subject', 'relation', 'object', 'source_file'])
        
        for rel in relations:
            writer.writerow([
                rel['subject'],
                rel['relation'],
                rel['object'],
                Path(rel['source_file']).name
            ])
    
    print(f"✅ Generated {len(relations)} rows in CSV")

# =============================================================================
# MAIN
# =============================================================================

def main():
    print("=" * 70)
    print("KNOWLEDGE_GRAPH Builder v0.1")
    print("Ontological minimum: ARTICLES/M → KNOWLEDGE_GRAPH")
    print("=" * 70)
    
    # Step 1: Load canonical relations
    canonical_relations = load_canonical_relations()
    
    # Step 2: Parse articles
    all_relations = parse_articles()
    
    if not all_relations:
        print("\n⚠️  No relations found to process")
        sys.exit(0)
    
    # Step 3: Validate
    valid_relations = validate_relations(all_relations, canonical_relations)
    
    # Step 4: Emit JSON-LD
    emit_jsonld(valid_relations)
    
    # Step 5: Emit CSV
    emit_csv(valid_relations)
    
    print("\n" + "=" * 70)
    print("✅ BUILD COMPLETE")
    print("=" * 70)
    print(f"\nGenerated:")
    print(f"  • {OUTPUT_JSONLD}")
    print(f"  • {OUTPUT_CSV}")
    print(f"\nGraph contains {len(valid_relations)} semantic relations")
    print("\n⚠️  Remember: KNOWLEDGE_GRAPH files are GENERATED.")
    print("   Do not edit them manually. Edit source files in ARTICLES/M instead.")
    print("=" * 70)

if __name__ == "__main__":
    main()
