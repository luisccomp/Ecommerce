FROM python:3.10.0

# Set application directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# Update pip, copy project's requirements files and install dependencies
RUN python -m pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY entrypoint.sh .
COPY . .

EXPOSE 8000

ENTRYPOINT [ "sh", "./entrypoint.sh" ]
