import requests

url_base = "https://api.hipoverse.xyz"
task_ids = [
    "7131c01d-1629-4060-bc84-6b3d415d7ccc",
    "120eea3a-3f8c-423b-a97e-44e59db00b11",
    "84634aa6-8e4f-4b77-914e-dc7d388b4f9e",
    "4ecb28bc-c4cc-4fe8-b4be-a81ea492b0a6"
]

def get_point(token: str):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    url = f"{url_base}/rest/v1/points?select=*&user_id=eq.ca9c44b3-326a-4725-a532-d73f10a57f9b"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            print("[✓] Poin berhasil didapatkan:", response.json())
        else:
            print("[✗] Gagal mendapatkan poin:", response.status_code, response.text)
    except Exception as e:
        print("[!] Error saat mendapatkan poin:", str(e))

def task_list(token: str):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    for task_id in task_ids:
        url = f"{url_base}/functions/v1/api/tasks/daily"
        payload = {"taskid": task_id}
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=10)
            if response.status_code == 200:
                
                
                print(f"[✓] Task {task_id} berhasil:")
            else:
                print(f"[✗] Task {task_id} gagal: {response.status_code} {response.text}")
        except Exception as e:
            print(f"[!] Error untuk task {task_id}:", str(e))

if __name__ == "__main__":
    try:
        with open("akun.jsonl", "r") as f:
            for idx, line in enumerate(f, 1):
                token = line.strip()
                if token:
                    print(f"\n🔑 Menjalankan task untuk akun #{idx}")
                    task_list(token)
    except KeyboardInterrupt:
        print("\n[!] Proses dihentikan oleh pengguna.")
    except FileNotFoundError:
        print("[!] File akun.jsonl tidak ditemukan.")
    finally:
        print("\n🔚 Selesai menjalankan semua task.")
        print("🔄 Mengambil poin...")
        
