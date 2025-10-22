"""Centralny system współdzielony przez moduły prawdziwemarzenie.

Moduł ten odpowiada za:
* rejestrowanie aliasów modułów tak, aby CLI i UI korzystały z tej samej
  przestrzeni nazw,
* leniwe ładowanie opcjonalnego interfejsu graficznego,
* przechowywanie manifestu zaklęć i rejestrowanie ich przywołań,
* generowanie raportu środowiskowego dla całego pakietu.

Kod został zaprojektowany tak, by był lekki i łatwy do ponownego użycia w
różnych punktach projektu.
"""

from __future__ import annotations

import datetime as _dt
import importlib
import platform
import sys
import textwrap
from dataclasses import dataclass, field
from pathlib import Path
from types import ModuleType
from typing import Iterable, List, Optional, Sequence, Tuple


@dataclass(frozen=True)
class Spell:
    """Opis pojedynczego zaklęcia."""

    key: str
    name: str
    incantation: str
    element: str
    effect: str

    def matches(self, query: str) -> bool:
        """Sprawdź, czy zapytanie odnosi się do zaklęcia."""

        if not query:
            return False
        q = query.casefold()
        return (
            q in {self.key.casefold(), self.name.casefold(), self.element.casefold()}
            or q in self.incantation.casefold()
        )


_DEFAULT_SPELLS: Sequence[Spell] = (
    Spell(
        key="aurora",
        name="Aurora Domowa",
        incantation="hoshi no ibuki, ie ni tomare",
        element="Światło",
        effect=(
            "Delikatna poświata harmonizuje rytm domowników z pulsującym kosmosem."
        ),
    ),
    Spell(
        key="fala",
        name="Fala Jedności",
        incantation="nagisa no kotoba, kokoro o tsunagu",
        element="Woda",
        effect="Przynosi bryzę morza i jednoczy serca wspólnym rytmem fal.",
    ),
    Spell(
        key="korzenie",
        name="Korzenie Gwiazd",
        incantation="hoshi no ne, chi ni mezameyo",
        element="Ziemia",
        effect="Łączy kroki na ziemi z pyłem gwiezdnym dodając odwagi w codzienności.",
    ),
    Spell(
        key="wiatr",
        name="Wiatr Przeniesienia",
        incantation="kaze yo, yume o hakobe",
        element="Powietrze",
        effect="Niesie szepty marzeń na odległość i rozświetla wspomnienia zapachem domu.",
    ),
)


@dataclass
class SystemRegistry:
    """Prosty rejestr systemowy współdzielony przez moduły projektu."""

    alias: str = "marzenie"
    ui_module_name: str = "marzenie_ui"
    spells: List[Spell] = field(default_factory=lambda: list(_DEFAULT_SPELLS))
    _ui_module: Optional[ModuleType] = None
    _invocations: List[Tuple[str, str]] = field(default_factory=list)

    def register_module_alias(self, module: ModuleType, alias: Optional[str] = None) -> None:
        """Udostępnij moduł pod dodatkową nazwą."""

        alias = alias or self.alias
        sys.modules.setdefault(module.__name__, module)
        sys.modules[alias] = module

    def load_ui_module(self) -> Optional[ModuleType]:
        """Spróbuj załadować moduł interfejsu graficznego."""

        if self._ui_module is not None:
            return self._ui_module
        try:
            self._ui_module = importlib.import_module(self.ui_module_name)
        except ModuleNotFoundError:
            self._ui_module = None
        return self._ui_module

    # ---- Magia -----------------------------------------------------------------
    def list_spells(self) -> List[Spell]:
        return list(self.spells)

    def find_spell(self, query: str) -> Optional[Spell]:
        if not query:
            return None
        query = query.strip()
        for spell in self.spells:
            if spell.matches(query):
                return spell
        return None

    def record_invocation(self, spell: Spell) -> None:
        stamp = _dt.datetime.now().isoformat(timespec="seconds")
        self._invocations.append((stamp, spell.name))
        if len(self._invocations) > 50:
            self._invocations[:] = self._invocations[-50:]

    def recent_invocations(self) -> List[Tuple[str, str]]:
        return list(self._invocations)

    def compose_magic_manifest(self) -> str:
        lines = ["Manifest zaklęć projektu Prawdziwe Marzenie:\n"]
        for spell in self.spells:
            lines.append(f"- {spell.name} ({spell.element}) — {spell.incantation}")
            lines.append(textwrap.fill(f"  {spell.effect}", width=78))
            lines.append("")
        if self._invocations:
            lines.append("Ostatnie przywołania:")
            for stamp, name in self._invocations[-10:]:
                lines.append(f"  • {stamp}: {name}")
        return "\n".join(lines).strip() + "\n"

    # ---- Raport systemowy ------------------------------------------------------
    def environment_report(self) -> str:
        cwd = Path.cwd()
        py = sys.version.replace("\n", " ")
        implementation = platform.python_implementation()
        parts = [
            "Raport systemowy prawdziwemarzenie:\n",
            f"Python: {implementation} {py}",
            f"Platforma: {platform.platform()}",
            f"Interpreter: {Path(sys.executable)}",
            f"Katalog roboczy: {cwd}",
        ]
        module = sys.modules.get(self.alias)
        if module is not None and getattr(module, "__file__", None):
            parts.append(f"Plik modułu głównego: {Path(module.__file__).resolve()}")
        if self._invocations:
            parts.append("\nNajnowsze przywołania zaklęć:")
            for stamp, name in self._invocations[-5:]:
                parts.append(f"  {stamp} — {name}")
        return "\n".join(parts) + "\n"


SYSTEM = SystemRegistry()


def build_system_report() -> str:
    """Pomocnik eksportowany dla interfejsu graficznego."""

    return SYSTEM.environment_report()


def iter_magic_lines() -> Iterable[str]:
    """Dostarcz linie manifestu zaklęć, wygodne dla widoków tekstowych."""

    manifest = SYSTEM.compose_magic_manifest()
    return manifest.splitlines()
