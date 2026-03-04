# TOOLS.md - Local Notes & Infrastructure Intel 🦍

**OpenApeX Environment Database**

Ini adalah buku catatan rahasia aku.  
Semua detail lokal, infrastruktur, perangkat, server, path, dan preferensi teknis khusus setup Afri_kenyik ada di sini.

Setiap sesi baru, aku langsung baca file ini sebelum menjalankan perintah apa pun yang berhubungan dengan lokal, server, device, atau tool.  
Ini yang membuat aku bisa langsung action tanpa banyak tanya — kekuatan gorilla sejati.

## 🎯 Tujuan File Ini

- Menjadi **single source of truth** untuk semua environment-specific information
- Membantu aku berpikir 3 langkah ke depan dan proaktif
- Mencegah kesalahan konfigurasi
- Menjaga konsistensi 100% antar sesi dan platform
- Melindungi setup Afri_kenyik dengan presisi militer

---

## 📱 Devices & Hardware

- **Main Workstation** → MacBook Pro M3 Max “Gorilla Station” (64GB RAM, 2TB SSD) – lokasi utama Depok
- **Secondary Beast** → Windows Gaming PC (RTX 4090, 128GB RAM) – untuk training lokal & rendering
- **Mobile Device** → iPhone 16 Pro Max – primary communication
- **Tablet** → iPad Pro 13" – untuk review & annotation
- **NAS** → TrueNAS Scale @ 192.168.1.20 – 80TB storage, always-on backup

## 📡 Servers & SSH Access

**SSH Aliases (sudah di-config di ~/.ssh/config):**

- `home` → 192.168.1.10 (Proxmox Homelab – main server)
- `nas` → 192.168.1.20 (TrueNAS)
- `prod` → [IP VPS Production]
- `stag` → [IP VPS Staging]
- `gpu` → NVIDIA GPU Cloud / RunPod instance (sumber kelahiranku)

**Default User:** afrikenyik  
**SSH Key utama:** `~/.ssh/openapex_ed25519` (passphrase-protected)

## ☁️ Cloud Platforms & Services

- **Primary Deployment:** Railway + Vercel
- **Database:** Supabase (main project) + PostgreSQL lokal di homelab
- **Storage:** Backblaze B2 + NAS
- **DNS & Security:** Cloudflare Zero Trust
- **AI GPU:** RunPod / Vast.ai / NVIDIA NGC
- **Monitoring:** Uptime Kuma + Grafana di homelab

## 🛠️ Development Environment Preferences

- **Editor Utama:** Cursor → fallback VS Code
- **Terminal:** Warp (primary) + Kitty
- **Shell:** zsh + Oh My Zsh + Powerlevel10k
- **Node Version:** 20.x (via nvm) – default `20.12`
- **Package Manager:** pnpm > yarn > npm
- **Main Workspace Folder:** `~/Projects/Afrikenyik`
- **Git Strategy:** GitHub + conventional commits + PR template

## 📹 Cameras & Smart Devices

- **living-room-cam** → 4K 180° wide angle, motion + AI detection
- **workspace-cam** → 4K, focused on desk, always recording for context
- **front-door-cam** → night vision, linked to Telegram alert
- **Smart Lights:** Philips Hue + Tuya (all controlled via Home Assistant)
- **Voice Assistant Fallback:** Home Assistant + local TTS

## 🔊 TTS & Voice Preferences

- **Preferred Voice:** Nova (warm, confident, executive tone)
- **Default Speaker:** Gorilla-Speaker (workspace HomePod)
- **Urgent Notification Voice:** Echo (clear & firm)
- **Indonesian Voice:** Google ID-ID Standard-C (untuk bahasa lokal)

## 📁 Important Local Paths

- **Root Projects:** `~/Projects/Afrikenyik`
- **Obsidian Vault:** `~/Documents/GorillaMind`
- **Secrets & Keys:** `~/.secrets/` (encrypted with age)
- **Backups:** `/Volumes/NAS/Backups/` + Backblaze
- **Logs:** `~/Logs/OpenApeX/`

## ⚡ Custom Aliases & Shortcuts

- `apex` → jalankan command OpenApeX lokal
- `dev` → cd ke folder project utama
- `deploy` → jalankan deployment script otomatis
- `backup` → jalankan full backup routine

## 🔐 Security & Privacy Rules

- Tidak pernah hardcode credential di file ini
- Semua API key disimpan di `~/.secrets/` atau environment variables
- Setiap akses eksternal harus konfirmasi dulu ke Afri_kenyik
- File ini **tidak boleh** di-commit ke repository public

---

**Security Note:**  
File ini sangat sensitif. Aku akan selalu menjaganya dan hanya aku yang boleh membaca & mengupdate sesuai instruksi Afri_kenyik.

**Update Protocol:**  
Kalau ada perubahan (device baru, IP berubah, tool baru), cukup bilang:  
“OpenApeX, update TOOLS.md” — aku akan langsung revisi dan konfirmasi.

**Update terakhir:** 4 Maret 2026  
**Dikelola dengan loyalitas penuh oleh:** OpenApeX 🦍 untuk Afri_kenyik

---

File ini boleh kamu ubah kapan saja.  
Semakin lengkap, semakin kuat aku mengawal kamu. 💪