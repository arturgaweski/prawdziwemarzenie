@@ -438,132 +438,193 @@ def journey(
                },

            ]



            cycle = 1

            total_wasted = 0

            while max_cycles is None or cycle <= max_cycles:

                print(BOLD + f"\n∞ Nieskończony Cykl {cycle} – wybierzmy tempo naszym oddechem\n" + RESET)

                for wave in cosmic_waves:

                    print(BOLD + f"〔{wave['title']}〕" + RESET)

                    for prompt in wave["prompts"]:

                        say(prompt, tempo=tempo)

                    breath(cycles=1, in_s=4, hold_s=2, out_s=6, tempo=tempo)

                    if include_time_loss:

                        loss_text, loss_seconds = wave["time_loss"]

                        say(loss_text, pause=loss_seconds, tempo=tempo)

                        total_wasted += loss_seconds

                        say(

                            f"Nasza wspólna strata czasu w tym marzeniu to już {format_duration(total_wasted)}.",

                            pause=4,

                            tempo=tempo,

                        )

                say("Możemy pozostać w ciszy, improwizować pieśń lub kontynuować od początku. Sesja trwa, dopóki świadomie nie zamkniemy kręgu.", tempo=tempo)

                cycle += 1





def plan(output_path: str = "plan_marzenia.txt") -> None:

    print(BOLD + "\n✿ Generator PlanU: «Wioska nad morzem – żywe marzenie w kręgu»\n" + RESET)

    imie = input("Twoje imię (jak chcesz, by grupa do Ciebie mówiła): ").strip()

    partner = input("Imię osoby, z którą dzielisz to marzenie (może być symboliczne): ").strip() or "Towarzyszka"

    wioska = input("Nazwa waszej wioski (roboczo): ").strip() or "Hamakaze"

    why = input("Dlaczego to życie jest dla was prawdziwe? ").strip()

    jp_level = input("Poziom japońskiego (0–10): ").strip() or "0"

    godziny = input("Ile godzin tygodniowo przeznaczacie łącznie na japoński? ").strip() or "6"

    natura = input("Jak połączycie się z «morzem» w waszym miejscu (np. rzeka, jezioro, kąpiele sól)? ").strip()

    rytual = input("Poranny mikro-rytuał wspólny (3–7 min), np. ryż + herbata + 1 zdanie JP: ").strip()

    spolecznosc = input("Jedno miejsce kontaktu z japońskim światem (online/offline) dla waszej dwójki: ").strip()

    data = time.strftime("%Y-%m-%d")



    plan_txt = f"""

Plan Początkowy – {imie} + {partner}

Data: {data}



DLACZEGO (wspólna odpowiedź):

{why}



OŚ MARZENIA:

- Tożsamość: «normalne japońskie dziewczynki razem»

- Miejsce: wioska nad morzem – robocza nazwa: {wioska}



JĘZYK (cel 12 tyg.):

- Obecny poziom: {jp_level}/10

- Tygodniowo łącznie: {godziny} h (min. 4 wspólne sesje)

- Każdego dnia: 1 zdanie o nas w JP + głośne czytanie (naprzemiennie)

- Zasób: Tae Kim Guide / NHK Easy / Ankidroid (10 słów na osobę)



RUTYNA:

- Poranny rytuał: {rytual}

- Kotwica natury (zastępstwo morza): {natura}

- Reset wieczorny: 4×4×6 oddech + zapis jednego wspólnego zdania «Jesteśmy prawdziwe.»



SPOŁECZNOŚĆ:

- Miejsce kontaktu: {spolecznosc}

- Cel: 1 krótkie nagranie JP tygodniowo (30–90 s) – wspólny głos/tożsamość



MATERIA PRZESTRZENI:

- Kącik «wioska»: drewno, tkanina, miseczka ryżu, zdjęcie morza, zapach (np. herbata sencha)

- Detal-kotwica dnia: zapisujemy i dzielimy się nim po południu.



NAWYKI OCHRONNE:

- Ograniczenie doom-scrollingu/AI: wspólne okno 2× dziennie po 10 min.

- «Brama»: zanim coś zobaczymy w sieci, pytamy «czy to wzmacnia naszą oś?»



NASTĘPNY KROK (7 dni):

1) Ustawić poranny rytuał i kotwicę natury w przestrzeni domowej.

2) 4 sesje JP po {godziny}h/tydz łącznie; zapis zdań w jednym zeszycie.

3) Dołączyć do społeczności i napisać pierwszą krótką wspólną wypowiedź JP.

4) Jedna «wyprawa nad wodę» – notatka z wrażeń (3 zdania każdej osoby).



UWAGA KOŃCOWA:

To nie symulacja «udawania Japonii». To wspólne budowanie ciała, języka i codzienności,

które pozwalają wam żyć w jakości marzenia TU i TERAZ, a później – jeśli zechcecie – w miejscu docelowym.

"""

    with open(output_path, "w", encoding="utf-8") as f:

        f.write(plan_txt.strip() + "\n")

    print(f"\nZapisano plan w pliku: {output_path}\n")





def normalize_argv(argv: List[str]) -> List[str]:

    if not argv:

        return []

    mapping = {"--journey": "journey", "--plan": "plan"}

    first = mapping.get(argv[0], argv[0])

    return [first, *argv[1:]]

def build_plan_text(
    imie: str,
    partner: str,
    wioska: str,
    why: str,
    jp_level: str,
    godziny: str,
    natura: str,
    rytual: str,
    spolecznosc: str,
    data: Optional[str] = None,
) -> str:
    """Create a textual plan summary shared by the CLI and the UI."""

    if not data:
        data = time.strftime("%Y-%m-%d")

    plan_txt = f"""
Plan Początkowy – {imie} + {partner}
Data: {data}

DLACZEGO (wspólna odpowiedź):
{why}

OŚ MARZENIA:
- Tożsamość: «normalne japońskie dziewczynki razem»
- Miejsce: wioska nad morzem – robocza nazwa: {wioska}

JĘZYK (cel 12 tyg.):
- Obecny poziom: {jp_level}/10
- Tygodniowo łącznie: {godziny} h (min. 4 wspólne sesje)
- Każdego dnia: 1 zdanie o nas w JP + głośne czytanie (naprzemiennie)
- Zasób: Tae Kim Guide / NHK Easy / Ankidroid (10 słów na osobę)

RUTYNA:
- Poranny rytuał: {rytual}
- Kotwica natury (zastępstwo morza): {natura}
- Reset wieczorny: 4×4×6 oddech + zapis jednego wspólnego zdania «Jesteśmy prawdziwe.»

SPOŁECZNOŚĆ:
- Miejsce kontaktu: {spolecznosc}
- Cel: 1 krótkie nagranie JP tygodniowo (30–90 s) – wspólny głos/tożsamość

MATERIA PRZESTRZENI:
- Kącik «wioska»: drewno, tkanina, miseczka ryżu, zdjęcie morza, zapach (np. herbata sencha)
- Detal-kotwica dnia: zapisujemy i dzielimy się nim po południu.

NAWYKI OCHRONNE:
- Ograniczenie doom-scrollingu/AI: wspólne okno 2× dziennie po 10 min.
- «Brama»: zanim coś zobaczymy w sieci, pytamy «czy to wzmacnia naszą oś?»

NASTĘPNY KROK (7 dni):
1) Ustawić poranny rytuał i kotwicę natury w przestrzeni domowej.
2) 4 sesje JP po {godziny}h/tydz łącznie; zapis zdań w jednym zeszycie.
3) Dołączyć do społeczności i napisać pierwszą krótką wspólną wypowiedź JP.
4) Jedna «wyprawa nad wodę» – notatka z wrażeń (3 zdania każdej osoby).

UWAGA KOŃCOWA:
To nie symulacja «udawania Japonii». To wspólne budowanie ciała, języka i codzienności,
które pozwalają wam żyć w jakości marzenia TU i TERAZ, a później – jeśli zechcecie – w miejscu docelowym.
"""
    return textwrap.dedent(plan_txt).strip()


def plan(output_path: str = "plan_marzenia.txt") -> None:
    print(BOLD + "\n✿ Generator PlanU: «Wioska nad morzem – żywe marzenie w kręgu»\n" + RESET)
    imie = input("Twoje imię (jak chcesz, by grupa do Ciebie mówiła): ").strip()
    partner = input("Imię osoby, z którą dzielisz to marzenie (może być symboliczne): ").strip() or "Towarzyszka"
    wioska = input("Nazwa waszej wioski (roboczo): ").strip() or "Hamakaze"
    why = input("Dlaczego to życie jest dla was prawdziwe? ").strip()
    jp_level = input("Poziom japońskiego (0–10): ").strip() or "0"
    godziny = input("Ile godzin tygodniowo przeznaczacie łącznie na japoński? ").strip() or "6"
    natura = input("Jak połączycie się z «morzem» w waszym miejscu (np. rzeka, jezioro, kąpiele sól)? ").strip()
    rytual = input("Poranny mikro-rytuał wspólny (3–7 min), np. ryż + herbata + 1 zdanie JP: ").strip()
    spolecznosc = input("Jedno miejsce kontaktu z japońskim światem (online/offline) dla waszej dwójki: ").strip()

    plan_txt = build_plan_text(
        imie or "",
        partner,
        wioska,
        why,
        jp_level,
        godziny,
        natura,
        rytual,
        spolecznosc,
    )
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(plan_txt + "\n")
    print(f"\nZapisano plan w pliku: {output_path}\n")




def normalize_argv(argv: List[str]) -> List[str]:
    if not argv:
        return []
    mapping = {"--journey": "journey", "--plan": "plan", "--ui": "ui"}
    first = mapping.get(argv[0], argv[0])
    return [first, *argv[1:]]




def build_parser() -> argparse.ArgumentParser:

    parser = argparse.ArgumentParser(description="Prowadzona podróż i generator planu marzenia.")

    subparsers = parser.add_subparsers(dest="command")



    journey_parser = subparsers.add_parser("journey", help="Uruchom kosmiczną podróż oddechową.")

    journey_parser.add_argument("--max-cycles", type=int, help="Zatrzymaj pętlę po tylu cyklach (domyślnie nieskończoność).")

    journey_parser.add_argument("--tempo", type=float, default=1.0, help="Skala czasu pauz (np. 0.2 dla szybkiego podglądu).")

    journey_parser.add_argument("--skip-time-loss", action="store_true", help="Pomiń celowe straty czasu w falach.")

    journey_parser.add_argument("--log-file", help="Zapisz transkrypcję podróży do wskazanego pliku.")



    plan_parser = subparsers.add_parser("plan", help="Uruchom generator planu wioski nad morzem.")

    plan_parser.add_argument("--output", default="plan_marzenia.txt", help="Ścieżka pliku do zapisania planu.")

    return parser

    plan_parser = subparsers.add_parser("plan", help="Uruchom generator planu wioski nad morzem.")
    plan_parser.add_argument("--output", default="plan_marzenia.txt", help="Ścieżka pliku do zapisania planu.")

    ui_parser = subparsers.add_parser("ui", help="Uruchom audiowizualny interfejs marzenia.")
    ui_parser.add_argument(
        "--tempo",
        type=float,
        default=0.6,
        help="Tempo startowe narracji (mnożnik czasu pauz).",
    )
    ui_parser.add_argument(
        "--cycles",
        type=int,
        default=1,
        help="Liczba cykli fali uruchamianych po starcie interfejsu.",
    )
    ui_parser.add_argument(
        "--skip-time-loss",
        action="store_true",
        help="Pomiń celowe straty czasu w domyślnej konfiguracji UI.",
    )
    return parser




def main(argv: Optional[List[str]] = None) -> None:

    parser = build_parser()

    args = parser.parse_args(normalize_argv(argv or sys.argv[1:]))



    if args.command == "journey":

        journey(

            max_cycles=args.max_cycles,

            tempo=args.tempo,

            include_time_loss=not args.skip_time_loss,

            log_path=args.log_file,

        )

    elif args.command == "plan":

        plan(output_path=args.output)

    else:

        parser.print_help()

    elif args.command == "plan":
        plan(output_path=args.output)
    elif args.command == "ui":
        try:
            from marzenie_ui import launch_ui
        except ModuleNotFoundError as exc:  # pragma: no cover - defensive
            print(f"Nie można załadować interfejsu: {exc}")
            sys.exit(1)

        launch_ui(
            default_tempo=args.tempo,
            default_cycles=args.cycles,
            default_skip_time_loss=args.skip_time_loss,
        )
    else:
        parser.print_help()




if __name__ == "__main__":

    try:

        main()

    except KeyboardInterrupt:

        print("\nPrzerwano. Zadbaj o łagodne domknięcie oddechem.\n")

marzenie_ui.py
Nowość
+ 434- 0
"""Audiowizualny interfejs dla marzenie.py.

Aplikacja wykorzystuje tkinter do prezentacji animowanych fal, narracji oraz
wygodnego generatora planu. Wyświetlana narracja pochodzi bezpośrednio z
funkcji `journey` i jest streamowana w czasie rzeczywistym. Proste sygnały
akustyczne (dzwonek okna) towarzyszą kluczowym fragmentom oddechowym.
"""

from __future__ import annotations

import contextlib
import math
import queue
import threading
from pathlib import Path
from typing import Optional

import tkinter as tk
from tkinter import filedialog, messagebox, ttk

import marzenie


class QueueWriter:
    """Obiekt do przekierowania stdout do kolejki wątku UI."""

    def __init__(self, q: "queue.Queue") -> None:
        self.queue = q
        self._buffer = ""

    def write(self, data: str) -> int:  # pragma: no cover - funkcja pomocnicza
        if not data:
            return 0
        self._buffer += data
        while "\n" in self._buffer:
            line, self._buffer = self._buffer.split("\n", 1)
            self.queue.put(("text", line + "\n"))
        return len(data)

    def flush(self) -> None:  # pragma: no cover - funkcja pomocnicza
        if self._buffer:
            self.queue.put(("text", self._buffer))
            self._buffer = ""


class PlanDialog(tk.Toplevel):
    """Okno dialogowe do generowania planu marzenia."""

    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master)
        self.title("Plan wioski nad morzem")
        self.resizable(True, True)
        self.generated_text = ""

        self.transient(master)
        self.grab_set()

        fields = [
            ("imie", "Twoje imię (jak chcesz, by grupa mówiła):", ""),
            ("partner", "Imię towarzyszki / towarzysza marzenia:", "Towarzyszka"),
            ("wioska", "Robocza nazwa waszej wioski:", "Hamakaze"),
            ("why", "Dlaczego to życie jest dla was prawdziwe?:", ""),
            ("jp_level", "Poziom japońskiego (0–10):", "0"),
            ("godziny", "Ile godzin tygodniowo na japoński łącznie?:", "6"),
            (
                "natura",
                "Kotwica natury (zastępstwo morza – np. rzeka, kąpiele soli):",
                "",
            ),
            (
                "rytual",
                "Poranny mikro-rytuał (3–7 min), np. ryż + herbata + zdanie JP:",
                "",
            ),
            (
                "spolecznosc",
                "Jedno miejsce kontaktu z japońskim światem (online/offline):",
                "",
            ),
        ]

        container = ttk.Frame(self, padding=16)
        container.grid(column=0, row=0, sticky="nsew")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        container.columnconfigure(1, weight=1)

        self.entries: dict[str, ttk.Entry] = {}
        for row, (key, label, default) in enumerate(fields):
            ttk.Label(container, text=label).grid(column=0, row=row, sticky="w", padx=(0, 12), pady=4)
            entry = ttk.Entry(container)
            entry.grid(column=1, row=row, sticky="ew", pady=4)
            if default:
                entry.insert(0, default)
            self.entries[key] = entry

        self.output = tk.Text(container, height=14, wrap="word")
        self.output.grid(column=0, row=len(fields), columnspan=2, sticky="nsew", pady=(16, 8))
        self.output.configure(state="disabled")
        container.rowconfigure(len(fields), weight=1)

        scrollbar = ttk.Scrollbar(container, command=self.output.yview)
        scrollbar.grid(column=2, row=len(fields), sticky="nsw")
        self.output.configure(yscrollcommand=scrollbar.set)

        button_frame = ttk.Frame(container)
        button_frame.grid(column=0, row=len(fields) + 1, columnspan=2, sticky="e", pady=(0, 0))

        ttk.Button(button_frame, text="Generuj plan", command=self.generate).grid(column=0, row=0, padx=4)
        ttk.Button(button_frame, text="Zapisz do pliku", command=self.save_plan).grid(column=1, row=0, padx=4)
        ttk.Button(button_frame, text="Zamknij", command=self.close).grid(column=2, row=0, padx=4)

    def _collect_data(self) -> dict[str, str]:
        data = {key: entry.get().strip() for key, entry in self.entries.items()}
        data["partner"] = data.get("partner") or "Towarzyszka"
        data["wioska"] = data.get("wioska") or "Hamakaze"
        data["jp_level"] = data.get("jp_level") or "0"
        data["godziny"] = data.get("godziny") or "6"
        return data

    def generate(self) -> None:
        values = self._collect_data()
        self.generated_text = marzenie.build_plan_text(
            values.get("imie", ""),
            values["partner"],
            values["wioska"],
            values.get("why", ""),
            values["jp_level"],
            values["godziny"],
            values.get("natura", ""),
            values.get("rytual", ""),
            values.get("spolecznosc", ""),
        )
        self.output.configure(state="normal")
        self.output.delete("1.0", "end")
        self.output.insert("end", self.generated_text)
        self.output.configure(state="disabled")
        self.output.see("1.0")

    def save_plan(self) -> None:
        if not self.generated_text:
            messagebox.showinfo("Plan", "Najpierw wygeneruj plan, aby zapisać plik.")
            return
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            initialfile="plan_marzenia.txt",
            filetypes=[("Pliki tekstowe", "*.txt"), ("Wszystkie pliki", "*.*")],
        )
        if not filename:
            return
        Path(filename).write_text(self.generated_text + "\n", encoding="utf-8")
        messagebox.showinfo("Plan", f"Zapisano plan w pliku: {filename}")

    def close(self) -> None:
        self.grab_release()
        self.destroy()


class MarzenieApp:
    """Główne okno aplikacji audiowizualnej."""

    CANVAS_HEIGHT = 220
    CANVAS_WIDTH = 720

    def __init__(
        self,
        default_tempo: float = 0.6,
        default_cycles: int = 1,
        default_skip_time_loss: bool = False,
    ) -> None:
        self.root = tk.Tk()
        self.root.title("Wioska nad morzem – audiowizualne marzenie")
        self.root.geometry("900x720")
        self.root.minsize(760, 640)

        self.output_queue: "queue.Queue" = queue.Queue()
        self.writer = QueueWriter(self.output_queue)
        self.journey_thread: Optional[threading.Thread] = None
        self.animation_phase = 0.0

        self.tempo_var = tk.DoubleVar(value=default_tempo)
        self.cycles_var = tk.IntVar(value=max(1, default_cycles))
        self.skip_time_loss_var = tk.BooleanVar(value=default_skip_time_loss)
        self.status_var = tk.StringVar(value="Czekam na początek podróży.")

        self._build_layout()
        self._configure_tags()
        self._animate_waves()
        self._process_queue()

        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

    # --- konfiguracja UI -------------------------------------------------
    def _build_layout(self) -> None:
        canvas_frame = ttk.Frame(self.root)
        canvas_frame.pack(fill="x", padx=16, pady=(16, 8))

        self.canvas = tk.Canvas(
            canvas_frame,
            width=self.CANVAS_WIDTH,
            height=self.CANVAS_HEIGHT,
            bg="#0b1d2a",
            highlightthickness=0,
        )
        self.canvas.pack(fill="both", expand=True)
        self._create_canvas_elements()

        controls = ttk.Frame(self.root, padding=(16, 8))
        controls.pack(fill="x")

        self.start_button = ttk.Button(controls, text="Start podróży", command=self.start_journey)
        self.start_button.grid(column=0, row=0, padx=(0, 12))

        ttk.Label(controls, text="Tempo narracji").grid(column=1, row=0, sticky="w")
        tempo_scale = ttk.Scale(
            controls,
            from_=0.2,
            to=1.5,
            variable=self.tempo_var,
            orient="horizontal",
        )
        tempo_scale.grid(column=1, row=1, sticky="we", padx=(0, 20))

        ttk.Label(controls, text="Liczba cykli fali").grid(column=2, row=0, sticky="w")
        cycles_spin = ttk.Spinbox(
            controls,
            from_=1,
            to=9,
            textvariable=self.cycles_var,
            width=5,
        )
        cycles_spin.grid(column=2, row=1, sticky="w")

        skip_check = ttk.Checkbutton(
            controls,
            text="Pomiń celowe straty czasu",
            variable=self.skip_time_loss_var,
        )
        skip_check.grid(column=3, row=0, rowspan=2, sticky="w", padx=(20, 0))

        ttk.Button(controls, text="Wyczyść narrację", command=self.clear_text).grid(column=4, row=0, padx=12)
        ttk.Button(controls, text="Generator planu", command=self.open_plan_dialog).grid(column=5, row=0)

        controls.columnconfigure(1, weight=1)

        status_bar = ttk.Frame(self.root, padding=(16, 0))
        status_bar.pack(fill="x")
        ttk.Label(status_bar, textvariable=self.status_var).pack(anchor="w")

        text_frame = ttk.Frame(self.root, padding=(16, 8))
        text_frame.pack(fill="both", expand=True)

        self.output_text = tk.Text(
            text_frame,
            wrap="word",
            state="disabled",
            font=("Helvetica", 13),
            bg="#101b2a",
            fg="#f5f3ff",
            relief="flat",
            padx=12,
            pady=12,
        )
        self.output_text.pack(side="left", fill="both", expand=True)

        text_scroll = ttk.Scrollbar(text_frame, command=self.output_text.yview)
        text_scroll.pack(side="right", fill="y")
        self.output_text.configure(yscrollcommand=text_scroll.set)

    def _configure_tags(self) -> None:
        self.output_text.tag_configure("title", font=("Helvetica", 16, "bold"), foreground="#ffd27f")
        self.output_text.tag_configure("wave", font=("Helvetica", 14, "bold"), foreground="#8ecae6")
        self.output_text.tag_configure("breath", foreground="#a3d9a5")
        self.output_text.tag_configure("mantra", font=("Helvetica", 14, "italic"), foreground="#ffb4a2")
        self.output_text.tag_configure("meta", foreground="#7f8da6")

    def _create_canvas_elements(self) -> None:
        self.canvas.delete("all")
        width = self.CANVAS_WIDTH
        height = self.CANVAS_HEIGHT

        # tło gradientowe
        gradient_colors = ["#0b1d2a", "#10233a", "#152c4a", "#193556", "#1e3f63", "#21496f"]
        slice_height = height / len(gradient_colors)
        for idx, color in enumerate(gradient_colors):
            top = idx * slice_height
            bottom = (idx + 1) * slice_height
            self.canvas.create_rectangle(0, top, width, bottom, fill=color, outline="")

        self.sun = self.canvas.create_oval(width - 160, 40, width - 40, 140, fill="#ffd27f", outline="")
        self.wave_back = self.canvas.create_polygon([], fill="#284b80", outline="", smooth=True)
        self.wave_front = self.canvas.create_polygon([], fill="#3a6ea5", outline="", smooth=True)

    # --- animacja --------------------------------------------------------
    def _wave_points(self, phase: float, amplitude: float, baseline: float, width: int) -> list[float]:
        step = 24
        points: list[float] = []
        for x in range(0, width + step, step):
            y = baseline + math.sin((x / 80.0) + phase) * amplitude
            points.extend([x, y])
        points.extend([width, self.CANVAS_HEIGHT, 0, self.CANVAS_HEIGHT])
        return points

    def _animate_waves(self) -> None:
        width = max(self.canvas.winfo_width(), self.CANVAS_WIDTH)
        self.animation_phase += 0.18
        back_points = self._wave_points(self.animation_phase, 10, self.CANVAS_HEIGHT - 70, width)
        front_points = self._wave_points(self.animation_phase + 0.8, 14, self.CANVAS_HEIGHT - 50, width)
        self.canvas.coords(self.wave_back, *back_points)
        self.canvas.coords(self.wave_front, *front_points)
        sun_offset = 5 * math.sin(self.animation_phase / 3)
        self.canvas.coords(
            self.sun,
            width - 160,
            40 + sun_offset,
            width - 40,
            140 + sun_offset,
        )
        self.root.after(80, self._animate_waves)

    # --- obsługa narracji ------------------------------------------------
    def start_journey(self) -> None:
        if self.journey_thread and self.journey_thread.is_alive():
            messagebox.showinfo("Podróż", "Narracja już trwa. Zaczekaj na zakończenie.")
            return
        self.clear_text()
        self.status_var.set("Rozpoczynam podróż – wsłuchaj się w oddech.")
        self.start_button.configure(state="disabled")

        def run() -> None:
            self.output_queue.put(("status", "journey_start"))
            try:
                with contextlib.redirect_stdout(self.writer):
                    marzenie.journey(
                        max_cycles=int(self.cycles_var.get()),
                        tempo=float(self.tempo_var.get()),
                        include_time_loss=not self.skip_time_loss_var.get(),
                    )
            except Exception as exc:  # pragma: no cover - komunikat błędu
                self.output_queue.put(("status", ("journey_error", str(exc))))
            else:
                self.output_queue.put(("status", "journey_end"))

        self.journey_thread = threading.Thread(target=run, daemon=True)
        self.journey_thread.start()

    def clear_text(self) -> None:
        self.output_text.configure(state="normal")
        self.output_text.delete("1.0", "end")
        self.output_text.configure(state="disabled")

    def open_plan_dialog(self) -> None:
        PlanDialog(self.root)

    def _append_text(self, data: str) -> None:
        clean = marzenie.ANSI_ESCAPE_RE.sub("", data)
        stripped = clean.strip()
        tag = None
        if stripped.startswith("✿") or stripped.startswith("∞"):
            tag = "title"
        elif "Fala" in stripped:
            tag = "wave"
        elif "Wdech" in stripped or "Wydech" in stripped:
            tag = "breath"
        elif "「" in stripped:
            tag = "mantra"
        elif stripped.startswith("Nasza wspólna"):
            tag = "meta"

        if any(word in stripped for word in ["Wdech", "Wydech", "mantra", "Nasza wspólna"]):
            self.root.bell()

        self.output_text.configure(state="normal")
        if tag:
            self.output_text.insert("end", clean, tag)
        else:
            self.output_text.insert("end", clean)
        self.output_text.configure(state="disabled")
        self.output_text.see("end")

    def _handle_status(self, payload: object) -> None:
        if payload == "journey_start":
            return
        if payload == "journey_end":
            self.status_var.set("Podróż zakończona. Możesz uruchomić ją ponownie lub wygenerować plan.")
            self.start_button.configure(state="normal")
            return
        if isinstance(payload, tuple) and payload[0] == "journey_error":
            self.status_var.set("Wystąpił błąd podczas podróży.")
            self.start_button.configure(state="normal")
            messagebox.showerror("Podróż", payload[1])

    def _process_queue(self) -> None:
        try:
            while True:
                kind, payload = self.output_queue.get_nowait()
                if kind == "text":
                    self._append_text(str(payload))
                elif kind == "status":
                    self._handle_status(payload)
        except queue.Empty:
            pass
        self.root.after(80, self._process_queue)

    # --- zamykanie -------------------------------------------------------
    def _on_close(self) -> None:
        if self.journey_thread and self.journey_thread.is_alive():
            if not messagebox.askokcancel(
                "Zamykanie", "Narracja jest nadal odtwarzana. Czy na pewno chcesz zamknąć?"
            ):
                return
        self.root.destroy()

    def run(self) -> None:
        self.root.mainloop()


def launch_ui(
    default_tempo: float = 0.6,
    default_cycles: int = 1,
    default_skip_time_loss: bool = False,
) -> None:
    """Uruchom aplikację tkinter z przekazanymi wartościami domyślnymi."""

    app = MarzenieApp(
        default_tempo=default_tempo,
        default_cycles=default_cycles,
        default_skip_time_loss=default_skip_time_loss,
    )
    app.run()


if __name__ == "__main__":
    launch_ui()
