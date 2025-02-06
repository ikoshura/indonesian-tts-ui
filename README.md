# Indonesian-TTS-UI: A User Interface for Indonesian TTS Built with Gradio

This repository provides a web-based UI for Indonesian text-to-speech (TTS) synthesis using Coqui TTS. It is designed to make it easy for users to generate Indonesian speech from text, utilizing models finetuned on high-quality datasets.

> **DO NOT USE FOR COMMERCIAL PURPOSES!**

![Screenshot 2025-02-06 161433](https://github.com/user-attachments/assets/29e07c73-a91f-44a9-8bd4-8de5feeb97a6)

---

## Table of Contents

- [Overview](#overview)
- [Model Changelog](#model-changelog)
- [Setup](#setup)
- [Usage](#usage)
- [Data](#data)
- [Citations](#citations)
- [Credits](#credits)

---

## Overview

This UI leverages Coqui TTS to synthesize Indonesian speech. It uses Gradio to provide a user-friendly interface and `g2p-id` for converting Indonesian text into phonemes before synthesis.

---

## Model Changelog

**v1.2 (Aug 12, 2022)**
- Finetuned from the v1.1 model on:
  - 4 hours of Audiobook dataset
  - 2000 samples from Azure TTS
  - High-quality TTS data for Javanese & Sundanese

**v1.1 (Aug 6, 2022)**
- Finetuned from the LJSpeech model on:
  - 4 hours of Audiobook dataset
  - 2000 samples from Azure TTS

**v1.0 (Jun 23, 2022)**
- Trained from scratch on:
  - 4 hours of Audiobook dataset

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

   > **Note:** This project requires Coqui TTS to be installed. The `tts` command used in the code comes from the Coqui TTS package.

4. **Download Model Files**

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
