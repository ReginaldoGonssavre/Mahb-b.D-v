import sys
import json
from quantum_processor import run_quantum_algorithm
from post_quantum.pqc_algorithms import encrypt_pqc, decrypt_pqc

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "No arguments provided."}))
        sys.exit(1)

    try:
        # Assuming the first argument is a JSON string of the job details
        job_details = json.loads(sys.argv[1])
        job_type = job_details.get("job_type")
        payload = job_details.get("payload", {})

        result = {}
        if job_type == "quantum_algorithm":
            algorithm_name = payload.get("algorithm_name")
            params = payload.get("params")
            result = run_quantum_algorithm(algorithm_name, params)
        elif job_type == "pqc_encrypt":
            plaintext = payload.get("plaintext")
            public_key = payload.get("public_key")
            algorithm = payload.get("algorithm")
            result = encrypt_pqc(plaintext, public_key, algorithm)
        elif job_type == "pqc_decrypt":
            ciphertext = payload.get("ciphertext")
            private_key = payload.get("private_key")
            algorithm = payload.get("algorithm")
            result = decrypt_pqc(ciphertext, private_key, algorithm)
        else:
            result = {"error": f"Unknown job type: {job_type}"}

        print(json.dumps(result))

    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)

if __name__ == "__main__":
    main()