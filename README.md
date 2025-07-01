## 📦 Block 1: Datumaro Integration Layer

- [x] Understand Datumaro API & plugin system
- [x] Clone and install Datumaro in editable mode
- [ ] Load and test COCO dataset using `datumaro.Dataset.import()`
- [ ] Load and test YOLO dataset using `datumaro.Dataset.import()`
- [ ] Normalize labels and metadata across formats
- [ ] Design simple plugin interface for embedding storage (hook to HDF5/mmap)
- [ ] Write utility to convert Datumaro items → embedding input format
- [ ] Test dataset loading on 2+ formats
- [ ] Validate metadata integrity (ID, label, caption consistency)



## 🧠 Block 2: Embedding Module

- [x] Install `transformers`, `optimum`, and `openvino`
- [x] Export `openai/clip-vit-base-patch32` to OpenVINO IR (image encoder)
- [x] Export `openai/clip-vit-base-patch32` to OpenVINO IR (text encoder)
- [X] Implement `extractor.py` for image embeddings using OpenVINO
- [X] Implement `extractor.py` for text embeddings using OpenVINO
- [X] Write `storage.py` for storing embeddings in HDF5 with metadata
- [X] Create CLI/utility for batch embedding generation
- [ ] Write unit tests for extractor on a sample dataset (10–100 items)
- [ ] Test large-scale extraction (1000+ samples)
- [ ] Optimize performance (batching, inference caching)
- [ ] Add error handling: missing file, inference fail, etc.

## 🔄 Integration Tasks (Optional for Week 3)

- [ ] Connect Datumaro loader output to embedding extractor
- [ ] Store embeddings + metadata using unified format
- [ ] Build debug CLI to extract + store + print shape and ID

# 🧠 Interactive Multimodal Data Explorer (GSoC 2025 - Midterm Report)

## 📌 Project Overview

This GSoC project aims to build an **Interactive Multimodal Data Explorer** that uses OpenVINO-accelerated CLIP models to extract, store, and visualize embeddings from datasets in multiple formats like COCO, YOLO, etc., with integration to Datumaro and a lightweight Streamlit frontend.

---

## ✅ Progress Summary (till Midterm)

### 🔹 Completed

- **Environment Setup**
  - Created isolated Python virtual environment
  - Installed all core libraries: `openvino`, `optimum`, `transformers`, `datumaro`, etc.

- **Model Export**
  - Exported `openai/clip-vit-base-patch32` to OpenVINO IR using Docker
  - Image encoder and text encoder exported successfully to `clip_ov/`

- **Embedding Pipeline**
  - Implemented `extractor.py` for both image and text encoding using OpenVINO runtime
  - Implemented `storage.py` to save embeddings in HDF5 format with metadata
  - Created `test_embed.py` for local testing of 2–3 image files (cat, dog, car)

- **File Structure**
  - Organized `src/core/embeddings/`, `scripts/`, and testing files clearly
  - Sample images and test setup ready

---

### 🟡 In Progress / Partial

- **CLI Tool**
  - `test_embed.py` simulates batch embedding generation, needs full CLI wrapper

- **Streamlit App**
  - Basic skeleton started, will connect once embedding generation is stabilized

---

### ❌ Not Achieved Yet

- **Datumaro Dataset Integration**
  - Haven't yet loaded or converted datasets like COCO/YOLO using `datumaro.Dataset.import(...)`
  - Normalization and format bridging code is pending

- **Unit Tests**
  - No automated test suite written yet for extractor/storage modules

- **Large-scale Dataset Embedding**
  - No benchmark dataset (>1000 items) tested yet due to missing Datumaro loader

- **Full CLI + Error Handling**
  - Embedding pipeline doesn't yet handle failure cases or CLI flags

---

## 🧱 Folder Structure



1. Validation: “What acceptance test should we use for the embedding extractor?”
2. Performance targets: “Any latency/throughput numbers we must hit?”
3. Data: “Which benchmark dataset would you prefer I cache first?”
4. Integration: “Confirm the API shape for Datumaro ingest—Python class or CLI?”
5. UI timeline: “Is a bare-bones Streamlit mock-up by Week 4 acceptable?”

| **Roadblock** | **What actually happened** | **Why it tripped you up** | **Quick fix / lesson learned** |
|---|---|---|---|
| `optimum-cli export openvino` kept failing | The command threw shape-mismatch and “unsupported op” errors when converting the CLIP model to OpenVINO IR. | The default ONNX version bundled with **optimum** was older than what OpenVINO expects. | Pin compatible versions (`pip install onnx==1.16.0 optimum==1.18.1`) *before* export. Record the combo for future setups. |
| CUDA vs. OpenVINO driver clash | OpenVINO’s GPU plugin grabbed the Intel iGPU instead of your RTX 3060, then silently fell back to CPU. | Mixed-GPU environments confuse OpenVINO unless the device is forced. | Specify the target: `compile_model(..., device_name="GPU.1")` or stick to CPU until later benchmarks. |
| Missing system dependencies | CMake and protobuf headers weren’t on `PATH`, so the model-optimizer script bailed. | OpenVINO calls these tools under the hood. | `sudo apt install cmake protobuf-compiler libprotobuf-dev` and note this in the README so no one repeats it. |
| Slow hostel Wi-Fi for model download | The 400 MB CLIP model from Hugging Face timed out twice. | Unstable network cost several hours. | Cache the model to a USB drive and use `--local-files-only` on retries; consider `aria2c` or campus LAN. |
| No visible progress log for mentors | Work stayed on your laptop; nothing pushed for four days. | Mentors couldn’t step in because they didn’t know you were blocked. | Open an “Export Blocker” issue once stuck > 2 hrs and push WIP branches nightly. |

*Take-away: most blockers were version mismatches or silent fallbacks—catch them early and surface them quickly to save whole days later.*

