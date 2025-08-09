# ransomware_sim.py (Safe Simulation)
import os

# Directory to simulate ransomware attack (change as needed)
TARGET_DIR = "C:/Users/PUNEETH/Desktop/test_folder"  # <- simulate inside this folder only

def simulate_encrypt(file_path):
    # Simulate encryption by renaming the file
    new_file_path = file_path + ".locked"
    os.rename(file_path, new_file_path)

def scan_and_simulate_encrypt(directory):
    print(f"[+] Simulating ransomware in: {directory}")
    for root, _, files in os.walk(directory):
        for file in files:
            if not file.endswith(".locked"):  # Avoid re-locking
                full_path = os.path.join(root, file)
                try:
                    simulate_encrypt(full_path)
                    print(f"[LOCKED] {full_path}")
                except Exception as e:
                    print(f"[ERROR] {full_path} - {e}")

if __name__ == "__main__":
    scan_and_simulate_encrypt(TARGET_DIR)
    print("\n[+] Simulation complete. All files renamed with .locked.")
