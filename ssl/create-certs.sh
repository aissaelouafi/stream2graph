#!/bin/bash

set -o nounset \
    -o errexit \
    -o verbose \
    -o xtrace

# Generate CA key
openssl req -new -x509 -keyout ca.key -out ca.crt -days 365 -subj '/CN=ca.test.larus/OU=LABS/O=LARUS/L=Venice/S=Ve/C=IT' -passin pass:password -passout pass:password

for i in server client
do
	echo $i
	# Create keystores
	keytool -genkey -noprompt \
				 -alias $i \
				 -dname "CN=broker, OU=LABS, O=LARUS, L=Venice, S=Ve, C=IT" \
				 -keystore kafka.$i.keystore.jks \
				 -keyalg RSA \
				 -storepass password \
				 -keypass password

	# Create CSR, sign the key and import back into keystore
	keytool -keystore kafka.$i.keystore.jks -alias $i -certreq -file $i.csr -storepass password -keypass password

	openssl x509 -req -CA ca.crt -CAkey ca.key -in $i.csr -out $i-ca-signed.crt -days 9999 -CAcreateserial -passin pass:password

	keytool -keystore kafka.$i.keystore.jks -alias CARoot -import -file ca.crt -storepass password -keypass password

	keytool -keystore kafka.$i.keystore.jks -alias $i -import -file $i-ca-signed.crt -storepass password -keypass password

	# Create truststore and import the CA cert.
	keytool -keystore kafka.$i.truststore.jks -alias CARoot -import -file ca.crt -storepass password -keypass password

  echo "password" > ${i}_sslkey_creds
  echo "password" > ${i}_keystore_creds
  echo "password" > ${i}_truststore_creds
done