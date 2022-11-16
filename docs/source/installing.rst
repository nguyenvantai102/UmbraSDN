Installing
==========

Prerequisites
*************

Currently, Umbra is developed and tested on Ubuntu 18.04.

There are no strict requirements of hardware for Umbra. It will depend on the size of the network that's being tested, and the configuration of resources to be allocated for nodes and links. 
Therefore, Umbra can be installed and run in different machine configurations, the need of specific hardware specs will depend on the use case being evaluated, which must be correctly dimensioned using the resource constraints for nodes and links available in Umbra.

The main components of Umbra require python 3. All the other requirements can be checked in the build scripts as described below. In general, Umbra uses apt, git and pip to install its requirements.


Main Components
***************

All the Umbra components requirements are installed together with them by the build.sh script inside the build folder.
The steps below contain the Umbra installation commands.

.. code-block:: bash

    $ git clone https://github.com/hyperledger-labs/umbra/

    $ cd umbra/build

    $ sudo chmod +x build.sh

    $ ./build.sh

    $ cd -


Please note, the script above (build.sh) install docker-ce and adds the $USER to the docker group (no need to user sudo before the docker command). To enable this setting, logout and login again, or execute `su $USER` (to start a new session). You can test if it works simply running `docker ps -a`.

When executing this script, it will install all the Umbra python components and their dependencies, and it will install containernet and its requirements.

Notice, two executables will be created, umbra-scenario and umbra-broker.


Requirements for Hyperledger Projects
*************************************

Umbra was designed to support multiple blockchains, so in an independent way each blockchain platform when supported has its own build files also inside the build folder. As such, for each blockchain platform there will be a installation script inside the build folder.
For instance, as Umbra supports Hyperledger Fabric v1.4, installing the requirements to execute Fabric on Umbra can be done with the steps below.

.. code-block:: bash

    $ cd umbra/build

    $ sudo chmod +x build_fabric.sh

    $ ./build_fabric.sh

    $ cd -


When executing this script, it will install the fabric-python SDK, download all the Fabric docker images, modify them accordingly to enable support for containernet functionalities (i.e., they must have the packages net-tools and iproute2 installed on them), and add the binaries configtxgen and cryptogen to the PATH env variable (i.e., as they are required by the fabric-python-sdk, and the umbra-broker component).
