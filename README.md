# Modelowanie-Kompleksow-N4BP1-z-AlphaFold
Pliki wejściowe, wyniki oraz kody pomocnicze stosowane w pracy licencjackiej

## Wykorzystane parametry programów

### Wykorzystane parametry AlphaFold 2 na [Galaxy.org](https://galaxy.org):

| Ustawienie                | Wartość domyślna                      | Opis                                           |
|--------------------------|-------------------------------------|------------------------------------------------|
| **Liczba modeli**         | `5`                                   | Generowana jest pięciomodelowa predykcja (domyślnie 5).       |
| **Amber Relax**           | `Włączony`                           | Automatyczna optymalizacja struktury po predykcji (domyślnie włączone). |
| **Plot MSA**              | `Włączony`                          | Wykresy wielokrotnych dopasowań sekwencji (MSA) (domyślnie wyłączone). |
| **Wyjścia confidence/PAE**| `Włączone`                          | Szczegółowe pliki z ocenami pewności predykcji i PAE (domyślnie wyłączone). |
| **Reuse MSA**             | `Wyłączone`                         | Opcja ponownego użycia istniejących MSA (domyślnie wyłączona). |
| **MSA-only / Collect MSAs**| `Wyłączone`                        | Opcje zbierania i zapisywania MSA (domyślnie wyłączone). |


### Domyślne ustawienia AlphaFold Multimer na [COSMIC²](https://cosmic-cryoem.org/):

| Ustawienie              | Wartość domyślna                    | Opis                                                      |
|------------------------|-----------------------------------|-----------------------------------------------------------|
| **Model**              | `multimer`                        | Tryb przewidywania struktur kompleksów białkowych (domyślnie monomer)       |
| **Models to relax**      | `none`                         | Automatyczna relaksacja struktury po predykcji (domyślnie none)        |
| **Database**            | `full_dbs`                         | Używana baza danych sekwencji (full_dbs domyślna)                           |
| **Ilość predykcji na model**      | `1`                      | Sekwencje wszystkich łańcuchów białkowych w kompleksie    |
| **Latest date to use for template search** | `2023-05-30` |  Najpóźniejsza data, do której mogą pochodzić szablony (struktury białkowe) użyte do dopasowania w bazie PDB, uzyta wartość domyślna |



---

Te ustawienia zapewniają dobre domyślne działanie dla większości analiz, jednocześnie dając użytkownikowi możliwość ręcznego dostosowania parametrów w interfejsie Galaxy.

---

*Źródła:* analiza obecnej wersji narzędzia AlphaFold na Galaxy.org oraz dokumentacja dostępna na platformie.
