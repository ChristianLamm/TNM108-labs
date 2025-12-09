**Explain the TextRank algorithm and how it works to the lab assistant:**

TextRank is an **unsupervised, graph-based algorithm** used for **extractive text summarization**.  
It treats sentences as nodes in a graph and uses their similarity to connect them.  
The idea is inspired by Google's PageRank: a sentence is important if it is linked to by other important sentences.

---

## How TextRank Works

1. **Split the document into sentences**  
   Each sentence becomes a node in a graph.

2. **Compute similarity between sentences**  
   Sentences are connected by edges weighted by how many meaningful words they share.  
   More shared words → stronger similarity score.

3. **Build a graph of sentences + similarity scores**

4. **Apply PageRank on the graph**  
   PageRank assigns each sentence an importance score based on its connections.

5. **Select the top-ranked sentences**  
   These sentences (in original order) form the extractive summary.

---

## Formula

Similarity(S1​,S2​)=∣Words(S1​)∩Words(S2​)∣​ / log(∣S1​∣)+log(∣S2​∣)

1. Count how many words the sentences share
(e.g. both contain “computer”, “learning”, …)

2. Normalize by the length of the sentences
This prevents long sentences from automatically getting high scores.

3. Higher overlap = stronger connection
This becomes the weight of the edge between the two sentences in the graph.

---

## Key Features

- **Unsupervised** — no training data needed  
- **Language-independent** — works for many languages  
- **Graph-based approach** — focuses on relationships between sentences  
- **Uses PageRank** to rank importance  
- **Extractive summarization** — outputs existing sentences, not generated text

---

## Pros

- ✔ Works without any training  
- ✔ Fast and efficient on long documents  
- ✔ Domain-independent (news, articles, transcripts, etc.)  
- ✔ Simple to implement and understand  

---

## Cons

- ✘ Only extractive — cannot rewrite sentences  
- ✘ Relies on surface similarity (word overlap)  
- ✘ Does not understand deeper semantic meaning  
- ✘ Summaries may lack coherence if selected sentences don't flow well together

---

## One-Sentence Summary

**TextRank ranks sentences using PageRank based on how similar they are, and selects the top-ranked ones to create an extractive summary.**



