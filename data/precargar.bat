@echo off
curl -X POST http://localhost:11434/api/generate ^
 -H "Content-Type: application/json" ^
 -d "{\"model\": \"mantenimiento-phi\", \"prompt\": \"ping\", \"stream\": false}"
pause
