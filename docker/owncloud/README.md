# produce your own cloud server with docker

* Installation von Docker auf dem eigenen Rechner (für die u.g. Tasks und auch für den Workshop)
* Aufsetzen eines OwnCloud-Servers mit MySQL Backend
* Images
  * https://hub.docker.com/r/owncloud/server/
  * https://hub.docker.com/_/mariadb/
* Ziele
  * OwnCloud ist mit Persistenz lokal erreichbar
  * Erstellen eines eigenen nginx-Images
  * Weiterleitung 80 -> 443
  * SSL-Terminierung für OwnCloud (self-signed Cert ist ok)
* Extras
  * Alle Container laufen nicht als root
  * Die Container werden mit docker-compose orchestriert
