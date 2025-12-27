# Cookiecutter Triton Kernel

A [cookiecutter](https://cookiecutter.readthedocs.io/) template for creating Triton GPU kernel projects.

## Usage

```bash
cookiecutter path/to/cookiecutter-triton
# or from a git repo
cookiecutter gh:username/cookiecutter-triton
```

## Options

| Variable | Default | Description |
|----------|---------|-------------|
| `project_slug` | `my_triton_kernel` | Project directory name |
| `kernel_name` | `custom_kernel` | Name of the kernel function |
| `kernel_description` | `A custom Triton kernel` | Brief description |
| `author` | `Your Name` | Author name |
| `block_size` | `1024` | Elements processed per program |
| `include_benchmark` | `yes` | Include benchmark script (`yes`/`no`) |
| `include_pyproject` | `no` | Include pyproject.toml (`yes`/`no`) |

## Generated Structure

```
my_triton_kernel/
├── custom_kernel.py      # Kernel implementation + launcher
├── benchmark.py          # (optional) Performance benchmark
├── pyproject.toml        # (optional) Project config
└── README.md
```

## Example

```bash
cookiecutter cookiecutter-triton --no-input \
    project_slug=vector_add \
    kernel_name=add \
    kernel_description="Element-wise vector addition"
```
