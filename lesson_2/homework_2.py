for i in [0, 1, 7, 8, 127, 128, 255]:
    bits = f"{i:08b}"
    signed = i if i < 128 else i - 256
    print(f"{bits:<10}{i:<15}{signed:<20}")