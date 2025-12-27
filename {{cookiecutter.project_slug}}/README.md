# {{ cookiecutter.project_slug }}

{{ cookiecutter.kernel_description }}

## Installation

```bash
uv sync
```

## Usage

```python
import torch
from {{ cookiecutter.kernel_name }} import {{ cookiecutter.kernel_name }}

x = torch.rand(1024, device="cuda", dtype=torch.float32)
output = {{ cookiecutter.kernel_name }}(x)
```

## Running Tests

```bash
uv run python {{ cookiecutter.kernel_name }}.py
```

{% if cookiecutter.include_benchmark == "yes" -%}

## Benchmarking

The benchmark will compare the Triton kernel against PyTorch implementation:

```bash
uv run python benchmark.py
```

Results will be saved to a PNG file in the current directory.
{%- endif %}

## Kernel Parameters

- **BLOCK_SIZE**: {{ cookiecutter.block_size }} (elements per program)

## Author

{{ cookiecutter.author }}
