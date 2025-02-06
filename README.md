# Indonesian-TTS-UI: A User Interface for Indonesian TTS Built with Gradio

This repository provides a web-based UI for Indonesian text-to-speech (TTS) synthesis using Coqui TTS. It is designed to make it easy for users to generate Indonesian speech from text, utilizing models finetuned on high-quality datasets.

> **DO NOT USE FOR COMMERCIAL PURPOSES!**

![Screenshot 2025-02-06 161433](https://github.com/user-attachments/assets/29e07c73-a91f-44a9-8bd4-8de5feeb97a6)

---

## Table of Contents

- [Overview](#overview)
- [Setup](#setup)
- [Usage](#usage)
- [Data](#data)
- [Citations](#citations)
- [Credits](#credits)
- [Example](#example)

---

## Overview

This UI leverages Coqui TTS to synthesize Indonesian speech. It uses Gradio to provide a user-friendly interface and `g2p-id` for converting Indonesian text into phonemes before synthesis.

---

## Setup

To set up the project, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/ikoshura/indonesian-tts-ui.git
   cd indonesian-tts-ui
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   ```

   Activate the virtual environment:

   - **Windows (cmd):**
     ```bash
     venv\Scripts\activate
     ```
   - **Linux/Mac:**
     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies**

   Install the required Python packages with:

   ```bash
   pip install -r requirements.txt
   ```
   If you face issues installing Coqui TTS on Python 3.13 or newer, use Python 3.11 instead:
   ```bash
   py -3.11 -m pip install -r requirements.txt 
   ```
   > **Note:** This project requires Coqui TTS to be installed. The `tts` command used in the code comes from the Coqui TTS package.

5. **Download Model Files**

   You can find the models in the [Releases](https://github.com/Wikidepia/indonesian-tts/releases/) tab of the `indonesian-tts` repository.
   
   Make sure to place your model checkpoint (`checkpoint.pth`), speakers (`speakers.pth`)
and configuration file (`config.json`) in the same folder as app.py or update the paths in the code accordingly.

---

## Usage

Run the application by opening the `run.bat` file or manually executing:

```bash
python app.py
```

This will launch the Gradio web interface where you can:
- Enter text in Indonesian.
- Choose a speaker from the dropdown (the available speaker IDs are fetched dynamically).
- Listen to the synthesized speech.

---

## Example

`Ardi (Azure)`:

https://user-images.githubusercontent.com/72781956/183240414-b1127e83-6ddd-427c-b58d-386c377f15b4.mp4

`Gadis (Azure)`:

https://user-images.githubusercontent.com/72781956/183240420-a5d0d335-af4a-4563-a744-40f6795955c5.mp4

`Wibowo (Audiobook)`:

https://user-images.githubusercontent.com/72781956/184360026-c81ac336-c9f1-48ee-97fb-907d66b7f343.mp4

---

## Data

- **Indonesian Azure TTS Dataset:** [Download Link](https://depia.wiki/files/azure-tts.tar)

---

## Citations

```bibtex
@misc{https://doi.org/10.48550/arxiv.2106.06103,
  doi = {10.48550/ARXIV.2106.06103},
  url = {https://arxiv.org/abs/2106.06103},
  author = {Kim, Jaehyeon and Kong, Jungil and Son, Juhee},
  title = {Conditional Variational Autoencoder with Adversarial Learning for End-to-End Text-to-Speech},
  publisher = {arXiv},
  year = {2021}
}

@inproceedings{kjartansson-etal-tts-sltu2018,
  title = {A Step-by-Step Process for Building TTS Voices Using Open Source Data and Framework for Bangla, Javanese, Khmer, Nepali, Sinhala, and Sundanese},
  author = {Keshan Sodimana and Knot Pipatsrisawat and Linne Ha and Martin Jansche and Oddur Kjartansson and Pasindu De Silva and Supheakmungkol Sarin},
  booktitle = {Proc. The 6th Intl. Workshop on Spoken Language Technologies for Under-Resourced Languages (SLTU)},
  year = {2018},
  address = {Gurugram, India},
  month = aug,
  pages = {66--70},
  URL = {http://dx.doi.org/10.21437/SLTU.2018-14}
}
```

---

## Credits

- **Indonesian TTS:** [indonesian-tts](https://github.com/Wikidepia/indonesian-tts)
- **Core TTS Engine:** [Coqui TTS](https://github.com/coqui-ai/TTS)
- **Grapheme-to-Phoneme Conversion:** [g2p-id](https://github.com/Wikidepia/g2p-id)
- **UI Design Inspiration:** [XTTS-2-UI](https://github.com/pbanuru/xtts2-ui)
