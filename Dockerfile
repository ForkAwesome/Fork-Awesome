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

WORKDIR /workspace
COPY Gemfile /workspace
COPY Gemfile.lock /workspace
RUN bundle install
COPY package.json /workspace
COPY package-lock.json /workspace
RUN npm ci
CMD bash
