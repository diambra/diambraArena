ARG BASE_IMAGE=diambra/base:latest
FROM $BASE_IMAGE

RUN apt-get -qy update && \
    apt-get -qy install python3-tk wget libqt5core5a libqt5widgets5 libqt5gui5 libsdl2-2.0-0 libsdl2-ttf-2.0-0
