SCHNITZEL_DIR=/path/to/SchnitzelBot 
alias schnitzel-build="cd $SCHNITZEL_DIR && sudo docker build -t schnitzel:latest ."
alias schnitzel-start="cd $SCHNITZEL_DIR && sudo docker compose up -d"
alias schnitzel-stop="cd $SCHNITZEL_DIR && sudo docker compose down && docker rm discord-bot"
