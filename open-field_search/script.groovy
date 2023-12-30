// https://www.leveluplunch.com/groovy/examples/parse-sitemap-xml-with-xmlsluper/

import groovy.xml.XmlSlurper

def String books = '''
    <response version-api="2.0">
        <value>
            <books>
                <book available="20" id="1">
                    <title>Don Quixote</title>
                    <author id="1">Miguel de Cervantes</author>
                </book>
                <book available="14" id="2">
                    <title>Catcher in the Rye</title>
                   <author id="2">JD Salinger</author>
               </book>
               <book available="13" id="3">
                   <title>Alice in Wonderland</title>
                   <author id="3">Lewis Carroll</author>
               </book>
               <book available="5" id="4">
                   <title>Don Quixote</title>
                   <author id="4">Miguel de Cervantes</author>
               </book>
           </books>
       </value>
    </response>
'''

def sitemapURL = "https://www.leveluplunch.com/sitemap.xml"
sitemapURL = "https://www.succubus.nl/sitemap.xml"
def siteMapLocation = sitemapURL.toURL().text

def linkCounter = 0;

def sitemapindex = new XmlSlurper().parseText(siteMapLocation)
sitemapindex.sitemap.each{
    //println it.loc
    def urlset = new XmlSlurper().parseText(it.loc.toURL().text)
    urlset.url.each{
        //println it.loc
        linkCounter += 1
        //println it.lastmod
        //println it.priority
        //println "^^^^^^^^"
    }
}

print linkCounter + '\n'

/*def urlset = new XmlSlurper().parseText(siteMapLocation)
urlset.url.each{
    println it.loc
    //println it.lastmod
    //println it.priority
    //println "^^^^^^^^"
}*/

def response = new XmlSlurper().parseText(books)
def authorResult = response.value.books.book[0].author

print authorResult

assert authorResult.text() == 'Miguel de Cervantes'
