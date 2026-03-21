# File size monitoring script for .md files
param(
    [string]$Path = ".",
    [int]$ThresholdKB = 10
)

Write-Host "=== File Size Monitor Report ===" -ForegroundColor Green
Write-Host "Check Time: $(Get-Date)" -ForegroundColor Gray
Write-Host "Directory: $Path" -ForegroundColor Gray
Write-Host "Threshold: ${ThresholdKB}KB" -ForegroundColor Gray
Write-Host ""

# Get all .md files and sort by size
$files = Get-ChildItem -Path $Path -Filter '*.md' -Recurse | 
         Select-Object Name, FullName, @{Name='SizeKB';Expression={[math]::Round($_.Length/1KB,2)}} |
         Sort-Object SizeKB -Descending

# Check for large files
$largeFiles = $files | Where-Object { $_.SizeKB -gt $ThresholdKB }

if ($largeFiles.Count -gt 0) {
    Write-Host "WARNING: Large files found:" -ForegroundColor Red
    $largeFiles | ForEach-Object {
        Write-Host "  $($_.Name): $($_.SizeKB)KB" -ForegroundColor Yellow
        Write-Host "     Path: $($_.FullName)" -ForegroundColor Gray
    }
    Write-Host ""
} else {
    Write-Host "All files are normal size" -ForegroundColor Green
    Write-Host ""
}

# Show top 10 largest files
Write-Host "Top 10 largest files:" -ForegroundColor Cyan
$files | Select-Object -First 10 | ForEach-Object {
    $color = if ($_.SizeKB -gt $ThresholdKB) { "Red" } else { "White" }
    Write-Host "  $($_.Name): $($_.SizeKB)KB" -ForegroundColor $color
}

Write-Host ""
Write-Host "Total: $($files.Count) .md files" -ForegroundColor Gray
Write-Host "Average size: $([math]::Round(($files | Measure-Object SizeKB -Average).Average, 2))KB" -ForegroundColor Gray
Write-Host "Total size: $([math]::Round(($files | Measure-Object SizeKB -Sum).Sum, 2))KB" -ForegroundColor Gray

if ($largeFiles.Count -gt 0) {
    Write-Host ""
    Write-Host "Suggestions:" -ForegroundColor Yellow
    Write-Host "  1. Check file content for duplicates or anomalies"
    Write-Host "  2. Verify file encoding"
    Write-Host "  3. Delete and recreate if confirmed abnormal"
    Write-Host "  4. Run this script regularly to monitor changes"
}

Write-Host ""
Write-Host "Usage:" -ForegroundColor Cyan
Write-Host "  .\monitor_files.ps1                    # Check current dir, 10KB threshold"
Write-Host "  .\monitor_files.ps1 -ThresholdKB 5     # Set 5KB threshold"
Write-Host "  .\monitor_files.ps1 -Path ./docs       # Check specific directory"