# http://rosalind.info/problems/revc/

from utils import get_data
import re

def main():
    result = ""
    with get_data('rosalind_revc.txt') as f:
        for row in f:
            result += re.sub('.', lambda m: {'A':'T', 'T':'A', 'C': 'G', 'G': 'C'}.get(m.group(), m.group()), row.strip())

    print(result[::-1])


if __name__ == "__main__":
    main()
