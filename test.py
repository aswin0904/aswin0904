def parse_map_data(verilog_text):
    """Parse Verilog-style map_data lines into a list of 4-bit strings."""
    lines = verilog_text.strip().splitlines()
    data = []
    for line in lines:
        if "4'b" in line:
            bits = line.split("4'b")[1].split(";")[0].strip()
            data.append(bits)
    print(f"✅ Parsed {len(data)} entries.")
    return data


def visualize_maze(map_bits):
    """Render maze cleanly using box-drawing characters."""
    n = int(len(map_bits) ** 0.5)
    print(f"\nMaze size: {n} x {n}\n")

    # Top border
    print("┌" + "──┬" * (n - 1) + "──┐")

    for i in range(n):
        # Walls and spaces
        row_top = "│"
        row_bottom = "├" if i < n - 1 else "└"

        for j in range(n):
            cell = map_bits[i * n + j]

            # bit positions: 0=top, 1=right, 2=bottom, 3=left
            top, right, bottom, left = cell[0], cell[1], cell[2], cell[3]

            # inside cell
            row_top += "  "

            # right wall
            row_top += "│" if right == "1" else " "

            # bottom walls
            if i < n - 1:
                row_bottom += "──" if bottom == "1" else "  "
                if j < n - 1:
                    # vertical join logic
                    row_bottom += "┼"
                else:
                    row_bottom += "┤"
            else:
                row_bottom += "──" if bottom == "1" else "  "
                if j < n - 1:
                    row_bottom += "┴"
                else:
                    row_bottom += "┘"

        print(row_top)
        if i < n - 1:
            print(row_bottom)
    print()


if __name__ == "__main__":
    print("Paste your Verilog map_data block below (end with ENTER + CTRL+D / CTRL+Z):\n")
    try:
        verilog_text = ""
        while True:
            line = input()
            verilog_text += line + "\n"
    except EOFError:
        pass

    map_bits = parse_map_data(verilog_text)
    visualize_maze(map_bits)
