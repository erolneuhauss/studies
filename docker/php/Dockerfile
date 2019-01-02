FROM php:7.3-apache

RUN apt-get update && \
  apt-get install -y \
    rsync \
    openssh-client \
    git \
    libmagickwand-dev imagemagick \
    zip \
    libzip-dev \
    zlib1g-dev

RUN pecl install apcu apcu_bc imagick

RUN docker-php-ext-configure zip --with-libzip && \
  docker-php-ext-install pdo_mysql zip

RUN a2enmod rewrite expires
