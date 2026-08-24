# Proof Graphs and Three Families of Self-Referential and Descent Proofs: A Graph-Theoretic Representation of Mathematical Justification Structure

**Gary Welz**
Researcher, New Media Lab, CUNY Graduate Center
Email: gwelz@gc.cuny.edu
ORCID: https://orcid.org/0009-0005-7806-0892

**Status:** Declined at desk review, *Journal of Logic and Computation*, June 2026 (genre fit) | Revising for *PLOS ONE* | Three-family taxonomy applied, August 2026 | Preprint: Zenodo DOI [10.5281/zenodo.21015812](https://doi.org/10.5281/zenodo.21015812) (v2.0, 29 June 2026; concept DOI [10.5281/zenodo.20510602](https://doi.org/10.5281/zenodo.20510602); v1 under prior title: [10.5281/zenodo.20510603](https://doi.org/10.5281/zenodo.20510603)) — **note: this is the latest deposited version; it predates the August 2026 retitle and three-family revision and is now stale. A new version should be deposited before submission.**
**Repository:** garywelz/atap
**Path:** collaborations/mathematics-database/proof-graphs.md

---

## Abstract

Mathematics encompasses three fundamentally distinct object types — algorithms, axiomatic systems, and proofs. These are conventionally treated as categorically separate in mathematical practice, education, and knowledge representation. We demonstrate that all three can be expressed as labeled directed graphs using Mermaid Markdown. This unified representation reveals structural properties that conventional prose and static diagrams obscure.

The central empirical finding is the regularity of **algorithm capsules** — embedded procedural substructures within proofs — across mathematically distant domains. Analysis of the Mathematics Database corpus identifies **three families** that share a capsule waist but differ in downstream resolution: **diagonal contradiction** (Cantor, Gödel, Turing, Rice), **fixed-point self-reference** (Kleene, Lawvere), and **well-founded descent** (Goodstein termination, Dickson, Higman). In each case the algorithm capsule is not incidental to the argument but is its structural core. These family resemblances are visible and measurable in the graph representation. They are not accessible from prose alone.

The representation is implemented as three graph types. Algorithmic flowcharts capture procedural structure. Axiomatic dependency graphs represent logical dependency among axioms, definitions, and theorems. Proof graphs — a hybrid form introduced here — encode justification structure using a domain-specific eight-role node vocabulary: source, assumption, construction, assertion, inference, algorithm capsule, contradiction, and conclusion. Together the three graph types constitute the Mathematics Database, a publicly accessible machine-readable corpus spanning classical geometry, number theory, algebra, set theory, mathematical logic, and theoretical computer science.

The methodology is a domain-specific application and extension of the Programming Framework, a general method for LLM-assisted process visualization. The mathematics case demonstrates that the framework's core claim extends from procedural processes to logical and justificatory structures: that formal structure is recoverable from natural language descriptions of complex systems, and is meaningful, measurable, and comparable once recovered.

**Keywords:** mathematical knowledge representation, proof graphs, axiomatic systems, LLM-generated diagrams, Mermaid, process visualization, graph-theoretic representation, Programming Framework

---

## 1. Introduction

### 1.1 The Representation Problem in Mathematical Proofs

Mathematical proofs are structured arguments in which assumptions, constructions, inferences, and conclusions carry distinct logical roles. Yet proofs are almost always published and taught in prose — linear text that conceals the dependency structure of the argument, obscures where procedural constructions sit within inferential steps, and offers no common format for comparing proofs across domains or methods.

This representational gap has consequences. A logician reading Gödel's incompleteness proof and a set theorist reading Cantor's diagonal argument may each recognize that a diagonal construction lies at the core of the argument, but comparing the structural role of those constructions — or measuring how each proof allocates complexity between procedure and inference — requires placing both arguments in a common representational space. That space does not exist in standard mathematical practice. Knowledge representation systems typically address axiomatic dependency charts or formal verification certificates, not the internal architecture of informal proof arguments as inspectable, comparable structures.

Algorithms and axiomatic systems — the other object types mathematicians work with routinely — suffer parallel representational fragmentation: procedures appear as pseudocode or flowcharts, theories as numbered axiom lists. This paper concentrates on proofs. The question is whether proof structure can be made explicit, measurable, and comparable — and whether doing so reveals regularities invisible in prose.

### 1.2 The Proposed Approach

This paper concentrates on **proof graphs** — labeled directed graphs that encode the justification structure of mathematical arguments — though the same pipeline also produces algorithmic flowcharts and axiomatic dependency graphs for comparative context (§3.1–§3.2, §6.2). The central empirical thread is a corpus study of fourteen proof graphs, with particular attention to nine arguments that fall into three structurally distinct families: diagonal contradiction (Cantor, Gödel, Turing, Rice), fixed-point self-reference (Kleene, Lawvere), and well-founded descent (Goodstein termination, Dickson, Higman). Represented as proof graphs, these proofs — usually treated as belonging to set theory, mathematical logic, computability, combinatorics, and category theory respectively — share a common structural signature at the capsule waist and diverge in how downstream tension is resolved. The three-family taxonomy is developed with exact corpus figures in §6.

Proof graphs expose the roles played by different proof steps, the presence of algorithm capsules, and the structural differences between proofs of the same theorem by different methods. Algorithmic flowcharts and axiomatic dependency graphs, generated by the same methodology, provide the comparative baseline against which proof-graph complexity can be measured.

A skeptical reader might ask whether the graph representation merely redescribes what a careful reader of the prose already knows, rather than revealing anything genuinely new. The answer is that making structure explicit is itself a form of discovery — specifically when the structure was previously inaccessible to measurement and comparison. Comparing the construction in Euclid's infinitude argument to the diagonal constructions in Cantor, Gödel, and Turing, or to the descent constructions in Goodstein and Dickson, requires a common representational space. The graph provides that space. It is what makes the three-family observation a finding rather than a redescription. The situation is analogous to phylogenetic trees in biology: evolutionary relationships were always present, but the tree representation made them comparable, measurable, and falsifiable in a way that prose natural history did not.

The mechanism for generating these graphs is the Programming Framework: a methodology for transforming natural language descriptions of processes into structured Mermaid Markdown diagrams using large language models (LLMs), with human-in-the-loop validation and versioned JSON storage [1].

### 1.3 Contributions

This paper contributes:

**Conceptual:** A proof-graph formalism with an eight-role node vocabulary (source, assumption, construction, assertion, inference, algorithm capsule, contradiction, conclusion) and the algorithm capsule as a representational device for embedded procedural substructures within proofs.

**Empirical:** A corpus study of fourteen proof graphs, with the identification of three families — diagonal contradiction, fixed-point self-reference, and well-founded descent — whose shared capsule waist and distinct downstream resolutions are visible and measurable in the graph representation but not recoverable from prose alone. The Mathematics Database provides the open, machine-readable infrastructure for this corpus.

**Methodological:** A human-in-the-loop pipeline for generating proof graphs from natural language descriptions using LLMs, as a domain-specific extension of the Programming Framework [1].

**Theoretical:** The claim that proof graphs regularly contain algorithm capsules, making explicit a structural relationship between proof and computation that is implicit in mathematical practice but rarely formalized at the diagram level — and that this relationship takes three measurable forms across mathematically distant domains: contradiction-forming diagonalization, fixed-point self-reference, and well-founded descent.

---

## 2. Related Work

### 2.1 Graph-Based Proof Representation

Graph-theoretic representations of proofs have been explored in proof complexity theory [9], where proof graphs (also called proof DAGs) are used to measure the size and depth of proofs in formal systems. DAG stands for directed acyclic graph: edges flow in one direction, and no step can depend, even indirectly, on itself. DAG-like proofs have been studied as a generalization of tree-like proofs [9].

The proof graphs in this paper are DAGs at the proof level. Several corpus entries contain algorithm capsule nodes whose internal structure is cyclic — the diagonal enumeration in the Rationals Are Countable proof, for example, contains an explicit loop. The algorithm capsule node type makes this two-level structure visible: cycles are encapsulated within capsule nodes rather than appearing at the proof graph's top level.

The present work differs from proof complexity in that it is concerned with the semantic roles of nodes in proofs — what each step does (assumption, construction, inference, and so on) — rather than with formal complexity bounds. Argument mapping [10] is a closer conceptual relative: the proof graph vocabulary in §3.3 can be understood as a domain-specific formalization of argument mapping applied to mathematical justification.

Formal proof assistants — Lean [3], Coq [5], Isabelle [6] — represent mathematics for machine verification rather than structural inspection. Section 4.1 contrasts Lean-style proof flow with the informal proof graphs used here; the two approaches are complementary, not competing.

### 2.2 LLM Diagram Generation

Large language models have demonstrated capacity for mathematical reasoning [11, 12], and recent work has explored LLM-assisted formalization of mathematics [13]. The present work uses LLMs differently: not to reason about mathematics or verify proofs, but to generate structured diagrammatic representations from natural language descriptions, as one step in a human-in-the-loop pipeline. This paper makes no claims about LLM mathematical reasoning ability, only about LLM utility as a diagram generation tool under human supervision.

### 2.3 Programming Framework and Generation Pipeline

The Programming Framework [1] is a general methodology for transforming textual process descriptions into structured Mermaid Markdown diagrams [14] using LLMs, with human-in-the-loop validation and versioned JSON storage. The present paper extends it to proof graphs by introducing the eight-role node vocabulary and algorithm capsule concept described in §3.3.

All proof graphs in the corpus were generated using the following pipeline:

**Step 1 — Source selection.** A proof is selected and a natural language description is prepared from standard reference sources — typically textbook or encyclopaedia prose.

**Step 2 — LLM prompting.** The description is submitted to a large language model with a structured prompt specifying the proof-graph node vocabulary, color scheme, and Mermaid syntax requirements.

**Step 3 — Human review.** The generated diagram is rendered and reviewed for logical dependency accuracy, node coverage, role assignment, and Mermaid validity.

**Step 4 — Metadata construction.** A JSON metadata record is constructed per the schema in §5.1; structural metrics are counted from the rendered diagram.

**Step 5 — Versioned storage.** The completed entry is committed to the Google Cloud Storage repository and made publicly accessible via the interactive viewer in §5.4.

The human review step is the primary quality control mechanism. It does not constitute formal expert validation — that limitation is noted in §7 — but it ensures that each entry has been inspected for logical accuracy by an author with familiarity with the relevant mathematical content.

---

## 3. The Three Graph Types

### 3.1 Algorithmic Flowcharts

An algorithmic flowchart in the Mathematics Database is a standard directed graph where:

- **Nodes** represent computational steps, decisions, or states
- **Edges** represent sequential or conditional flow
- **Node colors** follow the Programming Framework's five-category system: Red (inputs), Yellow (data structures/algorithms), Green (operations), Blue (intermediate states/decisions), Violet (outputs/results)
- **AND gates** represent steps that require multiple prior conditions to be satisfied before proceeding
- **OR gates** (decision nodes) represent conditional branches where one of several paths is taken
- **Loops** (back-edges) represent iterative or recursive structure

**Structural metrics captured:** node count, edge count, conditional count, AND gate count, OR gate count, loop count, graph type.

**Examples in the database:**
- Sieve of Eratosthenes — high loop depth, iterative primality marking
- Merge Sort — recursive structure, divide-and-conquer branching
- Dijkstra's Algorithm — priority queue management, relaxation loop
- Euclidean Algorithm — minimal loop, elegant termination condition
- Binary Search — logarithmic branching structure

Figure 1 illustrates the Euclidean Algorithm as an algorithmic flowchart using this color vocabulary. The algorithm is a clean example of iterative structure: a single decision node, a back-edge forming the loop, and a minimal path to termination. The color legend appears with the diagram.

```mermaid
flowchart TD
    A["Input integers a and b"] --> B{"b equals 0?"}
    B -->|Yes| C["GCD equals a"]
    B -->|No| D["r equals a mod b"]
    D --> E["a equals b"]
    E --> F["b equals r"]
    F --> B
    C --> G["Return GCD"]
    classDef red fill:#ff6b6b,color:#1e1e1e,stroke:#c0392b
    classDef yellow fill:#ffd43b,color:#1e1e1e,stroke:#f59f00
    classDef green fill:#51cf66,color:#1e1e1e,stroke:#40c057
    classDef lightblue fill:#74c0fc,color:#1e1e1e,stroke:#4dabf7
    classDef violet fill:#b197fc,color:#1e1e1e,stroke:#9775fa
    classDef lavender fill:#e6e6fa,color:#1e1e1e,stroke:#b19cd9
    class A red
    class B lavender
    class C,G violet
    class D,E,F green
```

*Figure 1: Euclidean Algorithm — algorithmic flowchart. GLMP 6-color scheme (exact hex values from the Mathematics Database table): Red = input, Lavender = decision, Green = operation, Violet = output.*

Algorithmic flowcharts are the most direct application of the Programming Framework's base methodology and require no extension to the standard vocabulary.

### 3.2 Axiomatic Dependency Graphs

An axiomatic dependency graph represents the logical architecture of a mathematical system as a directed acyclic graph (DAG) — the same structure defined in §2.1, where edges flow in one direction and no theorem can depend, even indirectly, on itself. In the axiomatic context, acyclicity is not merely a formal property but a logical requirement: if theorem B depends on theorem A, then A cannot simultaneously depend on B, or the entire deductive structure would be circular and the system would prove nothing.

The nodes and edges of an axiomatic dependency graph are:

- **Nodes** represent mathematical objects: Axiom, Definition, Lemma, Theorem, Corollary, Postulate, Primitive (undefined term)
- **Edges** represent logical dependency: an edge from A to B means B depends on, uses, or requires A
- **Node colors** encode object type: a domain-specific extension of the Programming Framework's color system applied to logical roles rather than process stages
- **Depth from axioms** measures how many inference steps separate a theorem from first principles

**Structural metrics captured:** node count, edge count, depth distribution, axiom-to-theorem ratio, number of distinct proof paths to key results.

**Examples in the database:** Euclid's Elements, Peano Arithmetic, ZFC Set Theory, and standard algebraic theories — 194 entries in total, listed in the live database (§5.4). This paper does not survey them entry by entry; they supply comparative context in §6.2.

Figure 2 gives an illustrative dependency slice of Book I of Euclid's Elements — postulates, common notions, and early propositions — with coloring by object type. Node labels are abbreviated after Heath's translation.

```mermaid
flowchart LR
    P1["Post. I draw segment between two points"]
    P2["Post. II extend a finite line"]
    P3["Post. III draw circle center and radius"]
    CN1["CN I equals of the same are equal"]
    CN3["CN III subtract equals, equals remain"]
    CN4["CN IV coincide implies equal"]
    CN5["CN V whole greater than part"]
    Prop1["Prop. I.1 equilateral triangle on segment"]
    Prop2["Prop. I.2 transport a length"]
    Prop3["Prop. I.3 cut off lesser from greater"]
    Prop4["Prop. I.4 SAS triangle congruence"]
    Prop5["Prop. I.5 isosceles base angles"]
    P1 --> Prop1
    P3 --> Prop1
    Prop1 --> Prop2
    P1 --> Prop2
    P2 --> Prop2
    P3 --> Prop2
    Prop2 --> Prop3
    P3 --> Prop3
    CN4 --> Prop4
    CN5 --> Prop4
    Prop1 --> Prop5
    P1 --> Prop5
    P2 --> Prop5
    CN1 --> Prop5
    CN3 --> Prop5
    Prop4 --> Prop5
    classDef red fill:#ff6b6b,color:#1e1e1e,stroke:#c0392b
    classDef yellow fill:#ffd43b,color:#1e1e1e,stroke:#f59f00
    classDef green fill:#51cf66,color:#1e1e1e,stroke:#40c057
    class P1,P2,P3 red
    class CN1,CN3,CN4,CN5 yellow
    class Prop1,Prop2,Prop3,Prop4,Prop5 green
```

*Figure 2: Euclid's Elements Book I — axiomatic dependency graph (illustrative; abbreviated node labels after Heath). Database palette: Red = Postulates, Yellow = Common Notions, Green = Propositions.*

Axiomatic dependency graphs require a domain-specific node vocabulary not present in the base Programming Framework, making them a natural extension case. The acyclicity of these graphs is not imposed as a technical constraint but follows from the logical requirement that deductive systems be non-circular.

### 3.3 Proof Graphs

Proof graphs are the novel contribution of this paper. A proof graph represents the justification structure of a mathematical proof as a directed graph where:

- **Nodes** carry an eight-role vocabulary encoding the proof-theoretic function of each step
- **Edges** represent logical dependency: an edge from A to B means B follows from, depends on, or uses A
- **Node colors** encode proof role, not process stage — a domain-specific extension of the Programming Framework's color system

**Proof graphs and acyclicity.** At the proof level, proof graphs are DAGs: logical dependency flows in one direction from premises to conclusion, and no step can depend, even indirectly, on itself. However, proof graphs differ from axiomatic dependency graphs in one important structural respect: they may contain algorithm capsule nodes whose internal structure is cyclic. The diagonal enumeration in the Rationals Are Countable proof contains an explicit loop; the anti-diagonal constructions in the Reals Are Uncountable and Cantor Power Set proofs encapsulate iterative procedures. The algorithm capsule node type is the representational device that makes this two-level structure visible and precise: cycles are encapsulated within capsule nodes rather than appearing at the proof graph's top level. This distinction — between proof-level acyclicity and capsule-level iteration — is one of the structural properties the unified representation makes explicit that prose cannot.

**The eight-role proof graph vocabulary:**

| Role | GLMP color | Definition |
|------|------------|------------|
| Source | Red (`#ff6b6b`) | The theorem, proposition, or claim being proved |
| Assumption | Yellow (`#ffd43b`) | A temporary assumption (e.g., for contradiction or induction) |
| Construction | Yellow (`#ffd43b`) | An object explicitly constructed in the proof |
| Assertion | Green (`#51cf66`) | A claim that follows from prior steps |
| Inference | Light blue (`#74c0fc`) | A logical inference rule or proof step |
| Algorithm Capsule | Green (`#51cf66`) | An embedded algorithmic substructure within the proof |
| Contradiction | Red (`#ff6b6b`) | A contradiction reached (in proof by contradiction) |
| Conclusion | Violet (`#b197fc`) | The final conclusion establishing the theorem |

All figures in this paper use the **exact GLMP 6-color fills** from the Mathematics Database table viewer: red, yellow, green, light blue, violet, and lavender (decision diamonds). Node labels are rendered in dark text (`#1e1e1e`) for print/PDF readability on the pastel fills. Proof roles map onto this palette as shown above.

**A note on rendering.** The live proof-graph entry pages in the Mathematics Database render the same eight roles with a dedicated eight-hue legend — amber (source), violet (assumption), moss (construction), steel (assertion), copper (inference), indigo (algorithm capsule), crimson (contradiction), teal (conclusion) — assigning each role its own hue against the pages' dark theme. The figures in this paper instead map the eight roles onto the table viewer's six-color palette, for consistency with the database's other graph types and for legibility in print. In both renderings the role semantics are carried by the node labels; the role vocabulary, not the hue assignment, is normative.

**On the mutual exclusivity of roles.** The eight roles are intended to be mutually exclusive: each node in a proof graph carries exactly one role. In practice, some proof steps are ambiguous — a step may function simultaneously as a construction and an assertion, or as an inference and a conclusion. The decision rule applied in the Mathematics Database is to assign the role that best captures the step's primary proof-theoretic function. A step that constructs an object and asserts a property of it in the same move is classified as a Construction if the object's existence is what the proof requires, and as an Assertion if the property is what the proof requires. A step that draws a final inference is classified as a Conclusion rather than an Inference if it directly establishes the theorem being proved. These decisions are recorded in the entry metadata and are available for review. The goal is consistency within the corpus rather than a claim that the boundaries are always sharp.

**The algorithm capsule concept.** An algorithm capsule is a node representing an embedded procedural substructure within a proof — an explicit construction or procedure that is carried out within the proof argument and is distinct in character from the logical inference steps surrounding it. Algorithm capsules are the most structurally significant node type in the proof graph vocabulary for two reasons.

First, they mark the boundary between the algorithmic and the inferential within a single proof. In Euclid's proof of the infinitude of primes, the construction of N = p₁p₂...pₙ + 1 is an algorithm capsule: it is a finite procedure whose output — a number not divisible by any listed prime — is what the proof's contradiction depends on. The inferential steps before and after the capsule are logically dependent on the capsule's output but are not themselves algorithmic. Making this boundary explicit as a node type reveals a structural relationship between proof and computation that is normally invisible in prose.

Second, as noted above, algorithm capsules are the location within proof graphs where cyclic structure — iterative or recursive procedures — appears. The proof graph remains a DAG at its top level; the cycles are contained within capsule nodes. This encapsulation is not a limitation of the representation but a feature: it preserves the DAG structure of the proof's logical dependency while accurately representing the computational structure of its embedded procedures.

**Examples in the database:**

*Euclid Book I Pilot Proofs* (41 nodes, 48 edges, hybrid graph type) — the foundational geometric proofs; rich in construction nodes; one algorithm capsule in I.1 (compass-and-straightedge construction).

*Infinitely Many Primes* (14 nodes, 17 edges, contradiction structure) — Euclid's proof; compact graph with clear contradiction arc and a central algorithm capsule (construction of N = p₁p₂...pₙ + 1).

*Pythagorean Theorem Proof Comparison* (33 nodes, 39 edges, multiple proof families) — graph representation of multiple distinct proofs of the same theorem; structural differences between proof families become visually and metrically comparable.

*Fundamental Theorem of Arithmetic* (27 nodes, 34 edges) — the unique prime factorization theorem; graph reveals the two-part structure (existence and uniqueness) and their distinct dependency chains.

*Cantor Diagonal Proofs* (42 nodes, 50 edges, hybrid family) — Cantor's diagonal argument in multiple variants; algorithm capsule is the structural core of all variants; graph reveals the family resemblance across proof variants and the two-level DAG/cycle structure described above.

*Gödel Completeness Theorem* (15 nodes, 15 edges) — proof graph pilot; dependency structure of the completeness argument; one algorithm capsule.

*Gödel First Incompleteness Theorem* (15 nodes, 17 edges) — proof graph pilot; the diagonal lemma appears as an algorithm capsule at a structural waist, with reductio edges feeding a contradiction hub; one temporary assumption; paired with the Gödel Numbering algorithm flowchart as the corpus's first algorithm/proof pair for the same content.

*Goodstein termination* (8 nodes, 7 edges) — Family 3 chain topology; ordinal-descent capsule; object-level termination only.

*Turing halting problem* (7 nodes, 7 edges) — Family 1 hub-and-bypass; diagonal self-application capsule; one temporary assumption.

*Rice's theorem* (9 nodes, 9 edges) — Family 1 hub-and-bypass via reduction to halting; one temporary assumption.

*Kleene's recursion theorem* (7 nodes, 6 edges) — Family 2 chain; s-m-n fixed-point capsule; no contradiction hub.

*Dickson's Lemma* (7 nodes, 6 edges) — Family 3 chain; componentwise-minimal descent capsule.

*Higman's Lemma* (9 nodes, 9 edges) — Family 3 hybrid; minimal-bad-sequence capsule with hub-and-bypass reductio; one temporary assumption.

*Lawvere's fixed-point theorem* (8 nodes, 7 edges) — Family 2 chain; diagonal self-application capsule; categorical abstraction of Kleene.

The three graph types differ not only in their node vocabularies but in the characteristic shapes they produce — topological signatures that are the subject of §4.

---

## 4. Structural Properties of the Three Graph Types

The three graph types introduced in §3 are distinguished not only by their node vocabularies but by their topological signatures — the characteristic shapes that different mathematical structures produce when rendered as directed graphs. This section develops four such signatures: the contrast between informal proof graphs and formal proof assistant representations (§4.1), the role of loops and back-edges in proof and algorithm graphs (§4.2), the contrast between merge and chain topologies in proof graphs (§4.3), and the AND/OR conjunctive structure of proof premises (§4.4).

### 4.1 Informal Proof Graphs and Lean-Style Proof Structure

Proof assistants such as Lean 4 [3] and its mathlib library [4] encode proofs as terms in dependent type theory. The interactive experience is a sequence of goals refined by tactics (`intro`, `have`, `rw`, `exact`, `contradiction`, and others). Mathlib and related libraries supply lemmas as certified building blocks. None of that is what the proof graphs in this paper are trying to duplicate: our graphs are pedagogical and structural — eight semantic roles applied to natural language arguments — not machine-checked certificates.

Still, it is useful to place the two representations side by side on the same mathematical idea: Euclid's argument that no finite list of primes is exhaustive. The informal proof graph emphasizes roles (source, assumption, algorithm capsule, contradiction, and so on). A schematic Lean-shaped graph emphasizes proof obligations and lemma dependencies as one might sketch after reading a formal proof. The labels below are illustrative, not a literal port of a specific Mathlib proof term.

**Informal proof graph (role-oriented).**

```mermaid
flowchart TD
    A["Source: claim infinitely many primes"]
    B["Assumption: finite list p1 through pn"]
    C["Algorithm capsule: N equals product of all listed primes plus 1"]
    D["Assertion: N not divisible by any listed prime"]
    E["Inference: N is prime or has a new prime factor"]
    F["Contradiction: list was complete"]
    G["Conclusion: no finite list is exhaustive"]
    A --> B --> C --> D --> E --> F --> G
    classDef red fill:#ff6b6b,color:#1e1e1e,stroke:#c0392b
    classDef yellow fill:#ffd43b,color:#1e1e1e,stroke:#f59f00
    classDef green fill:#51cf66,color:#1e1e1e,stroke:#40c057
    classDef lightblue fill:#74c0fc,color:#1e1e1e,stroke:#4dabf7
    classDef violet fill:#b197fc,color:#1e1e1e,stroke:#9775fa
    class A red
    class B yellow
    class C green
    class D green
    class E lightblue
    class F red
    class G violet
```

**Lean-schematic proof tree (goal and lemma oriented).**

```mermaid
flowchart TD
    T["Theorem goal: primes are not contained in any finite set"]
    G1["intro: hypothetical finite set S of primes"]
    G2["define N as product of S plus one"]
    G3["invoke: every n greater than 1 has a prime factor"]
    G4["have: some prime p divides N"]
    G5["show: p cannot be in S"]
    G6["contradiction: S was assumed exhaustive"]
    T --> G1 --> G2 --> G3 --> G4 --> G5 --> G6
    classDef red fill:#ff6b6b,color:#1e1e1e,stroke:#c0392b
    classDef yellow fill:#ffd43b,color:#1e1e1e,stroke:#f59f00
    classDef green fill:#51cf66,color:#1e1e1e,stroke:#40c057
    classDef lightblue fill:#74c0fc,color:#1e1e1e,stroke:#4dabf7
    class T red
    class G1 yellow
    class G2 yellow
    class G3,G4 green
    class G5 lightblue
    class G6 red
```

**How the two differ:**

| Dimension | Informal proof graph (this paper) | Lean-style schematic |
|-----------|-------------------------------------|----------------------|
| **Node meaning** | Epistemic role (assumption, construction, …) | Goal state, definition, or lemma application |
| **Edges** | Justifies or explains for a human reader | Resolves subgoal or depends on lemma in library |
| **Correctness** | Human review; not machine-checked | Kernel-checkable when fully formalized |
| **Granularity** | Chosen for clarity; steps may be coarse | Often fine-grained, many small tactic steps |
| **Construction** | LLM from prose, reviewed by author | Tactics or proof terms |
| **Algorithm capsule** | Explicit node type for procedural content | Corresponds to computable definitions inside terms |

**Takeaway.** Lean proofs and informal proof graphs are complementary: Lean answers "is this formally correct?"; proof graphs answer "how is the argument organized for inspection, teaching, and cross-proof comparison?" A natural research direction — noted in §8 — is to map or align Lean proof terms or tactic traces to role-labeled graphs so the same theorem can be viewed in both registers. That pipeline does not exist in the current Mathematics Database corpus, which remains informal and LLM-derived.

### 4.2 Loops, Back-Edges, and Iterative Structure

Algorithmic flowcharts may contain genuine cycles — back-edges that represent iteration or recursion. Proof graphs, as argued in §3.3, are DAGs at the proof level but may contain cycles encapsulated within algorithm capsule nodes.

One proof structure that appears to require a cycle at the proof level is mathematical induction. In prose, induction "reapplies the same step" at ever-larger indices, which suggests a loop. In the graph representation, however, induction is better rendered as a back-edge from the inductive step node to the inductive hypothesis node — semantically the same "next instance of the pattern," but a DAG with one back-edge that displays reliably in Mermaid and preserves the directional dependency structure.

```mermaid
flowchart TD
  S["Source: theorem P n for all natural n"]
  B["Base case: prove P 0"]
  IH["Assumption: inductive hypothesis P n"]
  ST["Inference: prove P of n plus 1 from IH"]
  S --> B
  B --> IH
  IH --> ST
  ST --> IH
  ST --> C["Conclusion: by induction P holds for all n"]
  B --> C
  classDef red fill:#ff6b6b,color:#1e1e1e,stroke:#c0392b
  classDef yellow fill:#ffd43b,color:#1e1e1e,stroke:#f59f00
  classDef green fill:#51cf66,color:#1e1e1e,stroke:#40c057
  classDef lightblue fill:#74c0fc,color:#1e1e1e,stroke:#4dabf7
  classDef violet fill:#b197fc,color:#1e1e1e,stroke:#9775fa
  class S red
  class B green
  class IH yellow
  class ST lightblue
  class C violet
```

The back-edge from ST to IH encodes the inductive pattern without introducing a full cycle into the proof graph. This is a principled representational choice: the back-edge marks where the inductive pattern repeats without implying that the proof's logical dependency is circular.

This treatment of induction illustrates a general design principle for proof graphs: **represent iterative proof patterns as back-edges rather than self-loops**, both for Mermaid rendering reliability and for logical clarity. Self-loops in Mermaid are rendered inconsistently across versions; back-edges to a prior node are reliable and semantically equivalent for the purposes of the proof graph representation.

### 4.3 Merge and Chain Topologies

Different proof strategies for the same theorem produce characteristically different graph topologies. The Pythagorean Theorem proof comparison entry in the Mathematics Database illustrates this most clearly.

A geometric proof — such as the similar-triangle construction — fans out into multiple construction nodes before converging on a central algorithm capsule, producing a **merge topology**: width followed by a join. An algebraic proof — proceeding by symbolic rewriting — produces a **chain topology**: a narrow sequential path of inference nodes with few constructions and shallow branching. The two topologies are shown side by side below.

**Merge topology (geometric proof).**

```mermaid
flowchart TD
  T["Source: Pythagorean theorem a squared plus b squared equals c squared"]
  C1["Construction: altitude to hypotenuse"]
  C2["Construction: mark similar triangles"]
  AC["Algorithm capsule: length or area chase"]
  AS["Assertion: proportional segments"]
  I["Inference: combine ratios to relate a b c"]
  CO["Conclusion: as required"]
  T --> C1 --> AC
  T --> C2 --> AC
  AC --> AS --> I --> CO
  classDef red fill:#ff6b6b,color:#1e1e1e,stroke:#c0392b
  classDef yellow fill:#ffd43b,color:#1e1e1e,stroke:#f59f00
  classDef green fill:#51cf66,color:#1e1e1e,stroke:#40c057
  classDef lightblue fill:#74c0fc,color:#1e1e1e,stroke:#4dabf7
  classDef violet fill:#b197fc,color:#1e1e1e,stroke:#9775fa
  class T red
  class C1,C2 yellow
  class AC green
  class AS green
  class I lightblue
  class CO violet
```

**Chain topology (algebraic proof).**

```mermaid
flowchart TD
  T2["Source: same theorem for legs a b and hypotenuse c"]
  A0["Assumption: nonnegative lengths"]
  R1["Inference: encode triangle constraint algebraically"]
  R2["Inference: expand and simplify"]
  R3["Inference: isolate c squared"]
  CO2["Conclusion: a squared plus b squared equals c squared"]
  T2 --> A0 --> R1 --> R2 --> R3 --> CO2
  classDef red fill:#ff6b6b,color:#1e1e1e,stroke:#c0392b
  classDef yellow fill:#ffd43b,color:#1e1e1e,stroke:#f59f00
  classDef lightblue fill:#74c0fc,color:#1e1e1e,stroke:#4dabf7
  classDef violet fill:#b197fc,color:#1e1e1e,stroke:#9775fa
  class T2 red
  class A0 yellow
  class R1,R2,R3 lightblue
  class CO2 violet
```

| Topology | Visual signature | Typical role mix |
|----------|-----------------|------------------|
| Merge (geometric) | Width then join into capsule | Several Construction and Algorithm capsule nodes |
| Chain (algebraic) | Serial inferences, shallow branching | Predominantly Inference, few constructions |
| Contradiction hub | Dense assumption/inference subgraph feeding single contradiction node | High Assumption and Inference count, minimal conclusion arc |
| Back-edge (induction) | Loop from inductive step to hypothesis | One Assumption node, repeated inferential pattern |

These topological signatures are visible by inspection and measurable by the metadata fields in the Mathematics Database schema. They constitute a vocabulary for describing what a proof graph looks like beyond raw node counts — and they are the basis for the cross-proof-family comparisons developed in §6.3.

### 4.4 Conjunctive Premises and AND Structure

A structural distinction important in proof graphs but not in algorithmic flowcharts is the difference between **alternative paths** and **joint premises**. In an algorithm, multiple edges pointing to a single node typically mean that control may arrive from alternative paths — an OR structure. In a proof, multiple edges pointing to a single node typically mean that all the incoming steps are required together — a conjunctive or AND structure representing joint justification.

In the Mathematics Database as currently deployed, this distinction is carried by node labels and colors rather than by distinct graph syntax. A design iteration under evaluation introduces a compact hexagonal AND marker for conjunctive joins, making joint justification explicitly visible in the graph without requiring a large decorative node. The working principle is to reserve AND markers for semantically important conjunctions — cases where the joint requirement of multiple premises is itself a proof-theoretic observation worth marking — rather than applying them uniformly to every node with multiple predecessors.

This design question — how to represent conjunctive premise structure without visual noise — is an open one for the proof graph representation and is noted here as a known limitation and active development direction.

---

## 5. The Mathematics Database

The three graph types and their topological properties described in §3 and §4 are implemented in the Mathematics Database — a publicly accessible corpus of LLM-generated graphs stored as versioned JSON metadata and rendered through an interactive HTML viewer.

### 5.1 Architecture

The Mathematics Database is implemented as a collection of JSON metadata files stored on Google Cloud Storage, with an interactive HTML viewer that renders the data in three sortable tables — algorithms, axiomatic theories, and proof graphs — and generates live Mermaid diagram previews.

Each entry in the database is a JSON object. The normative schema used in this paper — expressed in JSON Schema [15] — is:

```json
{
  "id": "string",
  "title": "string",
  "category": "algorithm | axiomatic_system | proof_graph | hybrid",
  "subcategory": "string",
  "graph_type": "flowchart | dependency | proof | hybrid",
  "complexity": "low | medium | high",
  "nodes": integer,
  "edges": integer,
  "conditionals": integer,
  "and_gates": integer,
  "or_gates": integer,
  "not_gates": integer,
  "loops": integer,
  "algorithm_capsules": integer,
  "temporary_assumptions": integer,
  "mermaid": "string",
  "collections": ["string"],
  "frontier": boolean,
  "source": "string",
  "llm_version": "string",
  "version": "string"
}
```

The deployed manifest uses `name` in place of `title` and `processType` in place of `category` for implementation compatibility. All other fields are identical between the normative schema and the deployed manifest.

The analytical focus of this paper is the fourteen-entry **proof graph corpus** documented in §5.3. The broader Mathematics Database — produced by the same pipeline — also contains 23 algorithmic flowcharts and 194 axiomatic dependency graphs (see §5.4 for the full manifest). Those entries supply comparative context in §6.2 but are not catalogued here.

The `frontier` flag marks entries where the graph representation pushes against the limits of Mermaid's expressivity or the LLM's reliability — cases requiring additional validation or suggesting future extensions to the methodology. No printed proof graph in this revision carries that flag. The Kirby–Paris independence graph remains a linked database entry, flagged `frontier` because it mixes object-level and meta-level reasoning in one diagram; it is not printed as a figure (see §8).

### 5.2 Named Collections

The database includes named collections — curatorial groupings of entries by mathematician or theorem family. Their purpose is navigational: a reader interested in Cantor's work, or Gödel's foundational results, or Euclid's geometry can locate all relevant entries together without searching by subcategory. Named collections currently cover 63 mathematicians and 32 theorem families, for a total of 95 groupings. They are a discoverability feature rather than a formal structural category and carry no analytical weight in the corpus metrics.

### 5.3 Corpus Overview

Table 1 gives exact node, edge, and algorithm capsule counts for the fourteen proof graph entries used in this revision. Seven inherited entries (Euclid Book I through Gödel First Incompleteness, excluding the former Kirby–Paris row) keep their May 2026 deployed-manifest counts. Goodstein termination and the six new family entries are counted from the rendered diagrams in §6.1.

*Table 1: Proof graph corpus — manifest figures for inherited entries; diagram counts for new family entries.*

| Entry | Nodes | Edges | Capsules | Temp. Assumptions | Frontier |
|-------|-------|-------|----------|-------------------|----------|
| Euclid Book I bundle | 41 | 48 | 1 | 0 | — |
| Pythagorean Theorem | 33 | 39 | 2 | 0 | — |
| Infinitely Many Primes | 14 | 17 | 1 | 1 | — |
| Fundamental Theorem of Arithmetic | 27 | 34 | 2 | 1 | — |
| Goodstein termination | 8 | 7 | 1 | 0 | — |
| Cantor Diagonal Proofs | 42 | 50 | 1 | 0 | — |
| Gödel Completeness | 15 | 15 | 1 | 0 | — |
| Gödel First Incompleteness | 15 | 17 | 1 | 1 | — |
| Turing halting problem | 7 | 7 | 1 | 1 | — |
| Rice's theorem | 9 | 9 | 1 | 1 | — |
| Kleene's recursion theorem | 7 | 6 | 1 | 0 | — |
| Dickson's Lemma | 7 | 6 | 1 | 0 | — |
| Higman's Lemma | 9 | 9 | 1 | 1 | — |
| Lawvere's fixed-point theorem | 8 | 7 | 1 | 0 | — |
| **Totals** | **242** | **271** | **16** | **6** | |
| **Averages** | **17.3** | **19.4** | **1.14** | **0.43** | |

All fourteen proof graph entries contain at least one algorithm capsule. Within the Euclid Book I bundle, only proposition I.1 contributes a capsule — I.4 and I.5 carry individual construction nodes rather than capsules — as discussed in §6.1. The average of 17.3 nodes and 19.4 edges per proof graph mixes large inherited bundles with the smaller single-proof family graphs added in this revision; both classes remain more inferentially loaded than a typical algorithmic flowchart in the same manifest.

### 5.4 Live Database

The Mathematics Database is publicly accessible at:

https://storage.googleapis.com/regal-scholar-453620-r7-podcast-storage/mathematics-processes-database/mathematics-database-table.html

Interactive viewers for all three graph types, including live Mermaid rendering, are available at:

https://huggingface.co/spaces/garywelz/programming_framework

An experimental viewer demonstrating the compact hexagonal AND marker grammar and revised proof-role palette — discussed in §4.4 — is available for the Infinitely Many Primes proof graph at:

https://storage.googleapis.com/regal-scholar-453620-r7-podcast-storage/mathematics-processes-database/proof-graphs/infinitely-many-primes-v2-demo.html

This URL should be understood as a shape-and-palette demonstration. The main corpus tables use the rectangular default rendering until migration and validation are complete.

---

## 6. Findings from the Proof Graph Corpus

This section reports three findings from the fourteen-entry proof graph corpus (Table 1, §5.3): three families of self-referential and descent proofs (§6.1), structural complexity differences between proof graphs and other graph types (§6.2), and topological differences between proof families for the same theorem (§6.3).

### 6.1 Three Families of Self-Referential and Descent Proofs

The proof graphs in the corpus that involve embedded procedural substructures fall into three structurally distinct families when represented under fixed conventions (§3.3). The families share the algorithm capsule at the structural waist — a procedural bottleneck through which every upstream construction must pass before downstream inference is licensed — but differ in downstream resolution and in the logical mechanism at work.

**Family 1: Diagonal contradiction.** Four proof graphs share a common topology: an algorithm capsule constructs an object by anti-diagonal procedure applied to an assumed enumeration or decider, and downstream resolution terminates at a contradiction hub. A long bypass edge runs from the reductio assumption node directly to the contradiction hub, bypassing the capsule output — the visual trace of self-reference, in which the assumed complete listing or decider is confronted with an object built from that very assumption.

Cantor's diagonal uncountability proof (Figure 8) constructs a real number differing from every row of an assumed listing — a finite flip procedure at each diagonal position. Gödel's First Incompleteness proof (Figure 9) constructs a self-referential sentence by primitive recursive self-substitution on a provability predicate. Turing's halting problem proof (Figure 10) constructs a machine that does the opposite of what any proposed halting decider would output on its own code. Rice's theorem (Figure 11) reduces any non-trivial semantic property to the halting problem via a construction that simulates one program or another depending on whether a given input halts.

All four proofs belong to the formal diagonalization lineage traced by Gaifman [16] — naming systems that yield self-referential constructions — and instantiate Lawvere's abstract fixed-point schema [17] in the special case where point-surjectivity fails, forcing a contradiction rather than a fixed point. Hub in-degree varies: Cantor's contradiction hub receives two incoming edges; Gödel's receives four; Turing's and Rice's differ in setup depth. These differences are countable under the conventions in §3.3 and reported in Tables 2a–2d.

Figure 8 is the family's archetype as it appears in the Cantor Diagonal Proofs database entry: the proof graph for the uncountability of the reals in (0,1). The algorithm capsule — read the *n*th digit of the *n*th listed real and flip it — sits at the structural center of the graph. Everything upstream of the capsule prepares its input (the assumed enumeration, written as decimal rows); everything downstream is inference about its output (the anti-diagonal real *x*), terminating at the contradiction hub where the completeness assumption collapses.

```mermaid
flowchart TD
  T["Source: reals in (0,1) are uncountable"]
  AL["Assumption: every real in (0,1) appears in a sequence r1, r2, r3, ..."]
  DR["Construction: write each rn as a decimal row"]
  DC["Source: choose decimal expansions not ending in repeating 9s"]
  DD["Algorithm capsule: read nth digit of rn and choose a different digit, avoiding 9"]
  CX["Construction: define x by the changed diagonal digits"]
  XI["Assertion: x is a real number in (0,1)"]
  DF["Assertion: x differs from rn in the nth digit for every n"]
  NL["Assertion: x is not equal to any listed rn"]
  CT["Contradiction: list was assumed complete, but x is missing"]
  DS["Inference: discharge assumption — no sequence lists all reals in (0,1)"]
  CC["Conclusion: reals are uncountable"]
  T --> AL --> DR --> DD --> CX
  DC --> DR
  DC --> DF
  CX --> XI
  CX --> DF
  DF --> NL
  AL --> CT
  NL --> CT
  CT --> DS --> CC
  classDef red fill:#ff6b6b,color:#1e1e1e,stroke:#c0392b
  classDef yellow fill:#ffd43b,color:#1e1e1e,stroke:#f59f00
  classDef green fill:#51cf66,color:#1e1e1e,stroke:#40c057
  classDef lightblue fill:#74c0fc,color:#1e1e1e,stroke:#4dabf7
  classDef violet fill:#b197fc,color:#1e1e1e,stroke:#9775fa
  class T,DC,CT red
  class AL yellow
  class DR,CX yellow
  class DD,XI,DF,NL green
  class DS lightblue
  class CC violet
```

*Figure 8: Cantor's diagonal argument for the uncountability of the reals in (0,1), rendered as a proof graph (from the Cantor Diagonal Proofs entry in the Mathematics Database). The algorithm capsule (the anti-diagonal digit procedure) is the structural core: assumptions and constructions feed it, assertions flow from it, and the argument terminates at the contradiction hub. Colors follow the GLMP 6-color role scheme: Red = source/contradiction, Yellow = assumption/construction, Green = assertion/algorithm capsule, Light blue = inference, Violet = conclusion.*

This is what **contradiction-forming diagonalization** looks like under the proof graph representation: visibly different from the **chain topology** of Family 2 and of algebraic proofs (§4.3). Two features mark Family 1 entries at a glance. First, the construction narrows to a **waist** at the algorithm capsule: everything the proof builds funnels through the diagonal procedure before any assertion can be made. Second, an assumption node throws a **long bypass edge** that meets the argument at the contradiction hub — in Cantor, the assumed complete enumeration confronted with the anti-diagonal object (`AL → CT` in Figure 8); in Gödel, the temporary assumption that *T* proves *G*, together with edges from the diagonal capsule and from the fixed-point equivalence, all feeding a single contradiction node (Figure 9). Neither feature is apparent from the prose of the proof; both are immediate in the picture.

```mermaid
flowchart TD
  T["Target: Gödel first incompleteness for consistent recursive T extending PA"]
  G["Given: arithmetization of syntax in T"]
  A["Assumption: T is consistent and strong enough for representability"]
  L1["Lemma: provability predicate Bew is Sigma1 definable"]
  R["Assertion: recursive sets are representable in T"]
  N["Construction: fix Gödel numbering of terms formulas and proofs"]
  DL["Construction: diagonal lemma yields fixed-point schema"]
  P["Algorithm capsule: build G by primitive recursive self-substitution on Bew negation code"]
  E["Assertion: G is equivalent in T to formal unprovability of G"]
  F["Assertion: if T proves G then standard arithmetic is inconsistent with truth of G"]
  TP["Assumption: T proves G"]
  Q["Contradiction: T consistency forbids T proving G"]
  DS["Inference: discharge reductio — G is not provable in T"]
  W["Assertion: under soundness G holds in the standard model"]
  K["Conclusion: T cannot decide every arithmetic sentence"]
  T --> G
  T --> A
  G --> L1 --> R --> N --> DL --> P
  P --> E
  A --> F
  E --> F
  TP --> Q
  P --> Q
  E --> Q
  F --> Q
  Q --> DS --> W --> K
  classDef red fill:#ff6b6b,color:#1e1e1e,stroke:#c0392b
  classDef yellow fill:#ffd43b,color:#1e1e1e,stroke:#f59f00
  classDef green fill:#51cf66,color:#1e1e1e,stroke:#40c057
  classDef lightblue fill:#74c0fc,color:#1e1e1e,stroke:#4dabf7
  classDef violet fill:#b197fc,color:#1e1e1e,stroke:#9775fa
  class T,G,L1 red
  class A,TP,N,DL yellow
  class P,R,E,F,W green
  class Q red
  class DS lightblue
  class K violet
```

*Figure 9: Gödel First Incompleteness proof graph (Mathematics Database entry). The diagonal self-substitution capsule is the waist; temporary assumption `TP`, the fixed-point equivalence `E`, and the capsule output `P` all feed the contradiction hub before discharge. Colors follow the GLMP 6-color role scheme as in Figure 8.*

```mermaid
flowchart TD
  T["Source: no Turing machine decides halting for all inputs"]
  A["Assumption: machine H decides halting for all inputs"]
  C["Construction: build machine D — on input x, run H(x,x) and do the opposite"]
  AC["Algorithm capsule: run D on its own code — D(D)"]
  Q["Contradiction: H cannot correctly decide D(D) — if H says halt, D loops; if H says loop, D halts"]
  DS["Inference: discharge reductio — no such H exists"]
  K["Conclusion: the halting problem is undecidable"]
  T --> A --> C --> AC --> Q --> DS --> K
  A --> Q
  classDef red fill:#ff6b6b,color:#1e1e1e,stroke:#c0392b
  classDef yellow fill:#ffd43b,color:#1e1e1e,stroke:#f59f00
  classDef green fill:#51cf66,color:#1e1e1e,stroke:#40c057
  classDef lightblue fill:#74c0fc,color:#1e1e1e,stroke:#4dabf7
  classDef violet fill:#b197fc,color:#1e1e1e,stroke:#9775fa
  class T,Q red
  class A,C yellow
  class AC green
  class DS lightblue
  class K violet
```

*Figure 10: Turing's halting problem as a proof graph. Hub-and-bypass topology matching Cantor and Gödel: the long edge `A → Q` confronts the assumed decider with the diagonal machine `D(D)`. Colors follow the GLMP 6-color role scheme as in Figure 8.*

```mermaid
flowchart TD
  T["Source: no non-trivial semantic property of programs is decidable"]
  G["Given: let P be any non-trivial semantic property of programs"]
  A["Assumption: machine M decides property P for all inputs"]
  C["Construction: fix a program p0 without property P and a program p1 with property P"]
  AC["Algorithm capsule: given input x, build program D(x) that simulates p1 if x halts, else simulates p0"]
  E["Assertion: D(x) has property P if and only if x halts"]
  I["Inference: M decides P implies M decides halting"]
  Q["Contradiction: halting is undecidable — contradiction with assumption"]
  K["Conclusion: no non-trivial semantic property of programs is decidable"]
  T --> G --> A --> C --> AC --> E --> I --> Q --> K
  A --> Q
  classDef red fill:#ff6b6b,color:#1e1e1e,stroke:#c0392b
  classDef yellow fill:#ffd43b,color:#1e1e1e,stroke:#f59f00
  classDef green fill:#51cf66,color:#1e1e1e,stroke:#40c057
  classDef lightblue fill:#74c0fc,color:#1e1e1e,stroke:#4dabf7
  classDef violet fill:#b197fc,color:#1e1e1e,stroke:#9775fa
  class T,G,Q red
  class A,C yellow
  class AC,E green
  class I lightblue
  class K violet
```

*Figure 11: Rice's theorem as a proof graph. Hub-and-bypass via reduction to Turing rather than a direct diagonal construction — a slight structural variant within Family 1. Colors follow the GLMP 6-color role scheme as in Figure 8.*

**Family 2: Fixed-point self-reference.** Two proof graphs share a chain topology in which the algorithm capsule performs a diagonal self-application that produces a fixed point rather than a contradiction. There is no reductio assumption, no contradiction hub, and no bypass edge. The proof terminates at a violet conclusion node via a chain of assertions following from the capsule output.

Kleene's recursion theorem (Figure 12) shows that for any total computable function *f*, some program index *e* satisfies the condition that running program *e* gives the same result as running *f* applied to *e* — a fixed point guaranteed by the s-m-n theorem and self-referential index construction. Lawvere's fixed-point theorem (Figure 13) shows that in any cartesian closed category, a point-surjective morphism from an object to its exponential object guarantees a fixed point for every endomorphism — a categorical abstraction that subsumes Kleene's theorem as a special case. Both proof graphs use diagonal self-application at the capsule; both resolve through chain rather than hub. The relationship between the two entries is itself a corpus finding: the same proof-graph topology appears at two levels of abstraction — one computational, one categorical.

Formal accounts in the Gaifman–Lawvere tradition explain what makes self-reference possible in these systems. The proof graphs show where the self-referential step sits in the justification structure and how downstream tension is resolved — by fixed-point construction rather than by reductio.

```mermaid
flowchart TD
  T["Source: for any total computable function f, some program e satisfies phi-e equals phi-f(e)"]
  G["Given: let f be any total computable function"]
  C["Construction: define a computable function s such that phi-s(x)(y) simulates f(x) applied to phi-x"]
  AC["Algorithm capsule: apply the s-m-n theorem to construct a self-referential index"]
  E["Assertion: the constructed index e satisfies e equals s(e)"]
  F["Assertion: phi-e equals phi-f(e) by definition of s"]
  K["Conclusion: e is the required fixed point — Kleene's recursion theorem holds"]
  T --> G --> C --> AC --> E --> F --> K
  classDef red fill:#ff6b6b,color:#1e1e1e,stroke:#c0392b
  classDef yellow fill:#ffd43b,color:#1e1e1e,stroke:#f59f00
  classDef green fill:#51cf66,color:#1e1e1e,stroke:#40c057
  classDef violet fill:#b197fc,color:#1e1e1e,stroke:#9775fa
  class T,G red
  class C yellow
  class AC,E,F green
  class K violet
```

*Figure 12: Kleene's recursion theorem as a proof graph. Chain topology with fixed-point construction at the capsule — no contradiction hub. Family 2. Colors follow the GLMP 6-color role scheme as in Figure 8.*

```mermaid
flowchart TD
  T["Source: every endomorphism of A has a fixed point, given point-surjectivity"]
  G1["Given: cartesian closed category C with object A and exponential object A^A"]
  G2["Given: point-surjective morphism f from A to A^A — every morphism from A to A is in the image of f"]
  C["Construction: for any endomorphism g of A, define h from A to A by h(a) = g applied to f(a) evaluated at a"]
  AC["Algorithm capsule: diagonal self-application — evaluate f at a and apply the result to a itself"]
  E["Assertion: point-surjectivity of f guarantees some d in A with f(d) equal to h"]
  F["Assertion: substituting d yields h(d) equal to g(f(d)(d)) equal to g(h(d))"]
  K["Conclusion: h(d) is a fixed point of g — every endomorphism of A has a fixed point"]
  T --> G1 --> G2 --> C --> AC --> E --> F --> K
  classDef red fill:#ff6b6b,color:#1e1e1e,stroke:#c0392b
  classDef yellow fill:#ffd43b,color:#1e1e1e,stroke:#f59f00
  classDef green fill:#51cf66,color:#1e1e1e,stroke:#40c057
  classDef violet fill:#b197fc,color:#1e1e1e,stroke:#9775fa
  class T,G1,G2 red
  class C yellow
  class AC,E,F green
  class K violet
```

*Figure 13: Lawvere's fixed-point theorem as a proof graph. Chain topology with diagonal self-application at the capsule. Family 2. Caption note: categorical language required — cartesian closed category, exponential object, point-surjective morphism. Subsumes Kleene's recursion theorem as a special case. Colors follow the GLMP 6-color role scheme as in Figure 8.*

**Family 3: Well-founded descent.** Three proof graphs share a topology in which the algorithm capsule executes a procedural step whose downstream consequence is a strict decrease in a well-ordered measure, forcing termination or the existence of a combinatorial object. Two entries use chain resolution; one uses hub-and-bypass.

Goodstein termination (Figure 14) assigns a countable ordinal below epsilon-zero to each term in the Goodstein sequence; the algorithm capsule rewrites the hereditary base and subtracts one at each stage; ordinal descent forces termination. Dickson's Lemma (Figure 15) assigns a componentwise partial order to *k*-tuples of natural numbers; the capsule extracts minimal elements stage by stage; well-foundedness of the order forces a non-decreasing subsequence. Both resolve through chain topology — ordinal assignment, descent lemma, termination assertion, conclusion — with no contradiction hub.

Higman's Lemma (Figure 16) proceeds differently: it assumes the existence of an infinite bad sequence and constructs a minimal one by greedy choice at each position. The capsule is the minimal bad sequence construction; downstream resolution terminates at a contradiction hub when any extension of the minimal sequence contradicts its minimality. This hub-and-bypass topology places Higman in a hybrid position between Family 1 and Family 3 — well-founded descent in spirit, contradiction hub in execution. The distinction is representation-dependent in the sense of §3.3: Higman's Lemma can also be proved by direct well-foundedness arguments without reductio, which would produce a chain topology. The corpus uses the minimal bad sequence presentation because it is the most widely cited and the most structurally distinctive.

Whether Goodstein termination belongs to a diagonal family in the same prose sense as Cantor and Gödel is arguable — as noted by Kirby (personal communication) and confirmed by the MathOverflow discussion that directed us to Gaifman [16] and Lawvere [17]. The proof graphs do not adjudicate that prose question. They show that Goodstein shares the capsule waist with Cantor and Gödel but not the hub-and-bypass resolution — a measurable structural difference under fixed conventions.[^kirby-paris]

```mermaid
flowchart TD
  T["Source: every Goodstein sequence reaches zero"]
  G["Given: Goodstein game on hereditary base-k numerals"]
  BG["Construction: hereditary base-k expansion at each stage"]
  SG["Algorithm capsule: reweight bases, subtract one, and rewrite"]
  OG["Construction: attach a countable ordinal below epsilon-zero to each term"]
  WG["Lemma: each Goodstein step strictly lowers the ordinal"]
  TG0["Assertion: well-founded descent forces termination"]
  K["Conclusion: every Goodstein sequence terminates"]
  T --> G --> BG --> SG --> OG --> WG --> TG0 --> K
  classDef red fill:#ff6b6b,color:#1e1e1e,stroke:#c0392b
  classDef yellow fill:#ffd43b,color:#1e1e1e,stroke:#f59f00
  classDef green fill:#51cf66,color:#1e1e1e,stroke:#40c057
  classDef violet fill:#b197fc,color:#1e1e1e,stroke:#9775fa
  class T,G,WG red
  class BG,OG yellow
  class SG,TG0 green
  class K violet
```

*Figure 14: Goodstein termination as a proof graph. Chain topology; object-level ordinal descent only; no contradiction hub and no meta-level independence node. Family 3. Colors follow the GLMP 6-color role scheme as in Figure 8.*

```mermaid
flowchart TD
  T["Source: every infinite sequence of k-tuples of natural numbers has an infinite non-decreasing subsequence"]
  G["Given: infinite sequence s1, s2, s3, ... of k-tuples in N^k"]
  C["Construction: assign componentwise partial order to N^k"]
  AC["Algorithm capsule: at each stage extract the componentwise minimal elements remaining"]
  L["Lemma: N^k is well-founded under componentwise order — no infinite strictly decreasing chain exists"]
  E["Assertion: well-founded descent forces eventual non-decrease in every component"]
  K["Conclusion: Dickson's Lemma holds — every infinite sequence contains a non-decreasing subsequence"]
  T --> G --> C --> AC --> L --> E --> K
  classDef red fill:#ff6b6b,color:#1e1e1e,stroke:#c0392b
  classDef yellow fill:#ffd43b,color:#1e1e1e,stroke:#f59f00
  classDef green fill:#51cf66,color:#1e1e1e,stroke:#40c057
  classDef violet fill:#b197fc,color:#1e1e1e,stroke:#9775fa
  class T,G,L red
  class C yellow
  class AC,E green
  class K violet
```

*Figure 15: Dickson's Lemma as a proof graph. Chain topology with descent at the capsule; no contradiction hub. Matches the Goodstein topology. Family 3. Colors follow the GLMP 6-color role scheme as in Figure 8.*

```mermaid
flowchart TD
  T["Source: every infinite sequence of words over a finite alphabet contains a word embeddable into a later one"]
  G["Given: infinite sequence w1, w2, w3, ... over finite alphabet Sigma"]
  A["Assumption: no embedding exists — the sequence is a bad sequence"]
  C["Construction: among all bad sequences, choose a minimal one by greedy lexicographic construction"]
  AC["Algorithm capsule: at each position choose the shortest possible word that extends the bad sequence minimally"]
  E["Assertion: any extension of the minimal bad sequence contradicts its minimality"]
  Q["Contradiction: the assumed minimal bad sequence cannot exist"]
  DS["Inference: discharge reductio — no bad sequence exists"]
  K["Conclusion: Higman's Lemma holds"]
  T --> G --> A --> C --> AC --> E --> Q --> DS --> K
  A --> Q
  classDef red fill:#ff6b6b,color:#1e1e1e,stroke:#c0392b
  classDef yellow fill:#ffd43b,color:#1e1e1e,stroke:#f59f00
  classDef green fill:#51cf66,color:#1e1e1e,stroke:#40c057
  classDef lightblue fill:#74c0fc,color:#1e1e1e,stroke:#4dabf7
  classDef violet fill:#b197fc,color:#1e1e1e,stroke:#9775fa
  class T,G,Q red
  class A,C yellow
  class AC,E green
  class DS lightblue
  class K violet
```

*Figure 16: Higman's Lemma via the minimal-bad-sequence argument. Hub-and-bypass reductio with a descent capsule — hybrid case bridging Family 1 and Family 3. Colors follow the GLMP 6-color role scheme as in Figure 8.*

[^kirby-paris]: The Kirby–Paris independence-from-PA graph remains a linked Mathematics Database entry and is not printed as a figure. It uses merge topology to mark the independence gap between object-level termination and the meta-level underivability result; that entry is flagged `frontier` because object-level and meta-level scopes are approximated in a single graph. See §8.

*Table 2a: Family 1 — diagonal contradiction. Counts from the rendered paper figures.*

| Entry | Figure | Nodes | Edges | Hub in-degree | Temp. assumptions |
|-------|--------|-------|-------|---------------|-------------------|
| Cantor uncountability | 8 | 12 | 13 | 2 | 1 |
| Gödel First Incompleteness | 9 | 15 | 17 | 4 | 1 |
| Turing halting problem | 10 | 7 | 7 | 2 | 1 |
| Rice's theorem | 11 | 9 | 9 | 2 | 1 |

*Table 2b: Family 2 — fixed-point self-reference. Counts from the rendered paper figures.*

| Entry | Figure | Nodes | Edges | Hub in-degree | Temp. assumptions |
|-------|--------|-------|-------|---------------|-------------------|
| Kleene's recursion theorem | 12 | 7 | 6 | — | 0 |
| Lawvere's fixed-point theorem | 13 | 8 | 7 | — | 0 |

*Table 2c: Family 3 — well-founded descent. Counts from the rendered paper figures.*

| Entry | Figure | Nodes | Edges | Hub in-degree | Temp. assumptions |
|-------|--------|-------|-------|---------------|-------------------|
| Goodstein termination | 14 | 8 | 7 | — | 0 |
| Dickson's Lemma | 15 | 7 | 6 | — | 0 |
| Higman's Lemma | 16 | 9 | 9 | 2 | 1 |

*Table 2d: Topological signatures of the three families.*

| Family | Mechanism | Resolution | Bypass edge |
|--------|-----------|------------|-------------|
| 1 Diagonal contradiction | Anti-diagonal construction against an assumed listing or decider | Contradiction hub | Yes |
| 2 Fixed-point self-reference | Diagonal self-application producing a fixed point | Chain of assertions | No |
| 3 Well-founded descent | Procedural step that strictly decreases a well-ordered measure | Chain (Goodstein, Dickson); hub-and-bypass hybrid (Higman) | Higman only |

The Gödel Numbering algorithm — included in the corpus as a standalone algorithmic flowchart — serves as the explicit capsule twin to the First Incompleteness proof graph, making this the first algorithm/proof pair in the corpus where the same mathematical content appears in both categories. This pairing directly supports the claim in §1.2: placing proofs and algorithms in a common representational space reveals structural relationships invisible when the two object types are represented separately.

**Scope note.** Gödel's second incompleteness theorem is represented in the current database only as an axiomatic dependency chart (Peano and Gödel sequence, Part 8). A dedicated proof graph for second incompleteness is deferred: it requires additional internal formalization of consistency statements and would exceed the validation burden of the first incompleteness pilot.

Algorithm capsules appear in all fourteen proof graph entries (Table 1). What the proof graph representation makes explicit — and measurable — is the structural boundary between the algorithmic and the inferential within a single proof. That boundary is visible in the graph and absent from prose.

Within the Euclid Book I bundle, the fact that only proposition I.1 contributes a capsule is instructive. I.4 (SAS Congruence) has zero capsules because its proof proceeds entirely by superposition: a methodological assumption rather than a construction. I.5 (Base Angles) has zero capsules because its construction steps are individual proof-specific auxiliary lines rather than a reusable procedure. The contrast between I.1, I.4, and I.5 within the same bundle illustrates the decision rule stated in §3.3: a capsule is a self-contained procedural substructure with its own input/output logic, not merely a sequence of construction steps.

### 6.2 Structural Complexity Comparison

The database's quantitative metadata enables direct complexity comparison across mathematical objects that are not usually compared. Using the exact figures from Table 1, the fourteen proof graph entries average 17.3 nodes and 19.4 edges. That average mixes large inherited bundles with the smaller single-proof family graphs added in this revision. Individual proof graphs range from 7 nodes and 6 edges (Kleene; Dickson) to 42 nodes and 50 edges (Cantor Diagonal Proofs bundle).

Three structural observations follow from the corpus metadata:

**Proof graphs are more complex than algorithmic flowcharts of comparable mathematical content.** The higher node and edge counts reflect the inferential overhead of justification relative to procedure: a proof must not only perform a computation but establish why the computation's output has the required property. The algorithm capsule node type makes this overhead visible by marking where procedure ends and inference begins.

**Proof graphs differ in complexity from axiomatic dependency graphs of related content.** Axiomatic charts in the broader database (e.g., Peano Arithmetic, ZFC) vary in depth-to-breadth ratio; proof graphs for the same domain allocate complexity differently, with higher inferential overhead reflected in node and edge counts.

**Proof-by-contradiction graphs have a distinctive topology.** A single contradiction node with high in-degree, preceded by a dense assumption and inference subgraph, followed by a minimal conclusion arc. This contradiction hub topology is visible in the Family 1 entries (Figures 8–11), in Higman's Lemma (Figure 16), and in the Infinitely Many Primes entry; it is one of the topological signatures identified in §4.3. Family 2 and the chain members of Family 3 resolve without a hub.

These observations are grounded in exact figures from a small, mixed corpus of fourteen proof graphs. They should be understood as findings from a systematic pilot rather than large-scale statistical claims. A larger corpus — developed through the community extension process described in §8 — would support stronger statistical inference.

### 6.3 Cross-Proof-Family Comparison

The Pythagorean Theorem proof comparison entry demonstrates a capability unique to the graph-theoretic approach: direct structural comparison of multiple proofs of the same theorem. The entry captures several distinct proof families — geometric, algebraic, and trigonometric — in a single hybrid graph, with node colors encoding proof family membership.

The topological contrast between proof families, developed in §4.3, becomes metrically grounded here. Geometric proofs allocate complexity differently from algebraic proofs: more construction nodes and algorithm capsules in the geometric family, longer inference chains and fewer constructions in the algebraic family, more assumption nodes in the trigonometric family (which requires more lemmas about trigonometric identities as starting points).

These differences are difficult to articulate precisely in prose. In the graph representation they are visible by inspection and measurable from the metadata. A proof with two construction nodes and two capsules feeding a single algorithm capsule hub has a different structural character from a proof with five sequential inference nodes and no capsules — and that difference is now expressible as a metric rather than a qualitative judgment.

The Pythagorean Theorem entry is the proof graph corpus's clearest demonstration that the representation enables a new kind of mathematical comparison: not "which proof is more elegant" — a judgment that depends on aesthetic criteria — but "which proof allocates its structural complexity differently, and in what specific ways." That is a question the graph representation can answer precisely.

---

## 7. Limitations

**LLM accuracy.** LLM-generated proof graphs may misrepresent the logical structure of proofs, particularly for complex or non-standard arguments. All entries in the current database have been reviewed by the author, but systematic expert validation — particularly by logicians and proof theorists — remains future work. The human-in-the-loop pipeline described in §2.3 mitigates but does not eliminate this risk.

**Mermaid expressivity.** Mermaid does not natively support some features that would be useful for proof graphs: parallel proof branches, multiple inheritance in axiomatic hierarchies, or quantifier structure. The most consequential expressivity limitation is the representation of conjunctive premises — distinguishing joint justification from alternative control flow paths. The AND marker grammar described in §4.4 addresses this partially; it remains under evaluation and has not yet been rolled out across the main corpus. These limitations are otherwise managed by approximation and noted in individual entry metadata.

**The DAG assumption and encapsulated cycles.** Proof graphs in this corpus are treated as DAGs at the proof level, with cycles encapsulated within algorithm capsule nodes. This is a principled representational choice, as argued in §3.3, but it means that the internal structure of capsule nodes is not fully represented in the top-level graph. A proof graph representation that exposed capsule-internal structure as a subgraph would be more expressive but significantly more complex to generate, validate, and render. This is a known limitation of the current implementation.

**Corpus size.** The proof graph corpus contains fourteen entries across set theory, logic, computability, combinatorics, number theory, geometry, and category theory. The findings in §6 are grounded in exact figures from this corpus but should be understood as findings from a systematic pilot rather than large-scale statistical claims. The observations about the three families, contradiction hub topology, and cross-proof-family complexity differences are structurally well-motivated but would benefit from a larger corpus for statistical confirmation.

**No formal semantics.** The graph representations are visually and structurally informative but do not carry formal logical semantics. They are not machine-verifiable in the sense of proof assistants. They are human-readable and machine-processable structural descriptions — a complement to formal verification systems rather than a substitute for them. The relationship to formal proof assistants is discussed in §4.1.

**Single author, single pipeline.** All current entries were generated and reviewed by a single author using a single LLM pipeline. Inter-rater reliability and multi-pipeline reproducibility have not been evaluated. This is a standard limitation of first-generation corpus construction and is noted here for transparency.

---

## 8. Future Directions

**Capsule-internal structure as subgraphs.** The current implementation encapsulates cyclic and iterative structures within algorithm capsule nodes, preserving DAG structure at the proof level. A natural extension is to expose capsule-internal structure as explicit subgraphs — rendering the diagonal enumeration in the Cantor proofs or the Goodstein-step rewrite in Figure 14 as fully expanded flowcharts linked to their parent proof graphs. This would make the two-level DAG/cycle structure described in §3.3 and §7 fully visible and navigable rather than implied by the capsule node type. The technical challenge is rendering complexity: subgraph expansion would significantly increase diagram size and may require a viewer interface that supports expand/collapse navigation rather than static Mermaid rendering.

**Kirby–Paris independence as a linked database entry.** This revision prints Goodstein termination as an object-level Family 3 chain (Figure 14) and does not reprint the Kirby–Paris independence-from-PA graph. That merge-topology graph remains in the Mathematics Database as a `frontier` entry: an object-level termination path runs in parallel with a meta-level underivability inference, and a long edge marks the independence gap. Keeping it in the database, rather than as a main-text figure, separates the termination proof from the independence result and honors prior review of that graph without letting meta-level complexity dominate the three-family taxonomy. A later paper could treat object-level / meta-level nesting as a first-class graph convention.

**Integration with proof assistants.** The Lean 4 mathematical library (Mathlib) and the Coq Proof Assistant contain large bodies of formalized mathematics. As sketched in §4.1, informal proof graphs and Lean-style proof structures are complementary rather than competing representations: Lean answers "is this formally correct?" while proof graphs answer "how is the argument organized for inspection and comparison?" A natural research direction is to align the two — mining tactic traces or proof terms from Lean into role-labeled graphs, or using Mathlib entries as ground truth for validating corpus entries. This pipeline does not exist in the current database but would significantly increase both corpus size and validation quality.

**Systematic corpus validation and metadata quality.** The manifest correction identified during preparation of this paper — the Euclid Book I bundle capsule count requiring update from 0 to 1 — points to a broader need for systematic metadata validation across the corpus. A validation pipeline that checks field consistency, flags zero-capsule proof graph entries for review, and cross-checks node and edge counts against rendered diagrams would improve corpus quality and reproducibility. This is particularly important before community extension, where submitted entries will not have been generated by the same author using the same pipeline.

**Community extension.** A community-driven submission and review process, modeled on arXiv or Zenodo, would enable other researchers to contribute entries, validate existing ones, and propose new named collections. The Mathematics Database's current single-author, single-pipeline construction is appropriate for a pilot corpus but limits scale and reproducibility. Community extension would require the validation pipeline described above as a prerequisite.

**Cross-domain comparison across the Programming Framework.** The Programming Framework has been applied across biology, chemistry, physics, computer science, and mathematics. The most ambitious extension of the present work is systematic comparison across the discipline-specific databases — identifying structural regularities that appear across domains and asking whether the algorithm capsule concept, the contradiction hub topology, or the DAG/cycle two-level structure have analogs in non-mathematical process graphs. This is the subject of a planned comparative paper.

**AI-assisted mathematics education.** The Mathematics Database's interactive viewers suggest a natural application in mathematics education. Students can explore the dependency structure of theorems, trace proof paths from axioms, and compare the structural complexity of different proofs of the same result. The named collections — grouping entries by mathematician or theorem family — provide entry points organized around the historical narrative of mathematics rather than formal subcategory. Development of educational interfaces tailored to undergraduate and graduate mathematics curricula is planned.

**Proof-graph shape grammar.** The topological signatures identified in §4.3 — contradiction hub, merge, chain, back-edge — constitute the beginning of a shape grammar for proof graphs. Extending this grammar systematically across the full corpus, testing whether the signatures scale to more complex proofs such as the Cantor diagonal family or the Fundamental Theorem of Arithmetic, and developing a formal vocabulary for describing proof graph topology beyond raw node counts is a natural next step. The AND marker grammar described in §4.4 is one component of this; a complementary OR/case-split marker for genuine alternative proof branches is a natural addition, to be used with the same discipline of reserving markers for semantically important structural features.

---

## 9. Conclusion

This paper has introduced proof graphs with algorithm capsules as a diagrammatic representation of mathematical justification structure, and reported a corpus study of fourteen proof graphs with a central finding: the arguments fall into three structurally distinct families — diagonal contradiction, fixed-point self-reference, and well-founded descent — that share a capsule waist and differ in downstream resolution. Those signatures are only visible in the graph representation. In each family-member proof the algorithm capsule is not incidental but is the structural core. The taxonomy cuts across the conventional domain boundaries of set theory, mathematical logic, computability, combinatorics, and category theory. It is a finding about mathematical structure, not merely about representation.

All fourteen proof graph entries in the corpus contain at least one algorithm capsule; the three families are the most structurally pronounced instance of a broader regularity.

A skeptic might ask whether the graph representation merely redescribes what a careful reader of the prose already knows. The answer developed in §1.2 bears restating here: making structure explicit is itself a form of discovery when the structure was previously inaccessible to measurement and comparison. The three-family taxonomy is not visible in prose descriptions of these proofs. It becomes visible — and measurable, and comparable — only when the proofs are placed in a common representational space. The same is true of the two-level DAG/cycle structure identified in §3.3: proof graphs are acyclic at the proof level but may contain cycles encapsulated within algorithm capsule nodes. That structural property is present in the proofs whether or not it is represented. The graph makes it nameable, inspectable, and available for cross-proof comparison in a way that prose does not.

The proof graph node vocabulary — eight roles encoding the proof-theoretic function of each step — and the algorithm capsule concept are contributions to the general Programming Framework vocabulary with applications beyond mathematics. Wherever embedded procedural substructures appear within larger logical or justificatory structures, the algorithm capsule node type provides a representational handle that makes those substructures visible, nameable, and comparable.

The Mathematics Database is offered as open infrastructure: a starting point that others can validate, extend, and critique. Its current scale — fourteen proof graphs, 194 axiomatic dependency graphs, 23 algorithmic flowcharts — is appropriate for a pilot corpus. The findings it supports are structurally well-motivated and grounded in exact public figures. A larger corpus, developed through the community extension and validation processes described in §8, would support stronger claims.

The broader argument of this paper is that formal structure is recoverable from natural language descriptions of complex systems, and is meaningful, measurable, and comparable once recovered. That argument was first made for procedural processes. This paper extends it to logical dependency structures and justificatory structures. The same representational move that makes algorithms inspectable as typed computational graphs makes mathematical proofs inspectable as typed justification graphs — and in doing so reveals that some of the most important proofs in the history of mathematics share a structural core that their surface differences in domain and technique have long obscured.

---

## References

[1] G. Welz, *The Programming Framework: A General Method for Process Analysis Using LLMs and Mermaid Visualization*, Zenodo preprint, DOI: 10.5281/zenodo.18463441, 2026.

[2] "The QED manifesto," in *Automated Deduction — CADE-12*, LNCS 814, Springer, 1994, pp. 237–251.

[3] J. Avigad, L. de Moura, S. Koon, and S. Ullrich, *Theorem Proving in Lean 4*, online textbook, Lean Community, https://lean-lang.org/theorem_proving_in_lean4/ (accessed May 2026).

[4] The mathlib Community, "The Lean mathematical library," in *Certified Programs and Proofs (CPP '20)*, ACM, 2020, pp. 130–144. DOI: 10.1145/3372885.3373824

[5] The Coq Development Team, *The Coq Proof Assistant* — documentation and releases, https://coq.inria.fr/ (accessed May 2026).

[6] T. Nipkow, L. C. Paulson, and M. Wenzel, *Isabelle/HOL: A Proof Assistant for Higher-Order Logic*, LNCS 2283, Springer, 2002.

[7] A. Grabowski, A. Korniłowicz, and A. Naumowicz, "Four decades of Mizar," *Journal of Automated Reasoning*, vol. 55, no. 3, pp. 191–198, 2015.

[8] OpenMath Society, *The OpenMath Standard* (2.0 / ongoing revisions), https://www.openmath.org/ (accessed May 2026).

[9] J. Krajíček, *Bounded Arithmetic, Propositional Logic, and Complexity Theory*, Cambridge University Press, 1995.

[10] C. R. Twardy, "Argument maps improve critical thinking," *Teaching Philosophy*, vol. 27, no. 1, pp. 1–22, 2004.

[11] OpenAI, "GPT-4 technical report," *arXiv:2303.08774*, 2024.

[12] A. Lewkowycz et al., "Solving quantitative reasoning problems with language models," *Nature*, vol. 619, pp. 471–478, 2022.

[13] S. Polu and I. Sutskever, "Generative language modeling for automated theorem proving," *arXiv:2009.03393*, 2020.

[14] K. Sveidqvist and contributors, *Mermaid* — diagram syntax and toolkit, https://www.mermaidjs.org/ (accessed May 2026).

[15] JSON Schema Consortium, *JSON Schema: A Media Type for Describing JSON Documents*, Draft 2020-12 and specifications, https://json-schema.org/ (accessed May 2026).

[16] H. Gaifman, "Naming and Diagonalization, from Cantor to Gödel to Kleene," *Logic Journal of the IGPL*, vol. 14, no. 5, pp. 709–728, 2006. DOI: 10.1093/jigpal/jzl006.

[17] F. W. Lawvere, "Diagonal Arguments and Cartesian Closed Categories," in *Category Theory, Homology Theory and their Applications II*, Lecture Notes in Mathematics vol. 92, Springer, 1969. DOI: 10.1007/BFb0080769.

---

## Acknowledgments

This work is part of the CopernicusAI Knowledge Engine project, which aims to create AI-powered tools for scientific research synthesis and knowledge discovery. The Mathematics Database and the Programming Framework serve as foundational methodological components of that project. The author thanks the CUNY Graduate Center New Media Lab for institutional support, and Laurie Kirby for comments on an earlier independence-graph rendering of the Goodstein result. That merge-topology graph remains a linked database entry (§8) and is not printed as a figure in this revision.

The diagrams in this paper were generated with large-language-model assistance as part of the Programming Framework methodology described herein; large-language-model tools were also used to assist with copy-editing and revision. All scholarly content, analysis, and conclusions are the author's own.
