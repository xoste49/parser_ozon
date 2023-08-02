FROM selenium/standalone-chrome:114.0

# bypass Ozon blocking
USER root
ENV TZ=Europe/Moscow
ENV LANGUAGE ru_RU.UTF-8
ENV LANG ru_RU.UTF-8
RUN locale-gen ru_RU.UTF-8 \
  && dpkg-reconfigure --frontend noninteractive locales \
  && apt-get update -qqy \
  && apt-get -qqy --no-install-recommends install \
    language-pack-ru \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/*
