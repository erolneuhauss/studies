# Evaluation of AlienVault OSSIM
## Key phrases from the company's website
```
AlienVault OSSIM:
The World’s Most Widely Used
Open Source SIEM
```

```
Intelligent, Affordable Security is Our Mission.
```

```
OSSIM, AlienVault’s Open Source Security Information
and Event Management (SIEM) product,
provides you with a feature-rich open source SIEM
complete with event collection, normalization and
correlation. Launched by security engineers because
of the lack of available open source products,
OSSIM was created specifically to address the reality
many security professionals face:
A SIEM, whether it is open source or commercial,
is virtually useless without the basic security controls
necessary for security visibility.

Our Open Source SIEM (OSSIM) addresses this reality
by providing one unified platform with many of the
essential security capabilities you need like:

    - Asset discovery
    - Vulnerability assessment
    - Intrusion detection
    - Behavioral monitoring
    - SIEM
```


2017-04-06: [https://www.alienvault.com/products/ossim](alienvault.com/products/ossim)

## Key aspects and focus of the evaluation
- does it come with read-to-use defaults and filters?
- how fast can it be set up, configure and have it running in production?
- what is the quality of the software itself and the web user interface?

## Prelimary results of the evaluation
- alienvault OSSIM is read-to-use with defaults, plugins and filters already in place
    - go to Environment -> Assets -> choose Host -> scroll down
- server setup is very fast due to installation via iso image (Linux Debian)
- installation of clients via wui very unhandy -- automatisation definitly needed
- high hardware system requirements and high resource consumtion. Minimum
    - 8 core CPU
    - 16 GB RAM
    - 1 TB fast HDD
- wui slow on 4 Core RAM, 6 GB RAM. 
    - go to Configuration -> Deployment and wait for status.
- plentyfull documentation, howtos, forum support and webcasts
- project und forum very alive
- no source code repository available online
- Alienvault consists on other open source software components
- Alienvault: all-in-one

## Resources for the evaluation
- [AlienVault Resource Center](https://www.alienvault.com/resource-center)
- [linoxide.com/security/install-configure-alienvault-siem-ossim/](http://linoxide.com/security/install-configure-alienvault-siem-ossim/)
- YouTube: [Alienvaulttv](https://www.youtube.com/user/alienvaulttv)
- YouTube: [OSSIM Tutorial: Best Practices for OSSIM Configuration](https://www.youtube.com/watch?v=qjaO1cNj2fo&index=4&list=PLvc7OorCTShovyYGc_9Q6abTLt-ucE_wT)
(17.12.2015)
- [www.alienvault.com/documentation/usm-appliance.htm](https://www.alienvault.com/documentation/usm-appliance.htm)
- [blog.muhammadattique.com/installing-configuring-alienvault-ossim-opensource-siem](http://blog.muhammadattique.com/installing-configuring-alienvault-ossim-opensource-siem)
- [blog.muhammadattique.com/configuring-ossec-clients-with-ossim](http://blog.muhammadattique.com/configuring-ossec-clients-with-ossim/)


## Version
5.3.6 installed. 5.3.7 is ready for customers.

## Architecture
### OSSIM uses OSSEC agent software on client
-   add an asset on the server via wui
-   add an agent onto the asset
-   extract key from agent and use it with ```manage_agent```
#### Client Installation

```
wget https://www.atomicorp.com/installers/atomic
wget https://ossec.github.io/files/OSSEC-ARCHIVE-KEY.asc
sudo gpg --import OSSEC-ARCHIVE-KEY.asc
sudo bash atomic

sudo yum -y install ossec-hids-agent.x86_64

sudo /var/ossec/bin/manage_agent -i <id>

sudo sed -i 's/192.168.10.100/192.168.56.104' /var/ossec/etc/ossec-agent.conf
sudo systemctl enable ossec-hids
sudo systemctl start ossec-hids
```