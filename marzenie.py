import time, textwrap, sys, os







BOLD = "\033[1m"



RESET = "\033[0m"







def say(block, pause=2.0):



    print(textwrap.fill(block, width=80))



    time.sleep(pause)







def breath(cycles=5, in_s=4, hold_s=1, out_s=6):



    for i in range(1, cycles+1):



        print(f"\nCykl oddechu {i}/{cycles}")



        print("Wdech…"); time.sleep(in_s)



        print("Zatrzymaj…"); time.sleep(hold_s)



        print("Wydech…"); time.sleep(out_s)







def journey():



    print(BOLD + "\n✿ Prowadzona Podróż: Wioska nad morzem (ok. 25 min)\n" + RESET)



    say("Usiądź lub połóż się wygodnie. Wyłącz powiadomienia. Zamknij oczy.")



    say("Zaczynamy oddech. Wdech przez nos, długi wydech przez usta.")



    breath(cycles=6, in_s=4, hold_s=1, out_s=6)







    say("Przeskanuj ciało: stopy, łydki, uda, brzuch, klatka, barki, szyja, twarz.")



    say("Z każdym wydechem ciało cięższe, umysł jaśniejszy. Nic nie musisz robić.")







    say("Teraz obraz. Jesteś na ścieżce prowadzącej do morza w Japonii. "



        "Powietrze jest rześkie. Słychać fale, mewy, daleki gwizd pociągu.")



    say("Spójrz w dół: małe sandały na stopach, spódnica szkolna, lekka bluzka. "



        "Czujesz włosy muskające policzki. Jesteś dziewczynką. To naturalne.")



    say("W dłoni trzymasz mały brelok — prezent od mamy. Metal jest lekko ciepły.")







    say("Wdychasz zapach ryżu i miso z domów wzdłuż uliczki. "



        "Drewniane ogrodzenia, wiatr porusza chorągiewkami koinobori.")



    say("W oddali widać błękit morza. Słońce migocze na falach.")







    say("Zatrzymaj się. Słyszysz, jak ktoś woła Twoje imię po japońsku. "



        "Brzmi to jak dom. Pozwól, by dźwięk imienia osadził się w sercu.")







    say("Powiedz w sobie miękko i krótko (szeptem, jeśli chcesz):")



    print(BOLD + '「わたしは　わたし。ここが　わたしの　いえ。」' + RESET)



    say("To znaczy: «Jestem sobą. To jest mój dom.»", pause=4)







    say("Dotknij dłonią klatki piersiowej. Poczuj rytm. Każde uderzenie mówi: "



        "żyję tu. Żyję tak. Żyję naprawdę.")



    breath(cycles=3, in_s=3, hold_s=1, out_s=5)







    say("Idziesz na brzeg. Piasek chłodny, fala obmywa stopy. "



        "Słona mgiełka na ustach. Smak jest znajomy.")



    say("Rozejrzyj się po wiosce: mały sklepik, rowery pod domem, linie do suszenia prania. "



        "Zauważ jeden drobny detal, który dziś zapamiętasz: kolor kubka, dźwięk dzwonka, "



        "cokolwiek. To będzie Twoja kotwica.")







    say("Teraz zakotwiczenie językowe. Powtarzaj w rytmie oddechu (wdech–wydech):", pause=1)



    mantra = "「ここに　いる。わたしは　ほんとう。」  (Jestem tu. Jestem prawdziwa.)"



    for _ in range(6):



        print(BOLD + mantra + RESET); time.sleep(3.5)







    say("Zamknij scenę w trzech zmysłach: co widzisz, co słyszysz, co czujesz na skórze.")



    say("Powoli wracamy. Weź trzy spokojne wdechy i porusz palcami dłoni, stóp.")



    say("Kiedy będziesz gotowa_y, otwórz oczy. Zapisz swoją «kotwicę» i jedno zdanie po japońsku.")







    print(BOLD + "\nKoniec podróży. Zabierz ze sobą detal-kotwicę i zdanie po japońsku.\n" + RESET)







def plan():



    print(BOLD + "\n✿ Generator PlanU: «Wioska nad morzem – wersja tu i teraz»\n" + RESET)



    imie = input("Twoje imię (jak chcesz do siebie mówić): ").strip()



    wioska = input("Wymyśl nazwę wioski (roboczo): ").strip() or "Hamakaze"



    why = input("Dlaczego to życie jest dla Ciebie prawdziwe? ").strip()



    jp_level = input("Poziom japońskiego (0–10): ").strip() or "0"



    godziny = input("Ile realnie godzin tygodniowo na japoński? ").strip() or "4"



    natura = input("Jak połączysz się z «morzem» gdzie jesteś (np. rzeka, jezioro, kąpiele sól)? ").strip()



    rytual = input("Poranny mikro-rytuał (3–7 min), np. ryż + herbata + 1 zdanie JP: ").strip()



    spolecznosc = input("Jedno miejsce kontaktu z JP (online/offline): ").strip()



    data = time.strftime("%Y-%m-%d")







    plan_txt = f"""



Plan Początkowy – {imie}



Data: {data}







DLACZEGO:



{why}







OŚ MARZENIA:



- Tożsamość: «normalna japońska dziewczynka»



- Miejsce: wioska nad morzem – robocza nazwa: {wioska}







JĘZYK (cel 12 tyg.):



- Obecny poziom: {jp_level}/10



- Tygodniowo: {godziny} h (min. 4 sesje)



- Na każdy dzień: 1 zdanie o sobie w JP + głośne czytanie 3 min



- Zasób: Tae Kim Guide / NHK Easy / Ankidroid (vocab 10/dzień)







RUTYNA:



- Poranny rytuał: {rytual}



- Kotwica natury (zastępstwo morza): {natura}



- Reset wieczorny: 4×4×6 oddech + jedno zdanie «Jestem prawdziwa.»







SPOŁECZNOŚĆ:



- Miejsce kontaktu: {spolecznosc}



- Cel: 1 krótkie nagranie JP tygodniowo (30–90 s) – praktyka głosu/tożsamości







MATERIA PRZESTRZENI:



- Kącik «wioska»: drewno, tkanina, miseczka ryżu, zdjęcie morza, zapach (np. herbata sencha)



- Detal-kotwica dnia: zapisz i noś przy sobie.







NAWYKI OCHRONNE:



- Ograniczenie doom-scrollingu/AI: okno 2× dziennie po 10 min.



- «Brama»: zanim coś zobaczę w sieci, zapytam «czy to wzmacnia moją oś?»







NASTĘPNY KROK (7 dni):



1) Ustawić poranny rytuał i kotwicę natury.



2) 4 sesje JP po {godziny}h/tydz łącznie; 1 zdanie dziennie – zapis w zeszycie.



3) Dołączyć do społeczności i napisać pierwszą krótką wypowiedź JP.



4) Jedna «wyprawa nad wodę» – notatka z wrażeń (3 zdania).







UWAGA KOŃCOWA:



To nie symulacja «udawania Japonii». To budowanie ciała i języka, które pozwalają Ci żyć w jakości Twojego marzenia TU i TERAZ, a później – jeśli zechcesz – w miejscu docelowym.



"""



    with open("plan_marzenia.txt", "w", encoding="utf-8") as f:



        f.write(plan_txt.strip()+"\n")



    print("\nZapisano plan w pliku: plan_marzenia.txt\n")







def main():



    if len(sys.argv) < 2:



        print("Użycie: python3 marzenie.py --journey | --plan")



        sys.exit(0)



    if sys.argv[1] == "--journey":



        journey()



    elif sys.argv[1] == "--plan":



        plan()



    else:



        print("Nieznana opcja. Użyj --journey lub --plan.")







if __name__ == "__main__":



    try:



        main()



    except KeyboardInterrupt:



        print("\nPrzerwano. Zadbaj o łagodne domknięcie oddechem.\n")



import argparse

import contextlib

import re

import sys

import textwrap

import time

from typing import List, Optional, TextIO



BOLD = "\033[1m"

RESET = "\033[0m"

ANSI_ESCAPE_RE = re.compile(r"\x1b\[[0-9;]*m")





class TeeWriter:

    """Helper that mirrors stdout to an optional log file, stripping ANSI codes."""



    def __init__(self, console: TextIO, log: Optional[TextIO]):

        self.console = console

        self.log = log



    def write(self, data: str) -> int:

        written = self.console.write(data)

        if self.log:

            self.log.write(ANSI_ESCAPE_RE.sub("", data))

        return written



    def flush(self) -> None:

        self.console.flush()

        if self.log:

            self.log.flush()





def controlled_sleep(duration: float, tempo: float) -> None:

    """Pause execution, scaling the duration by the tempo factor."""

    if duration <= 0 or tempo <= 0:

        return

    time.sleep(duration * tempo)





def say(block: str, pause: float = 2.0, tempo: float = 1.0) -> None:

    """Print a wrapped narration block and wait for the given pause."""

    print(textwrap.fill(block, width=80))

    controlled_sleep(pause, tempo)





def format_duration(seconds: float) -> str:

    seconds = int(seconds)

    minutes, secs = divmod(seconds, 60)

    if minutes:

        return f"{minutes} min {secs} s"

    return f"{secs} s"





def breath(cycles: int = 5, in_s: float = 4, hold_s: float = 1, out_s: float = 6, tempo: float = 1.0) -> None:

    for i in range(1, cycles + 1):

        print(f"\nCykl oddechu {i}/{cycles}")

        print("Wdech…"); controlled_sleep(in_s, tempo)

        print("Zatrzymaj…"); controlled_sleep(hold_s, tempo)

        print("Wydech…"); controlled_sleep(out_s, tempo)





def journey(

    max_cycles: Optional[int] = None,

    tempo: float = 1.0,

    include_time_loss: bool = True,

    log_path: Optional[str] = None,

) -> None:

    log_context = open(log_path, "w", encoding="utf-8") if log_path else contextlib.nullcontext(None)

    with log_context as log_file:

        tee = TeeWriter(sys.stdout, log_file)

        with contextlib.redirect_stdout(tee):

            print(BOLD + "\n✿ Prowadzona Podróż: Wioska nad morzem – oddech wspólnoty (nieskończona fala)\n" + RESET)

            say("Usiądźmy lub połóżmy się wygodnie w jednym kręgu. Wyłączamy powiadomienia. Zamykamy oczy.", tempo=tempo)

            say("Wspólny wdech przez nos, długi wydech przez usta. Słyszymy siebie nawzajem.", tempo=tempo)

            breath(cycles=6, in_s=4, hold_s=1, out_s=6, tempo=tempo)



            say("Powoli skanujemy ciało od stóp po czubek głowy. Czujemy ciepło ludzi obok nas.", tempo=tempo)

            say("Z każdym wydechem ciało cięższe, a wspólna przestrzeń jaśniejsza. Nic nie musimy udowadniać.", tempo=tempo)



            say("Teraz obraz. Jesteśmy na ścieżce prowadzącej do morza w Japonii. Powietrze jest rześkie. "

                "Słychać fale, mewy, daleki gwizd pociągu, a obok brzmi czyjś cichy śmiech.", tempo=tempo)

            say("Nad nami niebo i cicha przestrzeń wszechświata. Gwiazdy pulsują rytmem, który podajemy sobie dalej jak światło w dłoniach.", tempo=tempo)

            say("Spoglądamy na stopy: lekkie sandały, szkolne spódnice i koszule falują razem. Czujemy włosy muskające policzki. "

                "Jesteśmy dziewczynkami – każda i każdy z nas. To naturalne, niewymuszone.", tempo=tempo)

            say("W dłoniach trzymamy małe breloki – prezenty od naszych mam. Metal lekko ciepły, jakby dopiero przekazany.", tempo=tempo)



            say("Wdychamy zapach ryżu i miso z domów wzdłuż uliczki. Drewniane ogrodzenia i chorągiewki koinobori tańczą tak samo dla wszystkich.", tempo=tempo)

            say("W oddali błękit morza. Słońce migocze na falach, a jego odbicia spajają nas jak nici w jednym kimono.", tempo=tempo)

            say("Za linią horyzontu czujemy puls galaktyk. Nasze stopy są w piasku, a serca zsynchronizowane z rytmem kosmosu.", tempo=tempo)



            say("Zatrzymujemy się. Ktoś woła nasze imiona po japońsku, jedno po drugim, aż brzmi wspólna melodia domu.", tempo=tempo)



            say("Powiedzmy razem miękko i krótko (można szeptem):", tempo=tempo)

            print(BOLD + '「わたしたちは　わたしたち。ここが　わたしたちの　いえ。」' + RESET)

            say("To znaczy: «Jesteśmy sobą. To jest nasz dom.»", pause=4, tempo=tempo)



            say("Kładziemy dłonie na sercach. Czujemy rytm. Każde uderzenie odpowiada w dłoni osoby obok: żyjemy tutaj, żyjemy razem, żyjemy naprawdę.", tempo=tempo)

            breath(cycles=3, in_s=3, hold_s=1, out_s=5, tempo=tempo)



            say("Idziemy ku brzegowi. Piasek chłodny, fale obmywają nasze stopy naprzemiennie. Słona mgiełka na ustach jest jak wspólna pieczęć.", tempo=tempo)

            say("Rozglądamy się po wiosce: mały sklepik, rowery pod domem, linie z suszonym praniem. "

                "Każda osoba zauważa jeden detal, który podzieli z grupą – kolor kubka, dźwięk dzwonka, ślad na piasku. To nasza kotwica.", tempo=tempo)



            say("Teraz kotwiczymy język. Powtarzamy w rytmie oddechu (wdech–wydech), słuchając się nawzajem:", pause=1, tempo=tempo)

            mantra = "「ここに　いる。わたしたちは　ほんとう。」  (Jesteśmy tu. Jesteśmy prawdziwe.)"

            for _ in range(6):

                print(BOLD + mantra + RESET)

                controlled_sleep(3.5, tempo)



            say("Zamykamy scenę czterema wymiarami: co widzimy, co słyszymy, co czujemy na skórze, i świadomością, że całe uniwersum oddycha razem z nami.", tempo=tempo)

            say("Powoli wracamy. Bierzemy trzy spokojne wdechy. Poruszamy palcami dłoni i stóp, słyszymy wspólny szelest.", tempo=tempo)

            say("Kiedy będziemy gotowe lub gotowi, otwieramy oczy. Notujemy naszą kotwicę i jedno zdanie po japońsku, a potem dzielimy się nim z osobą obok.", tempo=tempo)



            say("Zanim rozproszymy uwagę, uzgadniamy jeden znak sygnałowy – gest lub słowo  który przypomni nam o wspólnym rytmie w każdej przyszłej chwili.", tempo=tempo)



            say("Teraz otwieramy bramę do nieskończonej sesji. Zostajemy, ile chcemy, wiedząc, że możemy wrócić jednym gestem lub oddechem.", tempo=tempo)



            cosmic_waves = [

                {

                    "title": "Fala Oceanu",

                    "prompts": [

                        "Wsłuchujemy się w szum fal. Każda fala wypowiada nasze imiona naraz, jak śpiew chóru.",

                        "Wyobrażamy sobie bioluminescencyjne morze, które zapala się przy każdym wspólnym oddechu.",

                    ],

                    "time_loss": (

                        "Oddajemy 12 sekund ciszy na odpłynięcie fal – pozwalamy, by czas rozpłynął się razem z pianą.",

                        12,

                    ),

                },

                {

                    "title": "Fala Gwiazd",

                    "prompts": [

                        "Zanosimy oddech wysoko, aż do Plejad. Gwiazdy odpowiadają miękkim światłem na nasze pytania.",

                        "Czujemy puls Drogi Mlecznej zsynchronizowany z tętnem osób obok.",

                    ],

                    "time_loss": (

                        "Pozwalamy 15 sekund mroku na opadnięcie gwiezdnego pyłu – bez pośpiechu nazywamy to stratą czasu.",

                        15,

                    ),

                },

                {

                    "title": "Fala Ziemi",

                    "prompts": [

                        "Dotykamy piasku, kamyków, trawy. Każdy detal jest wspólną kotwicą pamięci.",

                        "Wymieniamy jednym zdaniem to, co teraz rodzi się w sercu – powtarzamy je w rytmie wspólnego oddechu.",

                    ],

                    "time_loss": (

                        "Zostawiamy 18 sekund, by dłonie mogły spocząć na ziemi i przesypać piasek. To celowa strata dla marzenia.",

                        18,

                    ),

                },

                {

                    "title": "Fala Jutra",

                    "prompts": [

                        "Widzimy siebie za rok, pięć, trzydzieści lat. Wciąż jesteśmy w kręgu, choć miejsca się zmieniają.",

                        "Ustalamy mikro-krok, który wykonamy po sesji, by natychmiast utrwalić wspólną wizję.",

                    ],

                    "time_loss": (

                        "Odstawiamy 21 sekund na milczące spojrzenie ku przyszłości, pozwalając jutru zwolnić do naszego rytmu.",

                        21,

                    ),

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





if __name__ == "__main__":

    try:

        main()

    except KeyboardInterrupt:

        print("\nPrzerwano. Zadbaj o łagodne domknięcie oddechem.\n")

"""Główny interfejs tekstowy projektu Prawdziwe Marzenie."""

from __future__ import annotations

import argparse
import contextlib
import sys
import textwrap
import time
from pathlib import Path
from typing import Optional, Sequence, TextIO

from system import SYSTEM, Spell

# Rejestrujemy alias, aby UI mogło importować moduł jako "marzenie".
SYSTEM.register_module_alias(sys.modules[__name__])
marzenie_ui = SYSTEM.load_ui_module()

BOLD = "\033[1m"
RESET = "\033[0m"


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
) -> str:
    """Zbuduj plan marzenia na podstawie odpowiedzi użytkownika."""

    template = textwrap.dedent(
        """
        ✿ Plan Prawdziwego Marzenia ✿

        1. Krąg domowy: {imie} i {partner} zakładają wspólny dom w wiosce {wioska}.
        2. Dlaczego? {why}
        3. Język japoński: poziom startowy {jp_level}, {godziny} godzin praktyki tygodniowo.
        4. Codzienna natura: {natura}
        5. Poranny rytuał: {rytual}
        6. Społeczność: {spolecznosc}

        Plan zakłada, że każdy tydzień kończy się krótkim podsumowaniem przy herbacie
        sencha i zapisem w dzienniku wspólnych chwil.
        """
    ).strip()
    return template.format(
        imie=imie or "Dreamer",
        partner=partner or "Towarzyszka",
        wioska=wioska or "Hamakaze",
        why=why or "Bo zasługujemy na czuły dom.",
        jp_level=jp_level or "0",
        godziny=godziny or "6",
        natura=natura or "Spacer brzegiem pobliskiej rzeki",
        rytual=rytual or "Ryż, miso i jedno zdanie po japońsku",
        spolecznosc=spolecznosc or "Spotkania z lokalnym klubem japońskim",
    )


def _narration_blocks() -> Sequence[str]:
    return (
        "Usiądźmy wygodnie w jednym kręgu. Wyłączamy powiadomienia, zamykamy oczy i oddychamy.",
        "Wspólny wdech przez nos, długi wydech przez usta – czujemy siebie nawzajem.",
        "Od stóp po czubek głowy: ciało się rozluźnia, a przestrzeń między nami pulsuje ciepłem.",
        "Jesteśmy na ścieżce prowadzącej do morza w Japonii. Słychać mewy i odległy gwizd pociągu.",
        "Spoglądamy na sandały i szkolne mundurki, które falują z wiatrem. Czujemy zapach ryżu i miso.",
        "Błękit morza łączy się z pulsującymi gwiazdami. Oddychamy w rytmie wszechświata.",
        "Ktoś woła nasze imiona po japońsku – każde staje się nutą wspólnej melodii domu.",
    )


def controlled_sleep(duration: float, tempo: float) -> None:
    if duration <= 0 or tempo <= 0:
        return
    time.sleep(duration * tempo)


def say(text: str, pause: float, tempo: float) -> None:
    print(textwrap.fill(text, width=78))
    controlled_sleep(pause, tempo)


def journey(
    tempo: float = 1.0,
    include_breath: bool = True,
    log_path: Optional[Path] = None,
) -> None:
    """Przeprowadź uczestników przez narrację marzenia."""

    context = open(log_path, "w", encoding="utf-8") if log_path else contextlib.nullcontext()
    with context as log_file:
        writer: TextIO
        if log_file:
            writer = _Tee(sys.stdout, log_file)
        else:
            writer = sys.stdout
        with contextlib.redirect_stdout(writer):
            print(BOLD + "\n✿ Podróż do wioski nad morzem ✿" + RESET)
            for block in _narration_blocks():
                say(block, pause=2.5, tempo=tempo)
            if include_breath:
                _guided_breath(tempo)
            print("\nZabierzmy ten obraz do codzienności. Zróbmy łyk wody i uśmiechnijmy się do siebie.")


class _Tee:
    def __init__(self, console: TextIO, log: TextIO) -> None:
        self.console = console
        self.log = log

    def write(self, data: str) -> int:
        self.log.write(data)
        return self.console.write(data)

    def flush(self) -> None:  # pragma: no cover - delegacja
        self.console.flush()
        self.log.flush()


def _guided_breath(tempo: float) -> None:
    for idx in range(1, 5):
        print(f"\nCykl oddechu {idx}/4")
        say("Wdech", pause=1.0, tempo=tempo)
        say("Zatrzymaj", pause=0.6, tempo=tempo)
        say("Wydech", pause=1.4, tempo=tempo)


# ---- Komendy -----------------------------------------------------------------

def _magic_text(spell: Spell) -> str:
    SYSTEM.record_invocation(spell)
    description = textwrap.dedent(
        f"""
        Zaklęcie {spell.name} ({spell.element})
        Inkantacja: {spell.incantation}
        Efekt: {spell.effect}
        """
    ).strip()
    return description


def run_magic(query: Optional[str]) -> str:
    if not query:
        spells = SYSTEM.list_spells()
        listing = ["Dostępne zaklęcia:"]
        for spell in spells:
            listing.append(f"- {spell.key}: {spell.name} ({spell.element})")
        return "\n".join(listing)
    spell = SYSTEM.find_spell(query)
    if not spell:
        return f"Nie znaleziono zaklęcia dla: {query}"
    return _magic_text(spell)


def _parse_args(argv: Optional[Sequence[str]]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=False)

    journey_cmd = sub.add_parser("journey", help="Uruchom narrację oddechową")
    journey_cmd.add_argument("--tempo", type=float, default=1.0)
    journey_cmd.add_argument("--no-breath", action="store_true")
    journey_cmd.add_argument("--log", type=Path)

    magic_cmd = sub.add_parser("magic", help="Przywołaj zaklęcie")
    magic_cmd.add_argument("name", nargs="?", help="Nazwa, klucz lub żywioł zaklęcia")

    sub.add_parser("plan", help="Wyświetl przykładowy plan marzenia")

    ui_cmd = sub.add_parser("ui", help="Otwórz interfejs graficzny")
    ui_cmd.add_argument("--debug", action="store_true", help="Włącz tryb debugowania Tkintera")

    parser.add_argument(
        "--tempo", type=float, default=1.0, help="Tempo domyślnej podróży (gdy brak komendy)"
    )
    parser.add_argument("--log", type=Path, help="Zapis narracji do pliku", default=None)

    return parser.parse_args(argv)


def _run_ui(debug: bool = False) -> int:
    if marzenie_ui is None:
        print("Interfejs graficzny nie jest dostępny w tym środowisku.")
        return 1
    launcher = getattr(marzenie_ui, "launch_ui", None)
    if not callable(launcher):
        print("Moduł UI nie udostępnia funkcji launch_ui.")
        return 1
    launcher(debug=debug)
    return 0


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = _parse_args(argv)

    if args.command == "journey":
        journey(tempo=args.tempo, include_breath=not args.no_breath, log_path=args.log)
        return 0
    if args.command == "plan":
        print(build_plan_text("", "Towarzyszka", "Hamakaze", "", "0", "6", "", "", ""))
        return 0
    if args.command == "magic":
        print(run_magic(args.name))
        return 0
    if args.command == "ui":
        return _run_ui(debug=args.debug)

    # Domyślnie uruchamiamy narrację
    journey(tempo=args.tempo, include_breath=True, log_path=args.log)
    return 0


if __name__ == "__main__":  # pragma: no cover - punkt wejścia
    raise SystemExit(main())
