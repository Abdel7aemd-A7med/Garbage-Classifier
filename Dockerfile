# Use an official Python image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy files into the container
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Expose the Gradio default port
EXPOSE 7860

# Run the Gradio app
CMD ["python", "app.py"]
