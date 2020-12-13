package io.promouseus.etl;

import java.io.IOException;
import java.io.InputStream;
//import java.math.BigDecimal;
import java.net.URL;
import java.util.HashMap;
import java.util.Map;

import javax.json.Json;
import javax.json.stream.JsonParser;
import javax.json.stream.JsonParser.Event;

import com.redislabs.redistimeseries.Aggregation;
import com.redislabs.redistimeseries.RedisTimeSeries;

/**
 * Promouseus Extract, Transform, Load (ETL) App
 */
public class App {
    public static void main(String[] args) throws IOException {
        System.out.println("NiFi metric processor");

        RedisTimeSeries rts = new RedisTimeSeries("172.17.0.1", 6379);
   
        Map<String, String> labels = new HashMap<>();
        labels.put("country", "US");
        labels.put("cores", "8"); 
        rts.create("cpu1", 60*10, labels); /*10min*/
        
        rts.create("cpu1-avg", 60*10 /*10min*/, null);
        rts.createRule("cpu1", Aggregation.AVG, 60 /*1min*/, "cpu1-avg");
        
        rts.add("cpu1", System.currentTimeMillis()/1000 /* time sec */, 80.0);
        
        // Get all the timeseries in US in the last 10min average per min  
        rts.mrange(System.currentTimeMillis()/1000 - 10*60, System.currentTimeMillis()/1000, Aggregation.AVG, 60, "country=US");

        // https://www.oracle.com/technical-resources/articles/java/json.html
        // curl -i -X GET http://localhost:8081/nifi-api/system-diagnostics
        // curl -i -X GET http://localhost:8081/nifi-api/processors/5c4a3e69-0176-1000-ae09-065a40528643
        // curl -i -X GET http://localhost:8081/nifi-api/process-groups/5c4b698d-0176-1000-0f5e-723b041fa451
        URL url = new URL("http://172.17.0.1:8081/nifi-api/system-diagnostics");
        try (InputStream is = url.openStream(); JsonParser parser = Json.createParser(is)) {
            while (parser.hasNext()) {
                Event e = parser.next();
                if (e == Event.KEY_NAME) {
                    switch (parser.getString()) {
                        case "heapUtilization":
                            parser.next();
                            System.out.println(parser.getString());
                            break;
                        case "processorLoadAverage":
                            parser.next();
                            System.out.println(parser.getString());
                            break;
                        case "totalThreads":
                            parser.next();
                            System.out.println(parser.getString());
                            break;
                        case "daemonThreads":
                            parser.next();
                            System.out.println(parser.getString());
                            break;
                        case "statsLastRefreshed":
                            parser.next();
                            System.out.println(parser.getString());
                            break;
                    }
                }
            }
            parser.close();
        }

        System.out.println("----------");

        url = new URL("http://172.17.0.1:8081/nifi-api/processors/5c4a3e69-0176-1000-ae09-065a40528643");
        try (InputStream is = url.openStream(); JsonParser parser = Json.createParser(is)) {
            while (parser.hasNext()) {
                Event e = parser.next();
                if (e == Event.KEY_NAME) {
                    switch (parser.getString()) {
                        case "bytesRead":
                            parser.next();
                            System.out.println(parser.getString());
                            break;
                        case "bytesWritten":
                            parser.next();
                            System.out.println(parser.getString());
                            break;
                        case "totalThreads":
                            parser.next();
                            System.out.println(parser.getString());
                            break;
                        case "flowFilesIn":
                            parser.next();
                            System.out.println(parser.getString());
                            break;
                        case "flowFilesOut":
                            parser.next();
                            System.out.println(parser.getString());
                            break;
                        case "bytesIn":
                            parser.next();
                            System.out.println(parser.getString());
                            break;
                        case "bytesOut":
                            parser.next();
                            System.out.println(parser.getString());
                            break;
                        case "taskCount":
                            parser.next();
                            System.out.println(parser.getString());
                            break;
                        case "tasksDuration":
                            parser.next();
                            System.out.println(parser.getString());
                            break;
                        case "activeThreadCount":
                            parser.next();
                            System.out.println(parser.getString());
                            break;
                        case "statsLastRefreshed":
                            parser.next();
                            System.out.println(parser.getString());
                            break;
                    }
                }
            }
            parser.close();
        }

        System.out.println("----------");

        url = new URL("http://172.17.0.1:8081/nifi-api/process-groups/5c4b698d-0176-1000-0f5e-723b041fa451");
        try (InputStream is = url.openStream(); JsonParser parser = Json.createParser(is)) {
            while (parser.hasNext()) {
                Event e = parser.next();
                if (e == Event.KEY_NAME) {
                    switch (parser.getString()) {
                        case "flowFilesIn":
                            parser.next();
                            System.out.println(parser.getString());
                            break;
                        case "flowFilesOut":
                            parser.next();
                            System.out.println(parser.getString());
                            break;
                        case "bytesIn":
                            parser.next();
                            System.out.println(parser.getString());
                            break;
                        case "bytesOut":
                            parser.next();
                            System.out.println(parser.getString());
                            break;
                        case "flowFilesQueued":
                            parser.next();
                            System.out.println(parser.getString());
                            break;
                        case "bytesQueued":
                            parser.next();
                            System.out.println(parser.getString());
                            break;
                        case "bytesRead":
                            parser.next();
                            System.out.println(parser.getString());
                            break;
                        case "flowFilesTransferred":
                            parser.next();
                            System.out.println(parser.getString());
                            break;
                        case "bytesWritten":
                            parser.next();
                            System.out.println(parser.getString());
                            break;

                        case "bytesTransferred":
                            parser.next();
                            System.out.println(parser.getString());
                            break;
                        case "bytesReceived":
                            parser.next();
                            System.out.println(parser.getString());
                            break;
                        case "bytesSent":
                            parser.next();
                            System.out.println(parser.getString());
                            break;
                        case "flowFilesReceived":
                            parser.next();
                            System.out.println(parser.getString());
                            break;
                        case "flowFilesSent":
                            parser.next();
                            System.out.println(parser.getString());
                            break;
                        case "activeThreadCount":
                            parser.next();
                            System.out.println(parser.getString());
                            break;
                    }
                }
            }
            parser.close();
        }

        /*
         * URL url = new URL("http://172.17.0.1:8081/nifi-api/system-diagnostics"); try
         * (InputStream is = url.openStream(); JsonParser parser =
         * Json.createParser(is)) { while (parser.hasNext()) { Event e = parser.next();
         * if (e == Event.KEY_NAME) { switch (parser.getString()) { case "name":
         * parser.next(); System.out.print(parser.getString()); System.out.print(": ");
         * break; case "message": parser.next(); System.out.println(parser.getString());
         * System.out.println("---------"); break; } } } }
         */

        /*
         * final String result = "{\"name\":\"Falco\",\"age\":3,\"bitable\":false}";
         * final JsonParser parser = Json.createParser(new StringReader(result)); String
         * key = null; String value = null; while (parser.hasNext()) { final Event event
         * = parser.next(); switch (event) { //
         * https://javadoc.io/static/javax.json/javax.json-api/1.1/javax/json/stream/
         * JsonParser.html // {START_OBJECT }END_OBJECT [START_ARRAY ]END_ARRAY case
         * KEY_NAME: key = parser.getString(); System.out.println(key); break; case
         * VALUE_STRING: String string = parser.getString(); System.out.println(string);
         * break; case VALUE_NUMBER: BigDecimal number = parser.getBigDecimal();
         * System.out.println(number); break; case VALUE_TRUE: System.out.println(true);
         * break; case VALUE_FALSE: System.out.println(false); break; } }
         * parser.close(); } }
         */
    }
}
