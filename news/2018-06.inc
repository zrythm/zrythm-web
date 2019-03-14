<article>
<h3><a name="gnunet-0.11.0pre66-release">GNUnet 0.11.0pre66</a></h3>
<p>
Wed, 06/06/2018 - 07:20 - Christian Grothoff<br>
</p>
<p>Download link:
<li>http://ftpmirror.gnu.org/gnunet/gnunet-0.11.0pre66.tar.gz
<li>http://ftpmirror.gnu.org/gnunet/gnunet-0.11.0pre66.tar.gz.sig
<li>http://ftpmirror.gnu.org/gnunet/gnunet-gtk-0.11.0pre66.tar.gz
<li>http://ftpmirror.gnu.org/gnunet/gnunet-gtk-0.11.0pre66.tar.gz.sig
<li>http://ftpmirror.gnu.org/gnunet/gnunet-fuse-0.11.0pre66.tar.gz
<li>http://ftpmirror.gnu.org/gnunet/gnunet-fuse-0.11.0pre66.tar.gz.sig 
</p>
<p>We are pleased to announce the release of GNUnet 0.11.0pre66. 
</p>
<p>This is a pre-release to assist developers and downstream
packagers to test the package before the final release after four
years of development. 
</p>
<p>In terms of usability, users should be aware that there are still
a very large number of known open issues in particular with respect
to ease of use, but also some critical privacy issues especially for
mobile users. Also, the nascent network is tiny (~200 peers) and thus
unlikely to provide good anonymity or extensive amounts of
interesting information. As a result, the 0.11.0 release and
especially this pre-release are only suitable for early adopters with
some reasonable pain tolerance. 
</p>
<h4 class="western">License change</h4>
<p>GNUnet 0.11.0pre66 is the first release that will be made under
the GNU Affero General Public License v3+. After a significant amount
of internal discussion lead constructively by Lynx (thanks!), the
conclusion has been that the IPC and REST APIs should be extended
with support for an GNUNET_MESSAGE_TYPE_AGPL or /agpl request that
enables users of these client/service-style APIs to download the
source code. 
</p>
<p>Naturally, the discussion on licensing may not necessarily end
here, but at this point we are not aware of any dissent in the
community and this release seems to be the right time to make such a
change. While the final decision was not subjected to a broad
feedback round, this was done simply on the grounds that this
placement of the AGPL API seems to addresses all concerns that were
raised. Finally, thanks to the copyright assignment all developers
are participating in, the community will be able to revise this
decision later if necessary. 
</p>
<p>It should also be noted that this change does not impose
additional restrictions on the licensing models of GNU Taler or pEp:
both projects have agreements with GNUnet e.V. that ensure that they
can make decisions that fit these applications (not to mention
significant parts of GNU Taler are already AGPLv3+ already). 
</p>
<h4 class="western">About GNUnet</h4>
<p>GNUnet is a framework for secure peer-to-peer networking. GNUnet's
primary design goals are to protect the privacy of its users and to
guard itself against attacks or abuse. At this point, GNUnet offers
four primary applications on top of the framework: 
</p>
<p>The file-sharing service allows anonymous censorship-resistant
file-sharing. Files, searches and search results are encrypted to
make it hard to control, track or censor users. GNUnet's anonymity
protocol (gap) is designed to make it difficult to link users to
their file-sharing activities. Users can also individually trade-off
between performance and anonymity. Despite providing anonymity,
GNUnet's excess-based economy rewards contributing users with better
performance. 
</p>
<p>The VPN service allows offering of services within GNUnet (using
the .gnu TLD) and can be used to tunnel IPv4 and IPv6 traffic over
the P2P network. The VPN can also be used for IP protocol translation
(6-to-4, 4-to-6) and it is possible to tunnel IP traffic over GNUnet
(6-over-4, 4-over-6). Note that at this stage, it is possible for
peers to determine the IP address at which services are hosted, so
the VPN does not offer anonymity. 
</p>
<p>The GNU Name System (GNS) provides a fully-decentralized and
censorship resistant replacement for DNS. GNS can be used alongside
DNS and can be integrated with legacy applications (such as
traditional browsers) with moderate effort. GNS provides
censorship-resistance, memorable names and cryptographic integrity
protection for the records. Note that at this stage, it is possible
for a strong adversary to determine which peer is responsible for a
particular zone, GNS does not offer strong anonymity. However, GNS
offers query privacy, that is other participants can typically not
decrypt queries or replies. 
</p>
<p>Conversation allows voice calls to be made over GNUnet. Users are
identified using GNS and voice data is encrypted. However,
Conversation does not provide anonymity at this stage --- other peers
may observe a connection between the two endpoints and it is possible
to determine the IP address associated with a phone. 
</p>
<p>Other applications, including in particular the SecuShare social
networking application, are still strictly experimental. 
</p>
<p>For developers, GNUnet offers: 
</p>
<ul>
	<li><p style="margin-bottom: 0in">Access to all subsystems via clean
	C APIs 
	</p>
	<li><p style="margin-bottom: 0in">Mostly written in C, but
	extensions possible in other languages 
	</p>
	<li><p style="margin-bottom: 0in">Multi-process architecture for
	fault-isolation between components 
	</p>
	<li><p style="margin-bottom: 0in">Use of event loop and processes
	instead of threads for ease of development 
	</p>
	<li><p style="margin-bottom: 0in">Extensive logging and statistics
	facilities 
	</p>
	<li><p>Integrated testing library for automatic deployment of
	large-scale experiments with tens of thousands of peers 
	</p>
</ul>
<h4 class="western">Noteworthy improvements in 0.11.0pre66</h4>
<ul>
	<li><p style="margin-bottom: 0in">Improved documentation, converting
	Drupal handbook to Texinfo (thanks ng0!) 
	</p>
	<li><p style="margin-bottom: 0in">GNU Name System now can take over
	arbitrary TLDs, and support for conversion from DNS zones to GNS
	exists 
	</p>
	<li><p>Critical bugfixes in CORE, DHT and CADET subsystems 
	</p>
</ul>
<p>The above is just the short list, our bugtracker lists over 350
individual issues that were resolved (see
https://gnunet.org/bugs/changelog_page.php). 
</p>
<h4 class="western">Known Issues</h4>
<p>We have a few issues that are most likely not resolved in the
final release. Users should be aware of these issues, which we hope
to address shortly. 
</p>
<ul>
	<li><p style="margin-bottom: 0in">There are known major design
	issues in TRANSPORT, ATS and CORE which will need to be addressed
	for usability, performance and security. 
	</p>
	<li><p style="margin-bottom: 0in">There are known moderate
	implementation limitations in CADET that impact performance. 
	</p>
	<li><p style="margin-bottom: 0in">There are known moderate design
	issues in FS that also impact usability and performance. 
	</p>
	<li><p style="margin-bottom: 0in">There are minor implementation
	limitations in SET that create unnecessary attack surface for
	availability. 
	</p>
	<li><p style="margin-bottom: 0in">The Web site and manuals still
	need significant rework. 
	</p>
	<li><p>Subsystems related to SecuShare and RPS remain experimental. 
	</p>
</ul>
<p>In addition to this list, you may also want to consult our bug
tracker at https://gnunet.org/bugs/ which lists about 200 more
specific issues. Availability 
</p>
<p>The GNUnet 0.11.0pre66 source code is available from all GNU FTP
mirrors. The GTK frontends (which includes the gnunet-setup tool) are
a separate download. Please note that some mirrors might still be
synchronizing. 
</p>
<ul>
	<li><p style="margin-bottom: 0in">GNUnet on a FTP mirror near you
	http://ftpmirror.gnu.org/gnunet/gnunet-0.11.0pre66.tar.gz 
	</p>
	<li><p style="margin-bottom: 0in">GNUnet GTK on an FTP mirror near
	you http://ftpmirror.gnu.org/gnunet/gnunet-gtk-0.11.0pre66.tar.gz 
	</p>
	<li><p style="margin-bottom: 0in">GNUnet FUSE on an FTP mirror near
	you http://ftpmirror.gnu.org/gnunet/gnunet-fuse-0.11.0pre66.tar.gz 
	</p>
	<li><p style="margin-bottom: 0in">GNUnet on the primary GNU FTP
	server ftp://ftp.gnu.org/pub/gnu/gnunet/gnunet-0.11.0pre66.tar.gz 
	</p>
	<li><p style="margin-bottom: 0in">GNUnet GTK on the primary GNU FTP
	server
	ftp://ftp.gnu.org/pub/gnu/gnunet/gnunet-gtk-0.11.0pre66.tar.gz 
	</p>
	<li><p>GNUnet FUSE on the primary GNU FTP server
	ftp://ftp.gnu.org/pub/gnu/gnunet/gnunet-fuse-0.11.0pre66.tar.gz 
	</p>
</ul>
<p>Note that GNUnet is now started using &quot;gnunet-arm -s&quot;.
GNUnet should be stopped using &quot;gnunet-arm -e&quot;. 
</p>
<h4 class="western">Thanks</h4>
<p>This release was the work of many people. The following people
contributed code and were thus easily identified: Christian Grothoff,
Matthias Wachs, Bart Polot, Sree Harsha Totakura, Nathan S. Evans,
Martin Schanzenbach, Julius B&uuml;nger, Nils Gillmann, Philipp
T&ouml;lke, Florian Dold, &#1056;&#1091;&#1089;&#1083;&#1072;&#1085;
&#1048;&#1078;&#1073;&#1091;&#1083;&#1072;&#1090;&#1086;&#1074;,
tg(x), David Barksdale, Christian Fuchs, Nils Durner, Omar Tarabai,
Maximilian Szengel, Supriti Singh, lurchi, David Brodski, xrs, Fabian
Oehlmann, Carlo von lynX, Christophe Genevey Metat, Jeffrey Burdges,
Safey A.Halim, Daniel Golle, Phil, Bruno Cabral, Ji Lu, Heikki
Lindholm, Markus Teich, t3sserakt, Claudiu Olteanu, Marcello
Stanisci, Moon, anryko, Arthur Dewarumez, Julien Morvan, Adnan H, Lin
Tong, Andreas Fuchs, Christian Rupp, jah, Alejandra Morales, Matthias
Kolja Miehl, Andrew Cann, Antonio Ojea, Pascal Mainini, amirouche and
hark. 
</p>
</article>
