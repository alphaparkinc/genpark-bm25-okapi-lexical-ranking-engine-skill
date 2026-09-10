from client import BM25Engine

def main():
    print("=== Testing Okapi BM25 Ranking Engine ===")
    bm = BM25Engine()
    docs = [
        "the quick brown fox",
        "jumped over the lazy dog",
        "quick brown dogs are fast"
    ]
    bm.fit(docs)
    ranked = bm.score("quick fox")
    print("Ranked results:", ranked)
    assert ranked[0][0] == 0
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
