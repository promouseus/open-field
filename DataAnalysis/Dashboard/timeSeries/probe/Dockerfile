FROM python:latest
# Alphine not working with redisTS module compilation, seems related to wheel group
WORKDIR /opt
RUN /usr/local/bin/pip install --no-cache-dir redistimeseries
ADD probe.py .
RUN /bin/chmod +x *.py
CMD ["python", "./probe.py"]
