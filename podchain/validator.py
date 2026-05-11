import os

class Validator:
    @staticmethod
    def validate(pod_config, artifact_path):
        rules = pod_config.get("validator", {}).get("rules", [])
        report = {"passed": True, "details": []}

        for rule in rules:
            if rule["type"] == "file_exists":
                exists = os.path.exists(artifact_path)
                report["details"].append({
                    "rule": "file_exists",
                    "target": artifact_path,
                    "passed": exists
                })
                if not exists:
                    report["passed"] = False
            elif rule["type"] == "syntax_check":
                language = rule.get("language", "python").lower()
                passed = False
                error_msg = ""
                
                if language == "python":
                    import py_compile
                    try:
                        py_compile.compile(artifact_path, doraise=True)
                        passed = True
                    except Exception as e:
                        error_msg = str(e)
                
                report["details"].append({
                    "rule": "syntax_check",
                    "language": language,
                    "target": artifact_path,
                    "passed": passed,
                    "error": error_msg if not passed else None
                })
                if not passed:
                    report["passed"] = False

        return report
