QUESTIONS TO ASK MY MENTORS


🔹 High-Level Understanding
What specific goals of IMDE should be achieved by integrating parts of AnnFlux?

Do we intend to use AnnFlux as a submodule/library, or only extract concepts from it?

🔹 Technical Integration
Should IMDE directly use AnnFlux’s CLIP embedding pipeline and PCA logic, or reimplement our own version for modularity?

Can we rely on AnnFlux's CLI-based flow, or should IMDE be structured as a more modular Python library?

How important is AnnFlux’s current active learning logic for our use case — or should we design our own selection strategy?

🔹 Dataset and Annotation Compatibility
Should IMDE use the same folder structure as AnnFlux (data/project/images) or align with Datumaro’s dataset formats instead?

Is it expected that we modify AnnFlux to support multimodal datasets (e.g., text captions + images) natively within the tool?

🔹 UI and User Interaction
Is the current UI of AnnFlux sufficient for our needs, or are we expected to build a new frontend from scratch for IMDE?

Can parts of FluxIt (if it's more UI-focused) be integrated with AnnFlux's backend or reused as the frontend for IMDE?

🔹 Extensibility & Goals
Should IMDE support plugin-based model adapters like AnnFlux does for CLIP and PEFT?

Is there an expectation for IMDE to be annotation-focused (like AnnFlux) or exploration-focused (like embedding analysis, dataset cleaning)?

🔹 Evaluation
Are there benchmarks or user-level scenarios we should prepare to compare IMDE + AnnFlux workflows (e.g., annotation speed, label quality, embedding accuracy)?

Is AnnFlux’s PEFT fine-tuning capability something we are expected to include in IMDE as well?

