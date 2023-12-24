# open-field
The Promouseus open-field system for IT infrastructure landscaping.

IT infrastructure is moving from on-premisses/single service provider setups to a combination of cloud, all kinds of “as a Service” concepts and appliance providers.

To control and harvest the power of these new hybrid IT infrastructure Promouseus is working on the open-field project. At Promouseus we like to compare IT infrastructure with a piece of cropland or common land that is the foundation to build your crops or IT services on. In medieval times little land was owned by the user. The [Open-field system](https://en.wikipedia.org/wiki/Open-field_system) rented land to a user that had the control and harvest ability over it but had to pay rent in return.

The Promouseus open-field project aims to become the foundation to control your IT landscape with an out-of-the-box user and programming interface.

## User interface
The web-based user interface is focuses on end-users in small businesses.

## Programming interface
The programming interface is created to allow company’s with a deeper understanding of IT to connect the user interface to there own infrastructure services. For example: ISP’s are using Promouseus open-field to allow there users (customers) to manage there internet connections and firewall settings.

## Project status
Currently we are rebuilding all infrastructure tools, concepts and idea’s that we created in the last 20 years to the open-field project. All current code is draft. At the end of 2019 we expect to launch the first out-of-the-box version with an installer included.

# open-field_time-series
The time-series sub-element is part of the Promouseus open-field system for IT infrastructure landscaping.

We (are working on) following the Docker Official Images guidelines as stated at: https://github.com/docker-library/official-images. Build files are structured bases on the sub-requirements of these guidelines as stated at: https://docs.docker.com/develop/develop-images/dockerfile_best-practices/. Followed by the sub-requirements states at: https://12factor.net/processes

## Apache IoTDB
start-cli.sh

Volumes: /iotdb/logs & /iotdb/data

# open-field_search
The search sub-element is part of the Promouseus open-field system for IT infrastructure landscaping.

```
docker ps -q | xargs -n 1 docker inspect --format '{{ .Name }} {{range .NetworkSettings.Networks}} {{.IPAddress}}{{end}}' | sed 's#^/##';
ssh -L 8443:172.17.0.6:8443 -L 8888:172.17.0.3:8888 -L 8088:172.17.0.2:8088 -L 8047:172.17.0.4:8047 -L 7900:172.17.0.5:7900 root@83.149.73.229
```

# ECS Anywhere
echo "GRUB_CMDLINE_LINUX=\"cgroup_enable=memory systemd.unified_cgroup_hierarchy=false swapaccount=1\"" | sudo tee /etc/default/grub.d/cgroup.cfg
update-grub

# ExecuteScript
Nifi libraries: https://github.com/SeleniumHQ/selenium/releases/download/selenium-4.7.0/selenium-java-4.7.0.zip


## Groovy

https://pleac.sourceforge.net/pleac_groovy/internetservices.html

### Selenium
import org.apache.commons.io.IOUtils

import org.openqa.selenium.By
import org.openqa.selenium.Dimension
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver
import org.openqa.selenium.remote.RemoteWebDriver
import org.openqa.selenium.firefox.FirefoxOptions
import org.openqa.selenium.firefox.FirefoxDriver

// flowFile = session.get()
// if(!flowFile) return

FirefoxOptions firefoxOptions = new FirefoxOptions()
.addPreference("layout.css.devPixelsPerPx","2.0");

WebDriver driver = new RemoteWebDriver(new URL("http://selenium:4444"), firefoxOptions);

def dimension = new Dimension(1920, 3240);
driver.manage().window().setSize(dimension);


flowFileList = session.get(100)
if(!flowFileList.isEmpty()) {
flowFileList.each { flowFile ->
// Process each FlowFile here

      try {
          // Navigate to Url
          driver.get("https://www.succubus.nl/products/dr-martens-1460-pascal-virginia-veterlaarzen-zacht-leder-zwart?variant=14320265003066");

          File imgFile = ((TakesScreenshot)driver).getScreenshotAs(OutputType.FILE);
          byte[] imgFileContent = imgFile.bytes
          flowFile = session.write(flowFile, {outputStream ->
              outputStream.write(imgFileContent)
          } as OutputStreamCallback)
          session.transfer(flowFile, REL_SUCCESS);
      } catch(e) {
		  log.error('Something went wrong', e)
          session.transfer(flowFile, REL_FAILURE);
      } finally {

      }
}
}

driver.quit();

# https://gist.github.com/bensullivan/4631660