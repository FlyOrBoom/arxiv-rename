# arxiv-rename

Automatically renames downloaded arxiv PDFs to their author + year + title

## Installation

Clone this repository and install the required dependencies (`watchdog` and `arxiv`).
```bash
git clone https://github.com/FlyOrBoom/arxiv-rename.git
cd arxiv-rename
pip install requirements.txt
```

## Usage

Run this script in the background, 
replacing `~/Downloads` with the path to the directory where your arxiv PDFs are downloaded to.
```python
python3 main.py ~/Downloads
```

## Configuration

Go edit the code at `main.py` yourself!
