FROM alpine:latest

#COPY . /usr/src/
WORKDIR /usr/src/
RUN apk add --no-cache libssh git
# gcc cmake make
#clang binutils
RUN git clone https://git.libssh.org/projects/libssh.git libssh
WORKDIR /usr/src/libssh/build
#RUN cmake -DUNIT_TESTING=ON -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Debug ..
#RUN gcc -o myapp main.c
CMD ["top"]

# Mac by brew
## ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" < /dev/null 2> /dev/null
## brew install libssh
## brew install cmake
## get code:
# cd libssh
# mkdir build
# cd build
# cmake -DUNIT_TESTING=ON -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Debug .. # other t