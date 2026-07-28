from pathlib import Path
from governance.indexer.repo_indexer import RepoIndexer

def test_list_documents_smoke():
    repo_root = Path(__file__).parent.parent.parent.parent
    indexer = RepoIndexer(str(repo_root), ["docs/**/*.md"])
    docs = indexer.list_documents()
    assert len(docs) > 0
    assert all(d.endswith(".md") for d in docs)
