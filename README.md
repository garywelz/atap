# Axiomatic Theories, Algorithms and Proofs (ATAP)

Mathematics already distinguishes algorithms, axiomatic theories, and proofs. ATAP does not invent a fourth kind of object. It changes where you stand: the same arguments are recovered as labeled directed graphs, so family resemblance — a shared algorithm-capsule waist, a diagonal contradiction, a well-founded descent — can be seen and counted instead of only narrated.

ATAP is one of two engines in the Copernicus science suite (the other is [GLMP](https://github.com/garywelz/glmp)). This repository holds the engine's open questions and the manuscript tree. The browsable chart corpus was not moved here; it remains in the Copernicus Hugging Face Space folder and on Google Cloud Storage.

*Gary Welz · CUNY Graduate Center / New Media Lab · [gwelz@gc.cuny.edu](mailto:gwelz@gc.cuny.edu)*

---

## Browse the corpus

The public table — algorithms, axiomatic theories, and proof graphs, with live viewers — is the place to start:

**[mathematics-database-table.html](https://storage.googleapis.com/regal-scholar-453620-r7-podcast-storage/mathematics-processes-database/mathematics-database-table.html)**

The Hugging Face Space for this engine is **[huggingface.co/spaces/garywelz/atap](https://huggingface.co/spaces/garywelz/atap)**.

---

## What lives in this repo

| | |
|---|---|
| **Open questions** | [`docs/research_focus.json`](docs/research_focus.json) — the engine's current questions and frontier, including the limit that the central empirical claim still rests on a small encoded set |
| **Papers** | [`collaborations/mathematics-database/`](collaborations/mathematics-database/) — current manuscript `proof-graphs.md`, submission packets, and LaTeX rebuild |

The chart files and process metadata that the table renders are **not** sourced from this repository. Their source of truth remains the `mathematics-processes-database` folder in the [copernicus-web](https://github.com/garywelz/copernicus-web) Hugging Face Space tree, published on GCS at the browse URL above.

---

## The open step

The graphs make family resemblance visible. What they do not yet settle is whether that resemblance is a feature of the mathematics or an artifact of a small encoding. The current manuscript's central empirical claim still rests on a few proofs; a family that small can be a selection effect. The work that would change the frame is more encodings done without looking for capsules — or an independent encoder reading the same arguments.

The live questions and marked limits are in [`docs/research_focus.json`](docs/research_focus.json). Interim notes are welcome; there is no deadline that would make a thin encoding better than a careful one.

---

## Using ATAP inside your own Claude

If you use Claude, you can give it live access to ATAP's current state — the project overview and its open research questions — so it can help you explore the corpus, understand the graphs, and shape your suggestions. It reads directly from this repository, so it's always current.

**Set it up once:**

1. In Claude, create a new Project (name it "ATAP" or similar).
2. Open the project's **instructions** and paste the block below.
3. That's it — every conversation in that project now reads ATAP's current context live from GitHub.

```
This project works with Axiomatic Theories, Algorithms and Proofs (ATAP).
At the start of substantive work, fetch these from GitHub and treat them
as the current source of truth:
- https://raw.githubusercontent.com/garywelz/atap/main/README.md
- https://raw.githubusercontent.com/garywelz/atap/main/docs/research_focus.json

ATAP is Gary Welz's research project (CUNY Graduate Center / New Media Lab).
This is your window into the project: explore the proof graphs, the
Mathematics Database corpus, and the open research questions, and use
what you find to shape suggestions and analysis. The project's canonical
files live in GitHub and are maintained by the project lead — so treat
this as a rich read-only context to think with, not a workspace to edit.
```

Nothing to upload, nothing to keep in sync — when the project updates, your Claude sees it the next time you start a conversation.

---

## The idea, in brief

Conventional publication writes proofs as prose. Prose conceals dependency: where a construction sits inside an inference, where two distant arguments share a waist, where a proof is doing algorithmic work. ATAP treats that hidden structure as the object of study. The working vocabulary is an eight-role proof graph (source, assumption, construction, assertion, inference, algorithm capsule, contradiction, conclusion), applied so far to a public Mathematics Database corpus.

What is *not* settled is as important as what is visible. A family of a few encoded proofs can be a selection effect; the node vocabulary may still be missing roles; Mermaid may be the most-used method rather than the right one. Those limits are stated in [`docs/research_focus.json`](docs/research_focus.json) in the same voice as the findings. A clearly marked limit is part of the work.

The bridge a specialist on either side is likely to miss is methodological, not metaphorical: the same Programming Framework that recovers justificatory structure here is the method [GLMP](https://github.com/garywelz/glmp) uses on gene-regulatory logic. Shared method, disjoint subject matter. Whether pointing that structure at an under-mathematized domain produces discovery or only re-description remains an open question.

---

## Citation

If you build on this work, cite the current manuscript in this repository:

> Welz, G. (2026). *Proof Graphs and Three Families of Self-Referential and Descent Proofs: A Graph-Theoretic Representation of Mathematical Justification Structure.* Working manuscript. [github.com/garywelz/atap](https://github.com/garywelz/atap/blob/main/collaborations/mathematics-database/proof-graphs.md)

A prior deposit is on Zenodo ([10.5281/zenodo.21015812](https://doi.org/10.5281/zenodo.21015812)); it predates the August 2026 retitle and three-family revision.

## License

[CC0 1.0 Universal](LICENSE) — the contents of this repository are dedicated to the public domain to the extent allowed by law.
