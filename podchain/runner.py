import argparse
import os
import yaml
import subprocess
import sys
from .receipt import Receipt
from .validator import Validator

def run_pod(pod_dir, input_file):
    pod_yaml_path = os.path.join(pod_dir, "pod.yaml")
    
    if not os.path.exists(pod_yaml_path):
        print(f"Error: pod.yaml not found in {pod_dir}")
        return "BLOCKED"

    with open(pod_yaml_path, "r") as f:
        pod_config = yaml.safe_load(f)

    pod_name = pod_config.get("name", "unknown_pod")
    entrypoint = pod_config.get("entrypoint", "run.py")
    output_artifact = pod_config.get("output_artifact", "artifacts/output.txt")
    
    # Ensure entrypoint is absolute or relative to pod_dir
    script_path = os.path.join(pod_dir, entrypoint)
    
    print(f"🚀 Igniting Pod: {pod_name}")
    
    try:
        # 1. Execute the pod
        result = subprocess.run(
            [sys.executable, script_path, "--input", input_file],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            status = "FAIL"
            error = result.stderr
        else:
            # 2. Validate the artifact
            artifact_full_path = os.path.join(pod_dir, output_artifact)
            validation_report = Validator.validate(pod_config, artifact_full_path)
            
            if validation_report["passed"]:
                status = "PASS"
                error = None
            else:
                status = "FAIL"
                error = f"Validation failed: {validation_report['details']}"
                
    except Exception as e:
        status = "FAIL"
        error = str(e)

    # 3. Write Receipt
    receipt = Receipt.create(pod_name, status, os.path.join(pod_dir, output_artifact) if status == "PASS" else None, error)
    receipt_path = os.path.join(pod_dir, "receipt.json")
    Receipt.write(receipt, receipt_path)
    
    print(f"🏁 Pod {pod_name} finished with status: {status}")
    if error:
        print(f"❌ Error: {error}")
        
    return status

def main():
    parser = argparse.ArgumentParser(description="PodChain Runner")
    subparsers = parser.add_subparsers(dest="command")
    
    run_parser = subparsers.add_parser("run")
    run_parser.add_argument("type", choices=["pod", "chain"])
    run_parser.add_argument("target", help="Name of the pod or chain directory")
    run_parser.add_argument("--input", required=True, help="Path to input.yaml")
    
    args = parser.parse_args()
    
    if args.command == "run":
        if args.type == "pod":
            # Simple convention: examples/{target}
            pod_dir = os.path.join("examples", args.target)
            if not os.path.exists(pod_dir):
                print(f"Error: Pod directory {pod_dir} not found.")
                sys.exit(1)
                
            status = run_pod(pod_dir, args.input)
            if status != "PASS":
                sys.exit(1)
        else:
            print("Chain execution not yet implemented.")
            sys.exit(1)

if __name__ == "__main__":
    main()
