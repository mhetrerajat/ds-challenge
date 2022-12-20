# http://rosalind.info/problems/rna/

from utils import get_data

def main():
    result = ""
    with get_data('rosalind_rna.txt') as f:
        for row in f:
            result += row.strip().replace('T', 'U')

   
    print(result)


if __name__ == "__main__":
    main()

