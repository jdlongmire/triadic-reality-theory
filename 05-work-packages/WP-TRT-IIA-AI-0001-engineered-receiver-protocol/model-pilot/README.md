# Protocol 001 Model Pilot

This directory defines the provider-neutral execution boundary for the model-dependent
gate. It intentionally contains no API key handling, provider SDK, or paid endpoint.

## Receiver contract

The runner starts the declared receiver command once per task-condition request,
writes one JSON object to stdin, and requires exactly one JSON object on stdout.

Input fields: `task_id`, `condition`, `instruction`, `question`, `evidence`.

Required output: `answer`.

Recommended output: `confidence`, `sampling_config`, `input_tokens`,
`output_tokens`, `verifier_action`, and `corrected`.

## Example

```text
python3 model_runner.py \
  --tasks ../pilot/tasks.json \
  --receiver python3 receiver_adapter_example.py \
  --model-id local-model \
  --model-version frozen-version \
  --out results/local-model
```

The example adapter always abstains. It exists only to validate the process boundary.

## Experimental discipline

C0 and C5 receive no evidence. C1-C4 receive the frozen corpus where one exists.
The receiver must not silently retrieve external information for C0/C5. Provider,
model version, sampling configuration, raw output, prompt hash, and task-manifest
hash are retained.

Model execution results are not committed as evidence unless the receiver identity,
version, and configuration are reproducible. Paid external API execution requires
separate approval under the work-package authority boundary.

Claim decomposition and citation/support adjudication are a subsequent evaluator
stage. They must remain separable from generation.
