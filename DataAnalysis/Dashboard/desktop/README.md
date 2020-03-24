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
emcc main.c -o main.html -s EXPORTED_FUNCTIONS='["_int_sqrt"]' -s EXTRA_EXPORTED_RUNTIME_METHODS='["ccall", "cwrap"]'
- Add EMSCRIPTEN_KEEPALIVE above function should also export the function?

# Run build-in webserver
emrun --no_browser --port 8080 .

# Interact from HTML
https://emscripten.org/docs/porting/connecting_cpp_and_javascript/Interacting-with-code.html
<input id="clickMe" type="button" value="clickme" onclick="int_sqrt = Module.cwrap('int_sqrt', 'number', ['number']); int_sqrt(12);" />