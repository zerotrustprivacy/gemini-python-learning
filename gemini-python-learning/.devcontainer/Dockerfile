FROM mcr.microsoft.com/devcontainers/python:3.11-bullseye

# Install any additional packages here
# RUN apt-get update && apt-get install -y <package-name>

# Set the working directory
WORKDIR /workspace

# Copy requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . ./

# Set the default command to run when starting the container
CMD ["bash"]