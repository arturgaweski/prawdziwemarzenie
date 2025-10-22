"""Audiowizualny interfejs Tkinter dla prawdziwego marzenia."""

from __future__ import annotations

import contextlib
import queue
import threading
from pathlib import Path
from typing import Optional

import tkinter as tk
from tkinter import filedialog, messagebox, ttk

import marzenie
from system import SYSTEM, build_system_report, iter_magic_lines


class QueueWriter:
    """Przekierowuje dane tekstowe do kolejki wątku głównego."""

    def __init__(self, target: "queue.Queue[str]") -> None:
        self._target = target
        self._buffer = ""

    def write(self, data: str) -> int:  # pragma: no cover - logika UI
        if not data:
            return 0
        self._buffer += data
        while "\n" in self._buffer:
            line, self._buffer = self._buffer.split("\n", 1)
            self._target.put(line + "\n")
        return len(data)

    def flush(self) -> None:  # pragma: no cover - logika UI
        if self._buffer:
            self._target.put(self._buffer)
            self._buffer = ""


class NarrationThread(threading.Thread):
    """Uruchamia narrację w osobnym wątku i przesyła wynik do kolejki."""

    def __init__(self, q: "queue.Queue[str]", tempo: float) -> None:
        super().__init__(daemon=True)
        self.queue = q
        self.tempo = tempo

    def run(self) -> None:  # pragma: no cover - wątek UI
        writer = QueueWriter(self.queue)
        with contextlib.redirect_stdout(writer):
            marzenie.journey(tempo=self.tempo, include_breath=True)
        writer.flush()


class PlanDialog(tk.Toplevel):
    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master)
        self.title("Plan marzenia")
        self.resizable(True, True)
        self.generated = ""

        container = ttk.Frame(self, padding=16)
        container.grid(sticky="nsew")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        container.columnconfigure(1, weight=1)

        fields = [
            ("imie", "Imię marzycielki/marzyciela", ""),
            ("partner", "Imię towarzyszki", "Towarzyszka"),
            ("wioska", "Nazwa wioski", "Hamakaze"),
            ("why", "Dlaczego to prawdziwe?", ""),
            ("jp_level", "Poziom japońskiego", "0"),
            ("godziny", "Godziny tygodniowo", "6"),
            ("natura", "Kotwica natury", ""),
            ("rytual", "Poranny rytuał", ""),
            ("spolecznosc", "Kontakt ze społecznością", ""),
        ]
        self._entries: dict[str, ttk.Entry] = {}
        for idx, (key, label, default) in enumerate(fields):
            ttk.Label(container, text=label).grid(column=0, row=idx, sticky="w", padx=(0, 8), pady=4)
            entry = ttk.Entry(container)
            entry.grid(column=1, row=idx, sticky="ew", pady=4)
            if default:
                entry.insert(0, default)
            self._entries[key] = entry

        self.output = tk.Text(container, height=12, wrap="word")
        self.output.grid(column=0, row=len(fields), columnspan=2, sticky="nsew", pady=(12, 8))
        container.rowconfigure(len(fields), weight=1)
        scrollbar = ttk.Scrollbar(container, command=self.output.yview)
        scrollbar.grid(column=2, row=len(fields), sticky="nsw")
        self.output.configure(yscrollcommand=scrollbar.set, state="disabled")

        buttons = ttk.Frame(container)
        buttons.grid(column=0, row=len(fields) + 1, columnspan=2, sticky="e")
        ttk.Button(buttons, text="Generuj", command=self._generate).grid(column=0, row=0, padx=4)
        ttk.Button(buttons, text="Zapisz", command=self._save).grid(column=1, row=0, padx=4)
        ttk.Button(buttons, text="Zamknij", command=self.destroy).grid(column=2, row=0, padx=4)

    def _collect(self) -> dict[str, str]:
        return {key: entry.get().strip() for key, entry in self._entries.items()}

    def _generate(self) -> None:
        data = self._collect()
        self.generated = marzenie.build_plan_text(
            data.get("imie", ""),
            data.get("partner", ""),
            data.get("wioska", ""),
            data.get("why", ""),
            data.get("jp_level", ""),
            data.get("godziny", ""),
            data.get("natura", ""),
            data.get("rytual", ""),
            data.get("spolecznosc", ""),
        )
        self.output.configure(state="normal")
        self.output.delete("1.0", "end")
        self.output.insert("end", self.generated)
        self.output.configure(state="disabled")
        self.output.see("1.0")

    def _save(self) -> None:
        if not self.generated:
            messagebox.showinfo("Plan", "Najpierw wygeneruj plan.")
            return
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            initialfile="plan_marzenia.txt",
            filetypes=[("Pliki tekstowe", "*.txt"), ("Wszystkie pliki", "*.*")],
        )
        if not filename:
            return
        Path(filename).write_text(self.generated + "\n", encoding="utf-8")
        messagebox.showinfo("Plan", f"Zapisano plan w {filename}")


class SystemDialog(tk.Toplevel):
    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master)
        self.title("System i magia")
        self.resizable(True, True)

        container = ttk.Frame(self, padding=16)
        container.grid(sticky="nsew")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        text = tk.Text(container, wrap="word")
        text.grid(column=0, row=0, sticky="nsew")
        container.rowconfigure(0, weight=1)
        scrollbar = ttk.Scrollbar(container, command=text.yview)
        scrollbar.grid(column=1, row=0, sticky="nsw")
        text.configure(yscrollcommand=scrollbar.set)

        report = build_system_report() + "\n" + "\n".join(iter_magic_lines())
        text.insert("end", report)
        text.configure(state="disabled")

        ttk.Button(container, text="Zamknij", command=self.destroy).grid(column=0, row=1, sticky="e", pady=(12, 0))


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Prawdziwe Marzenie")
        self.geometry("760x520")

        self.queue: "queue.Queue[str]" = queue.Queue()
        self._thread: Optional[NarrationThread] = None

        main = ttk.Frame(self, padding=16)
        main.grid(sticky="nsew")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        main.columnconfigure(0, weight=1)
        main.rowconfigure(1, weight=1)

        controls = ttk.Frame(main)
        controls.grid(column=0, row=0, sticky="ew", pady=(0, 12))
        controls.columnconfigure(4, weight=1)

        ttk.Button(controls, text="Start podróży", command=self.start_narration).grid(column=0, row=0, padx=4)
        ttk.Button(controls, text="Plan", command=self.open_plan).grid(column=1, row=0, padx=4)
        ttk.Button(controls, text="System", command=self.open_system).grid(column=2, row=0, padx=4)
        ttk.Button(controls, text="Zaklęcia", command=self.show_spells).grid(column=3, row=0, padx=4)

        self.tempo_var = tk.DoubleVar(value=1.0)
        ttk.Label(controls, text="Tempo").grid(column=4, row=0, sticky="e")
        ttk.Spinbox(controls, from_=0.5, to=2.0, increment=0.1, textvariable=self.tempo_var, width=5).grid(
            column=5, row=0, padx=4
        )

        self.output = tk.Text(main, wrap="word", state="disabled")
        self.output.grid(column=0, row=1, sticky="nsew")
        scrollbar = ttk.Scrollbar(main, command=self.output.yview)
        scrollbar.grid(column=1, row=1, sticky="nsw")
        self.output.configure(yscrollcommand=scrollbar.set)

        self.after(100, self._poll_queue)

    def start_narration(self) -> None:
        if self._thread and self._thread.is_alive():
            messagebox.showinfo("Podróż", "Narracja jest już w toku.")
            return
        self.output.configure(state="normal")
        self.output.delete("1.0", "end")
        self.output.configure(state="disabled")
        self._thread = NarrationThread(self.queue, tempo=float(self.tempo_var.get()))
        self._thread.start()

    def open_plan(self) -> None:
        PlanDialog(self)

    def open_system(self) -> None:
        SystemDialog(self)

    def show_spells(self) -> None:
        spells = SYSTEM.list_spells()
        listing = "\n".join(f"• {s.name} ({s.element})" for s in spells)
        messagebox.showinfo("Zaklęcia", listing)

    def _poll_queue(self) -> None:
        try:
            while True:
                chunk = self.queue.get_nowait()
                self.output.configure(state="normal")
                self.output.insert("end", chunk)
                self.output.see("end")
                self.output.configure(state="disabled")
        except queue.Empty:  # pragma: no cover - logika UI
            pass
        self.after(100, self._poll_queue)


def launch_ui(debug: bool = False) -> None:  # pragma: no cover - UI start
    if debug:
        tk.Tk.report_callback_exception = lambda *exc: print("Błąd Tkinter:", exc)
    app = App()
    app.mainloop()


def main() -> None:  # pragma: no cover
    launch_ui()


if __name__ == "__main__":  # pragma: no cover
    main()
