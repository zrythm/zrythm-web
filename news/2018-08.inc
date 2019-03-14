<h3>
2018-08: GSoC 2018 - GNUnet Web-based User Interface
</h3>
<p>
Tue, 08/14/2018 - 07:55 - Phil Buschmann 
</p>
<h4>What was done?</h4>
<p>
In the context of Google Summer of Code 2018, my mentor (Martin Schanzenbach) and I have worked on creating and extending the REST API of GNUnet. Currently, we mirrored the functionality of following commands:
<ul>
<li>gnunet-identity
<li>gnunet-namestore
<li>gnunet-gns
<li>gnunet-peerinfo
</ul>
</p>
<p>
Additionally, we developed a website with the Javascript framework Angular 6 and the design framework iotaCSS to use the new REST API. The REST API of GNUnet is now documented with Sphinx.
</p>

<h4>Why did we create a REST API?</h4>
<p>
... when you can use the command line tools?
We need to keep in mind, that everyone has the right to stay secure and private but not everyone feels comfortable using a terminal. The further developed REST access to GNUnet APIs in addition to the new web application allows new users to interact with GNUnet over a well known tool: their browsers. This addition to the C API and the command line tools may attract new users and developers.
</p>

<h4>How can we use it?</h4>
<ol>
<li>The REST API developed in GNUnet
The REST API is already merged into the gnunet.git repository (GNUnet Main Git).
To use the new features, clone the repository and follow the Installation on gnunet.org. Then, start the rest service with "gnunet-arm -i rest".

<li>The Web Application
The web application is available under the gnunet-webui.git repository (GNUnet WebUI Git).
You need to install the newest version of 'node' and 'yarn'. Dependent on your system, you may need to download newer versions and install them manually and not over your packet manager. After the installation succeeded, you need to clone the repository. Then, you need to run "yarn install" and "yarn start" for testing purposes. To deploy the website (keep in mind, that this website communicates with another localhost instance) use "yarn build" for building the web application and use the output in the 'dist' directory.

<li>The Documentation
The documentation is available under the gnunet-rest-api.git repository (GNUnet REST API Docmentation Git).
Clone the repository and "make html". Then open the 'index.html' under 'build/html/'.
</ol>
<p>
Please, give it a try and contact me, if you find any bugs or unintentional features. ;)
</p>

<h4>What can be improved?</h4>
<p>
Right now, the build process of the web application may be a little too complex for a casual user. We may be able to solve this by using docker.
Additionally, the web application does not prevent wrong inputs but responds with error messages. Adding GNUnet Records is currently only usable for people, who know how a GNS Record looks like. This can be adapted to each record type.
Last but not least, additional features, design changes, etc...
</p>
<p>
Thanks for reading.
</p>
