import json
import pandas as pd
import re
import os


def json_to_excel_table(json_path, output_path="ranking_table.xlsx"):
    # wczytanie danych z pliku JSON
    with open(json_path, 'r') as f:
        data = json.load(f)

    # wyciągnięcie i zaokrąglenie wyników, zamiana nazw modeli na liczby
    scores = {
        int(re.search(r"model_(\d+)", key).group(1)): round(value, 3)
        for key, value in data["iptm+ptm"].items()
    }

    # stworzenie DataFrame z kolumną 'model' pisaną małymi literami
    df = pd.DataFrame(sorted(scores.items()), columns=["model", "iptm + ptm"])

    # jeśli JSON zawiera listę 'order' (jak w otrzymanych rankingach), to sortuj modele zgodnie z tą kolejnością
    if "order" in data and "model" in df.columns:
        # wyciągnij numery modeli z listy 'model_1', 'model_2', ... jako liczby całkowite
        order = [
            int(re.search(r"model_(\d+)", name).group(1))
            for name in data["order"]
        ]
        # utwórz tymczasową kolumnę z pozycją modelu w podanej kolejności (jeśli brak ustaw na nieskończoność)
        df["Order"] = df["model"].apply(lambda x: order.index(x) if x in order else float('inf'))
        # posortuj tabelę według tej kolejności i usuń tymczasową kolumnę
        df = df.sort_values("Order").drop(columns="Order")

    # jeśli plik już istnieje -> jest usuwany, żeby uniknąć błędu zapisu
    if os.path.exists(output_path):
        os.remove(output_path)

    # eksport danych do excela z podstawowym formatowaniem
    with pd.ExcelWriter(output_path, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Scores")
        workbook = writer.book
        worksheet = writer.sheets["Scores"]

        # formatowanie nagłówka
        header_format = workbook.add_format({
            'bold': True,
            'text_wrap': True,
            'valign': 'middle',
            'align': 'center',
            'fg_color': '#D7E4BC',
            'border': 1
        })

        # formatowanie komórek
        cell_format = workbook.add_format({
            'align': 'center',
            'valign': 'vcenter',
            'border': 1
        })

        for col_num, value in enumerate(df.columns.values):
            worksheet.write(0, col_num, value, header_format)
            worksheet.set_column(col_num, col_num, 15, cell_format)

    print(f"Tabela Excela zapisana do: {output_path}")

# ścieżka do folderu z plikami JSON
directory = "Multimer/ranking"

# przetwarzanie każdego pliku JSON w folderze
for filename in os.listdir(directory):
    if filename.endswith(".json"):
        json_path = os.path.join(directory, filename)
        base_name = os.path.splitext(filename)[0]
        output_file = f"{base_name}.xlsx"

        json_to_excel_table(json_path, output_path=output_file)
