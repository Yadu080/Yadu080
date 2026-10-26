<p align="center">
  <a href="#world-select"><img src="assets/arcade-hero.svg" width="100%" alt="YADU.EXE — AI experiments. Real code. Scroll to select one of five project worlds." /></a>
</p>

<p align="center">
  <b>Yadunandan M Nimbalkar · @Yadu080</b><br />
  I build AI tools, recommendation systems, and the interfaces that make them explorable.
</p>

<p align="center">
  <a href="#world-select"><b>▶ START EXPLORING</b></a> &nbsp; · &nbsp;
  <a href="#the-inventory">OPEN INVENTORY</a> &nbsp; · &nbsp;
  <a href="#source-code-challenge">TAKE THE CHALLENGE</a>
</p>

<br />

<a name="the-inventory"></a>
<img src="assets/section-inventory.svg" width="100%" alt="The inventory — technologies used in my repositories" />

<p align="center">
  <code>Python</code> &nbsp; <code>TypeScript</code> &nbsp; <code>JavaScript</code><br />
  <code>PyTorch</code> &nbsp; <code>scikit-learn</code> &nbsp; <code>SentenceTransformers</code> &nbsp; <code>FAISS</code><br />
  <code>FastAPI</code> &nbsp; <code>Flask</code> &nbsp; <code>SQLite</code> &nbsp; <code>SQLAlchemy</code><br />
  <code>React</code> &nbsp; <code>Next.js</code> &nbsp; <code>Three.js</code> &nbsp; <code>Tailwind CSS</code>
</p>

<br />

<a name="world-select"></a>
<img src="assets/section-worlds.svg" width="100%" alt="World select — choose a project" />

<table>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/Yadu080/AI-Codebase-Analyzer"><img src="assets/world-01-code.svg" width="100%" alt="World 01: AI Codebase Analyzer — enter the repository" /></a>
<p><b>The mission:</b> understand an unfamiliar codebase. Ask questions with retrieved source-code snippets supplied as context to an LLM.</p>
<p><code>FastAPI</code> <code>Next.js</code> <code>FAISS</code></p>
<p><a href="https://github.com/Yadu080/AI-Codebase-Analyzer"><b>▶ Explore</b></a> · <a href="https://github.com/Yadu080/AI-Codebase-Analyzer/blob/main/app/qa_engine.py">Inspect the Q&amp;A engine</a></p>
</td>
<td width="50%" valign="top">
<a href="https://github.com/Yadu080/Two-Tower_Recommendation_System"><img src="assets/world-02-recomai.svg" width="100%" alt="World 02: RECOMAI — enter the repository" /></a>
<p><b>The mission:</b> find the next movie. Combine two-tower neural retrieval with gradient-boosted re-ranking and a React interface.</p>
<p><code>PyTorch</code> <code>scikit-learn</code> <code>React</code></p>
<p><a href="https://github.com/Yadu080/Two-Tower_Recommendation_System"><b>▶ Explore</b></a> · <a href="https://github.com/Yadu080/Two-Tower_Recommendation_System/blob/main/ml/models/two_tower.py">Inspect the two towers</a></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/Yadu080/Model_Hunter"><img src="assets/world-03-modelhunter.svg" width="100%" alt="World 03: ModelHunter — enter the repository" /></a>
<p><b>The mission:</b> stress-test a model. Explore adversarial attacks, defense experiments, and downloadable evaluation reports.</p>
<p><code>PyTorch</code> <code>FastAPI</code> <code>SQLAlchemy</code></p>
<p><a href="https://github.com/Yadu080/Model_Hunter"><b>▶ Explore</b></a> · <a href="https://github.com/Yadu080/Model_Hunter/blob/main/backend/app/attacks/registry.py">Inspect the attack registry</a></p>
</td>
<td width="50%" valign="top">
<a href="https://github.com/Yadu080/silence-engine"><img src="assets/world-04-silence.svg" width="100%" alt="World 04: Silence Engine — enter the repository" /></a>
<p><b>The mission:</b> investigate missing activity. Triage potential service-access gaps and reporting failures in a prototype demonstrated on synthetic data.</p>
<p><code>Python</code> <code>Flask</code> <code>SQLite</code></p>
<p><a href="https://github.com/Yadu080/silence-engine"><b>▶ Explore</b></a> · <a href="https://github.com/Yadu080/silence-engine/blob/main/backend/silence_engine/triage.py">Inspect the triage rules</a></p>
</td>
</tr>
</table>

<a href="https://github.com/Yadu080/musicdna"><img src="assets/world-05-musicdna.svg" width="100%" alt="World 05, final stop: MusicDNA — enter the galaxy" /></a>

**The mission:** explore music taste through genre profiles, listening-history analysis, and an interactive 3D artist galaxy.

<code>Next.js</code> <code>TypeScript</code> <code>Three.js</code> <code>FastAPI</code>

[**▶ Explore MusicDNA**](https://github.com/Yadu080/musicdna) · [Inspect the taste-vector engine](https://github.com/Yadu080/musicdna/blob/main/backend/ml/taste.py)

<br />

<a name="source-code-challenge"></a>
<img src="assets/section-challenge.svg" width="100%" alt="Source-code challenge — three questions with click-to-reveal answers" />

Choose an answer to reveal the result. Give yourself one point for each correct first pick; the linked code is the answer key.

**ROUND 01 · What does Codebase Analyzer send to the LLM alongside your question?**

<details>
<summary>A · Retrieved code chunks and their file paths</summary>
<p><strong>✓ Correct.</strong> <code>generate_answer</code> builds context from each chunk's <code>file_path</code> and <code>chunk</code>, then places that context in the prompt with your question.</p>
<p><a href="https://github.com/Yadu080/AI-Codebase-Analyzer/blob/main/app/qa_engine.py">Inspect the answer →</a></p>
</details>

<details>
<summary>B · Only the repository name</summary>
<p><strong>Try the other route.</strong> The prompt includes retrieved source snippets and their paths, giving the model code to work from.</p>
<p><a href="https://github.com/Yadu080/AI-Codebase-Analyzer/blob/main/app/qa_engine.py">Follow the context construction →</a></p>
</details>

**ROUND 02 · Which model re-ranks RECOMAI's retrieved candidates?**

<details>
<summary>A · A second large language model</summary>
<p><strong>Try the other route.</strong> The ranking script imports <code>GradientBoostingClassifier</code> from scikit-learn.</p>
<p><a href="https://github.com/Yadu080/Two-Tower_Recommendation_System/blob/main/ml/scripts/train_ranker.py">Read the ranking pipeline →</a></p>
</details>

<details>
<summary>B · A gradient-boosted classifier</summary>
<p><strong>✓ Correct.</strong> The ranker scores user–movie pairs using engineered features such as embedding similarity and genre overlap.</p>
<p><a href="https://github.com/Yadu080/Two-Tower_Recommendation_System/blob/main/ml/scripts/train_ranker.py">Inspect the answer →</a></p>
</details>

**ROUND 03 · A service's recorded activity drops. Does that alone prove a service-access gap?**

<details>
<summary>A · Yes — low activity is sufficient proof</summary>
<p><strong>Try the other route.</strong> Missing or degraded reporting can also produce a drop. Silence Engine treats its categories as hypotheses for human verification.</p>
<p><a href="https://github.com/Yadu080/silence-engine/blob/main/backend/silence_engine/triage.py">Read the triage rules →</a></p>
</details>

<details>
<summary>B · No — investigate feed health and other evidence</summary>
<p><strong>✓ Correct.</strong> The system distinguishes potential access gaps, reporting problems, expected variation, and uncertain cases.</p>
<p><a href="https://github.com/Yadu080/silence-engine/blob/main/backend/silence_engine/triage.py">Inspect the answer →</a></p>
</details>

<p align="center"><sub>Score yourself: 1/3 · Explorer &nbsp; / &nbsp; 2/3 · Code detective &nbsp; / &nbsp; 3/3 · Source navigator</sub></p>

<br />

<a href="https://github.com/Yadu080?tab=repositories"><img src="assets/arcade-footer.svg" width="100%" alt="Continue? Browse all of Yadu's repositories." /></a>

<p align="center"><a href="#world-select">↑ Back to world select</a> · <a href="https://github.com/Yadu080?tab=repositories">All repositories ↗</a></p>
