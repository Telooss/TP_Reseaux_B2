# TP1 : Maîtrise réseau du poste

Pour ce TP, on va utiliser **uniquement votre poste** (pas de VM, rien, quedal, quetchi).

Le but du TP : se remettre dans le bain tranquillement en manipulant pas mal de concepts qu'on a vu l'an dernier.

C'est un premier TP *chill*, qui vous(ré)apprend à maîtriser votre poste en ce qui concerne le réseau. Faites le seul ou avec votre mate préféré bien sûr, mais jouez le jeu, faites vos propres recherches.

La "difficulté" va crescendo au fil du TP, mais la solution tombe très vite avec une ptite recherche Google si vos connaissances de l'an dernier deviennent floues.

- [TP1 : Maîtrise réseau du poste](#tp1--maîtrise-réseau-du-poste)
- [I. Basics](#i-basics)
- [II. Go further](#ii-go-further)
- [III. Le requin](#iii-le-requin)

# I. Basics

> Tout est à faire en ligne de commande, sauf si précision contraire.

☀️ **Carte réseau WiFi**

```
ipconfig.exe /all

Carte réseau sans fil Wi-Fi :

   Adresse physique . . . . . . . . . . . : 4C-03-4F-E9-73-F7
   Adresse IPv6 de liaison locale. . . . .: fe80::4e03:4fff:fee9:73f7%12(préféré)
   Adresse IPv4. . . . . . . . . . . . . .: 10.33.76.222(préféré)
   Masque de sous-réseau. . . . . . . . . : 255.255.240.0
   Passerelle par défaut. . . . . . . . . : 10.33.79.254
```
---

☀️ **Déso pas déso**

Pas besoin d'un terminal là, juste une feuille, ou votre tête, ou un tool qui calcule tout hihi. Déterminer...

- l'adresse de réseau du LAN auquel vous êtes connectés en WiFi : ``10.33.64.0``
- l'adresse de broadcast : ``10.33.79.255.``
- le nombre d'adresses IP disponibles dans ce réseau : ``4094``

---

☀️ **Hostname**

- déterminer le hostname de votre PC :
```
PS C:\Users\alanw> hostname
TelosGVNG
```

---

☀️ **Passerelle du réseau**

```
ipconfig.exe /all

Carte réseau sans fil Wi-Fi :

   Adresse physique . . . . . . . . . . . : 4C-03-4F-E9-73-F7
   Passerelle par défaut. . . . . . . . . : 10.33.79.254
```

---

☀️ **Serveur DHCP et DNS**

```
ipconfig.exe /all

Carte réseau sans fil Wi-Fi :

   Serveur DHCP . . . . . . . . . . . . . : 10.33.79.254
   Serveurs DNS. . .  . . . . . . . . . . : 8.8.8.8
                                       1.1.1.1
```

---

☀️ **Table de routage**

```
IPv4 Table de routage
===========================================================================
Itinéraires actifs :
Destination réseau    Masque réseau  Adr. passerelle   Adr. interface Métrique
          0.0.0.0          0.0.0.0      172.20.10.1      172.20.10.2     35
```
---

![Not sure](./img/notsure.png)

# II. Go further

> Toujours tout en ligne de commande.

---

☀️ **Hosts ?**

```w
192.168.56.101 mon-super-site.local
10.4.1.11 node1
51.75.205.76 kymonovps.net 
1.1.1.1 b2.hello.vous

 
 

PS C:\Users\alanw> ping b2.hello.vous

Envoi d’une requête 'ping' sur b2.hello.vous [1.1.1.1] avec 32 octets de données :
Réponse de 1.1.1.1 : octets=32 temps=42 ms TTL=53
```

---

☀️ **Go mater une vidéo youtube et déterminer, pendant qu'elle tourne...**

[Capture WireShark](.Youtube.pcap)

---

☀️ **Requêtes DNS**

Déterminer...

```bash
telos@TelosGVNG:~$ dig www.ynov.com

;; ANSWER SECTION:
www.ynov.com.           0       IN      A       104.26.11.233
www.ynov.com.           0       IN      A       172.67.74.226
www.ynov.com.           0       IN      A       104.26.10.233
```

- à quel nom de domaine correspond l'IP `174.43.238.89`

```bash
telos@TelosGVNG:~$ dig -x 174.43.238.89

;; ANSWER SECTION:
89.238.43.174.in-addr.arpa. 0   IN      PTR     89.sub-174-43-238.myvzw.com.
```

---

☀️ **Hop hop hop**

```bash
telos@TelosGVNG:~$ nslookup ynov.com

Non-authoritative answer:
Name:   ynov.com
Address: 172.67.74.226
Name:   ynov.com
Address: 104.26.10.233
Name:   ynov.com
Address: 104.26.11.233
Name:   ynov.com
Address: 2606:4700:20::ac43:4ae2
Name:   ynov.com
Address: 2606:4700:20::681a:be9
Name:   ynov.com
Address: 2606:4700:20::681a:ae9
```

---

☀️ **IP publique**

```bash
telos@TelosGVNG:~$ curl ifconfig.me
195.7.117.146
```

---

☀️ **Scan réseau**

```bash

telos@TelosGVNG:~$ sudo nmap -sn 10.33.64.0/20
[...]
Nmap done: 4096 IP addresses (530 hosts up) scanned in 1076.29 seconds
```
![Stop it](./img/stop.png)

# III. Le requin

Faites chauffer Wireshark. Pour chaque point, je veux que vous me livrez une capture Wireshark, format `.pcap` donc.

Faites *clean* 🧹, vous êtes des grands now :

- livrez moi des captures réseau avec uniquement ce que je demande et pas 40000 autres paquets autour
  - vous pouvez sélectionner seulement certains paquets quand vous enregistrez la capture dans Wireshark
- stockez les fichiers `.pcap` dans le dépôt git et côté rendu Markdown, vous me faites un lien vers le fichier, c'est cette syntaxe :

```markdown
[Lien vers capture ARP](./captures/arp.pcap)

---

☀️ **Capture ARP**

- 📁 fichier `arp.pcap`
[ARP.pcap](ARP.pcap)

(Filtre : (arp.src.proto_ipv4 == 10.33.76.222 && arp.dst.proto_ipv4 == 10.33.79.254) || (arp.src.proto_ipv4 == 10.33.79.254 && arp.dst.proto_ipv4 == 10.33.76.222)
)

---

☀️ **Capture DNS**

- 📁 fichier `dns.pcap`
[dns.pcap](dns.pcap)

```bash
telos@TelosGVNG:~$ dig google.com
```

(Filtre : dns)

---

☀️ **Capture TCP**

- 📁 fichier `tcp.pcap`
- effectuez une connexion qui sollicite le protocole TCP
- je veux voir dans la capture :
  - un 3-way handshake
  - un peu de trafic
  - la fin de la connexion TCP

> Si vous utilisez un filtre Wireshark pour mieux voir ce trafic, précisez-le moi dans le compte-rendu.

---

![Packet sniffer](img/wireshark.jpg)

> *Je sais que je vous l'ai déjà servi l'an dernier lui, mais j'aime trop ce meme hihi 🐈*