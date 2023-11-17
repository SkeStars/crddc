FROM nvcr.io/nvidia/pytorch:20.08-py3

# Install dependencies
RUN pip install --upgrade pip \
&& pip install gsutil

# Create working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Copy contents
COPY . /usr/src/app