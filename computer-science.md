# Computer Science

# A - Level

Control Unit - controls, coordinates CPU activity - directs flow of data between CPU & devices, decodes instructions, stores resulting data back in memory/registers
Bus - set a of parallel wires connecting computer components - 8,16,32,64 lines
address bus - when CPU sends address to memory - transmits memory addresses of words used in instructions, so data can be retrieved & sent to processor.
data bus - sends data returned to CPU - 8,16,32,64 lines - bi-directional - moving data and instructions
  - when instruction is performed and result is stored at particular memory location, data bus used
control bus - sends control signals - bi-directional - transmit command, timing, specific status info between components:
  - Bus request - indicates device request data bus
  - bus grant - indicates CPU grant data bus
  - Memory write - data on data bus written into addressed location
  - Memory read - data from addressed location placed on data bus
  - Interrupt request - device request access to CPU
  - Clock - synchronises operations
word - unit of memory - fixed size group of digits - 16,32,64 bits - handled by processor
  - each word has own specific address 
ALU(Arithmetic-Logic Unit) - performs arithmetic & logical operations, shift operations, boolean logic operations - AND, OR, NOT, XOR
Registers - very high speed special memory cells - temporarily stores all operation results
Accumulator - 
PC(Program counter) - holds address of next instruction to be executed 
  - if current instruction is a branch/jump, holds address to jump to, copied from CIR
Current Instruction Register(CIR) - holds current instruction execuded, operand and opcode
MAR(Memory address register) - address of memory location from which data is to be fetched or written
MDR(Memory data register) - temporarily store data read/written to memory - aka memory buffer register

### OOP
- works best in situations where you can encapsulate and model entities as objects.
- useful for GUIs
- computer games are a good example of the use of OOP - characters,players, items, enemies etc with methods
- Advantages:
  1. Code reuse - can use in other programs - faster program development
  2. encapsulation reduces complexity - can hide methods & attributes from user
  3. Maintenance easier - can troubleshoot and modify program easier
  4. Reinforces security










# GCSE
## Paper 1 - Computer Systems

### Components of a Computer System
Hardware - physical items in a computer system - you can see them
Software - programs or applications that computer system runs (e.g Operating System)
General purpose computer - designed to perform many tasks
Dedicated systems - designed for one particular function
Embedded system - systems, usually dedicated, built into another larger device. (E.g: Calculator, washing machine, car navigations, ATMs.) - uses firmware
  - Adv: Low energy consumption, robust & durable - tend to last longer
  - Dis: difficult to program, hard to repair


CPU - Central Processing Unit - processes all data & instructions (from memory) - fetch-decode-execute cycle - executes instructions
Control Unit(CU) - decodes, executes instructions in cycle || controls flow of data in (to registers) and out (main memory, input/output devices) of CPU || controls hardware
Arithmetic Logic Unit(ALU) - performs all calculations, logic operations and binary shifts needed - stores result in accumulator
Cache - very fast primary memory - stores frequently used data for quicker access by CPU - more expensive, lower capacity than RAM, slower than registers, faster than RAM.
Level 1 Cache - quickest, lowest capacity (64KB) - closest to CPU 
Level 2 - slower, bigger capacity (512KB)
Level 3 - slowest, highest capacity (2MB)
Register - temporary stores for data being used in CPU
##### Fetch-decode-execute cycle - PURPOSE OF CPU:
Fetch:
1) Program counter checked - holds address of next instruction
2) Address sent to MAR - uses address to fetch instruction from main memory(RAM,Cache) - brings it to MDR
3) Program counter incremented by 1 - go to next instruction
Decode:
- CU converts data/instruction in MDR into machine code to be understood - machine code different for every manufacturer of CPU.
Execute:
1) If instruction needs to perform a calculation then ALU performs calculation - stores result in AC - otherwise instruction goes straight to AC 
 - This process repeats millions of times per instruction
### CPU Performance
Speed of computer measured in Hz or GHz
Hertz - how many F-D-E cycles are performed per second (4 GHz = 4 Billion cycles)
Core - individual processing unit in CPU - can process 1 instruction at a time
1) Cache Size - more gives faster access to more data - if cache fills up, some commonly accessed instructions have to be stored on further level - slower. More = stays fast on higher capacities
2) Cores - more cores means more instructions can be carried out at once = faster processing - 2 cores doesn't mean 2x speed as software might not need to use full capacity of both cores
3) Clock speed - number of instructions processor can carry out per second - speed of core (Hz) = upgrading this will always mean faster processing


### System Software
Operating System - OS - complex piece of software - manages hardware and runs software. Main functions:
   1) Communicate with hardware(internal & external) by device drivers
   2) Provide user interface
   3) Provide a platform for different applications to run
   4) Controls memory resources and CPU - allows computer to multi-task 
   5) File management, disk management
   6) Manage security of system - through user accounts
Multi-tasking OS - can run multiple applications at once
1) Device drivers - 'translators' between OS to hardware - software to communicate with internal hardware/peripherals 
- every piece of hardware has a driver
- When computer booted up, OS chooses correct drivers for the hardware
- If new hardware is connected, system will install the new, matching driver
- Device manufacturers can release updates to drivers to fix bugs, add features or improve performance of hardware.
2) User interface - allows user to interact with computer system 
    - GUI - Graphical UI - visual, interactive, intuitive - optimised for specific input methods - WIMP (Windows, Icons, Menus, Pointers) or touchscreen - Android, iOS - use finger gestures like swiping, pinching 
    - Command-line interface - text based - user enters specific commands for tasks - less resource heavy than GUIs - for advanced users, far more efficient and powerful than GUIs - can automate processes using scripts
3&4) OS helps CPU carry out multi-tasking by efficiently managing memory and CPU processing time: (app = application)
   - When app opened, OS moves necessary parts of app to memory, + additional parts when required. OS decides if apps or features been used recently - if not, maybe removed from memory
   - multiple apps=OS makes apps not overwrite/interfere another. A memory manager allocates certain apps certain memory addresses, so their processes are placed in separate locations
   - Only one process processed by CPU at once - OS divides CPU time between open apps, prioritises processes in order for most efficient order
   - When required, OS organises movement of data to and from virtual memory
5) File & disk management - organisation of data in a useable hierarchical structure - movement, editing, deletion of data.
   - file extensions (.jpg, .mp3, .mpeg) tell computer which software used to open file
   - hard disk managed by OS - splits physical disk into storage sectors, decides which sectors to write data to, keeps track of free space of disk.
   - Utility software - helps maintain or configure a computer.
      - file compression software - reduces size of files
      - encryption software - securs contents of files
      - Defragmentation software - helps organise and maintain hard disk by collecting all free space together
6) User accounts - OS can be single-user or multi-user:
  - Single user OS - allow only one user to use computer at once. (Windows 10, OS X). Even if computer has multiple user accounts or is connected to a network, still single-user.
  - Multi user OS - allow several users to use computer at once. Often used on mainframes and give many users simultaneous access. e.g ATMs allow thousands of people access to a bank's mainframe at same time (eg. UNIX server)
User account control - allows different users to be granted access to specific resources on a computer.
 - On most desktop OS, each user has their own personal data and desktop, but cant access other users' data
 - OS may have anti-theft measures to prevent other users from accessing locked devices/accounts to steal info. Accounts may be password, PIN, fingerprint, specific patterns or face ID protected
###### Utility Software
Defragmenting - reorganising storage on HDD to put fragmented files back together, & collects all free space to prevent further fragmentation. | Fragmented files makes reading & writing much slower as R/W head has to move back and forth.
 - An SSD uses flash storage(no moving parts) - cant be fragmented - can access data quickly no matter how arranged. SSDs have a limited number of read/writes, defragmenting shortens lifespan
Backup - copy of files and settings stored externally. Data can be recovered in event of data loss
Backup utility - software wtih facilities like scheduling regular backups, rescue disks, disk images, options of full or incremental backups.
Full backup - copy is taken of every file on system. Use a lot of storage space - take a long time to create, but faster to restore from
Incremental backup - only files created or edited since last backup copied. Use Less storage space, much quicker to create. A full system restore is slow as last full backup must be restored, and every incremental backup since then.
Compression software - reduces size of files to take up less disk space. Used loads on internet. (.zip, .rar). Compressed files need to be extracted before used.
Encryption software - encrypts data to stop third-parties from accessing it. Can be decrypted using a special 'key'
#### Open Source vs Proprietary
Open Source Software - software where source code is freely available. Users can legally modify source code to create own spin-off software, that can be shared under same license and terms as original. (Examples: Apache HTTP server, GIMP, Firefox, VLC, Linux)
  - Linux is hugely successful open source OS released in 1991 - most popular linux based OSs are: UBUNTU, Debian & Android
  - Popular open source software is always supported by a strong community - users actively help improve software
Advantages:
1) Usually free
   1) Made for greater good - not profit - benefits everyone, encourages collaboration, sharing of ideas
2) Software adapted by users to fit needs
3) Wide pool of collaborators can be more creative and innovative than original programmers.
4) Popular software - very reliable and secure - any problems quickly solved by community.
Disadvantages:
1) Small projects may not be regularly updated - can be buggy/have unpatched security holes
2) Limited user documentation
3) No warranties
4) No official customer support
5) Companies using open-source custom code may not want competitors to see their code, but have no choice
Proprietary software - closed source - paid for - only compiled code is released & source code is closely-guarded secret. Licenses restrict modification, copying, redistribution of software.
 - Businesses often use proprietary as it tends to have better customer support options. 
 - Examples include: Microsoft(Office, Windows, Outlook) and Adobe(Photoshop, Illustrator)
Advantages:
1) Comes with warranties, documentation, customer support
2) Well-tested and reliable as company's reputation depends on it. Fixes & updates more regularly or scheduled
3) Usually cheaper for business - dont need to develop custom software
Disadvantages:
1) Expensive
2) May not exactly fit users needs
3) Software companies may not maintain older software after warranties expire - want people to buy latest product


### Memory
Main Memory - where all data, files, programs are stored when being used
Primary storage - Memory CPU can access very quickly: (Registers, Cache, RAM, ROM, flash memory)
- fastest read/write times
- mostly volatile
RAM - main memory in computer - can be read & written to - volatile - slower than CPU cache
ROM - Read Only Memory - can only be read - non-volatile - built into the motherboard. 
- Contains BIOS(Basic Input/Output System) - all instructions needed for a computer to boot up. 
- Copies OS into RAM.

Secondary storage - non-volatile - where all data is stored when not in use: Magnetic HDDs, SSD, CD, Magnetic tapes, SDs
- read/write times are alot slower than primary storage
1) HDD - internal storage in PC/laptops 15000rpm - data stored magnetically in sectors within circular tracks, read/write heads access sectors on disk 
- long lasting, reliable, cheap, high capacity | less portable, durable, slower
2) SSD - no moving parts - most use flash memory - internal storage 
- significantly faster read/write times than HDD - fastest secondary storage
- dont need defragmenting
- more shock-proof
- silent
- shorter R/W life
- hybrid drives exist, using SSD to boot up computer and HDD for data
- limited number of read/writes - defragmenting shortens lifespan
3) Optical discs - CD, DVD, Blu-ray - CD = 700 MB, DVD = 4.7GB, Blu-ray = 25GB,
  Read-only (CD-ROM, DVD-ROM, BD-ROM) - Write-once(CD-R, DVD-R, BD-R) - rewriteable(CD-RW, DVD-RW, BD-RW)
- cheap, portable, durable from water or shocks
- use is declining, low capacity
- very slow R/W times
- poor reliability
4) Magnetic tapes:
- greater capacity than HDDs (very high)
- extremely low cost per GB (cheapest S.Storage)
- very slow when finding specific data, but fast R/W speeds when data in correct place.
- Often used by large businesses in archive libraries to store huge amounts of data


### Networks
LAN - Local Area Network - small geographical area located on a single site - all hardware owned by organisation - wired or wireless - in homes, businesses, schools, universities etc.
Advantages:
- Sharing files is easier - network users can access same files, work at same time and copy files between machines
- Can share same hardware (eg printers)
- Internet connection shared to every device
- Can install and update software on all computers at once
- cheap, easy communication with other members - instant messaging
- User accounts stored centrally - users can log in from any device
Disadvantages:
- Increased security risks to data - Malware/viruses spread easily between computers
- If server fails, computers connected to it don't work
- Computers may run slowly if lots of data travelling on network
WAN - Wide Area Network - large area, connecting multiple LANs together - Infrastructure between LANs leased from telecommunication companies - own, manage it - connected by telephone lines, fibre optic cables, satellite links
Switch - hardware - sends data between computers on a LAN - recieve data in frames, segment traffic by forwarding traffic to correct computer, using MAC address.
  - Usually connected by UTP copper cable - cheap, flexible = easy to install
Router - sends data between different networks with packets - creates WAN - uses an IP to route traffic
  - Usually connected with fibre optic cable - higher bandwidth, suffers less from interference
WAP - allows devices to connect wirelessly, as a switch
NIC - built-in hardware - allows devices to connect to a network - connects to router/WAP - every NIC has a MAC address
- Difference between IP/MAC address:
    - 1) IP = WAN, MAC = LAN, 2) MAC = provided by manufacturer, IP = provided by service provider, 3) MAC = actual device, IP = destination/address
Bluetooth - direct connection between 2 devices, connection range = 10m, low bandwidth - 2.4GHz or 5GHz
Wifi - used by multiple devices, range = 40-100m, higher bandwidth, used in routers, desktops, laptops.
2 GHz - Adv: Greater range/coverage \\ Dis: More interference from other devices - crowded frequency
5 GHz - Adv: Less crowded - higher transmission rates \\ Dis: Less able to penetrate through objects/walls
Network performance; affected by:
  - Wireless/Wired - + type of wire being used - fibre optic fastest
  - Bandwidth
  - Range 
  - No. of people on network
  - Obstacles between connecters - wireless - walls, distance, other devices
Server - computer that manages and stores files, or provides services to other computers
Client - computer that relies on servers to provide data - have no control over network
Peer - computer equal in rights and control as every computer on network - store own files
Client-server network - data hosted on main server and accessed by client devices - server manages access, security, internet, printing, emails, backups - client makes requests to server for data
  - Adv: Easier to manage security
    - Easier to do backups of all data
    - Easier to install software updates
  - Dis: Expensive to setup & maintain
    - Requires IT staff
Peer-to-peer(P2P) network - all computers are equal in responsbility and status - no central switch - store own files and can be accessed by other peers. Both client and server
  - Adv: Very easy to maintain
    - Specialist staff not needed
    - No dependancy on single server
    - Cheaper - no expensive hardware needed
  - Dis: Network less secure
    - Users need manage own backup
    - Viruses, malware more easily transferred over - no central firewall
    - Difficult to maintain well-ordered file store
Cloud Computing Applications - Google Drive, Onedrive, Dropbox - potentially limitless

### Topologies - layout of network
Star - all devices connected to a central switch:
-  Adv: If one device fails, network unaffected
   -  Fast data transfer to hub - wires arent shared - no interference
   -  Easily add devices
-  Dis: If central switch fails, whole network fails
   -  Needs additional hardware - switch, cables 
Ring - Data moves in one direction - removes collisions - only one device can send data at once
Bus - slow - data collisions on single backbone cable
Mesh - Each device connected to every device - partial mesh used with star topology to create larger networks
- Adv: can send data fastest route.
  - no single point where network can fail
  - Wireless mesh have massive potential to provide Wifi for organisations, cities, even countries
  - data can be sent simultaneously
  - new nodes can be added without interruption/interference
- Dis: very expensive - need a lot of wire
  - Network maintenance and administration is dufficult
  - Some routes may be redundant - waste

### Protocols & Packets
Internet - massive WAN all over world - based around TCP/IP
- Internet is hardware of network - WWW is data, collection of websites hosted on web servers, accessed through http
Packet switching - process of data broken down into packets, then reassembled in order at destination - file broken into packets of 512 bytes
 - Data split into packets, numbered - each packet sent fastest route across internet by routers - rearranged in order by packet numbers - if packets missing - timeout message sent.
 - each packet given: IP address of destination, IP of where sent, packet number to be put back in order, error checking data
Protocol - set of rules for how devices transmit data across a network
#### Layers 
- protocols divided, protocols with similar functions grouped
Layer 1: Data Link - Send data over network (cables/physical network) - Ethernet
2: Network - Direct data packets, handle traffic, used by ROUTERS - IP
3: Transport - Control flow of data (protocols, packet size, speed) - TCP
4: Application - Turn data into app/website - HTTP, FTP, SMTP
Advantages:
- Each layer independent - can be modified without disrupting other layers
- Breaks communication into manageable pieces - developers concentrate on one area on its own
- Set rules for each layer = companies make compatible, universal hard+software, brands can work with each other in same way.

### Internet
Internet - network of networks - global WAN - based around TCP/IP
WWW - collection of websites | hosted on web servers - HTTP
URL - address to access web servers and resources - protocol :// domain - linked to an IP / Path - specific page
DNS - Domain Name Server - translates domain into IP address 
Cloud - internet hosting for general storage & online software::
Hosting - business using its servers to store other business' files
Advantages: Can access from any connected device 
 - Easy to increase storage
 - No expensive hardware
 - No IT staff management
 - Provides security & backups for you, updates automatically
Disadvantages:
 - Needs internet connection
 - Dependent on host for security/back-ups
 - Vulnerable to hackers/malware !!!
 - Subscription fees for software



### Network Threats - Malware
Malware - malicious software - installed on a device without person's knowledge or consent
Types of Malware (3 main ones):
1) Virus - copy themselves & attach to certain files (.exe, autorun scripts) - users spread them by copying them - activate them when file is opened
2) Worms - viruses that self-replicate without user help - spread very quickly - exploit weaknesses in network security
3) Trojans - malware disguised as real software - don't replicate, users install them through links
Actions of malware:
1) Scareware - tells user their computer is infected - scare them into malicious links or paying to fix problems
2) Ransomware - encrypts all files on computer - demands money in exchange for decryption key
3) Spyware - secretly monitor users actions (key presses), sends info to the hacker
4) Rootkits - alter permissions - give malware and hackers administrator-level access to devices
5) Backdoors - holes in security used for future attacks
##### Attacks:
Passive attack - monitors data travelling on a network and intercepts any sensitive information - network-monitoring ware like packet sniffers - hard to detect - best defence: encryption
Active attack - someone attacks a network with malware/ planned attacks - more easily detected - best defence: firewall
  - Brute force attack - type of active attack - gain information by cracking passwords through trial and error - automated software to produce hundreds of likely combinations - defences: account lock after number of failed attempts, strong passwords
Insider attack - person within organisation exploiting network access to steal information
Denial-of-service (DoS) attack - hacker stops users from accessing a part of network or website - involve flooding network with useless traffic - make network extremely slow or inaccessible

Social engineering - gaining sensitive information|illegal access to networks through influencing people, usually employees
Phishing - sending emails/texts to people pretending to be from well-known business - contains links to spoof websites - enter personal information - hackers access their genuine account (Vishing, smishing, whaling, angler, pharming)
 - Vishing - voice phishing - phishing over voice calls - asks them for personal info
 - Smishing - SMS(text) phishing - phishing with mobile texts
 - Whaling - phishing directed at high-level executives - pretends to be a known, trusted person
 - Angler - social media phishing - e.g pretending to be customer support to get details
 - Pharming - redirecting people to fake malicious websites - enter personal info - harder to identify
 - Ways to tell its fake: poor grammar/spelling, check the email @ is correct, suspicious links, sense of urgency 
SQL injections - used for weak validation, insecure SQL databases - pieces of SQL typed in a websites input box that reveal sensitive information - "1=1" is always true in SQL 
##### Network policies:
Penetration testing - organisation employ specialists to try to attack their network - identify weaknesses
Network forensics - investigations undertaken to find cause of an attack - system to analyse data packets entering network - discover how & prevent future attacks
Passwords - prevent unauthorised access - strong passwords - 10+ characters long, upper and lowercase, numbers and symbols, changed regularly
User access levels - different users can access more parts of network - help limit number of people with access to important data - prevents insider attacks, harder to scam network
Anti-malware - software designed to find and stop malware from damaging network - e.g antivirus programs
- firewalls - block unauthorised access - examine all data entering and leaving network, block any potential threats
Encryption - data(plain text) translated into unreadable cipher text - only person with decryption key can access - essential for sending data over network securely - prevents passive attacks etc.
  - Private key(Symmetric) - one key used to encrypt & decrypt data - must be given to recipient to decrypt
  - Public key(Asymmetic) - two keys used - one public key to encrypt, and a personal private key to decrypt - more secure as you never have to reveal/share your decryption key

### Data representation
Binary addition - 0+0=0, 0+1=1, 1+1=0(carry 1) | 1+1+1 = 1 carry 1
Binary shift - Left = multiply, Right=divide
Character set - collection of characters recognised/represented by a computer system (by binary number)
ASCII - 7-bit character set - (128 characters) - uses less memory space
ASCII extended - 8-bit - 256 characters
Unicode - 16/32-bit - 65,000+ characters - every possible character in every language

Pixel - smallest area of an image - 1 dot
Images - made up of pixels. Colour of each pixel is a binary number
Colour depth - no. of bits used for each pixel (Bit depth)
  - 2^(number of bits) = no. of colours
  - improves quality, bigger file size
Resolution - concentration of pixels in an area - given as WidthxHeight - dpi(dots per inch) - higher resolution = better quality, bigger file size
Metadata - information about image file, stored within it. (e.g height,width,colour depth,resolution, format, image time&date)

Analogue sound - a pressure wave causing air to vibrate - computer cant interpret
 - Amplitude - height - Volume
 - Frequency - wavelength - pitch
Speakers etc - sound converted from digital back to analogue - vibrating cone causes pressure waves
Sound - has to be converted from analogue --> digital to be stored by computer. Done by sampling:
Sampling - Amplitude measured at regular intervals, creates digital representation of wave.
  - more frequent samples = more accurate = better quality, bigger file size
  - Sample rate = rate of interval recordings
  - Can also improve quality by increasing no. of bits representing each sample (Sample resolution)

Compression - makes file size smaller - data faster to send, quicker to download, faster to load, less storage space
Lossy - permanently removes some data from file - image/audio lower quality (JPEG, MPEG, MP3)
  - data transfer of file quicker
  - useful for data not fully needed, can store more data and it runs quicker
Lossless - data temporarily removed, put back together when file opened. - useful for files that need all data in (PDF, GIF, Text documents, .exe)
  - reduces file less than lossy
  - one method - RLE(run-length encoding)
RLE - sequences displaying redundant data stored as single value
 - e.g - a,a,a,b,c,c,c,c = a3,b1,c4

### Legislation laws
#### Legal
Data protection Act 2018 
- data must be fairly & lawfully processed
- used for intended purposes
- must be relevant, accurate and up to date
- musnt be kept for longer than necessary
- must be handled with security
Computer Misuse Act 1990 - illegal to access data you're unauthorised to (referred to hacking), with intent of further offences or to modify data (malware)
Copyright Designs and Patents Act 1988 - cant copy, modify, distribute, sell any type of material without owner's permission
#### Ethical
moral principles, rules by society. include:
- ensuring public safety - most important
- security of data - data is safe and trusted by customers
privacy, censorship, surveillance
#### Cultural
Effects on nature/culture of society:
- digital divide - divide between people with access to tech and people without - age or money - limits information access
- changing nature of employment - working from home, e-communication, machinery stolen some jobs (warehouse packaging) \\ more high skilled work available to maintain automated systems
#### Environment
materials used for manufacturing computers + energy used - web servers, DNS, data centres need 24/7 energy to maintain
- E-waste - throw away working devices because we want to upgrade - smartphone every year, computers ever 3-4 yrs
- 





## Paper 2 - Computational Thinking, Algorithms and Programming

Casting - changing a data type
Module - external python file which often contains functions
Structured (modular) programming - decomposing the program that you want to write into manageable modules - short, simple, easy to understand
Trace table - table to test that a program is working - shows output of program - can find errors
Random integer = randint(1, 6) (from 1 to 6)
### Algorithms
#### Computational Thinking
Decomposition - breaking a complex problem into smaller problems to solve individually
Abstraction - filtering unnecessary information, simplifying to important information in a problem
Algorithmic thinking - logical way of solving problems, step by step solution

Algorithm - ordered set of instructions to complete a task
Pseudo-code - universal - follows similar structure of every coding language - easily readable - can be converted into any programming language - used to figure out structure of program
Flowcharts - diagram showing algorithms, using different symbols, arrows.
 - Start/End - oval
 - Decision - Diamond
 - Input/Output - parallelogram
 - Process - rectangle - rectangle with 2 lines on each end = subroutine

Binary search - start in middle, slice - Adv: More efficient than linear, Dis: complex to program, only ordered lists
Linear search - start from beginning, check each item - Adv: any list, Dis: not efficient - long time with long lists

Bubble sort - compares first two values, swaps, moves to next value - biggest value to right - Adv: Simple, Dis: long time
Merge sort - decomposition method - find middle, split, sort, merge back - Adv: (Most) Efficient, Dis: Slow
Insertion sort - compares each value to first value, swaps - biggest value to left - Quick for small lists, slow for long

### Programming
Data type - String, Integer, Boolean, Real, Character
Variable - identifier with name that stores value - can be changed in run-time
Constant - variable that **cant** be changed whilst program is running
Local variable - can only be used in the structure they're declared in (subroutine)
Global variable - variable that can be used anywhere in code, after declared
Exponentation - powers - e.g 2**3 or 2^3 
Quotient DIV - DIV - integer division
Modulo division -  MOD - Remainder - %
Array - data structure - can store  group of values, of one same type, under one name
1D-Arrays - list 
2D-Array - table - lists within a list  
Sequence - order of instructions carried out chronologically in program
Selection - when program **interacts** with user - decisions
Iteration - when the program uses repitition/loops (For, Repeat(do)-until, while)
- Indefinite iteration - (Condition-contolled) when the loop repeats until a condition is met - WHILE, DO-UNTIL
- Definite iteration - (Count-controlled) when loop repeats exact number of times instructed. - FOR
- Nested iteration - loop inside another loop
CASE statement - performs different actions for different values of same variable
#### String manipulation 
x.length - Outputs length of string (Starts at 1)
x.upper - changes string to all upper case
x.lower - string all lower case
x(i) - Outputs character in position of integer(i) (Starts from 0)
x.substring(a,b) - Gives characters from a with length b. (e.g x=word, x.substring(2,2) = "rd")
#### File handling
file = openRead("myfile.txt") - Opens file in read mode
file = openWrite("myfile.txt") - Opens in write mode
file.writeLine("Hello") - Writes line to file
file.readLine() - Reads 1 line of file
file.close - closes files
file.endOfFile() - determines/checks end of file

### Databases

Sub-program - set of instructions stored under a name, which can be called to run whole set
Function - Sub-program that returns a value
Procedure - doesnt return a value
Parameter - variables  passed as a value into subroutine
Argument - the values that you assign to the parameters
Database - persistent store of related data - stored in records, stored in files
Attribute - one item of data
Record - data structure - can store different data types - single row in a data table
 - each item of data written to or from a file
Field - each data items within a record - columns in the data table - data type, name
SQL(Structured Query Language) - language used to manage relational databases and perform various operations on data in them
  - SELECT - * or name of column - what you want displayed to you
  - FROM - (name of table)
  - WHERE - condition - AND,OR, % or LIKE

### Defensive Design
Defensive design - programmers test their code to: reduce number of errors, prevent misuses, for well-maintained code
Input sanitisation - removes any unwanted characters entered into program
Input validation - Checks if data meets certain criteria before passing it through program. Following checks can be used:
 - Presence check - data has been entered
 - Length check - data is correct length
 - Range check - data within set range
 - Format check - in correct format (e.g dd/mm/yy)
 - Check digit - numerical data entered correctly
 - Look-up table - checks against a table of accepted values
Authentication - program confirms identity of user before giving access to full program. - user accounts, passwords
Maintainability - well-maintained code = easy to edit without causing errors:
 - Comments - other programmers understand code, easier to read
 - Indentation - easy for programmers to see flow of diagram - easier to read, can convert to other languages easier
 - related variable/subprogram names
#### Testing
Final testing - program tested once at end of development - all in one go
Iterative testing - tested & changes made throughout development cycle - may go through process few times
Test plan - test to see if a program input is working by testing its boundaries
Normal data - valid data that user would input into program
Boundary data - data on boundary of what program should accept
Erroneous data - data the program shouldn't accept
Syntax error - doesn't follow rules or grammar of the language(SPaG error) - computer doesnt understand - program doesnt run
Logic error - unexpected output - program does run but returns an unexpected output (human error)
Functionality testing 
 - Performance - how quickly features run, impact on computer resources
 - Usability - how user-friendly interface and features are
 - Security - test vulnerability to attacks & how securely data stored
 - Load/Stress - how it copes under extreme conditions (loads of users)
Testing flow chart - Requirements, Design, Implementation, Testing, Maintenance
### Logic gates
NOT gate - output is opposite of input (0, 1)
AND gate - if both inputs are 1, then output is 1. Otherwise 0. (0, 0, 0, 1)
OR gate - if one or more inputs is 1, output is 1. The output is only 0 if all inputs are 0 (0, 1, 1, 1)
XOR gate(not needed) - exclusive OR - if exactly one input is 1, output is 1. Otherwise output is 0. (0,1,1,0)
A and B - A ^ B
A OR B - A v B
NOT A - ¬A
Truth table - show all possible combinations of inputs and outputs in circuit
- Computers use binary to represent flow of electricity in circuits. 1=on, 0=off
Bit - single binary digit
Nibble - 4 bits
Byte - 8 bits
KiloByte(KB) - 1000 bytes
Megabyte(MB) - 1000 Kilobytes
Gigabyte(GB) - 1000 Megabytes
Terabyte(TB) - 1000 GB
Petabyte(PB - 1000 TB)

### Languages
High level language - need to be translated into machine code - cannot be understood by computer (Python, java)
 - Each instruction is many machine code instructions
 - Code transferable to many different computers and processors
 - Data stored in structures (lists, arrays)
 - Easy to read, understand
 - Dis: Less memory efficient - no control over CPU
Low level language - Machine code(binary) & Assembly:
 - written for one particular machine/processor
 - programmer needs to understand how CPU manages memory
 - Difficult to read, understand
 - Machine code can be executed without translators
 - More memory efficient - control what CPU does

Assemblers - turn assembly language to machine code
Compilers - Translate all code in one - creates executeable file. (Source code --> assembly --> machine)
 - can take a long time, but final code runs quickly
 - gives list of errors for entire program
 - Adv: Execution faster, no need for translation software at run-time, code optimised
 - Dis: Source code easier to write in high-level, but program wont run with syntax errors - more difficult
   - code needs to be recompiled when changed
   - Designed for specific type of processor
Interpreters - translates source code one line at a time. - code translated every time it runs
Adv: - Easy to write source code - program always runs, stops when finds syntax error
     - does not need to be recompiled when changed - easy to try out commands when program finds error
     - easy for beginner programmers to learn to write code
Dis: - Translation software needed at run-time
     - Slower
     - code not optimised
     - source code is needed
IDE(Integrated Development Environment) - software with features that help programmers code
 1) Editors - line numbers, colour coding for different features of code
 2) Run-time environment - lets programmer run code quickly to test for errors
 3) Debugging tools - help find and solve errors
 4) Translator - translate code into machine code
 5) Breakpoints - stop program on certain lines







## year 10 

### Revision

- Concatenation is when you join 2 strings together
- You can find the length of a string by using the len() function
    - len("Hello") would give 5
- A substring is a part of a longer string
    - In psuedocode, we use the function: stringname.subString(StartPos, numberOfChars)
        - This takes a substring starting at the 'startPos'th character, and takes the number of stated characters
- Types Of Errors
    - Syntax Errors
        - A syntax error is a mistake or error in the way the code is written
        - Syntax errors prevent programs from running as a translator needs code to be syntactically correct.
        - Examples
            - example of an error : prnt("Hello,  World!");
                - Spelling error
            - another example: newbalance = newBalance * 1.05;
                - Wrong capitalisation
            - error: myBoolean = True NOT False;
                - NOT does not take two operands
    - Logic errors
        - Logic errors are hard to detect because the translator will not detect them for us
        - Logic errors are mistakes in the logic of the program
        - The program will run but the outcome will not be as intended
        - Examples
            - Mixing up AND and OR: True AND False = False, True OR False = True
    - Runtime Errors
        - Runtime errors are errors that Happen while the program is running.
        - Runtime errors cannot be found during translation
        - These errors can only be detected while a program is running\
        - The chance of experiencing a runtime error can be reduced through testing.
        - Examples
            - Bad inputs that throw out an unhandled exception
            - Receiving unexpected or corrupted data
            - Running out of memory
- Python
    - Python is a high-level interpreted programming language
    - Python is used for general purpose programming
    - One of the key considerations in Python development is the readability of code.
    - Programming Paradigms
        - Programming Paradigms are different styles of programming
            - Python is a multi-paradigm language and allows code to be written procedurally or in an object oriented style.
- Fetch Decode Execute cycle
    - Fetch:
        - The program counter is checked as it holds the address of the next instruction to be executed.
        - The address is sent to the Memory Address Register (MAR) - holds address of where data is to be fetched or stored from - in order to fetch the instruction needed from Main memory (Cache or RAM) and bring it to the Memory Data Register (MDR).
        - The PC is incremented by 1.
    - Decode:
        - The MDR sends the instruction to the Control Unit (CU), which decodes and converts the data into binary so it can be understood.
        - Machine code is different for every manufacturer of CPU.
    - Execute:
        - The instruction is sent back to the Cache to pass the instruction of that address, and place it in the MDR.
        - If the instruction has to perform a calculation, then it will be sent to the Algorithmic Logic Unit(ALU) to do the calculation. It will then store the result in the accumulator.
        - If not, then it will go straight to the accumulator
- Hertz - how many full cycles of F.D.E cycles can be performed in 1 second.
- Clock speed - the speed at which a computer operates.
- Core - processing unit within a CPU
- Embedded system - a system with a dedicated purpose and is limited to what it can do. eg - Microwave, TV, toaster, camera, kettle, wifi router, radio, satnav. difficult to program and hard to repair
- 

- Test Revision
    - Data types
        - String
            - A piece of text eg ‘Hello’
        - Real
            - Any number eg 3.67
        - Integer
            - A whole number eg 5
        - Boolean
            - True or false
    - Casting
        - Casting is the process of converting data from one type to another.
        - One of the most common reasons for casting is output.
        - Output must be formatted as a string, and so we may need to convert a certain piece of data to a string.
        - All input also comes as a string, and must then be converted to other data types.
        - Casting to a string can be done with the str function
            - str(5) gives 5
        - Casting to an integer can be done with the int function
            - int(5.4) gives 5
        - Casting to an float can be done with the float function
            - float("3.7") gives 3.7
    - Operators
        - DIV is integer division, it returns the whole part of a division
        - MOD gives the remainder of a division
        - Addition is +
        - Subtraction is -
        - Division is /
        - Multiplication is *
        - Exponentiation is ^
    - SQL
        - SELECT,FROM,WHERE
        - SELECT = what is included in your range of data, or the type of data you are selecting
        - FROM = where you get the data from
        - WHERE = the condition that has to be met for it to be selected
        - SELECT * = Selects all
        - 
- Test Revision 2
    - Sound
        - Sound is a pressure wave that causes the air to vibrate
        - A computer cannot interpret an analogue sound wave. It must be turned into binary numbers or digitised.
        - Sample rate - In order for a computer to store sounds digitally, a sample is taken at regular intervals. This is sample rate, measured in Hz
        - The sample measures the voltage and converts it into binary
        - The more samples you take per second, the better the audio quality.
        - Sample resolution - Another way to improve audio quality is increase the number of bits used to represent each sample, or sample resolution
        - Speakers allow devices to generate sound from these binary numbers
        - A vibrating cone in the speaker causes pressure waves, which we hear as sound
        - Amplitude is the height of the wave. Higher the amplitude, higher the volume.
        - Frequency is how close the waves are. Higher frequency is higher pitch
    - Images
        - Image file types
            - BMP
            - JPG
            - GIF
            - PDF
            - TIF
        - Each pixel is a single colour and is given a binary value which represents that colour.
        - Resolution - concentration of pixels within a specific area - defined by width and height - eg. 72x72 is used for web pages
        - Each pixel value represents a different colour, using one bit per pixel
        - Larger image resolution, quality and higher colour depth will increase file size
        - Metadata - data/information about an image - date, author, resolution, file size
