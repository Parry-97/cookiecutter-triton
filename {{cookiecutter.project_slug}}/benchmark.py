"""
Benchmark for {{ cookiecutter.kernel_name }}.

Author: {{ cookiecutter.author }}
"""

import torch
import triton

from {{ cookiecutter.kernel_name }} import {{ cookiecutter.kernel_name }}


@triton.testing.perf_report(
    triton.testing.Benchmark(
        x_names=["size"],
        x_vals=[2**i for i in range(12, 28, 1)],
        x_log=True,
        line_arg="provider",
        line_vals=["triton", "torch"],
        line_names=["Triton", "Torch"],
        styles=[("blue", "-"), ("green", "-")],
        ylabel="GB/s",
        plot_name="{{ cookiecutter.kernel_name }}-performance",
        args={},
    )
)
def benchmark(size, provider):
    x = torch.rand(size, device="cuda", dtype=torch.float32)
    quantiles = [0.5, 0.2, 0.8]

    if provider == "triton":
        ms, min_ms, max_ms = triton.testing.do_bench(
            lambda: {{ cookiecutter.kernel_name }}(x), quantiles=quantiles
        )
    else:
        # TODO: Replace with equivalent torch operation for comparison
        ms, min_ms, max_ms = triton.testing.do_bench(
            lambda: x.clone(), quantiles=quantiles
        )

    # Calculate bandwidth (read + write)
    gbps = lambda ms: 2 * x.numel() * x.element_size() * 1e-9 / (ms * 1e-3)
    return gbps(ms), gbps(max_ms), gbps(min_ms)


if __name__ == "__main__":
    benchmark.run(print_data=True, save_path=".")
