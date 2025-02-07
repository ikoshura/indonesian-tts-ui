import subprocess
import gradio as gr
from g2p_id import G2P
import ast
import re

# Inisialisasi modul G2P
g2p = G2P()

def get_speaker_idxs():
    """
    Menjalankan perintah TTS untuk mendapatkan daftar speaker.
    Hanya kode berbentuk "JV-XXXX" dan "SU-XXXX" yang akan diubah menjadi "Pembicara X".
    Nama lainnya tetap dipertahankan.
    """
    try:
        result = subprocess.run(
            "tts --model_path checkpoint.pth --config_path config.json --list_speaker_idxs",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        output = result.stdout
        # Cari dictionary dalam output
        start_index = output.find("{")
        end_index = output.rfind("}")
        if start_index != -1 and end_index != -1:
            dict_str = output[start_index:end_index+1]
            speaker_dict = ast.literal_eval(dict_str)
            original_keys = list(speaker_dict.keys())
            
            mapping = {}
            counter = 1  # Untuk "Pembicara X"

            for key in speaker_dict.keys():
                if re.match(r"^(JV|SU)-\d+$", key):
                    if key.startswith("JV"):
                        mapping[key] = f"Pembicara {counter} (Jawa)"
                    else:  # key pasti diawali SU
                        mapping[key] = f"Pembicara {counter} (Sunda)"
                    counter += 1
                else:
                    mapping[key] = key

            return mapping
        else:
            print("Dictionary tidak ditemukan dalam output.")
            return {}
    except Exception as e:
        print("Error menjalankan perintah list_speaker_idxs:", e)
        return {}

# Dapatkan mapping speaker friendly
speaker_mapping = get_speaker_idxs()
friendly_names = list(speaker_mapping.values())  # Untuk dropdown
reverse_mapping = {v: k for k, v in speaker_mapping.items()}  # Untuk konversi balik

print("Mapping speaker:", speaker_mapping)

def generate_tts(text, friendly_speaker):
    """
    Konversi teks ke fonem menggunakan g2p-id,
    lalu sintetis audio dengan TTS berdasarkan pilihan speaker.
    """
    original_key = reverse_mapping.get(friendly_speaker, "wibowo")
    
    # Konversi teks ke fonem
    phoneme_text = g2p(text)
    print("Teks asli:", text)
    print("Hasil konversi fonem:", phoneme_text)
    
    # Jalankan perintah TTS
    command = (
        f"tts --text \"{phoneme_text}\" "
        f"--model_path checkpoint.pth "
        f"--config_path config.json "
        f"--speaker_idx {original_key} "
        f"--out_path output.wav"
    )
    print("Menjalankan perintah:", command)
    subprocess.run(command, shell=True, check=True)
    
    return "output.wav"

# Gradio Interface
interface = gr.Interface(
    fn=generate_tts,
    inputs=[
        gr.Textbox(lines=2, placeholder="Masukkan teks...", label="Teks"),
        gr.Dropdown(choices=friendly_names, label="Speaker")
    ],
    outputs=gr.Audio(label="Output Audio"),
    title="TTS Generator Bahasa Indonesia"
)

if __name__ == "__main__":
    interface.launch()
