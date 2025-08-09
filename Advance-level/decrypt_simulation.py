# decrypt_sim.py
import os

TARGET_DIR = "C:/Users/PUNEETH/Desktop/test_folder"

def simulate_decrypt(file_path):
    if file_path.endswith(".locked"):
        new_path = file_path.replace(".locked", "")
        os.rename(file_path, new_path)

def scan_and_decrypt(directory):
    print(f"[+] Simulating decryption in: {directory}")
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".locked"):
                full_path = os.path.join(root, file)
                try:
                    simulate_decrypt(full_path)
                    print(f"[UNLOCKED] {full_path}")
                except Exception as e:
                    print(f"[ERROR] {full_path} - {e}")

if __name__ == "__main__":
    scan_and_decrypt(TARGET_DIR)
    print("\n[+] Simulation complete. Files restored.")
