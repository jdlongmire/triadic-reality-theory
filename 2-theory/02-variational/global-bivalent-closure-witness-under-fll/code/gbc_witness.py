#!/usr/bin/env python3
"""Reference calculation for the symmetric global-bivalent closure under GBC witness.

The null is a closed binary context with one latent bivalent value and R
conditionally independent record fragments.  Each fragment's probability of a
specified forbidden report (00 gap or 11 glut), conditional on either latent
value, is bounded by epsilon.  The union bound is then 2 * epsilon**R.
"""

from __future__ import annotations

import argparse
import math


def fll_bound(epsilon: float, fragments: int) -> float:
    if not 0.0 <= epsilon <= 1.0:
        raise ValueError("epsilon must be in [0,1]")
    if fragments < 1:
        raise ValueError("fragments must be positive")
    return min(1.0, 2.0 * epsilon**fragments)


def _binomial_lower_cdf(trials: int, events: int, rate: float) -> float:
    """P[X <= events] for X ~ Binomial(trials, rate), rare-event stable."""
    if rate == 0.0:
        return 1.0
    if rate == 1.0:
        return 1.0 if events == trials else 0.0
    term = math.exp(trials * math.log1p(-rate))
    total = term
    odds = rate / (1.0 - rate)
    for k in range(events):
        term *= (trials - k) / (k + 1) * odds
        total += term
    return max(0.0, min(1.0, total))


def clopper_pearson_upper(events: int, trials: int, alpha: float) -> float:
    """Exact one-sided Clopper-Pearson upper confidence limit."""
    if not 0 <= events <= trials or trials < 1:
        raise ValueError("calibration events/trials are invalid")
    if not 0.0 < alpha < 1.0:
        raise ValueError("alpha must be in (0,1)")
    if events == trials:
        return 1.0
    low = events / trials
    high = 1.0
    for _ in range(80):
        mid = (low + high) / 2.0
        if _binomial_lower_cdf(trials, events, mid) > alpha:
            low = mid
        else:
            high = mid
    return (low + high) / 2.0


def joint_fll_bound(
    trials: int,
    t_gap: int,
    f_gap: int,
    t_glut: int,
    f_glut: int,
    family_alpha: float = 0.05,
) -> float:
    """Bound coherent forbidden patterns without fragment independence.

    The four rates are calibrated directly on the complete joint record under
    known true (T) and false (F) preparations. Bonferroni allocation gives
    simultaneous one-sided coverage of at least 1-family_alpha.
    """
    per_rate_alpha = family_alpha / 4.0
    gap = max(
        clopper_pearson_upper(t_gap, trials, per_rate_alpha),
        clopper_pearson_upper(f_gap, trials, per_rate_alpha),
    )
    glut = max(
        clopper_pearson_upper(t_glut, trials, per_rate_alpha),
        clopper_pearson_upper(f_glut, trials, per_rate_alpha),
    )
    return min(1.0, gap + glut)


def binomial_upper_tail(trials: int, events: int, null_rate: float) -> float:
    """Exact P[X >= events] for X ~ Binomial(trials, null_rate)."""
    if not 0 <= events <= trials:
        raise ValueError("events must be between zero and trials")
    if not 0.0 <= null_rate <= 1.0:
        raise ValueError("null_rate must be in [0,1]")
    if events == 0:
        return 1.0
    if null_rate == 0.0:
        return 0.0
    if null_rate == 1.0:
        return 1.0

    # Sum the shorter lower tail by recurrence. This avoids constructing huge
    # binomial coefficients and makes the million-trial reference case fast.
    term = math.exp(trials * math.log1p(-null_rate))
    lower = term
    odds = null_rate / (1.0 - null_rate)
    for k in range(events - 1):
        term *= (trials - k) / (k + 1) * odds
        lower += term
    return max(0.0, min(1.0, 1.0 - lower))


def self_test() -> None:
    assert math.isclose(fll_bound(0.01, 3), 2e-6)
    assert fll_bound(1.0, 3) == 1.0
    assert binomial_upper_tail(10, 0, 0.2) == 1.0
    assert math.isclose(binomial_upper_tail(10, 10, 0.2), 0.2**10)
    exact_zero = clopper_pearson_upper(0, 1_000_000, 0.0125)
    assert math.isclose(exact_zero, 1.0 - 0.0125 ** (1.0 / 1_000_000), rel_tol=1e-10)
    bound = joint_fll_bound(1_000_000, 0, 0, 0, 0)
    assert 0.0 < bound < 0.01
    try:
        fll_bound(-0.1, 2)
    except ValueError:
        pass
    else:
        raise AssertionError("negative epsilon accepted")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--epsilon", type=float, default=0.01)
    parser.add_argument("--fragments", type=int, default=3)
    parser.add_argument("--trials", type=int, default=1_000_000)
    parser.add_argument("--events", type=int, default=1)
    parser.add_argument("--joint-calibration-trials", type=int)
    parser.add_argument("--t-gap", type=int, default=0)
    parser.add_argument("--f-gap", type=int, default=0)
    parser.add_argument("--t-glut", type=int, default=0)
    parser.add_argument("--f-glut", type=int, default=0)
    parser.add_argument("--family-alpha", type=float, default=0.05)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        print("self-test: PASS")
        return

    if args.joint_calibration_trials is None:
        bound = fll_bound(args.epsilon, args.fragments)
        mode = "conditional_independence_reference"
    else:
        bound = joint_fll_bound(
            args.joint_calibration_trials,
            args.t_gap,
            args.f_gap,
            args.t_glut,
            args.f_glut,
            args.family_alpha,
        )
        mode = "direct_joint_calibration"
    p_value = binomial_upper_tail(args.trials, args.events, bound)
    print(f"mode={mode}")
    print(f"B_GBC={bound:.12g}")
    print(f"observed_rate={args.events / args.trials:.12g}")
    print(f"one_sided_p_value={p_value:.12g}")


if __name__ == "__main__":
    main()
