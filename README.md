# Modelowanie-Kompleksow-N4BP1-z-AlphaFold
Pliki wejściowe, wyniki oraz kody pomocnicze stosowane w pracy licencjackiej.

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

## Skrypty pomocnicze
### DomainGenerator
Użyty w pracy do wizualizacji. Generuje pasek z zaznaczonymi w odpowiednich miejscach sekwencji nazwami domen w wybranych kolorach oraz skrypt do Chimery, który koloruje domeny białka zgodnie z nimi.

### multimerFileGenerator
Tworzenie plików wejściowych do programu AlphaFold Multimer - umożliwia wybieranie pożądanych części sekwencji i umieszcza je w jednym pliku akceptowanym przez COSMIC².

### TableGenerator
Przetwarzanie plików JSON na tabele w Excelu, zaokrąglenie wartości do trzech miejsc po przecinku

## Wymagania
Wszystkie wymagane biblioteki znajdują się w pliku requirements.txt. Aby je zainstalować, użyj polecenia:
```bash
pip install -r requirements.txt
```
## Pliki wynikowe

Ze względu na rozmiar danych foldery `Monomer/` (uwzględniający jedynie N4BP1 jako przykład ze względu na rozmiar) oraz `Multimer/` zostały spakowane jako archiwum `.7z`.

**Przed użyciem należy rozpakować plik:**

```bash
7z x multimer.7z

