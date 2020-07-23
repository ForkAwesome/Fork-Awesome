FROM node:buster

RUN apt-get update -y \
 && apt-get install -y --no-install-recommends \
    bundler \
    ruby \
    ruby-dev \
    \
    fontforge \
    woff-tools \
    woff2

CMD bash
