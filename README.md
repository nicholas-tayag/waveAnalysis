# WaveAnalysis Program

WaveAnalysis is a program designed to calculate the angles of waves using Cartesian coordinates. It involves analyzing two images to determine the wave's break angle.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Program](#running-the-program)
- [Usage](#usage)
- [Future Implementations](#future-implementations)
- [License](#license)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

## Prerequisites

Before running the program, ensure you have the following installed on your local machine:

- **Python 3.7+**
- **pip** (Python package installer)

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/nicholas-tayag/waveAnalysis.git
    cd waveAnalysis
    ```

2. **Set Up Virtual Environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install Required Packages**:
    ```bash
    pip install -r requirements.txt
    ```

   If `requirements.txt` does not exist, manually install the necessary packages, such as:
   - opencv-python
   - numpy

## Running the Program

1. **Prepare Your Images**:
   Place your images in the `imgs` directory within the `waveAnalysis` folder. For this example, the program assumes two images, `pic1.png` and `pic2.png`.

2. **Run the Script**:
   Execute the script to analyze the images and calculate the wave angles:
   ```bash
   python waveAngle.py

## Future Implementations

In future versions, we aim to automate the wave angle calculation process using machine learning. These enhancements include:

- **Integration of YOLO**: Utilize YOLO for automatic detection of wave crests and features in images.
- **Machine Learning Models**: Develop and train machine learning models to predict and analyze wave angles from video footage or images automatically, minimizing the need for manual point selection.
- **Automated Workflow**: Implement a fully automated workflow that ingests video or image data, processes it using machine learning models, and outputs calculated wave angles and other relevant metrics.

These improvements will enhance the accuracy and efficiency of the wave analysis process, enabling more comprehensive data analysis and potentially real-time processing.
