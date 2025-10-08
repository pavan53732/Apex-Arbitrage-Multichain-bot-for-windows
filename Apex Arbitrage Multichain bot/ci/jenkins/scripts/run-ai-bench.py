#!/usr/bin/env python3
import sys
import subprocess

def run_ai_benchmarks():
    print("Running AI benchmarks...")
    result = subprocess.run(["python", "benchmarks/ai/ai-integration-bench.py"], capture_output=True)
    if result.returncode != 0:
        print(f"AI benchmarks failed: {result.stderr.decode()}")
        sys.exit(1)
    print("AI benchmarks completed successfully")

if __name__ == "__main__":
    run_ai_benchmarks()
