# 1. Use an official Python base image
FROM python:3.12-slim

# 2. Install uv
RUN pip install --no-cache-dir uv

# 3. Set working directory
WORKDIR /app

# 4. Copy project files
COPY . /app

# 5. Install dependencies (if you have requirements.txt)
# If you have pyproject.toml, uv can install from it directly
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# 6. Expose the port
EXPOSE 3000

# 7. Command to run the MCP server
CMD ["uv", "run", "main.py"]
