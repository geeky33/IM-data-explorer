#  GSoC Weekly Meeting Summary – Status Update

## ✅ What I’ve Completed So Far (Last 2–3 Weeks)

### 📦 Block 1: Datumaro Setup
- ✅ Cloned and installed **Datumaro** in editable mode inside a virtual environment.
- ✅ Explored the **Datumaro API and plugin system** structure.
- ⚠️ Started designing a **storage plugin interface**, not yet connected to Datumaro loader.

### 🧠 Block 2: Embedding Module
- ✅ Installed all key dependencies: `transformers`, `optimum`, `openvino`.
- ✅ Successfully exported the **CLIP model (image + text encoder)** to OpenVINO IR via Docker.
- ✅ Built core embedding pipeline:
  - `extractor.py` – working OpenVINO inference for image & text.
  - `storage.py` – saving embeddings + metadata to `.h5`.
- ✅ Tested embedding inference manually on a few sample images/texts.
- ⚠️ Basic test file (`test_embed.py`) is working, but not formalized yet as CLI or pytest test.

---

## ❌ What’s Pending / Incomplete

### 🔄 Integration
- ❌ Haven’t loaded real datasets (COCO/YOLO) via `datumaro.Dataset.import()`.
- ❌ No connected pipeline between Datumaro → embedding extractor.
- ❌ Still need unit tests, CLI utility for batch embedding, and error handling improvements.

---

## 🧱 Roadblocks Faced

| Issue                   | What Happened                                               | How I Fixed / Working on                                 |
|------------------------|-------------------------------------------------------------|-----------------------------------------------------------|
| ❌ OpenVINO export      | `optimum-cli export openvino` broke multiple times         | Used Docker with fixed dependencies — finally successful  |
| ⚠️ Mixed GPU drivers    | OpenVINO defaulted to Intel GPU                            | Forced CPU usage for now — will benchmark GPU later       |
| ⚠️ Version mismatches   | `optimum` / `onnx` / `openvino` were mismatched             | Learned to pin compatible versions early on               |
---

## 🙋‍♀️ What I Need Mentor Input On

1. **Acceptance Criteria**  
   → For embedding pipeline, what counts as "working"? 100 samples? CLI? Unit tests?

2. **Datumaro Integration**  
   → Should I write a CLI that pulls data from Datumaro or connect through Python class?

3. **Dataset for Midterm**  
   → Is there a benchmark dataset you'd recommend I cache and work on for testing?

4. **Streamlit UI**  
   → Would a simple interface for embedding preview be okay by **end of Week 4**?

---

## 🗺️ What I’ll Do Next

- 🔜 Finalize CLI script for embedding generation (batch mode)
- 🔜 Write unit tests using `pytest` for image/text embedding
- 🔜 Add robust error handling and logging
- 🔜 Begin testing with real datasets via Datumaro (COCO first)

---
