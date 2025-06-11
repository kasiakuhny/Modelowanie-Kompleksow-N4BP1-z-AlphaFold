import os


def read_fasta(fasta_path):
    """czytanie pliku fasta i zwrocenie sekwencji jako string"""
    with open(fasta_path, "r") as file:
        lines = file.readlines()

    sequence = "".join(line.strip() for line in lines if not line.startswith(">"))
    return sequence


def get_sequence(sequence, start, end):
    """wyekstrahowanie wybranej czesci sekwencji"""
    return sequence[start - 1:end]  # Correct slicing: end is included!


def main():
    sequences = []

    while True:
        name = input("Podaj nazwe sekwencji (lub wpisz 'end' zeby zakonczyc): ").strip()
        if name.lower() == 'end':
            break

        fasta_path = input("Podaj sciezke do pliku FASTA: ").strip()

        # usuniecie ewentualnych cudzyslowiow z podawanej sciezki
        fasta_path = fasta_path.strip('"').strip("'")

        if not os.path.exists(fasta_path):
            print(f"Plik {fasta_path} nie istnieje. Spradz sciezke.")
            continue

        sequence = read_fasta(fasta_path)

        choice = input(
            "Wpisz 'calosc' zeby wyekstrahowac pelna sekwencje lub 'zakres' zeby podac poczatkowa i koncowa pozycje: ").strip().lower()

        if choice == 'calosc':
            extracted_seq = sequence
        else:
            start = int(input("Podaj poczatkowa pozycje: ").strip())
            end = int(input("Podaj koncowa pozycje: ").strip())
            extracted_seq = get_sequence(sequence, start, end)

        # dodawanie nowego fragmentu sekwencji do pliku
        sequences.append(f">{name}\n{extracted_seq}")

    output_name = input("Podaj nazwe pliku wyjsciowego: ").strip()
    output_path = os.path.join("Multimer", f"{output_name}.fasta")

    with open(output_path, "w") as f:
        f.write("\n".join(sequences))

    print(f"Plik wyjsciowy zapisany w {output_path}")


if __name__ == "__main__":
    main()
