import itertools
import time

def parse_input_set(s):
    # Accept input like: 1,2, -3 , 4
    if not s.strip():
        return []
    parts = s.split(',')
    nums = []
    for p in parts:
        p = p.strip()
        if p == '':
            continue
        try:
            nums.append(int(p))
        except ValueError:
            raise ValueError(f"Invalid value: '{p}' is not an integer.")
    return nums

def find_all_subsets_equal_target(S, target):
    solutions = []
    n = len(S)
    # Try all subset sizes from 0 to n
    for r in range(n + 1):
        for comb in itertools.combinations(S, r):
            if sum(comb) == target:
                solutions.append(comb)
    return solutions

def main():
    try:
        s = input("Enter the set of integers (comma-separated): ").strip()
        S = parse_input_set(s)
    except ValueError as e:
        print("Input Error:", e)
        return

    try:
        target_input = input("Enter the target sum: ").strip()
        target = int(target_input)
    except ValueError:
        print("Target must be an integer.")
        return

    print(f"Set = {S}")
    print(f"Target = {target}")
    print("Running brute-force search...")

    start = time.time()
    solutions = find_all_subsets_equal_target(S, target)
    end = time.time()

    elapsed = end - start
    print(f"Finished in {elapsed:.6f} seconds.")

    if solutions:
        print(f"Found {len(solutions)} solution(s):")
        for sol in solutions:
            print(sol, " sum =", sum(sol))
    else:
        print("No subset found.")

    # Save results to a file
    with open("results.txt", "w", encoding="utf-8") as f:
        f.write(f"Set = {S}\n")
        f.write(f"Target = {target}\n")
        f.write(f"Elapsed = {elapsed:.6f} seconds\n")
        if solutions:
            f.write(f"Found {len(solutions)} solution(s):\n")
            for sol in solutions:
                f.write(f"{sol}  sum = {sum(sol)}\n")
        else:
            f.write("No subset found.\n")

    print("Results saved to results.txt")

if __name__ == "__main__":
    main()
