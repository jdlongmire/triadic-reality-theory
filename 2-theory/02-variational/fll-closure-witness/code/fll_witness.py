#!/usr/bin/env python3
"""Reference calculation for the symmetric global-FLL closure witness.

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
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        print("self-test: PASS")
        return

    bound = fll_bound(args.epsilon, args.fragments)
    p_value = binomial_upper_tail(args.trials, args.events, bound)
    print(f"B_FLL={bound:.12g}")
    print(f"observed_rate={args.events / args.trials:.12g}")
    print(f"one_sided_p_value={p_value:.12g}")


if __name__ == "__main__":
    main()
