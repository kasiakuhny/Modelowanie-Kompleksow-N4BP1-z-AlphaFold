import matplotlib.pyplot as plt
import matplotlib.patches as patches

# pobranie długości sekwencji od użytkownika
seq_length = int(input("Podaj całkowitą długość sekwencji: "))

# ustawienie zakresu dużego prostokąta (stała wartość 50)
max_visual_length = 50

# skalowanie wartości
scale_factor = max_visual_length / seq_length

# tworzenie pliku z komendami dla Chimera
chimera_script = []

# dodanie komendy zmiany koloru tła na solid white
chimera_script.append("background solid white")

# tworzenie figury i osi
fig, ax = plt.subplots(figsize=(20, 6)) 

# ustawienie tła
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

# wysokość dużego prostokąta
large_rect_height = 2

# tworzenie dużego prostokąta z kolorem #a9a9a9 (dark gray)
large_rect = patches.Rectangle((0, 0), max_visual_length, large_rect_height, linewidth=2, edgecolor='#a9a9a9', facecolor='#a9a9a9')
ax.add_patch(large_rect)

# lista na prostokąty
small_rects = []

print("\nPodaj dane prostokątów w formacie: start, end, kolor, napis")
print("Kolor wpisz w formacie HEX, dostępne na stronie: https://www.cgl.ucsf.edu/chimera/docs/UsersGuide/colortables.html")
print("Wpisz 'end' aby zakończyć\n")

while True:
    user_input = input("Prostokąt: ")
    if user_input.lower() == "end":
        break

    try:
        start, end, color, label = user_input.split(", ")
        start, end = int(start), int(end)

        # skalowanie wartości do zakresu 0-50
        start_scaled = start * scale_factor
        end_scaled = end * scale_factor

        small_rects.append((start_scaled, end_scaled, color, label, start, end))

        # dodanie komendy do skryptu Chimery
        chimera_script.append(f"color {color} :{start}-{end}")

    except ValueError:
        print("Błędny format! Wprowadź dane jako: start, end, kolor, napis")
        continue

# dodanie komendy dla początkowego koloru białka na ciemnoszary
chimera_script.insert(0, "color darkgrey")

# rysowanie prostokątów
for start_scaled, end_scaled, color, label, start, end in small_rects:
    width_scaled = end_scaled - start_scaled
    rect = patches.Rectangle((start_scaled, 0), width_scaled, large_rect_height, linewidth=2, edgecolor=color, facecolor=color)
    ax.add_patch(rect)

    # dodanie napisu na prostokącie
    ax.text(start_scaled + width_scaled / 2, large_rect_height / 2, label, ha='center', va='center', fontsize=15, color='white', fontname='Calibri')

    # dodanie oryginalnych wartości pod prostokątami
    ax.text(start_scaled, -0.5, str(start), ha='center', va='center', fontsize=12, color='black', fontname='Calibri')
    ax.text(end_scaled, -0.5, str(end), ha='center', va='center', fontsize=12, color='black', fontname='Calibri')

# usuwanie osi
ax.axis('off')

# ustawienie zakresu
ax.set_xlim(-1, max_visual_length + 1)
ax.set_ylim(-1, large_rect_height + 1)

# poprawienie proporcji
ax.set_aspect(1)

# zmniejszenie białych marginesów
plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)

# wyświetlenie wykresu
plt.show()

# zapisanie skryptu dla Chimery
with open("color_chimera.cmd", "w") as file:
    file.write("\n".join(chimera_script))

print("\nPlik 'color_chimera.cmd' został utworzony. Możesz go uruchomić w Chimerze, wpisując:")
print("    open color_chimera.cmd")
