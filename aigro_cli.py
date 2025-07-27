import argparse
import subprocess
import os
import sys

# Add the current directory to the path to allow importing other scripts
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

def run_script(script_name, description):
    """Executes a python script as a subprocess."""
    if not os.path.exists(script_name):
        print(f"Error: Script not found at {script_name}")
        return

    print(f"Executing {description}...")
    try:
        subprocess.run(['python', script_name], check=True)
        print(f"{description} finished.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the script: {e}")
    except FileNotFoundError:
        print("Error: 'python' command not found. Is python installed and in PATH?")

def run_anomaly_detection():
    """Runs the anomaly detection script."""
    run_script(
        'aiops_ml_anomaly_detection_Version3.py',
        'AIOps ML Anomaly Detection'
    )

def run_quantum_example():
    """Runs the qiskit example script."""
    run_script(
        'qiskit_example.py',
        'Qiskit Deutsch-Jozsa example'
    )

def run_tests():
    """Executes the test script."""
    script_path = './scripts_run_tests.sh'
    if not os.path.exists(script_path):
        print(f"Error: Test script not found at {script_path}")
        return

    print(f"Running tests using {script_path}...")
    try:
        # Make sure the script is executable
        subprocess.run(['chmod', '+x', script_path], check=True)
        # Run the script
        subprocess.run([script_path], check=True)
        print("Tests finished.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running tests: {e}")
    except FileNotFoundError:
        print("Error: 'chmod' or the script itself not found. Is bash installed and in PATH?")


def main():
    """Main function to parse arguments and dispatch commands."""
    parser = argparse.ArgumentParser(
        description="AigroQuantumSaaS CLI - Your personal assistant for managing the project."
    )
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    subparsers.required = True

    # 'run' command parser
    parser_run = subparsers.add_parser('run', help='Run a specific project script')
    run_subparsers = parser_run.add_subparsers(dest='script', help='Script to run')
    run_subparsers.required = True

    # 'run anomaly-detection' command
    parser_anomaly = run_subparsers.add_parser(
        'anomaly-detection',
        help='Run the AIOps ML anomaly detection script.'
    )
    parser_anomaly.set_defaults(func=run_anomaly_detection)

    # 'run quantum-example' command
    parser_quantum = run_subparsers.add_parser(
        'quantum-example',
        help='Run the Qiskit Deutsch-Jozsa example.'
    )
    parser_quantum.set_defaults(func=run_quantum_example)

    # 'test' command parser
    parser_test = subparsers.add_parser('test', help='Run project tests')
    parser_test.set_defaults(func=run_tests)

    args = parser.parse_args()
    args.func()

if __name__ == '__main__':
    main()
