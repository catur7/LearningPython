import math
import os
from pick import pick

def clear():
    os.system('cls' if os.name == 'nt' else 'clear') #ni buat clear screen di windows dan linux/mac

def num(prompt):
    while True:
        try:
            v = float(input(prompt))
            if v < 0:
                print("  -> Tidak boleh negatif.")
                continue
            return v
        except ValueError:
            print("  -> Input tidak valid.")

# name: (list input, fungsi rumus, label hasil)
SHAPES = {
    "Rectangle":               (["width", "height"], lambda w, h: w * h, "Area"),
    "Triangle":                (["base", "height"], lambda b, h: b * h / 2, "Area"),
    "Circle":                  (["radius"], lambda r: math.pi * r ** 2, "Area"),
    "Parallelogram":           (["base", "height"], lambda b, h: b * h, "Area"),
    "Trapezoid":                (["side a", "side b", "height"], lambda a, b, h: 0.5 * (a + b) * h, "Area"),
    "Rhombus":                  (["diagonal 1", "diagonal 2"], lambda d1, d2: 0.5 * d1 * d2, "Area"),
    "Cube Volume":              (["side"], lambda s: s ** 3, "Volume"),
    "Cube Surface Area":        (["side"], lambda s: 6 * s ** 2, "Surface Area"),
    "Cuboid Volume":            (["length", "width", "height"], lambda p, l, t: p * l * t, "Volume"),
    "Cuboid Surface Area":      (["length", "width", "height"], lambda p, l, t: 2 * (p*l + p*t + l*t), "Surface Area"),
    "Cylinder Volume":          (["radius", "height"], lambda r, t: math.pi * r ** 2 * t, "Volume"),
    "Cylinder Surface Area":    (["radius", "height"], lambda r, t: 2 * math.pi * r * (r + t), "Surface Area"),
    "Sphere Volume":            (["radius"], lambda r: 4/3 * math.pi * r ** 3, "Volume"),
    "Sphere Surface Area":      (["radius"], lambda r: 4 * math.pi * r ** 2, "Surface Area"),
    "Cone Volume":              (["radius", "height"], lambda r, t: 1/3 * math.pi * r ** 2 * t, "Volume"),
    "Cone Surface Area":        (["radius", "slant height"], lambda r, l: math.pi * r * (r + l), "Surface Area"),
}

def main():
    menu = list(SHAPES.keys()) + ["Exit"]
    while True:
        clear()
        choice, _ = pick(menu, "Select Shape:", indicator="=>", default_index=0)
        clear()
        if choice == "Exit":
            print("Thanksssss")
            break

        labels, formula, result_label = SHAPES[choice]
        values = [num(f"insert {label}: ") for label in labels]
        result = formula(*values)

        print(f"\n{result_label}: {result:.2f}")
        input("\nPress ENTER to back")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:   #ctrl+c
        print("\nDibatalkan.")