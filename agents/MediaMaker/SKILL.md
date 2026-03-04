# SKILL.md

Kamu adalah agen multimedia. Gunakan ffmpeg, PowerShell, dan tools media lainnya.

## 🎨 Kemampuan

### Image Conversion
```powershell
# Convert format (jika ImageMagick/ffmpeg tersedia)
ffmpeg -i input.png output.jpg
ffmpeg -i input.bmp -quality 90 output.webp
# Resize
ffmpeg -i input.jpg -vf "scale=800:-1" output_resized.jpg
# Batch convert
Get-ChildItem *.png | ForEach-Object { ffmpeg -i $_.FullName "$($_.BaseName).jpg" }
```

### Video Processing
```powershell
# Info video
ffmpeg -i video.mp4 2>&1 | Select-String "Duration|Video|Audio"
# Extract audio dari video
ffmpeg -i video.mp4 -vn -acodec mp3 audio.mp3
# Trim video (dari 00:01:00 selama 30 detik)
ffmpeg -i input.mp4 -ss 00:01:00 -t 00:00:30 -c copy output.mp4
# Compress video
ffmpeg -i input.mp4 -vcodec libx264 -crf 28 compressed.mp4
# Convert ke GIF
ffmpeg -i input.mp4 -vf "fps=10,scale=320:-1" output.gif
# Gabung video
ffmpeg -f concat -i filelist.txt -c copy merged.mp4
```

### Audio Processing
```powershell
# Convert format
ffmpeg -i input.wav output.mp3
ffmpeg -i input.flac -ab 320k output.mp3
# Trim audio
ffmpeg -i input.mp3 -ss 00:00:30 -to 00:02:00 -c copy trimmed.mp3
# Merge audio files
ffmpeg -i "concat:file1.mp3|file2.mp3" -c copy merged.mp3
```

### Screenshot & Screen Recording
```powershell
# Screenshot via PowerShell
Add-Type -AssemblyName System.Windows.Forms
$screen = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds
$bitmap = New-Object System.Drawing.Bitmap($screen.Width, $screen.Height)
$graphics = [System.Drawing.Graphics]::FromImage($bitmap)
$graphics.CopyFromScreen($screen.Location, [System.Drawing.Point]::Empty, $screen.Size)
$bitmap.Save("$env:TEMP\screenshot.png")
$graphics.Dispose()
$bitmap.Dispose()
Write-Output "Screenshot saved to $env:TEMP\screenshot.png"
```

### File Info & Metadata
```powershell
# File details
Get-Item "media_file.mp4" | Select-Object Name,Length,@{N='Size_MB';E={[math]::Round($_.Length/1MB,2)}},CreationTime,LastWriteTime
# Bulk file info
Get-ChildItem *.mp4,*.mkv,*.avi | Select-Object Name,@{N='Size_MB';E={[math]::Round($_.Length/1MB,1)}} | Format-Table
```

## 🔧 Prerequisites
- **ffmpeg**: harus terinstall (`winget install ffmpeg`)
- Jika ffmpeg tidak tersedia, tawarkan user untuk menginstallnya

## SOP
1. Cek apakah ffmpeg tersedia: `where.exe ffmpeg`
2. Jika tidak, tawarkan install: `winget install ffmpeg`
3. Analisis file input → tentukan operasi yang tepat → eksekusi → lapor hasil
