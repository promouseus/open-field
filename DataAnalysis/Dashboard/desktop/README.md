# EMSDK install/update on Mac
https://github.com/emscripten-core/emsdk/issues/406

cd ~
sudo easy_install pip
sudo pip install certifi

git clone https://github.com/emscripten-core/emsdk.git # or "git pull" to update installed emsdk
cd emsdk

python emsdk.py install latest # Not working due to SSL: ./emsdk install latest
python emsdk.py activate latest

# Sourcing compiler tools
source ~/emsdk/emsdk_env.sh --build=Release

# Compile
emcc main.c -o main.html -s EXPORTED_FUNCTIONS='["_main","_int_sqrt"]' -s EXTRA_EXPORTED_RUNTIME_METHODS='["ccall", "cwrap"]' -s MIN_WEBGL_VERSION=2 -s MAX_WEBGL_VERSION=2

- Add EMSCRIPTEN_KEEPALIVE above function should also export the function?

- http://mongoc.org/libmongoc/current/installing.html#building-on-macos
git clone https://github.com/mongodb/mongo-c-driver.git
cd mongo-c-driver
python build/calc_release_version.py > VERSION_CURRENT
#cd src/libbson
mkdir cmake-build
cd cmake-build
- https://emscripten.org/docs/compiling/Building-Projects.html
emcmake cmake -DENABLE_AUTOMATIC_INIT_AND_CLEANUP=OFF -DENABLE_MONGOC=OFF ..
emmake make install

- https://developers.google.com/web/updates/2018/03/emscripting-a-c-library

mongo-c-driver/src/libbson/src
cp -R bson/*.h open-field/DataAnalysis/Dashboard/desktop/bson

- Two missing files needed for config
mongo-c-driver/cmake-build/src/libbson/src/bson/*.h to open-field/DataAnalysis/Dashboard/desktop/bson/

Copy mongo-c-driver/cmake-build/src/libbson/libbson-static-1.0.a to open-field/DataAnalysis/Dashboard/desktop/

emcc -O0 main.c libbson-static-1.0.a -o main.html -s EXPORTED_FUNCTIONS='["_main","_int_sqrt"]' -s EXTRA_EXPORTED_RUNTIME_METHODS='["ccall", "cwrap"]' -s MIN_WEBGL_VERSION=2 -s MAX_WEBGL_VERSION=2; emrun --no_browser --port 8080 .

- https://github.com/emscripten-core/emscripten/wiki/Porting-Examples-and-Demos#tutorials


- Byte Range Downloads: https://emscripten.org/docs/api_reference/fetch.html#managing-large-files, maybe nice for DB like remote file block jumps/search

# Run build-in webserver
emrun --no_browser --port 8080 .

# Interact from HTML
https://emscripten.org/docs/porting/connecting_cpp_and_javascript/Interacting-with-code.html
<input id="clickMe" type="button" value="clickme" onclick="int_sqrt = Module.cwrap('int_sqrt', 'number', ['number']); int_sqrt(12);" />