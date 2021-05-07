#!/bin/bash

# Cache sudo password
sudo -v

# Get latest OpenSSL 1.0.2 version from https://openssl.org/source/
# v1.1.0 seems to have removed SSLv2/3 support
openssl_version=1.0.2k

# Install build dependencies
sudo apt -y install build-essential

# Build OpenSSL
wget https://openssl.org/source/openssl-$openssl_version.tar.gz
tar -xvf openssl-$openssl_version.tar.gz
cd openssl-$openssl_version
# --prefix will make sure that make install copies the files locally instead of system-wide
# --openssldir will make sure that the binary will look in the regular system location for openssl.cnf
# no-shared builds a mostly static binary
./config --prefix=`pwd`/local --openssldir=/usr/lib/ssl enable-ssl2 enable-ssl3 no-shared
make depend
make
# -i continues on errors, since make install may try to put some files in /usr/lib/ssl, which we don't want
make -i install