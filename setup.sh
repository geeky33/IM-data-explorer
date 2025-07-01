#!/bin/bash

echo "[📦] Creating virtual environment..."
python3 -m venv freshenv
source freshenv/bin/activate

echo "[⬇️] Installing dependencies..."
pip install -r requirements.txt

echo "[✅] Setup complete. Run Streamlit with:"
echo "     streamlit run src/ui/streamlit_app/app.py"
