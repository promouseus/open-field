# open-field
The Promouseus open-field system for IT infrastructure landscaping.

IT infrastructure is moving from on-premisses/single service provider setups to a combination of cloud, all kinds of “as a Service” concepts and appliance providers.

To control and harvest the power of these new hybrid IT infrastructure Promouseus is working on the open-field project. At Promouseus we like to compare IT infrastructure with a piece of cropland or common land that is the foundation to build your crops or IT services on. In medieval times little land was owned by the user. The [Open-field system](https://en.wikipedia.org/wiki/Open-field_system) rented land to a user that had the control and harvest ability over it but had to pay rent in return.

The Promouseus open-field project aims to become the foundation to control your IT landscape with an out-of-the-box user and programming interface.

## IT infrastructure management functions

| Term      | Description    |
| ------------- | --------- |
| **ITSM (IT Service Management)** | The entirety of activities—directed by policies, organized and structured in processes and supporting procedures—that organizations perform to design, plan, deliver, operate, and control IT services. |
| **IPAM (IP Address Management)** | The administration of DNS and DHCP, which includes the management of IP addresses. |
| **DCIM (Data Center Infrastructure Management)** | A management platform combining system, network, and facilities management for a physical or virtualized data center. |
| **CMDB (Configuration Management Database)** | A database that contains all relevant information about the hardware and software components used in an organization's IT services and the relationships between those components. |
| **Change Management** | The process of handling modifications and updates to a system in a planned and systematic way. |
| **Incident Management** | The activities of an organization to identify, analyze, and correct hazards to prevent a future occurrence. |
| **Asset Management** | Involves tracking and managing physical or virtual devices/assets, including lifecycle management. |
| **SLA (Service Level Agreement)** | A commitment between a service provider and a client. Particular aspects of the service—quality, availability, responsibilities—are agreed upon between the service provider and the service user. |
| **SaaS (Software as a Service)<br/>IaaS (Infrastructure as a Service)<br/>PaaS (Platform as a Service)** | Service models in cloud computing where different levels of the service (like applications, runtime platform, or underlying infrastructure) are provided as a service. |
| **Virtualization** | The process of creating a software-based (or virtual) representation of something rather than a physical one. It can apply to applications, servers, storage, and networks. |
| **High Availability** | Systems that are continuously operational for a desirably high length of time. |
| **Disaster Recovery** | A Set of policies, tools, and procedures enabling the recovery or continuation of vital technology infrastructure and systems following a natural or human-induced disaster. |
| **Business Continuity** | The process of creating systems of prevention and recovery to deal with potential threats to a company. |

### open-field CMDB
C2IT is a Python-based application that builds upon the NetBox API to deliver a minimalistic Configuration Management Database (CMDB). NetBox, as a single source of truth for your network, lays the groundwork for C2IT's advanced functionalities. We augment NetBox's data center infrastructure management (DCIM) and IP address management (IPAM) capabilities to provide you with a comprehensive solution for managing your IT infrastructure.
Key Features
#### Asset Lifecycle Management
C2IT can track the entire lifecycle of all your IT assets, from procurement to retirement. Fields for recording information such as the purchase date, warranty expiration, deployment date, decommissioning date, etc., offer a clear view of an asset's status at any given point in time.
#### Relationships and Dependency Mapping
Through C2IT, you can establish and visualize complex relationships between your assets. For example, you can define that Application A runs on Server B, which in turn is hosted on Hypervisor C. This allows for a comprehensive view of your infrastructure's interdependencies.
#### IT Service Desk Integration
C2IT's power lies in its deep integration with your day-to-day operations. It is designed to link seamlessly with your IT Service Desk, creating a clear connection between incidents and the associated infrastructure components, thereby enhancing incident management.
#### Change Management
C2IT integrates with your IT service management solution, enabling accurate tracking and management of planned changes. This functionality allows you to anticipate potential issues, reduce downtime, and ensure the smooth operation of your IT services.
#### Enhanced Inventory Management
Our tool extends NetBox's inventory management capabilities to provide comprehensive tracking of servers, CPUs, memory, hard drives, applications, and version numbers, amongst other parameters.
#### Reporting and Visualization
C2IT provides powerful visualization tools for your infrastructure, generating insightful visual representations of your assets and their interdependencies for efficient management.

## User interface
The web-based user interface is focuses on end-users in small businesses. This user interface, offerend both in web and app form, is called Promouseus and combines the open-field and C2IT back-end functionality in a single user interface.

## Programming interface
The open-field programming interface is realized in C2IT, is created to allow company’s with a deeper understanding of IT to connect the user interface to their own infrastructure services. For example: ISPs are using Promouseus open-field to allow there users (customers) to manage there internet connections and firewall settings.

# open-field_time-series (SLA)
The time-series sub-element is part of the Promouseus open-field system for IT infrastructure landscaping.

We (are working on) following the Docker Official Images guidelines as stated at: https://github.com/docker-library/official-images. Build files are structured bases on the sub-requirements of these guidelines as stated at: https://docs.docker.com/develop/develop-images/dockerfile_best-practices/. Followed by the sub-requirements states at: https://12factor.net/processes

## Apache IoTDB
start-cli.sh

Volumes: /iotdb/logs & /iotdb/data

# open-field_search (CMDB C/I/A management)
The search sub-element is part of the Promouseus open-field system for IT infrastructure landscaping. This search component indexes other data to find relations to IT infrastructure components.

```
docker ps -q | xargs -n 1 docker inspect --format '{{ .Name }} {{range .NetworkSettings.Networks}} {{.IPAddress}}{{end}}' | sed 's#^/##';
ssh -L 8443:172.17.0.6:8443 -L 8888:172.17.0.3:8888 -L 8088:172.17.0.2:8088 -L 8047:172.17.0.4:8047 -L 7900:172.17.0.5:7900 root@192.168.0.1
```


## ExecuteScript
* Nifi libraries: https://github.com/SeleniumHQ/selenium/releases/download/selenium-4.7.0/selenium-java-4.7.0.zip
* Groovy examples: https://pleac.sourceforge.net/pleac_groovy/internetservices.html
* Selenium example: https://gist.github.com/bensullivan/4631660

### Selenium
```
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
```