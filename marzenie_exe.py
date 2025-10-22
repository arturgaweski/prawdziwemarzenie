#!/usr/bin/env python3
"""Wykonywalny punkt wejścia dla projektu prawdziwemarzenie."""

from __future__ import annotations

import marzenie
from system import SYSTEM


def main() -> None:
    """Uruchom główny interfejs CLI z zachowaniem aliasów systemowych."""

    SYSTEM.register_module_alias(marzenie)
    raise SystemExit(marzenie.main())


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrzerwano. Niech magia nadal łagodnie płynie po Ziemi.\n")
