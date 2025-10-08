#!/usr/bin/env python3
import subprocess
import sys

def run_benchmarks():
    print("Running AI benchmarks for GitLab CI...")
    result = subprocess.run(["python", "benchmarks/ai/ai-integration-bench.py"])
    sys.exit(result.returncode)

if __name__ == "__main__":
    run_benchmarks()
