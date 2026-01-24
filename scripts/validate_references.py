#!/usr/bin/env python3
"""
validate_references.py
Validates that all file references in protocol files actually exist.
"""

import json
import yaml
import re
from pathlib import Path

def check_file_exists(file_path):
    """Check if a referenced file exists in the repository."""
    path = Path(file_path)
    if not path.exists():
        print(f"❌ Missing referenced file: {file_path}")
        return False
    return True

def validate_jsonld_references(jsonld_path):
    """Extract and validate file references from structured_data.jsonld."""
    print(f"\n🔍 Validating references in: {jsonld_path}")
    
    with open(jsonld_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    all_valid = True
    
    if '@graph' in data:
        for item in data['@graph']:
            # Check operator references (e.g., CORE/operators.yaml#diff)
            if 'operator' in item:
                op = item['operator']
                # Extract file path before # if present
                if '#' in op:
                    file_part = op.split('#')[0]
                    if file_part and not file_part.startswith('http'):
                        if not check_file_exists(file_part):
                            all_valid = False
    
    # Check KNOWLEDGE_GRAPH reference
    for item in data.get('@graph', []):
        if 'output' in item and 'KNOWLEDGE_GRAPH' in item['output']:
            kg_path = item['output'].split('→')[-1].strip()
            if not check_file_exists(kg_path):
                all_valid = False
    
    return all_valid

def validate_yaml_references(yaml_path):
    """Validate references in YAML files (QUICK_START, API_SPEC)."""
    print(f"\n🔍 Validating references in: {yaml_path}")
    
    with open(yaml_path, 'r', encoding='utf-8') as f:
        content = f.read()
        data = yaml.safe_load(content)
    
    all_valid = True
    
    # Check for CORE/ references
    core_refs = re.findall(r'CORE/[a-zA-Z0-9_\-\./]+\.yaml', content)
    for ref in set(core_refs):  # Remove duplicates
        if not check_file_exists(ref):
            all_valid = False
    
    return all_valid

def main():
    print("=== REFERENCE VALIDATION FOR METAMONISM PROTOCOL ===\n")
    
    all_valid = True
    
    # Validate structured_data.jsonld
    jsonld_path = "structured_data.jsonld"
    if Path(jsonld_path).exists():
        if not validate_jsonld_references(jsonld_path):
            all_valid = False
    else:
        print(f"⚠ File not found: {jsonld_path}")
        all_valid = False
    
    # Validate QUICK_START_FOR_AI.yaml
    quickstart_path = "QUICK_START_FOR_AI.yaml"
    if Path(quickstart_path).exists():
        if not validate_yaml_references(quickstart_path):
            all_valid = False
    else:
        print(f"⚠ File not found: {quickstart_path}")
        all_valid = False
    
    # Validate API_SPECIFICATION.yaml
    api_spec_path = "API_SPECIFICATION.yaml"
    if Path(api_spec_path).exists():
        if not validate_yaml_references(api_spec_path):
            all_valid = False
    else:
        print(f"⚠ File not found: {api_spec_path}")
        all_valid = False
    
    # Final result
    if all_valid:
        print("\n✅ All file references are valid and exist.")
        return True
    else:
        print("\n❌ Some referenced files are missing.")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
