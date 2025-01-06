# Use an official PHP CLI base image
# quick test
FROM php:8.1-cli

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    zip \
    unzip

# Install Composer
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
    && php composer-setup.php --install-dir=/usr/local/bin --filename=composer \
    && php -r "unlink('composer-setup.php');"

# Create a working directory
WORKDIR /var/www

# Create a new Laravel project named "test-laravel"
RUN composer create-project --prefer-dist laravel/laravel test-laravel

# Switch into the new app directory
WORKDIR /var/www/test-laravel

# Expose port 8000 for the built-in PHP server
EXPOSE 8000

# Start the built-in Laravel development server
CMD [ "php", "artisan", "serve", "--host=0.0.0.0", "--port=8000" ]