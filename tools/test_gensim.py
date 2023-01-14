import gensim.downloader


def main():
    vectors = gensim.downloader.load("glove-wiki-gigaword-300")

    while True:
        word1 = input("Word 1:")
        word2 = input("Word 2:")
        print(vectors.similarity(word1, word2))


if __name__ == "__main__":
    main()