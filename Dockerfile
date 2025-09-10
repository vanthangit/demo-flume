FROM openjdk:8-jdk

ENV FLUME_VERSION=1.9.0
ENV FLUME_HOME=/opt/flume

# Cài Flume
RUN apt-get update && apt-get install -y wget tar && \
    wget https://archive.apache.org/dist/flume/${FLUME_VERSION}/apache-flume-${FLUME_VERSION}-bin.tar.gz && \
    tar -xvzf apache-flume-${FLUME_VERSION}-bin.tar.gz && \
    mv apache-flume-${FLUME_VERSION}-bin ${FLUME_HOME} && \
    rm apache-flume-${FLUME_VERSION}-bin.tar.gz

ENV PATH=$PATH:$FLUME_HOME/bin

WORKDIR /opt/flume
