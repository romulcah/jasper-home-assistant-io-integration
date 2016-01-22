# jasper-home-assistant-io-integration

A simple integration for [Jasper](http://jasperproject.github.io/) and [Home-Assistant.io](https://home-assistant.io/)


Currently just checks who is at home by using the device tracker. By issuing the command "Who is at home" it will tell you the "friendly name" of the devices at home and will also tell you if there is any devices logged at "Work" - a custom location.


Make sure the following is copied and populated in ~/.jasper/profile.yml


```
 ha_url: 

 ha_port: 

 ha_password: 
```

**For example**


```
 ha_url: http://localhost/

 ha_port: 8123

 ha_password: abcd1234
```
