# NiFi installation on Ubuntu 22

## Setup (basic)

```bash
wget https://dlcdn.apache.org/nifi/2.0.0-M1/nifi-2.0.0-M1-bin.zip -O nifi.bin.zip
unzip nifi.bin.zip

apt-get install openjdk-21-jre-headless

cd nifi-2.0.0-M1/
#bin/nifi.sh start
bin/nifi.sh install

service nifi start

# User/pass is in log file after first boot
Select-String "Gener" .\nifi-app.log
#nifi-app.log:1241:Generated Username [****]
#nifi-app.log:1242:Generated Password [****]

# Or set userpass (restart service after change)
./bin/nifi.sh set-single-user-credentials <username> <password>

certbot certonly --standalone --staging -d loom.extralo.nl --agree-tos -m input@00010110.nl --no-eff-email --key-type ecdsa
```

# File Hash Function Selection: BLAKE2b-512

During the development of our project, it was crucial to choose a cryptographic hash function to create a unique ID for files stored in our system. This ID needed to serve as an efficient way of comparing documents and ensuring data integrity by guarding against unintentional changes. It was necessary for the hash function to provide strong collision resistance and high performance on modern hardware, particularly 64-bit architectures. After evaluating several options, including SHA-2 and SHA-3, we chose BLAKE2b-512.

## Considered Options

We considered several alternatives from the SHA-2 and SHA-3 families. These hash functions have been extensively vetted and are widely supported across platforms.

### SHA-2 Family (SHA-256 and SHA-512):

SHA-256 and SHA-512 provide robust security and avoid known vulnerabilities. However, while SHA-512 is well-optimized for 64-bit platforms, SHA-256 isn't. This makes SHA-256 slower in comparison to hash functions optimized for a 64-bit architecture.

### SHA-3 Family (SHA3-256 and SHA3-512):

SHA-3 is the latest approved standard, solving several theoretical problems present in SHA-2. Despite being more secure, SHA-3 hash functions generally perform slower than both their SHA-2 counterparts and other modern hash functions, such as BLAKE2b.

## Why BLAKE2b-512?

BLAKE2b-512 is a member of the BLAKE2 family, which was designed as an alternative to MD5 and SHA-2. It maintains a high-security level while significantly performing faster than MD5, SHA-1, SHA-2, SHA-3, and SHA-512 on 64-bit platforms. Here are three main reasons why we chose BLAKE2b-512:

- **Performance**: In our benchmark tests, BLAKE2b-512 outperformed SHA-256, SHA-512, and SHA3-256, making it the most performant option for our use case.
- **Security**: BLAKE2 offers similar or better security compared to the latest standard, SHA-3, and is more secure than SHA-2. It uses a cryptographic primitive that has no known vulnerabilities.
- **Compatibility**: The design of BLAKE2 is simpler than SHA-3, reducing risk of implementation errors, and it has well-established support, ensuring compatibility with various systems and standards.

By choosing BLAKE2b-512 for our project, we aimed to maximize performance and security while ensuring broad compatibility across systems.

# NAR list
https://repo1.maven.org/maven2/org/apache/nifi/
https://nifi.apache.org/documentation/nifi-2.0.0-M1/html/developer-guide.html#build

# Compile from source
cd <nifi_source_folder>/nifi-assembly
# mvn clean install -Pinclude-grpc,include-graph,include-media
mvn clean install -Pinclude-all

Parquet NAR
<configuration>
<property>
<name>hadoop.tmp.dir</name>
<value>/home/abimanyu/temp</value>   
</property>

 <property>
  <name>fs.default.name</name>
  <value>file:///</value>
 </property>

</configuration>


# Registry install
```bash
wget https://dlcdn.apache.org/nifi/2.0.0-M1/nifi-registry-2.0.0-M1-bin.zip -O nifi-registry.bin.zip
unzip nifi-registry.bin.zip

cd nifi-registry-2.0.0-M1/
bin/nifi-registry.sh install
# systemctl daemon-reload

vim conf/nifi-registry.properties
# nifi.registry.web.http.host=127.0.0.1

service nifi-registry start
```

# Secure REgistry

#toolkit
bin/tls-toolkit.sh standaline -n "localhost" -C "CN=sys_admin, OU=NIFI" -o target
# Writes target\localhost folder with cert
# Keystore and truststore copy to conf folder op registry

# From nifi.properties in toolik copy nifi/security.keystore & truststore lines to nifi-registry.properties in registry conf
# Also change web.http yo web.https 18443 and set .https.host
# authorizers.xml: set "Initial Admin Identity" and "Initial User Identity 1" to CN=sys_admin, OU=NIFI


# Nifi
create localhost cn add that to registry settings on nifi and set user on regitry to Read Buckets and "Can proxy user requests" (last to use rights of the current cert user logged in to NiFi

# Registry Git
# Configure H2 only (nifi.registry.web.https.application.protocols)
Create git repo and personal token to it
# Remote Clone Repository, should auto download/create exisiting GIT withit manual pull from cli
In conf edit providers.xml
Change flowPersistenceProvider to Git
- "Remote To Push": origin




# Own CA ECC: https://www.erianna.com/ecdsa-certificate-authorities-and-certificates-with-openssl/
# Show curves: openssl ecparam -list_curves

# Create CA private key
openssl ecparam -genkey -name secp384r1 -out ca.key

# https://www.openssl.org/docs/man1.0.2/man5/x509v3_config.html
# https://node-security.com/posts/openssl-creating-a-ca/
# https://superuser.com/questions/738612/openssl-ca-keyusage-extension
# https://www.scottbrady91.com/openssl/creating-elliptical-curve-keys-using-openssl

# TODO cRL: https://www.pixelstech.net/article/1445498968-Generate-certificate-with-cRLDistributionPoints-extension-using-OpenSSL

# ca.conf        pathlen -1 for each intermediate level
basicConstraints=critical,CA:true,pathlen:2
keyUsage=critical,cRLSign,keyCertSign
[req]
distinguished_name = req_distinguished_name
prompt = no
[req_distinguished_name]
C=NL
ST=North Holland
L=Zaandam
O=00010110 B.V.
CN=00010110 Root CA


# Try to mimic LetsEncrypt settings: https://letsencrypt.org/certs/isrg-root-x2.txt

openssl req -x509 -new -sha384 -nodes -key ca.key -days 7307 -out ca.crt -config ca.conf
# Check cert: openssl x509 -noout -text -in ca.crt

# Client cert (for Pulbic root, enterprise can be different): max 398 days

# https://pki-tutorial.readthedocs.io/en/latest/

#Naming and components: https://www.encryptionconsulting.com/a-detailed-guide-on-building-your-own-pki/
