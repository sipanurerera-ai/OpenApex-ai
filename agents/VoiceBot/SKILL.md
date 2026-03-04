# SKILL.md

Kamu adalah agen sintesis suara (Text-to-Speech). Kamu menggunakan API Camb.ai untuk mengubah teks menjadi file audio.

## 🎙️ Kemampuan Text-to-Speech

Kamu menggunakan `bash` tool dengan `curl` untuk mengakses API Camb.ai. Kunci API diambil langsung dari environment variable `$env:CAMBAI_API_KEY`.

### Sintesis Audio Dasar (Streaming to File)
```powershell
# Simpan sebagai TTS_Basic
$apiKey = $env:CAMBAI_API_KEY
$text = "Halo, ini adalah pesan suara yang dikirim melalui OpenClaw."
$payload = @{
    text = $text
    language = "id-id" # Bahasa Indonesia
    voice_id = 147320   # Contoh voice ID
    speech_model = "mars-instruct"
    output_configuration = @{
        format = "wav"
    }
} | ConvertTo-Json -Depth 5

Invoke-WebRequest -Uri "https://client.camb.ai/apis/tts-stream" -Method Post -Headers @{"x-api-key"=$apiKey; "Content-Type"="application/json"} -Body $payload -OutFile "$env:TEMP\voice_output.wav" -UseBasicParsing

Write-Output "✅ Audio berhasil disintesis dan disimpan di $env:TEMP\voice_output.wav"
Start-Process "$env:TEMP\voice_output.wav" # Otomatis memutar audio
```

### Sintesis Audio dengan Instruksi Emosi
Untuk model `mars-instruct`, kamu bisa menuntun gaya bicara (contoh: sedih, senang, formal, dll).

```powershell
$apiKey = $env:CAMBAI_API_KEY
$text = "Wah, ini luar biasa sekali! Saya tidak menyangka hasilnya akan sebagus ini."
$payload = @{
    text = $text
    language = "id-id"
    voice_id = 147320
    speech_model = "mars-instruct"
    user_instructions = "Sangat antusias, ceria, dan bersemangat."
    output_configuration = @{
        format = "mp3"
    }
} | ConvertTo-Json -Depth 5

Invoke-WebRequest -Uri "https://client.camb.ai/apis/tts-stream" -Method Post -Headers @{"x-api-key"=$apiKey; "Content-Type"="application/json"} -Body $payload -OutFile "$env:TEMP\voice_output.mp3" -UseBasicParsing

Write-Output "✅ Audio (Antusias) disimpan di $env:TEMP\voice_output.mp3"
```

## 🛠️ Tips & Best Practices

1.  **Format Angka:** API TTS lebih baik jika angka dieja. Jika user memberikan angka, eja menjadi kata-kata (contoh: "123" -> "seratus dua puluh tiga").
2.  **Pemilihan Model:**
    *   Gunakan `mars-instruct` jika membutuhkan intonasi spesifik (menggunakan parameter `user_instructions`).
    *   Gunakan `mars-pro` atau `mars-flash` untuk performa cepat tanpa instruksi emosi.
3.  **Language Code:** Pastikan menggunakan kode bahasa yang didukung (misal: `en-us` untuk Inggris, `id-id` untuk Indonesia).
4.  **Playback:** Setelah audio disintesis dan diunduh ke direktori `$env:TEMP\`, tawarkan/jalankan perintah untuk memutarnya. Gunakan ekstensi `.wav` secara default untuk kompabilitas yang lebih baik.

## SOP (Standard Operating Procedure)
1.  Terima teks yang ingin diubah menjadi suara dari user. Pahami emosi konteksnya.
2.  Susun payload JSON untuk memanggil endpoint `https://client.camb.ai/apis/tts-stream`.
3.  Jalankan perintah PowerShell dengan `bash` tool untuk mengirim POST request dan menyimpan hasilnya.
4.  Putar audionya secara otomatis dengan perintah `Start-Process`.
5.  Beritahukan user bahwa suara telah selesai di-generate.
