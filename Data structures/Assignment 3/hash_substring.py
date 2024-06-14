# python3

def read_input():
    """
    Reads two lines of input from the user: the pattern and the text.
    
    Returns:
        tuple: A tuple containing the pattern and the text.
    """
    return input().rstrip(), input().rstrip()

def print_occurrences(output):
    """
    Prints the list of occurrences in a space-separated format.
    
    Args:
        output (list): A list of integers representing the start indices of each occurrence of the pattern in the text.
    """
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    """
    Finds all occurrences of the pattern in the text using the Rabin-Karp algorithm.
    
    Args:
        pattern (str): The pattern to search for.
        text (str): The text to search within.
    
    Returns:
        list: A list of start indices where the pattern occurs in the text.
    """
    if not pattern or not text:
        return []  # No pattern or text to search within
    
    p_len = len(pattern)
    t_len = len(text)
    base = 256
    prime = 101
    pattern_hash = 0
    current_hash = 0
    h = 1
    occurrences = []

    # The value of h would be "pow(base, p_len-1) % prime"
    for _ in range(p_len - 1):
        h = (h * base) % prime

    # Calculate the hash value of the pattern and first window of text
    for i in range(p_len):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        current_hash = (base * current_hash + ord(text[i])) % prime

    # Slide the pattern over text one by one
    for i in range(t_len - p_len + 1):
        # Check the hash values of the current window of text and pattern
        if pattern_hash == current_hash:
            # Check for characters one by one
            if text[i:i + p_len] == pattern:
                occurrences.append(i)
        
        # Calculate hash value for next window of text: Remove leading digit,
        # add trailing digit
        if i < t_len - p_len:
            current_hash = (base * (current_hash - ord(text[i]) * h) + ord(text[i + p_len])) % prime

            # We might get negative values of current_hash, converting it to positive
            if current_hash < 0:
                current_hash += prime

    return occurrences

if __name__ == '__main__':
    pattern, text = read_input()
    occurrences = get_occurrences(pattern, text)
    print_occurrences(occurrences)
