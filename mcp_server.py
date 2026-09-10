import sys
import json
from client import BM25Engine

def main():
    bm = BM25Engine()
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "fit":
            bm.fit(params.get("docs", []))
            res = {"status": "indexed", "num_docs": len(bm.corpus)}
        elif method == "score":
            res = {"ranked": bm.score(params.get("query", ""))}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
