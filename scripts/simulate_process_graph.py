#!/usr/bin/env python3
"""
simulate_process_graph.py
Simulates traversal of the process graph and validates its continuity.
"""

import json
import yaml
from pathlib import Path

def load_process_graph(jsonld_path):
    """Load and structure the process graph from JSON-LD."""
    with open(jsonld_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    processes = {}
    for item in data.get('@graph', []):
        if 'Process' in item.get('@type', []):
            pid = item['@id']
            processes[pid] = {
                'name': item.get('name', ''),
                'follows': item.get('follows'),
                'precedes': item.get('precedes'),
                'operator': item.get('operator', '')
            }
    
    return processes

def load_ritual_stages(quickstart_path):
    """Extract ritual stages from QUICK_START_FOR_AI.yaml."""
    with open(quickstart_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    stages = []
    if 'ritual' in data and 'stages' in data['ritual']:
        for stage in data['ritual']['stages']:
            stages.append({
                'stage': stage.get('stage', ''),
                'action': stage.get('action', ''),
                'operator': stage.get('operator', '')
            })
    
    return stages

def validate_graph_continuity(processes):
    """Check that all processes form a continuous chain."""
    print("\n🔗 Validating process graph continuity...")
    
    # Find start (process with no 'follows')
    start_processes = [pid for pid, p in processes.items() if p['follows'] is None]
    
    if len(start_processes) != 1:
        print(f"❌ Graph should have exactly 1 start process. Found: {len(start_processes)}")
        return False
    
    start = start_processes[0]
    print(f"   Start process: {start}")
    
    # Traverse the graph
    current = start
    visited = []
    
    while current:
        visited.append(current)
        next_pid = processes[current]['precedes']
        
        if next_pid:
            # Check backward link
            if processes[next_pid]['follows'] != current:
                print(f"❌ Broken link: {current} → {next_pid} but {next_pid} follows {processes[next_pid]['follows']}")
                return False
            
            current = next_pid
        else:
            # End of chain
            break
    
    # Check all processes were visited
    unvisited = set(processes.keys()) - set(visited)
    if unvisited:
        print(f"❌ Disconnected processes: {unvisited}")
        return False
    
    print(f"✅ Continuous chain verified: {' → '.join(visited)}")
    return True

def validate_ritual_alignment(processes, stages):
    """Validate that graph processes align with ritual stages."""
    print("\n🔄 Validating alignment with ritual stages...")
    
    if len(processes) != len(stages):
        print(f"❌ Process count mismatch: {len(processes)} processes, {len(stages)} ritual stages")
        return False
    
    # Check action/operator alignment
    process_list = list(processes.values())
    
    for i, (process, stage) in enumerate(zip(process_list, stages)):
        # Check action types match
        process_action = process['operator'].split('#')[-1] if 'operator' in process else ''
        stage_action = stage.get('action', '')
        
        # Map ritual actions to process operators
        action_map = {
            'initiate': 'ban_of_absolute_identity',
            'experience': None,  # No direct operator
            'transform': 'diff',
            'constrain': 'diss',
            'propagate': 'propagate'
        }
        
        expected_operator = action_map.get(stage_action)
        if expected_operator and expected_operator not in process['operator']:
            print(f"❌ Stage {i+1} mismatch: ritual action '{stage_action}' vs process operator '{process['operator']}'")
            return False
    
    print("✅ Process graph aligns with ritual stages.")
    return True

def main():
    print("=== PROCESS GRAPH SIMULATION & VALIDATION ===\n")
    
    jsonld_path = "structured_data.jsonld"
    quickstart_path = "QUICK_START_FOR_AI.yaml"
    
    if not Path(jsonld_path).exists():
        print(f"❌ File not found: {jsonld_path}")
        return False
    
    if not Path(quickstart_path).exists():
        print(f"❌ File not found: {quickstart_path}")
        return False
    
    # Load data
    processes = load_process_graph(jsonld_path)
    stages = load_ritual_stages(quickstart_path)
    
    print(f"📊 Loaded {len(processes)} processes from graph")
    print(f"📊 Loaded {len(stages)} stages from ritual")
    
    # Run validations
    continuity_ok = validate_graph_continuity(processes)
    alignment_ok = validate_ritual_alignment(processes, stages)
    
    # Final simulation report
    print("\n" + "="*50)
    print("SIMULATION REPORT:")
    
    if continuity_ok and alignment_ok:
        print("✅ GRAPH VALIDATION PASSED")
        print("   - Continuous, unbroken process chain")
        print("   - Perfect alignment with ritual stages")
        print("   - Ready for AI traversal")
        return True
    else:
        print("❌ GRAPH VALIDATION FAILED")
        if not continuity_ok:
            print("   - Process chain has breaks or inconsistencies")
        if not alignment_ok:
            print("   - Misalignment between graph and ritual")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
