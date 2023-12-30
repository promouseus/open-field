curl 'http://localhost:8050/render.html?url=https://www.succubus.nl/products/irregular-choice-halloween-ghostly-waltz-laarzen-zwart?variant=39715601317936&timeout=10&wait=0.5'

curl 'http://localhost:8050/render.png?url=https://www.succubus.nl/products/irregular-choice-halloween-ghostly-waltz-laarzen-zwart?variant=39715601317936&timeout=10'

curl --header "Content-Type: application/json" \
  --request POST \
  -o suc.png \
  --data '{"url":"https://www.succubus.nl/products/irregular-choice-halloween-ghostly-waltz-laarzen-zwart?variant=39715601317936","timeout":10, "wait":10, "timeout":20, "width":1920, "height": 1080}' \
  http://localhost:8050/render.png

# Full page
curl --header "Content-Type: application/json" \
  --request POST \
  -o suc_full.png \
  --data '{"url":"https://www.succubus.nl/products/irregular-choice-halloween-ghostly-waltz-laarzen-zwart?variant=39715601317936","timeout":10, "wait":10, "timeout":20, "render_all":1}' \
  http://localhost:8050/render.png



https://medium.com/@masreis/text-extraction-and-ocr-with-apache-tika-302464895e5f


  Spot hondje voor achtergrond search (none real-time)

https://en.m.wikipedia.org/wiki/Search_engine_indexing

Index Merging: version nummer for index on nodes to make background new tree generator possible

Meta tag indexing: self index minner, advise about there website. Show in results that this is quality result (layers of search results, motivate better web standards)

Focus indexing web engines, like Wordpress, etc

Validator (external minner to dubbel check some things)

https://dbis1.github.io/courses/ws20/advanced_topics/simd2.pdf



Scraper
https://splash.readthedocs.io/en/stable/install.html



https://www.succubus.nl/collections/lace-up-boots
Sorry, er zijn geen producten in deze collectie

Wel
RECENTLY VIEWED PRODUCTS


===
Bekijk: 1 - 48 van 4771

docker run -p 127.0.0.1:8050:8050 scrapinghub/splash:latest


#####
https://github.com/SeleniumHQ/docker-selenium
pip install selenium
pip install webdriver-manager

docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-firefox:4.1.3-20220405
docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-firefox:4.2.1-20220531

#####

docker run -it --name tika-server-ocr -d -p 9998:9998 apache/tika:latest-full

docker exec -it tika-server-ocr /bin/bash
apt-get update
apt-get install tesseract-ocr-nld

curl -T image2_headless.png http://localhost:9998/tika --header "Accept: application/json" --header "Content-type: image/png" --header "X-Tika-OCRLanguage: nld"|json_pp



{
   "Chroma BlackIsZero" : "true",
   "Chroma ColorSpaceType" : "RGB",
   "Chroma NumChannels" : "4",
   "Compression CompressionTypeName" : "deflate",
   "Compression Lossless" : "true",
   "Compression NumProgressiveScans" : "1",
   "Content-Type" : "image/png",
   "Content-Type-Override" : "image/png",
   "Content-Type-Parser-Override" : "image/ocr-png",
   "Data BitsPerSample" : "8 8 8 8",
   "Data PlanarConfiguration" : "PixelInterleaved",
   "Data SampleFormat" : "UnsignedIntegral",
   "Dimension ImageOrientation" : "Normal",
   "Dimension PixelAspectRatio" : "1.0",
   "IHDR" : "width=3840, height=6310, bitDepth=8, colorType=RGBAlpha, compressionMethod=deflate, filterMethod=adaptive, interlaceMethod=none",
   "Transparency Alpha" : "nonpremultipled",
   "X-TIKA:Parsed-By" : [
      "org.apache.tika.parser.DefaultParser",
      "org.apache.tika.parser.image.ImageParser",
      "org.apache.tika.parser.ocr.TesseractOCRParser"
   ],
   "X-TIKA:Parsed-By-Full-Set" : [
      "org.apache.tika.parser.DefaultParser",
      "org.apache.tika.parser.image.ImageParser",
      "org.apache.tika.parser.ocr.TesseractOCRParser"
   ],
   "X-TIKA:content" : "<html xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n<meta name=\"Transparency Alpha\" content=\"nonpremultipled\" />\n<meta name=\"tiff:ImageLength\" content=\"6310\" />\n<meta name=\"Compression CompressionTypeName\" content=\"deflate\" />\n<meta name=\"Dimension PixelAspectRatio\" content=\"1.0\" />\n<meta name=\"Data BitsPerSample\" content=\"8 8 8 8\" />\n<meta name=\"Data PlanarConfiguration\" content=\"PixelInterleaved\" />\n<meta name=\"IHDR\" content=\"width=3840, height=6310, bitDepth=8, colorType=RGBAlpha, compressionMethod=deflate, filterMethod=adaptive, interlaceMethod=none\" />\n<meta name=\"Compression NumProgressiveScans\" content=\"1\" />\n<meta name=\"Content-Type-Parser-Override\" content=\"image/ocr-png\" />\n<meta name=\"X-TIKA:Parsed-By\" content=\"org.apache.tika.parser.DefaultParser\" />\n<meta name=\"X-TIKA:Parsed-By\" content=\"org.apache.tika.parser.image.ImageParser\" />\n<meta name=\"X-TIKA:Parsed-By\" content=\"org.apache.tika.parser.ocr.TesseractOCRParser\" />\n<meta name=\"Chroma ColorSpaceType\" content=\"RGB\" />\n<meta name=\"Chroma BlackIsZero\" content=\"true\" />\n<meta name=\"Compression Lossless\" content=\"true\" />\n<meta name=\"width\" content=\"3840\" />\n<meta name=\"Dimension ImageOrientation\" content=\"Normal\" />\n<meta name=\"tiff:BitsPerSample\" content=\"8 8 8 8\" />\n<meta name=\"tiff:ImageWidth\" content=\"3840\" />\n<meta name=\"Content-Type-Override\" content=\"image/png\" />\n<meta name=\"Chroma NumChannels\" content=\"4\" />\n<meta name=\"Data SampleFormat\" content=\"UnsignedIntegral\" />\n<meta name=\"Content-Type\" content=\"image/png\" />\n<meta name=\"height\" content=\"6310\" />\n<title></title>\n</head>\n<body><div class=\"ocr\">Shop de hele collectie in onze 50Om2 winkel, elke ma-za van 10 tot 5 + 6-6 van 12 tot 5! Kijk hier voor info XxX\n\nGEEN VERZENDKOSTEN - ACHTERAF BETALEN - EENVOUDIG RETOURNEREN Zoekopdracht a\n\ndueeubus\n\nÃinkelwagen 0 Inloggen of Account aanmaken\n\nKinderen Home &amp; Gifts eK IEA Ela Mijn Verlanglijst Spotlight\n\n \n\nIrregular Choice Halloween Ghostly Waltz Laarzen\n\nZwart\n\nMerk: Irregular Choice\nProduct Type: Schoenen\nâ¬179,95\n\nDit sprookje neemt een duistere wending: de Irregular Choice Halloween collectie!\nMooie dame toch op die oude foto? Blijf kijken en zie het leven uit haar verdwijnen!\n\nDe laarzen zelf zijn super stijlvol voor het najaar, rijkelijk versierd met donkergroen metallicl,\ngedrapeerde stof (bijeengehouden door spinnetjes!) en een grote strik. De 9,5 cm hoge\nhak is bedekt met glitters en loopt comfortabel door het zachte voetbed en ze sluiten met\n\neen rits aan de binnenkant.\n\nDe vrolijke print aan de zool kan je met de Irregular Choice Sole Protectors extra lang\n\nbeschermen.\n\nDeze collectie is maar eenmalig uitgegeven, dus wacht vooral niet als je je zwarte hartje\n\nverloren bent.\n\n \n\nHakhoogte: 9,5 cm. Materiaal: textiel en overige\n\nSchoenmaten : 39 MAATTABEL\n\nTOEVOEGEN AAN WINKELWAGEN D\n\nOOK VERKRIJGBAAR IN:\n\n \n\n \n\n \n\nIrregular Choice Halloweeâ¦. Irregular Choice Halloweeâ¦. Irregular Choice Halloweeâ¦. Irregular Choice Halloweeâ¦. Irregular Choice Halloweeâ¦.\nâ¬144,95 â¬219,95 â¬164,95 â¬164,95 â¬219,95\ne\nKlanten-reviews\n&amp; WW ww Nog geen beoordelingen Schrijf een recensie Een vraag stellen\n\n \n\n \n\n \n\n \n\n \n\nVAAK SAMEN GEKOCHT:\n\n  \n\nIrregular Choice Sole. Irregular Choice x Hello... Irregular Choice x Hello... Irregular Choice Go Fish... Irregular Choice Happy...\n\nâ¬9,95 â¬259,95 â¬229,95 â¬124,95 â¬149,95\n\nSHOP OP INFORMATIE KLANTENSERVICE BLIJF OP DE HOOGTE!\n\nQ lo) d\nn/ e Ss,\n\narden\n\nCadeaubonnen\nubt hland\nubus International\n\nMeldt je aan r de nie\n\nrt een 9,4 geb\n\nZE\n\n \n\n \n</div>\n\n</body></html>",
   "height" : "6310",
   "tiff:BitsPerSample" : "8 8 8 8",
   "tiff:ImageLength" : "6310",
   "tiff:ImageWidth" : "3840",
   "width" : "3840"
}

Add tensor flow image dection (shoes, etc)
 https://cwiki.apache.org/confluence/display/tika/TikaAndVision


#### PIP
source venv/bin/activate 



