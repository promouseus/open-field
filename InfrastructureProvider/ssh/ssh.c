#include <libssh/libssh.h>
#include <stdlib.h>
#include <stdio.h>
 
int main()
{
  ssh_session my_ssh_session;
  int rc;
 
  my_ssh_session = ssh_new();
  if (my_ssh_session == NULL)
    exit(-1);
 
  ssh_options_set(my_ssh_session, SSH_OPTIONS_HOST, "localhost");
 
  rc = ssh_connect(my_ssh_session);
  if (rc != SSH_OK)
  {
    fprintf(stderr, "Error connecting to localhost: %s\n",
            ssh_get_error(my_ssh_session));
    exit(-1);
  }
 
 
  ssh_disconnect(my_ssh_session);
  ssh_free(my_ssh_session);
}