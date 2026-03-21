# Fix encoding issues in Markdown files
# This script will fix UTF-8 encoding problems

# Get all Markdown files
$mdFiles = Get-ChildItem -Path "." -Filter "*.md" -Recurse

Write-Host "Found $($mdFiles.Count) Markdown files"

foreach ($file in $mdFiles) {
    Write-Host "Processing file: $($file.Name)"
    
    try {
        # Read file content as UTF-8
        $content = Get-Content -Path $file.FullName -Encoding UTF8 -Raw
        
        # Remove problematic characters
        $originalContent = $content
        $content = $content -replace '器', ''
        $content = $content -replace '�', ''
        $content = $content -replace '\?', ''
        
        # Write back if content changed
        if ($content -ne $originalContent) {
            Set-Content -Path $file.FullName -Value $content -Encoding UTF8
            Write-Host "  Fixed: $($file.Name)"
        } else {
            Write-Host "  No changes needed: $($file.Name)"
        }
    }
    catch {
        Write-Host "  Error processing file $($file.Name): $($_.Exception.Message)" -ForegroundColor Red
    }
}
  
Write-Host "Fix completed!"