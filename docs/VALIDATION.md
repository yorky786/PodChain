# Validation Rules

Validation in PodChain is binary: **PASS** or **FAIL**.

## Types of Validation
1. **Structural:** Does the output file exist? Is the JSON valid?
2. **Content:** Does the content match specific patterns or constraints?
3. **Logic:** Does the artifact pass a custom validation script?

If a validator returns anything other than PASS, the chain is **BLOCKED**.
