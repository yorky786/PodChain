# Error Handling

PodChain prioritizes safety over recovery.

1. **FAIL:** The pod executed but the output was invalid.
2. **BLOCKED:** The pod cannot run because a dependency failed or is missing.
3. **CRASH:** An unexpected system error occurred during execution.

All errors are logged in the `receipt.json` with a full traceback and state snapshot.
