import json
import hashlib
from datetime import datetime

class Receipt:
    @staticmethod
    def create(pod_name, status, artifact_path=None, error=None):
        artifact_hash = None
        if artifact_path:
            try:
                with open(artifact_path, "rb") as f:
                    artifact_hash = hashlib.sha256(f.read()).hexdigest()
            except FileNotFoundError:
                pass

        return {
            "pod_name": pod_name,
            "timestamp": datetime.utcnow().isoformat(),
            "status": status,
            "artifact_hash": artifact_hash,
            "error": error
        }

    @staticmethod
    def write(receipt, path):
        with open(path, "w") as f:
            json.dump(receipt, f, indent=2)
