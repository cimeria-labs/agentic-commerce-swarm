"""
Persistent memory layer for Agentic Commerce Swarm.

This module keeps the public portfolio version simple and safe. It uses
ChromaDB when available and falls back gracefully if local persistence is not
configured.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass
class MemoryRecord:
    task: str
    strategy: str
    final_copy: str
    qa_report: str
    quality_score: int


class SwarmMemory:
    def __init__(self, persist_dir: str | None = None) -> None:
        self.persist_dir = Path(persist_dir or os.getenv("ACS_MEMORY_DIR", "data/chroma"))
        self._client = None
        self._collection = None
        self._enabled = False
        self._init_chroma()

    def _init_chroma(self) -> None:
        try:
            import chromadb

            self.persist_dir.mkdir(parents=True, exist_ok=True)
            self._client = chromadb.PersistentClient(path=str(self.persist_dir))
            self._collection = self._client.get_or_create_collection("agentic_commerce_runs")
            self._enabled = True
        except Exception:
            # Memory should never prevent the demo/workbench from running.
            self._enabled = False

    def save_run(
        self,
        task: str,
        strategy: str,
        final_copy: str,
        qa_report: str,
        quality_score: int,
    ) -> None:
        if not self._enabled or self._collection is None:
            return

        doc = f"""
Task:
{task}

Strategy:
{strategy}

Final copy:
{final_copy}

QA report:
{qa_report}

Quality score: {quality_score}/10
"""
        doc_id = f"run-{abs(hash(doc))}"
        self._collection.upsert(
            ids=[doc_id],
            documents=[doc],
            metadatas=[{"quality_score": quality_score}],
        )

    def search(self, query: str, n: int = 3) -> List[str]:
        if not self._enabled or self._collection is None:
            return []
        try:
            result = self._collection.query(query_texts=[query], n_results=n)
            return result.get("documents", [[]])[0]
        except Exception:
            return []
