# tree.py
import sys, random, math

def draw_tree(H=12):
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    RED = "\033[31m"
    CYAN = "\033[36m"
    MAG = "\033[35m"
    RESET = "\033[0m"

    width = 2*H - 1
    mid = width // 2

    # Star
    print(' ' * mid + YELLOW + '*' + RESET)

    for i in range(H):
        leaves = 2*i + 1
        pad = mid - i
        line = ' ' * pad
        for j in range(leaves):
            p = random.random()
            if p < 0.09 and i > 1:
                t = random.random()
                if t < 0.33:
                    line += RED + 'o' + RESET
                elif t < 0.66:
                    line += CYAN + '@' + RESET
                else:
                    line += MAG + 'O' + RESET
            else:
                line += GREEN + '^' + RESET
        print(line)

    trunk_h = max(1, H // 4)
    trunk_w = H // 3
    if trunk_w % 2 == 0: trunk_w += 1
    pad = mid - trunk_w // 2
    for _ in range(trunk_h):
        print(' ' * pad + YELLOW + '|' * trunk_w + RESET)

if __name__ == "__main__":
    H = 12
    if len(sys.argv) > 1:
        try: H = max(4, int(sys.argv[1]))
        except: pass
    draw_tree(H)