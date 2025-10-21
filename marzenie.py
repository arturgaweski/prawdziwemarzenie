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
