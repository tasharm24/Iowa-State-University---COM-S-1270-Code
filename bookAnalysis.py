f = open('alice.txt', 'r')
count = {}


def analyzeBook(word):
    count = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
    # remove punctuation
            line = line.translate(str.maketrans('', '', string.punctuation)).lower
            words = line.split()
            for word in words:
                count[word] = count.get(word, 0) + 1
    return count
            
def outputAnalysis(count, f):
    keys = sorted(count.keys())
    title = filename.rsplit('.', 1)[0]
    output_filename = f"{title}_analysis.txt"
    with open(output_filename, 'w', encoding='utf-8') as out:
        for word in keys:
            out.write(f"{word} {count[word]} \n")
    print(f"Analysis saved to {output_filename}")

def main():
    filename = input("Enter the .txt filename: ").strip()
    count = analyzeBook(filename)
    outputAnalysis(count, filename)

if __name__ == "__main__":
    main()