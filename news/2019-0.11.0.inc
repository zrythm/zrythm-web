<article>
<h3>
<a name="gnunet-0.11.0-release">2019-02: GNUnet 0.11.0 released</a>
</h3>

<p>
We are pleased to announce the release of GNUnet 0.11.0.
<p>

<p>
This is a major release after about five years of development.  In
terms of usability, users should be aware that there are still a large
number of known open issues in particular with respect to ease of use,
but also some critical privacy issues especially for mobile users.
Also, the nascent network is tiny (about 200 peers) and thus unlikely to
provide good anonymity or extensive amounts of interesting
information.  As a result, the 0.11.0 release is still only suitable
for early adopters with some reasonable pain tolerance.
</p>

<h4>Download links</h4>
  <ul>
    <li><a href="http://ftpmirror.gnu.org/gnunet/gnunet-0.11.0.tar.gz">http://ftpmirror.gnu.org/gnunet/gnunet-0.11.0.tar.gz</a></li>
    <li><a href="http://ftpmirror.gnu.org/gnunet/gnunet-0.11.0.tar.gz.sig">http://ftpmirror.gnu.org/gnunet/gnunet-0.11.0.tar.gz.sig</a></li>
    <li><a href="http://ftpmirror.gnu.org/gnunet/gnunet-gtk-0.11.0.tar.gz">http://ftpmirror.gnu.org/gnunet/gnunet-gtk-0.11.0.tar.gz</a></li>
    <li><a href="http://ftpmirror.gnu.org/gnunet/gnunet-gtk-0.11.0.tar.gz.sig">http://ftpmirror.gnu.org/gnunet/gnunet-gtk-0.11.0.tar.gz.sig</a></li>
    <li><a href="http://ftpmirror.gnu.org/gnunet/gnunet-fuse-0.11.0.tar.gz">http://ftpmirror.gnu.org/gnunet/gnunet-fuse-0.11.0.tar.gz</a></li>
    <li><a href="http://ftpmirror.gnu.org/gnunet/gnunet-fuse-0.11.0.tar.gz.sig">http://ftpmirror.gnu.org/gnunet/gnunet-fuse-0.11.0.tar.gz.sig</a></li>
  </ul>
<p>
Note that due to mirror synchronization, not all links might be functional
early after the release. For direct access try <a href="http://ftp.gnu.org/gnu/gnunet/">http://ftp.gnu.org/gnu/gnunet/</a>
</p>
<p>
Note that GNUnet is now started using <tt>gnunet-arm -s</tt>. GNUnet should be
stopped using <tt>gnunet-arm -e</tt>.
</p>

<h4>Noteworthy changes in 0.11.0</h4>

  <ul>
    <li>The Web site and manuals have undergone significant rework. You can find an
        archive of the old Web site at <a href="https://old.gnunet.org/">old.gnunet.org</a>.</li>
    <li>The code now builds again on macOS. GNUnet on macOS is <i>experimental</i>.
        While it builds and seems to run fine, some tests are known to fail.</li>
    <li>Build process now works properly with libidn2</li>
    <li>Except for <tt>gnunet-qr</tt>, all Python code was migrated to Python 3.7.</li>
    <li>Fixed security issues in secret sharing cryptography logic</li>
    <li>Services running out of file descriptors on <tt>accept()</tt> no longer busy wait</li>
    <li>Fixed crash in gnunet-gns2dns proxy</li>
    <li>GNS responses are now padded to minimize information disclosure from the size</li>
    <li>Fixed API issues and (rare) crash bugs in CADET</li>
    <li>The experimental SecuShare code is not included in the release, you can
        now find it in the <a href="https://git.gnunet.org/gnunet-secushare/">gnunet-secushare</a>
        Git repository.</li>
    <li>The Ascension tool (separate download) now allows importing DNS zones into GNS via AXFR.</li>
    <li>GNUnet now includes a decentralised identity attribute sharing service:
        reclaimID. A ready-to-use client can be found in an
        <a href="https://gitlab.com/reclaimid/client">external repo</a>.</li>
    <li>The code now builds again on NetBSD. GNUnet on NetBSD is <i>experimental</i>.
        While it builds and seems to run fine, full support requires more
        changes in the core of GNUnet
        It will soon be available via pkgsrc.
    <li>Many things changed on the build system side. If you package
        GNUnet for an operating system or otherwise package manager,
        make sure that you read the README.</li>
  </ul>
  The above is just the short list, our bugtracker lists
  <a href="https://bugs.gnunet.org/changelog_page.php?version_id=258">
  over 100 individual issues</a> that were resolved since 0.11.0pre66.

<h4>Known Issues</h4>
  <ul>
    <li>There are known major design issues in the TRANSPORT, ATS and CORE subsystems
        which will need to be addressed in the future to achieve acceptable usability,
        performance and security.</li>
    <li>There are known moderate implementation limitations in CADET that
        negatively impact performance. Also CADET may unexpectedly deliver messages out-of-order.</li>
    <li>There are known moderate design issues in FS that also impact
        usability and performance.</li>
    <li>There are minor implementation limitations in SET that create
        unnecessary attack surface for availability.</li>
    <li>The RPS subsystem remains experimental.</li>
    <li>Some high-level tests in the test-suite fail non-deterministically due to
        the low-level TRANSPORT issues.</li>
  </ul>
<p>
In addition to this list, you may also want to consult our bug tracker
at <a href="https://bugs.gnunet.org/">bugs.gnunet.org</a> which lists
about 150 more specific issues.
</p>

<h4>Thanks</h4>
<p>
This release was the work of many people. The following people
contributed code and were thus easily identified:
Christian Grothoff, Matthias Wachs, Bart Polot, Sree Harsha Totakura,
Nathan S. Evans, Martin Schanzenbach, Julius B&#xFC;nger, ng0,
Philipp T&#xF6;lke, Florian Dold, &#x420;&#x443;&#x441;&#x43B;&#x430;&#x43D; &#x418;&#x436;&#x431;&#x443;&#x43B;&#x430;&#x442;&#x43E;&#x432;, tg(x), David Barksdale,
Christian Fuchs, Nils Durner, Omar Tarabai, Maximilian Szengel, Supriti
Singh, lurchi, David Brodski, xrs, Fabian Oehlmann, Carlo von lynX,
Christophe Genevey Metat, Jeffrey Burdges, Safey A.Halim, Daniel Golle,
Phil, Bruno Cabral, Ji Lu, Heikki Lindholm, Markus Teich, t3sserakt,
Claudiu Olteanu, Marcello Stanisci, Moon, Hernani Marques, anryko, Arthur Dewarumez,
Julien Morvan, Adnan H, rexxnor, Lin Tong, Andreas Fuchs, Christian Rupp, jah,
Alejandra Morales, Bernd Fix, Feideus, Matthias Kolja Miehl, Andrew Cann, Antonio Ojea,
Pascal Mainini, amirouche and hark.
<a href="https://bugs.gnunet.org/view.php?id=5569">Special thanks</a> to Florian Weimer.
</p>
</article>
