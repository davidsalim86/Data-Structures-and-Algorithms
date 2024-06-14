# python3

import sys

class Solver:
    def __init__(self, s, t):
        self.s = s
        self.t = t
        self.p = 31  # A prime number used for the hash base
        self.m = 10**9 + 7  # A large prime number used as modulus
        self.n = len(s)
        self.m_t = len(t)
        self.s_prefix_hashes = self.compute_prefix_hashes(s)
        self.t_prefix_hashes = self.compute_prefix_hashes(t)
        self.s_powers = self.compute_powers(self.n)
        self.t_powers = self.compute_powers(self.m_t)

    def compute_prefix_hashes(self, string):
        """Computes hash of every prefix of the string."""
        n = len(string)
        hash_values = [0] * (n + 1)
        for i in range(n):
            hash_values[i + 1] = (hash_values[i] * self.p + ord(string[i]) - ord('a') + 1) % self.m
        return hash_values

    def compute_powers(self, length):
        """Computes powers of p up to the given length."""
        powers = [1] * (length + 1)
        for i in range(1, length + 1):
            powers[i] = (powers[i - 1] * self.p) % self.m
        return powers

    def get_hash(self, prefix_hashes, powers, start, length):
        """Computes hash for the substring of given length starting at start."""
        end = start + length
        hash_value = (prefix_hashes[end] - prefix_hashes[start] * powers[length] % self.m + self.m) % self.m
        return hash_value

    def has_common_substring_of_length(self, length):
        """Checks if there's a common substring of the given length."""
        if length == 0:
            return True, 0, 0
        
        hash_dict = {}
        for i in range(self.n - length + 1):
            hash_s = self.get_hash(self.s_prefix_hashes, self.s_powers, i, length)
            if hash_s not in hash_dict:
                hash_dict[hash_s] = []
            hash_dict[hash_s].append(i)
        
        for j in range(self.m_t - length + 1):
            hash_t = self.get_hash(self.t_prefix_hashes, self.t_powers, j, length)
            if hash_t in hash_dict:
                # Verify the actual substrings to avoid hash collisions
                for i in hash_dict[hash_t]:
                    if self.s[i:i + length] == self.t[j:j + length]:
                        return True, i, j
        
        return False, -1, -1

    def find_longest_common_substring(self):
        left = 0
        right = min(self.n, self.m_t)
        best_length = 0
        best_i = 0
        best_j = 0
        
        while left <= right:
            mid = (left + right) // 2
            found, i, j = self.has_common_substring_of_length(mid)
            if found:
                best_length = mid
                best_i = i
                best_j = j
                left = mid + 1
            else:
                right = mid - 1
        
        return best_i, best_j, best_length

def main():
    input = sys.stdin.read().strip().split()
    results = []
    for line in range(0, len(input), 2):
        s = input[line]
        t = input[line + 1]
        solver = Solver(s, t)
        i, j, length = solver.find_longest_common_substring()
        results.append(f"{i} {j} {length}")
    
    print("\n".join(results))

if __name__ == '__main__':
    main()
