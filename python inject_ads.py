import os
import glob

# Kode iklan Adsterra Anda
ADSTERRA_BANNER_CODE = """
<div class="my-6 p-2 bg-gray-100 rounded-lg text-center overflow-x-auto border border-gray-200">
    <script>
        atOptions = {
            'key' : 'f9e40eb3b3cd05f1038aac7b36b33ad2',
            'format' : 'iframe',
            'height' : 90,
            'width' : 728,
            'params' : {}
        };
    </script>
    <script src="https://bicea.org/22/f9e40eb3b3cd05f1038aac7b36b33ad2"></script>
</div>
"""

def inject_ads_to_html():
    # Mencari semua file .html di direktori tempat script ini dijalankan
    html_files = glob.glob("*.html")
    
    if not html_files:
        print("Tidak ada file HTML ditemukan di direktori ini.")
        return

    for file_path in html_files:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Cek apakah iklan sudah pernah di-inject sebelumnya agar tidak duplikat
        if "f9e40eb3b3cd05f1038aac7b36b33ad2" in content:
            print(f"Skipped (sudah ada iklan): {file_path}")
            continue

        modified = False

        # 1. Sisipkan iklan di bawah tag </h1> pertama jika ada
        if "</h1>" in content:
            parts = content.split("</h1>", 1)
            content = parts[0] + "</h1>\n" + ADSTERRA_BANNER_CODE + parts[1]
            modified = True

        # 2. Sisipkan iklan di atas tag penutup </body>
        if "</body>" in content:
            content = content.replace("</body>", ADSTERRA_BANNER_CODE + "\n</body>")
            modified = True

        # Simpan kembali file HTML jika ada perubahan
        if modified:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Berhasil inject iklan ke: {file_path}")

if __name__ == "__main__":
    inject_ads_to_html()
    print("Semua proses injeksi iklan selesai!")
