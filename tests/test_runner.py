import unittest
import os
import shutil
from podchain.validator import Validator

class TestPodChainCore(unittest.TestCase):
    def setUp(self):
        # Setup a temporary artifact directory
        self.test_dir = "test_artifacts"
        os.makedirs(self.test_dir, exist_ok=True)
        self.artifact_path = os.path.join(self.test_dir, "output.py")

    def tearDown(self):
        # Clean up
        shutil.rmtree(self.test_dir)

    def test_syntax_check_pass(self):
        """Verifier should PASS valid Python code."""
        with open(self.artifact_path, "w") as f:
            f.write("def hello():\n    print('world')\n")
        
        pod_config = {
            "validator": {
                "rules": [
                    {"type": "syntax_check", "language": "python"}
                ]
            }
        }
        
        report = Validator.validate(pod_config, self.artifact_path)
        self.assertTrue(report["passed"], "Valid python should pass syntax check")

    def test_syntax_check_fail(self):
        """Verifier should FAIL invalid Python code (The Interlock)."""
        # Intentional syntax error (missing colon)
        with open(self.artifact_path, "w") as f:
            f.write("def broken()\n    print('world')\n")
        
        pod_config = {
            "validator": {
                "rules": [
                    {"type": "syntax_check", "language": "python"}
                ]
            }
        }
        
        report = Validator.validate(pod_config, self.artifact_path)
        self.assertFalse(report["passed"], "Invalid python must fail syntax check")
        self.assertEqual(report["details"][0]["rule"], "syntax_check")

    def test_file_exists_pass(self):
        """Verifier should PASS if file exists."""
        with open(self.artifact_path, "w") as f:
            f.write("test")
            
        pod_config = {
            "validator": {
                "rules": [
                    {"type": "file_exists"}
                ]
            }
        }
        
        report = Validator.validate(pod_config, self.artifact_path)
        self.assertTrue(report["passed"])

if __name__ == "__main__":
    unittest.main()
