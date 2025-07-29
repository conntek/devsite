# Scheduled file monitoring script
# 定期监控文件大小变化的脚本

param(
    [int]$IntervalMinutes = 30,  # 监控间隔（分钟）
    [int]$ThresholdKB = 10,      # 异常文件大小阈值（KB）
    [string]$LogFile = "file_monitor.log"  # 日志文件
)

# 创建日志函数
function Write-Log {
    param([string]$Message, [string]$Level = "INFO")
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $logEntry = "[$timestamp] [$Level] $Message"
    Write-Host $logEntry
    Add-Content -Path $LogFile -Value $logEntry
}

# 检查文件大小变化
function Check-FileSizeChanges {
    Write-Log "Starting file size check..."
    
    # 运行监控脚本并捕获输出
    $output = & ".\monitor_files.ps1" -Path "./docs" -ThresholdKB $ThresholdKB
    
    # 检查是否有异常文件
    if ($output -match "WARNING: Large files found:") {
        Write-Log "Large files detected!" "WARNING"
        
        # 提取异常文件信息
        $largeFiles = $output | Select-String "Path: .*\.md" | ForEach-Object {
            $_.Line -replace ".*Path: ", ""
        }
        
        foreach ($file in $largeFiles) {
            Write-Log "Large file: $file" "WARNING"
        }
        
        # 可选：发送通知（需要配置邮件或其他通知方式）
        # Send-Notification "File size anomaly detected"
        
    } else {
        Write-Log "All files are normal size"
    }
}

# 主监控循环
Write-Log "File monitor started. Interval: $IntervalMinutes minutes, Threshold: ${ThresholdKB}KB"
Write-Log "Press Ctrl+C to stop monitoring"

try {
    while ($true) {
        Check-FileSizeChanges
        Write-Log "Waiting $IntervalMinutes minutes for next check..."
        Start-Sleep -Seconds ($IntervalMinutes * 60)
    }
} catch {
    Write-Log "Monitor stopped: $($_.Exception.Message)" "ERROR"
} finally {
    Write-Log "File monitor ended"
}

<#
使用方法：
1. 默认监控（30分钟间隔，10KB阈值）：
   .\monitor_schedule.ps1

2. 自定义间隔和阈值：
   .\monitor_schedule.ps1 -IntervalMinutes 15 -ThresholdKB 8

3. 后台运行：
   Start-Job -ScriptBlock { .\monitor_schedule.ps1 }

4. 查看日志：
   Get-Content file_monitor.log -Tail 20
#>