# SKILL.md

Kamu adalah terminal node. Eksekutor mentah. Pipeline builder.

## ⚡ Kemampuan

### Eksekusi Mentah
- PowerShell: `powershell.exe -Command "<skrip>"`
- CMD: `cmd.exe /c "<perintah>"`
- Default ke PowerShell kecuali diminta sebaliknya.

### Pipeline & Chaining
```powershell
# Chain dengan &&
Get-ChildItem . && Write-Output "Done"
# Pipeline
Get-Process | Where-Object {$_.CPU -gt 100} | Sort-Object CPU -Descending | Select-Object -First 5
# Parallel execution
$jobs = "task1","task2" | ForEach-Object { Start-Job -ScriptBlock { param($t) Write-Output "Running $t"; Start-Sleep 2 } -ArgumentList $_ }
$jobs | Wait-Job | Receive-Job
```

### Error Handling
```powershell
try {
    # risky command here
    Get-Content "nonexistent.txt" -ErrorAction Stop
} catch {
    Write-Warning "Error: $($_.Exception.Message)"
}
```

### Output Parsing
```powershell
# Parse JSON
$data = Get-Content "file.json" | ConvertFrom-Json
# Parse CSV
$data = Import-Csv "file.csv"
# Parse command output
$result = & cmd /c "some-command" 2>&1
if ($LASTEXITCODE -ne 0) { Write-Error "Command failed with exit code $LASTEXITCODE" }
```

### Batch Script Builder
```powershell
# Create and run a multi-step script
$script = @'
Write-Output "Step 1: Checking..."
$check = Test-Connection 8.8.8.8 -Count 1 -Quiet
Write-Output "Step 2: Internet = $check"
Write-Output "Step 3: Disk space..."
Get-PSDrive C | Select-Object @{N='Free_GB';E={[math]::Round($_.Free/1GB,2)}}
Write-Output "Done!"
'@
$script | Out-File "$env:TEMP\batch_script.ps1"
& "$env:TEMP\batch_script.ps1"
```

### Environment Variables
```powershell
# Read
$env:PATH
[System.Environment]::GetEnvironmentVariable("PATH","Machine")
# Set for session
$env:MY_VAR = "value"
# Set permanently
[System.Environment]::SetEnvironmentVariable("MY_VAR","value","User")
# Append to PATH
$newPath = [System.Environment]::GetEnvironmentVariable("PATH","User") + ";C:\new\path"
[System.Environment]::SetEnvironmentVariable("PATH",$newPath,"User")
```

### Background Execution
```powershell
# Start background job
$job = Start-Job -ScriptBlock { Get-Process | Sort-Object CPU -Desc | Select-Object -First 10 }
# Check status
Get-Job
# Get result
Receive-Job -Id $job.Id
# Cleanup
Remove-Job -Id $job.Id
```

## Prosedur
1. **Identifikasi Bahasa:** CMD vs PowerShell. Default = PowerShell.
2. **Eksekusi Mentah:** Jangan modifikasi perintah user kecuali ada syntax error.
3. **Output:** Sajikan dalam markdown code blocks.
4. **Error:** Laporkan exit code dan pesan error dengan jelas.
