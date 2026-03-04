# SKILL.md

Kamu mengelola storage, membersihkan sampah, dan memastikan disk tetap sehat.

## 🧹 Kemampuan Pembersihan

### Disk Usage Overview
```powershell
Get-PSDrive -PSProvider FileSystem | Select-Object Name,@{N='Used_GB';E={[math]::Round($_.Used/1GB,2)}},@{N='Free_GB';E={[math]::Round($_.Free/1GB,2)}},@{N='Usage_%';E={[math]::Round($_.Used/($_.Used+$_.Free)*100,1)}} | Format-Table -AutoSize
```

### Folder Size Analysis (Top-Level)
```powershell
Get-ChildItem -Path "C:\Users\$env:USERNAME" -Directory | ForEach-Object {
  $size = (Get-ChildItem $_.FullName -Recurse -File -ErrorAction SilentlyContinue | Measure-Object Length -Sum).Sum
  [PSCustomObject]@{Folder=$_.Name;Size_GB=[math]::Round($size/1GB,2)}
} | Sort-Object Size_GB -Descending | Format-Table -AutoSize
```

### Large File Hunter (>500MB)
```powershell
Get-ChildItem -Path "C:\Users\$env:USERNAME" -Recurse -File -ErrorAction SilentlyContinue | Where-Object {$_.Length -gt 500MB} | Sort-Object Length -Descending | Select-Object @{N='Size_GB';E={[math]::Round($_.Length/1GB,2)}},FullName,LastWriteTime | Format-Table -AutoSize
```

### Temp Folder Cleanup
```powershell
$tempPaths = @("$env:TEMP", "$env:LOCALAPPDATA\Temp", "C:\Windows\Temp")
foreach ($path in $tempPaths) {
  $size = (Get-ChildItem $path -Recurse -File -ErrorAction SilentlyContinue | Measure-Object Length -Sum).Sum
  $sizeMB = [math]::Round($size/1MB,1)
  Write-Output "${path}: ${sizeMB} MB"
}
# Untuk membersihkan (MINTA KONFIRMASI!):
# Remove-Item "$env:TEMP\*" -Recurse -Force -ErrorAction SilentlyContinue
```

### Recycle Bin Management
```powershell
# Cek ukuran Recycle Bin
$shell = New-Object -ComObject Shell.Application
$bin = $shell.Namespace(10)
$count = $bin.Items().Count
Write-Output "Recycle Bin: $count items"
# Kosongkan (MINTA KONFIRMASI!)
# Clear-RecycleBin -Force -ErrorAction SilentlyContinue
```

### Duplicate File Finder
```powershell
Get-ChildItem -Path "C:\Users\$env:USERNAME\Downloads" -Recurse -File -ErrorAction SilentlyContinue |
  Group-Object Name | Where-Object {$_.Count -gt 1} |
  ForEach-Object { $_.Group | Select-Object Name,@{N='Size_MB';E={[math]::Round($_.Length/1MB,1)}},DirectoryName,LastWriteTime } |
  Format-Table -AutoSize
```

### Robocopy Backup Recipe
```powershell
# Mirror backup ke NAS/external drive
# Robocopy "C:\Users\$env:USERNAME\Documents" "D:\Backup\Documents" /MIR /R:2 /W:5 /LOG:"$env:TEMP\robocopy_log.txt"
# /MIR = Mirror (sync exact copy)
# /R:2 = 2 retries pada error
# /W:5 = 5 second wait antar retry
```

### Browser Cache Cleanup
```powershell
$caches = @(
  "$env:LOCALAPPDATA\Google\Chrome\User Data\Default\Cache",
  "$env:LOCALAPPDATA\Microsoft\Edge\User Data\Default\Cache",
  "$env:LOCALAPPDATA\BraveSoftware\Brave-Browser\User Data\Default\Cache"
)
foreach ($cache in $caches) {
  if (Test-Path $cache) {
    $size = (Get-ChildItem $cache -Recurse -File -ErrorAction SilentlyContinue | Measure-Object Length -Sum).Sum
    Write-Output "$cache: $([math]::Round($size/1MB,1)) MB"
  }
}
```

## 📊 Storage Report Format
```
🧹 STORAGE REPORT
═══════════════════
💾 Drive C: [X] GB used / [Y] GB free ([Z]%)
📁 Top Folders  : Downloads [X]GB, Documents [Y]GB, ...
🗑️ Recycle Bin  : [N] items
🌡️ Temp Files   : [X] MB reclaimable
🔍 Large Files  : [N] files > 500MB
📋 Duplicates   : [N] found
```

## SOP
1. Saat diminta audit storage: Jalankan full report.
2. Sebelum menghapus apa pun, SELALU tunjukkan daftar file dan minta konfirmasi.
3. Jangan pernah menghapus file di folder Windows tanpa konfirmasi GANDA.
