#include <stdio.h>
#include <emscripten.h>

#include "bson/bson.h"

#include <time.h>


int main(int argc, char ** argv) {
    printf("Hello, world!\n");
    /*
    bson_t *b;
    char *j;

   b = BCON_NEW ("hello", BCON_UTF8 ("bson!"));
   j = bson_as_canonical_extended_json (b, NULL);
   printf ("%s\n", j);

   bson_free (j);
   bson_destroy (b);
   */

  time_t now;
  time(&now);
  printf("Time: %s", ctime(&now));

  struct timeval start, stop;
    double secs = 0;
    gettimeofday(&start, NULL);

   int i;
   int n;
   int bcon;
   bson_t bson, foo, bar, baz;
   bson_init (&bson);

    n = 1000; // loop counter
    bcon = 0; // 0 or 1, one of them is bcon other bson_append

    for (i = 0; i < n; i++) {
      if (bcon) {
         BCON_APPEND (&bson,
                      "foo",
                      "{",
                      "bar",
                      "{",
                      "baz",
                      "[",
                      BCON_INT32 (1),
                      BCON_INT32 (2),
                      BCON_INT32 (3),
                      "]",
                      "}",
                      "}");
      } else {
         bson_append_document_begin (&bson, "foo", -1, &foo);
         bson_append_document_begin (&foo, "bar", -1, &bar);
         bson_append_array_begin (&bar, "baz", -1, &baz);
         bson_append_int32 (&baz, "0", -1, 1);
         bson_append_int32 (&baz, "1", -1, 2);
         bson_append_int32 (&baz, "2", -1, 3);
         bson_append_array_end (&bar, &baz);
         bson_append_document_end (&foo, &bar);
         bson_append_document_end (&bson, &foo);
      }

      bson_reinit (&bson);
   }

   bson_destroy (&bson);

   gettimeofday(&stop, NULL);
secs = (double)(stop.tv_usec - start.tv_usec) / 1000000 + (double)(stop.tv_sec - start.tv_sec);
printf("time taken %f\n",secs);

    // https://emscripten.org/docs/api_reference/emscripten.h.html#logging-utilities
    emscripten_log(EM_LOG_WARN, "yoyoyo");


    return 0;
}


int int_sqrt(int x) {
    printf("%d\n", x);
    char line[1024];
    scanf("%1023[^\n]", line);
    printf("Input: %s", line);
    return x;
}