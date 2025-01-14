# python_image_analysis


This project is a Python-based image analysis tool that allows you to load images (PNG or JPG) and derive various color statistics. The application computes metrics such as the average color, median color, unique colors, and the most common colors. It also provides a user-friendly GUI built with **PyQt6** to visualize these results. For image processing, this project uses **PIL**.

## Features

- **Image Loading**  
  - Supports PNG and JPG formats.
- **Color Statistics**  
  - Calculates average color  
  - Calculates median color  
  - Identifies unique colors  
  - Finds the most common colors
- **GUI**  
  - Built with PyQt6

## Getting Started

### Prerequisites

- Python 3.7+  
- PyQt6
- PIL
- Any other dependencies listed in `requirements.txt`

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/lukas3482/python_image_analysis.git
    ```
2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. **Run the main script**:
    ```bash
    python main.py
    ```
2. **Load an Image**:  
   - Use the “Select Img” button in the GUI to select a PNG or JPG file.  
3. **Analyse Image**:  
   - Use the "Bild Analysieren" button in the GUI to Analyse the provided image.  
