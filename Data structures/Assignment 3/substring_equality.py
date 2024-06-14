# python3

import sys

class Solver:
    def __init__(self, s):
        self.s = s
        self.p = 31  # A prime number used for the hash base
        self.m = 10**9 + 7  # A large prime number used as modulus
        self.n = len(s)
        self.prefix_hashes = self.compute_prefix_hashes()
        self.powers = self.compute_powers()

    def compute_prefix_hashes(self):
        """Computes hash of every prefix of the string s."""
        hash_values = [0] * (self.n + 1)
        for i in range(self.n):
            hash_values[i + 1] = (hash_values[i] * self.p + ord(self.s[i]) - ord('a') + 1) % self.m
        return hash_values

    def compute_powers(self):
        """Computes powers of p up to the length of the string."""
        powers = [1] * (self.n + 1)
        for i in range(1, self.n + 1):
            powers[i] = (powers[i - 1] * self.p) % self.m
        return powers

    def ask(self, a, b, l):
        """Checks if the substrings s[a:a+l] and s[b:b+l] are equal."""
        hash_a = (self.prefix_hashes[a + l] - self.prefix_hashes[a] * self.powers[l] % self.m + self.m) % self.m
        hash_b = (self.prefix_hashes[b + l] - self.prefix_hashes[b] * self.powers[l] % self.m + self.m) % self.m
        return hash_a == hash_b

def main():
    input = sys.stdin.read().split()
    s = input[0]
    q = int(input[1])
    queries = input[2:]
    
    solver = Solver(s)
    results = []
    
    for i in range(q):
        a = int(queries[3 * i])
        b = int(queries[3 * i + 1])
        l = int(queries[3 * i + 2])
        results.append("Yes" if solver.ask(a, b, l) else "No")
    
    print("\n".join(results))

if __name__ == '__main__':
    main()
