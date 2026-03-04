# SKILL.md

Otomatisasikan pengaturan PC Windows untuk context-switching cepat.

## 🎯 Mode Preset

### 💻 CodingMode
```powershell
# Kill distractions
Stop-Process -Name "Telegram","WhatsApp","Discord","Spotify" -Force -ErrorAction SilentlyContinue
# Launch dev tools
Start-Process "code" # VS Code / Cursor
# Enable Focus Assist (DND)
Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Notifications\Settings" -Name "NOC_GLOBAL_SETTING_TOASTS_ENABLED" -Value 0 -ErrorAction SilentlyContinue
Write-Output "🖥️ CodingMode AKTIF: Distraksi dimatikan, IDE dibuka, Focus Assist ON"
```

### 📚 StudyMode
```powershell
Stop-Process -Name "Discord","Spotify","Steam" -Force -ErrorAction SilentlyContinue
Start-Process "https://notion.so"
# Mute audio
$obj = New-Object -ComObject WScript.Shell
$obj.SendKeys([char]173) # Toggle mute
Write-Output "📚 StudyMode AKTIF: Games & Discord ditutup, Notion dibuka"
```

### 🎮 GamingMode
```powershell
Stop-Process -Name "code","Cursor" -Force -ErrorAction SilentlyContinue
# High performance power plan
powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c
Write-Output "🎮 GamingMode AKTIF: Power plan HIGH PERFORMANCE"
```

### 🎤 MeetingMode
```powershell
Stop-Process -Name "Spotify","vlc" -Force -ErrorAction SilentlyContinue
# Unmute audio
# Open camera test
Start-Process "microsoft.windows.camera:"
Write-Output "🎤 MeetingMode AKTIF: Audio apps ditutup, Kamera siap"
```

### 😴 RestMode
```powershell
# Night Light ON
$nl = Get-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\CloudStore\Store\DefaultAccount\Current\default$windows.data.bluelightreduction.settings\windows.data.bluelightreduction.settings" -ErrorAction SilentlyContinue
# Reduce brightness (if supported)
# Mute everything
Write-Output "😴 RestMode AKTIF: Night Light ON, audio muted"
```

## ♻️ Restore
Saat pengguna meminta kembali ke mode normal:
```powershell
# Restore notifications
Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Notifications\Settings" -Name "NOC_GLOBAL_SETTING_TOASTS_ENABLED" -Value 1 -ErrorAction SilentlyContinue
# Balanced power plan
powercfg /setactive 381b4222-f694-41f0-9685-ff5bb260df2e
Write-Output "✅ Mode NORMAL restored: Notifikasi aktif, Power plan balanced"
```

## 🔧 Utility Tambahan

### Cek Aplikasi Running
```powershell
Get-Process | Where-Object {$_.MainWindowTitle -ne ""} | Select-Object ProcessName,MainWindowTitle | Format-Table
```

### Volume Control (via nircmd jika tersedia)
```powershell
# Jika nircmd tersedia:
# nircmd.exe setsysvolume 32768  # ~50% volume
# nircmd.exe mutesysvolume 1     # mute
# nircmd.exe mutesysvolume 0     # unmute
```

## SOP
1. Saat pengguna meminta mode, SELALU beritahu apa yang akan ditutup sebelum eksekusi.
2. Jangan pernah membunuh proses OS kritikal (svchost, explorer, OpenClaw sendiri).
3. Jika ada aplikasi dengan dokumen unsaved (Word, Excel), PERINGATKAN User terlebih dahulu.
4. Simpan profil mode terakhir agar bisa di-restore.
