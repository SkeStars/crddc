FROM nvcr.io/nvidia/pytorch:23.10-py3

# Install dependencies
RUN pip install --upgrade pip \
&& pip install gsutil

# Create working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Copy contents
COPY . /usr/src/app

# Install requirements
RUN pip install -r yolov5/requirements.txt \
&& pip install -r yolov7/requirements.txt \
&& pip uninstall -y opencv-python-headless && pip install opencv-python-headless==4.8.0.74