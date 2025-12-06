#!/bin/bash

# Function to kill background processes on exit
cleanup() {
    echo "Stopping servers..."
    kill $BACKEND_PID
    kill $FRONTEND_PID
    exit
}

trap cleanup SIGINT

echo "Starting Backend (FastAPI)..."
python src/api.py &
BACKEND_PID=$!

echo "Starting Frontend (Vite)..."
cd web_ui
npm run dev &
FRONTEND_PID=$!

echo "Servers are running!"
echo "Backend: http://localhost:8000"
echo "Frontend: http://localhost:5173"

wait
