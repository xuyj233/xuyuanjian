# Jekyll Server Startup Script
$env:Path += ";C:\Ruby34-x64\bin"
cd C:\Users\z\Desktop\code\acad-homepage.github.io

Write-Host "Starting Jekyll server..." -ForegroundColor Green
Write-Host "Server will be available at: http://localhost:4000" -ForegroundColor Yellow
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Cyan
Write-Host ""

bundle exec jekyll serve --host 127.0.0.1 --port 4000

