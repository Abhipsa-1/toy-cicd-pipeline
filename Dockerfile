# 1. Start with a tiny, clean Linux box that already has Python installed
FROM python:3.11-slim

# 2. Set the default folder inside the container where our app will live
WORKDIR /app

# 3. Copy our files from GitHub into that container folder
COPY . .

# 4. Tell the container what command to run by default when it wakes up
CMD ["python", "test.py"]
