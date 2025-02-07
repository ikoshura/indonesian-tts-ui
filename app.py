import subprocess
import gradio as gr
from g2p_id import G2P
import ast
import re
import webbrowser
import threading
import time

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
        start_index = output.find("{")
        end_index = output.rfind("}")
        if start_index != -1 and end_index != -1:
            dict_str = output[start_index:end_index+1]
            speaker_dict = ast.literal_eval(dict_str)
            
            mapping = {}
            counter = 1  # Untuk "Pembicara X"

            for key in speaker_dict.keys():
                if re.match(r"^(JV|SU)-\d+$", key):
                    if key.startswith("JV"):
                        mapping[key] = f"Pembicara {counter} (Jawa)"
                    else:
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

def generate_tts(text, friendly_speaker):
    """
    Konversi teks ke fonem menggunakan g2p-id,
    lalu sintetis audio dengan TTS berdasarkan pilihan speaker.
    """
    original_key = reverse_mapping.get(friendly_speaker, "wibowo")
    phoneme_text = g2p(text)
    print("Teks asli:", text)
    print("Hasil konversi fonem:", phoneme_text)
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

# Fungsi untuk menampilkan animasi loading di terminal
def loading_animation(text="Sedang memuat interface indonesian-tts-ui", duration=5):
    for i in range(duration):
        for dots in range(1, 4):
            print(f"\r{text}{'.'*dots}", end="", flush=True)
            time.sleep(0.5)
    print("\n")

# Fungsi untuk membuka browser setelah server mulai
def open_browser():
    time.sleep(5)  # Beri waktu tunggu untuk server mulai
    webbrowser.open("http://127.0.0.1:7860")

# Gradio Interface dengan UI bahasa Indonesia
interface = gr.Interface(
    fn=generate_tts,
    inputs=[
        gr.Textbox(lines=2, placeholder="Masukkan teks di sini...", label="Teks Input"),
        gr.Dropdown(choices=friendly_names, label="Pilih Pembicara", allow_custom_value=True)
    ],
    outputs=gr.Audio(label="Hasil Audio"),
    title="🌻 Generator Text-to-Speech Bahasa Indonesia",
    description=(
        "Aplikasi untuk menghasilkan suara dari teks dalam bahasa Indonesia. "
        "Pilih pembicara dan masukkan teks lalu klik 'Hasilkan'.\n\n"
        "🔊 Pembicara dengan label (Jawa) atau (Sunda) menggunakan model khusus aksen daerah tersebut."
    ),
    examples=[
        ["Selamat pagi, bagaimana kabar Anda hari ini?", "Pembicara 1 (Jawa)"],
        ["Halo, selamat datang di aplikasi text-to-speech kami.", "Pembicara 44 (Sunda)"],
        ["Terima kasih telah menggunakan layanan ini.", "wibowo"]
    ],
    flagging_mode="never"  # Ganti dari allow_flagging ke flagging_mode
)

if __name__ == "__main__":
    loading_animation("Sedang memuat interface indonesian-tts-ui", duration=5)
    threading.Thread(target=open_browser, daemon=True).start()
    interface.launch(inbrowser=False, server_name="0.0.0.0")
