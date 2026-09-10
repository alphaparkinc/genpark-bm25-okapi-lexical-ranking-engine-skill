import math
import collections

class BM25Engine:
    """
    Okapi BM25 Lexical Ranking Engine for relevance scoring.
    """
    def __init__(self, k1=1.5, b=0.75):
        self.k1 = k1
        self.b = b
        self.corpus = []
        self.doc_lens = []
        self.avgdl = 0.0
        self.df = collections.defaultdict(int)

    def fit(self, docs):
        self.corpus = [d.lower().split() for d in docs]
        self.doc_lens = [len(d) for d in self.corpus]
        self.avgdl = sum(self.doc_lens) / len(self.doc_lens) if self.doc_lens else 0.0
        n = len(self.corpus)
        for doc in self.corpus:
            for term in set(doc):
                self.df[term] += 1

    def score(self, query):
        q_terms = query.lower().split()
        scores = []
        n = len(self.corpus)
        for idx, doc in enumerate(self.corpus):
            doc_len = self.doc_lens[idx]
            s = 0.0
            tf_counts = collections.Counter(doc)
            for q in q_terms:
                if q in tf_counts:
                    tf = tf_counts[q]
                    idf = math.log(1.0 + (n - self.df[q] + 0.5) / (self.df[q] + 0.5))
                    num = tf * (self.k1 + 1.0)
                    denom = tf + self.k1 * (1.0 - self.b + self.b * (doc_len / self.avgdl))
                    s += idf * (num / denom)
            scores.append((idx, s))
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores
