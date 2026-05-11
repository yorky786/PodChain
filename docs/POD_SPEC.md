# Pod Specification

A Pod is defined by a YAML file with the following fields:

```yaml
name: "pod_name"
version: "1.0.0"
description: "What this pod does"
input_schema: "path/to/schema"
output_artifact: "path/to/output"
validator:
  type: "file_exists|regex|schema_match"
  rules: [...]
```
