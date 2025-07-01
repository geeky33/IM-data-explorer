I focused heavily on setting up the environment, resolving export issues with the CLIP model, and ensuring the core embedding pipeline works end-to-end. The model was not exporting cleanly using the standard optimum-cli, so I had to switch to Docker and adjust dependencies multiple times.

As a result, most of my effort went into Block 2 (Embedding) to ensure the foundation was stable. I now have image/text embedding extractors working with OpenVINO and storing in HDF5, tested on sample images.

The integration with Datumaro (Block 1) is pending because:

I haven't yet written the adapter code that connects Datumaro's dataset items to the embedding extractor inputs (e.g., image loading and ID normalization).

I need to fetch and load a sample COCO/YOLO dataset to properly test the pipeline.

Now that the embedding pipeline is stable, I'm ready to shift full focus to the integration layer. I estimate this will take 2–3 focused working sessions if I can get mentor input on how you'd prefer the data adapter to be structured (Python class vs CLI).
I’ve learned that doing integration too early without working model inference would have backfired. So now that Block 2 is stable, the rest should move faster.
