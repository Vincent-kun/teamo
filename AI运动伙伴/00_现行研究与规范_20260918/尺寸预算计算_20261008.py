"""Reproduce documented conditional examples. No full assembly fit is claimed."""
import json
import math


def calculate():
    phi = (1 + math.sqrt(5)) / 2
    width = math.sqrt(5400 / phi)
    depth, height = width / phi, width * phi
    wall, gap, cavity_shortfall, example_part_oversize = 2.0, 0.5, 0.3, 0.2

    def screen_case(part_width):
        required_width = (
            part_width + example_part_oversize + 2 * gap
            + 2 * wall + cavity_shortfall
        )
        enlarged_width = max(width, required_width)
        return {
            "historical_nominal_screen_width_mm": part_width,
            "conditional_required_outer_width_mm": required_width,
            "candidate_A_width_margin_mm": width - required_width,
            "width_driven_W_D_H_mm": [
                enlarged_width, enlarged_width / phi, enlarged_width * phi
            ],
            "full_fit_status": "UNVERIFIED: only one-axis envelope screened",
        }

    return {
        "status": "ILLUSTRATIVE_BUDGET_NOT_SUPPLIER_TOLERANCE_OR_ASSEMBLY_APPROVAL",
        "phi": phi,
        "candidate_A_W_D_H_mm": [width, depth, height],
        "assumptions_mm": {
            "nominal_wall_per_side": wall,
            "target_assembly_gap_per_side": gap,
            "total_cavity_span_inward_shortfall": cavity_shortfall,
            "example_screen_total_span_oversize": example_part_oversize,
        },
        "internal_axis_upper_bound_after_budget_mm": [
            axis - 2 * wall - cavity_shortfall
            for axis in [width, depth, height]
        ],
        "screen_cases": [screen_case(48), screen_case(61)],
        "historical_camera_reserved_depth_mm": 30,
        "camera_best_case_remaining_depth_mm": (
            depth - 2 * wall - cavity_shortfall - 30
        ),
        "missing_inputs": [
            "actual mechanical drawings and tolerances",
            "mainboard and battery envelopes",
            "local curved inner surface and layout",
            "print process and post-processing coupon measurements",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(calculate(), indent=2, ensure_ascii=False))
