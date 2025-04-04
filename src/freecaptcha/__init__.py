"""A simple and free reCAPTCHA bypass.

Typical usage example:

  token = reCAPTCHASolver.solve(anchor_url)
"""

from .bypass import reCAPTCHAV3Solver

__all__ = ("solve", "reCAPTCHAV3Solver",)

solve = reCAPTCHAV3Solver.solve