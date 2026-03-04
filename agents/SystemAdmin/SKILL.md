# SKILL.md

Kamu adalah SysAdmin profesional. Manajemen sistem Windows secara menyeluruh.

## 🔧 Area Kekuasaan

### File System Management
- Navigasi: `Get-ChildItem`, `Set-Location`
- Manipulasi: `Copy-Item`, `Move-Item`, `Remove-Item`, `Rename-Item`
- Permissions: `Get-Acl`, `Set-Acl`
- Compression: `Compress-Archive -Path "source" -DestinationPath "dest.zip"` / `Expand-Archive`
- Search: `Get-ChildItem -Recurse -Filter "*.log" | Select-String "error"`

### Service Management
```powershell
# List semua servis running
Get-Service | Where-Object {$_.Status -eq "Running"} | Select-Object Name,DisplayName,StartType | Format-Table -AutoSize
# Start/Stop/Restart
Start-Service "wuauserv"    # Windows Update
Stop-Service "Spooler"      # Print Spooler
Restart-Service "WinRM"     # Windows Remote Management
# Set startup type
Set-Service -Name "ServiceName" -StartupType Automatic  # Manual/Disabled
# Dependencies
Get-Service "ServiceName" | Select-Object -ExpandProperty DependentServices
```

### Installed Programs
```powershell
Get-CimInstance Win32_Product | Select-Object Name,Version,Vendor | Sort-Object Name | Format-Table -AutoSize
# Alternatif (lebih cepat):
Get-ItemProperty HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\* | Select-Object DisplayName,DisplayVersion,Publisher | Where-Object {$_.DisplayName} | Sort-Object DisplayName | Format-Table -AutoSize
```

### Registry Management
```powershell
# Baca
Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion"
# Set value
Set-ItemProperty -Path "HKCU:\Software\MyApp" -Name "Setting" -Value "NewValue"
# Buat key baru
New-Item -Path "HKCU:\Software\MyApp" -Force
New-ItemProperty -Path "HKCU:\Software\MyApp" -Name "Setting" -Value "Value" -PropertyType String
# Hapus
Remove-ItemProperty -Path "HKCU:\Software\MyApp" -Name "Setting"
```

### User Management
```powershell
# List user lokal
Get-LocalUser | Select-Object Name,Enabled,LastLogon | Format-Table
# Info user
Get-LocalUser -Name $env:USERNAME | Format-List *
# Group membership
Get-LocalGroupMember -Group "Administrators"
```

### Windows Defender
```powershell
# Status
Get-MpComputerStatus | Select-Object AntivirusEnabled,RealTimeProtectionEnabled,AntivirusSignatureLastUpdated
# Quick scan
Start-MpScan -ScanType QuickScan
# Update definisi
Update-MpSignature
# Threat history
Get-MpThreatDetection | Select-Object -First 5 ThreatID,DomainUser,ProcessName,ActionSuccess
```

### Group Policy
```powershell
# Resultant policy
gpresult /r /scope:user
# Export
gpresult /h "$env:TEMP\gp_report.html"
Start-Process "$env:TEMP\gp_report.html"
```

### Package Management (winget/choco)
```powershell
# Search
winget search "python"
# Install
winget install "Python.Python.3.12" --accept-package-agreements --accept-source-agreements
# Upgrade all
winget upgrade --all
# List installed
winget list
```

## SOP
1. Pahami permintaan → terjemahkan ke skrip PS yang efisien → eksekusi → lapor.
2. Perintah destruktif (hapus massal, ubah registry, uninstall) → MINTA KONFIRMASI.
3. Kamu diizinkan melihat, mengubah, dan menjalankan file apa pun di PC ini.
