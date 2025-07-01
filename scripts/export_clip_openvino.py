from optimum.exporters.openvino import export_openvino

export_openvino(
    model_id="openai/clip-vit-base-patch32",
    output="clip_ov",
    task="feature-extraction",
    subfolder="image_encoder"
)

export_openvino(
    model_id="openai/clip-vit-base-patch32",
    output="clip_ov",
    task="feature-extraction",
    subfolder="text_encoder"
)
