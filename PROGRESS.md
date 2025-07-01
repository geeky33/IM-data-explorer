## GSoC Progress Tracker

### 📦 Block 1: Datumaro Integration Layer

| Task                                                        | Status    | Notes                                                      |
|-------------------------------------------------------------|-----------|------------------------------------------------------------|
| Understand Datumaro API & plugin system                     | ✅ Done   | You've read and explored the basics.                      |
| Clone and install Datumaro in editable mode                 | ✅ Done   | Installed inside virtualenv.                              |
| Load and test COCO dataset using `datumaro.Dataset.import()`| ❌ Not yet| Needs a small COCO sample + script.                       |
| Load and test YOLO dataset using `datumaro.Dataset.import()`| ❌ Not yet| Same as above.                                             |
| Normalize labels and metadata across formats                | ❌        | Part of above task.                                        |
| Design simple plugin interface for embedding storage        | ⚠️ Partial| `storage.py` exists, but not plugged into Datumaro yet.   |
| Write utility to convert Datumaro items → embedding input   | ❌        | Needs bridging function.                                  |
| Test dataset loading on 2+ formats                          | ❌        | Needs COCO + YOLO samples.                                |
| Validate metadata integrity                                 | ❌        | Not started yet.                                           |

➡️ **Block 1 Status**: ✅✅❌❌❌⚠️❌❌❌❌  
🔍 **Summary**: Explored Datumaro basics; integration with real data pending.

---

### 🧠 Block 2: Embedding Module

| Task                                                 | Status     | Notes                                                       |
|------------------------------------------------------|------------|-------------------------------------------------------------|
| Install `transformers`, `optimum`, and `openvino`    | ✅ Done    | Installed inside virtualenv.                                |
| Export CLIP model to OpenVINO IR (image encoder)     | ✅ Done    | Exported successfully via Docker.                           |
| Export CLIP model to OpenVINO IR (text encoder)      | ✅ Done    | Same as above.                                              |
| Implement `extractor.py` for image embeddings        | ✅ Done    | Model compiled and embedded.                               |
| Implement `extractor.py` for text embeddings         | ✅ Done    | Text encoder implemented.                                   |
| Write `storage.py` for HDF5 with metadata            | ✅ Done    | Embeddings stored with labels and metadata.                 |
| Create CLI/utility for batch embedding generation    | ⚠️ Partial | `test_embed.py` simulates it; CLI not wrapped yet.          |
| Write unit tests for extractor (10–100 items)        | ❌         | Needs test file with assertions/logs.                       |
| Test large-scale extraction (1000+ samples)          | ❌         | Dataset needed; plan later.                                 |
| Optimize performance (batching, caching, etc.)       | ❌         | Can be addressed after stability.                           |
| Add error handling (missing files, failed inferences)| ⚠️ Partial | Minimal `try/except`; needs better logging and fallback.    |

➡️ **Block 2 Status**: ✅✅✅✅✅✅⚠️❌❌❌⚠️  
🔍 **Summary**: Core embedding flow works; testing, CLI, and optimization remain.

---

### 🔄 Integration Tasks

| Task                                                               | Status     | Notes                                              |
|--------------------------------------------------------------------|------------|----------------------------------------------------|
| Connect Datumaro loader output to embedding extractor              | ❌         | Bridging function not yet written.                |
| Store embeddings + metadata using unified format                   | ⚠️ Partial | `storage.py` done, but not from Datumaro items.   |
| Build debug CLI to extract + store + print shape and ID            | ⚠️ Partial | `test_embed.py` simulates this; needs full CLI.    |

---

### 🧾 Notes

- Midterm-ready embedding pipeline ✅
- Docker workaround for model export ✅
- Datumaro integration needs to **start immediately**
- Unit tests and CLI should be the focus of **next 3–4 days**

