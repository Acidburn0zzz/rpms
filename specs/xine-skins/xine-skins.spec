# $Id$
# Authority: matthias
# Dist: nodist

%define skindir %(rpm -ql xine | grep '/skins$' || :)

Summary: Collection of skins for the Xine multimedia player
Name: xine-skins
Version: 1.9
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://xinehq.de/
Source0: http://www.xinehq.de/index.php/force-download/skins/Galaxy.tar.gz
#Source1: http://www.xinehq.de/index.php/force-download/skins/CelomaChrome.tar.gz
Source2: http://www.xinehq.de/index.php/force-download/skins/CelomaGold.tar.gz
Source3: http://www.xinehq.de/index.php/force-download/skins/CelomaMdk.tar.gz
Source4: http://www.xinehq.de/index.php/force-download/skins/Centori.tar.gz
Source5: http://www.xinehq.de/index.php/force-download/skins/Crystal.tar.gz
Source6: http://www.xinehq.de/index.php/force-download/skins/Keramic.tar.gz
#Source7: http://www.xinehq.de/index.php/force-download/skins/cloudy.tar.gz
#Source8: http://www.xinehq.de/index.php/force-download/skins/concept.tar.gz
Source9: http://www.xinehq.de/index.php/force-download/skins/lcd.tar.gz
Source10: http://www.xinehq.de/index.php/force-download/skins/mp2k.tar.gz
#Source11: http://www.xinehq.de/index.php/force-download/skins/pitt.tar.gz
#Source12: http://www.xinehq.de/index.php/force-download/skins/xinetic.tar.gz
Source13: http://www.xinehq.de/index.php/force-download/skins/mplayer.tar.gz
Source14: http://www.xinehq.de/index.php/force-download/skins/KeramicRH8.tar.gz
Source15: http://www.xinehq.de/index.php/force-download/skins/OMS_legacy.tar.gz
Source16: http://www.xinehq.de/index.php/force-download/skins/Sunset.tar.gz
Source17: http://www.xinehq.de/index.php/force-download/skins/blackslim2.tar.gz
Source18: http://www.xinehq.de/index.php/force-download/skins/caramel.tar.gz
Source19: http://www.xinehq.de/index.php/force-download/skins/Bambino-Blue.tar.gz
Source20: http://www.xinehq.de/index.php/force-download/skins/Antares.tar.gz
Source21: http://www.xinehq.de/index.php/force-download/skins/Polaris.tar.gz
Source22: http://www.xinehq.de/index.php/force-download/skins/Bluton.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: xine >= 0.99.0
BuildRequires: xine >= 0.99.0
BuildArch: noarch

%description
This package contains a collection of additional skins for the original
Xine video player frontend. Install this package if you wish to change the
appeareance of Xine.


%prep
%setup -c %{name}-%{version} -a2 -a3 -a4 -a5 -a6 -a9 -a10 -a13 -a14 -a15 -a16 -a17 -a18 -a19 -a20 -a21 -a22


%build
find . -type d -and \( -name "CVS" -or -name ".xvpics" \) \
    -exec %{__rm} -rf {} \; || :


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{skindir}
%{__cp} -a * %{buildroot}%{skindir}/


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(0644, root, root, 0755)
%{skindir}/*


%changelog
* Thu Jan 13 2005 Matthias Saou <http://freshrpms.net/> 1.9-1
- Added Polaris and Bluton skins.

* Tue Jul  6 2004 Matthias Saou <http://freshrpms.net/> 1.8-1
- Added blackslim2, caramel, Bambino-Blue (no more, it's big) and Antar�s.

* Mon Jan  5 2004 Matthias Saou <http://freshrpms.net/> 1.7-1
- Removed cloudy (included in xine-ui).
- Added Sunset.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.6-2
- Rebuild for Fedora Core 1.

* Tue Aug 26 2003 Matthias Saou <http://freshrpms.net/>
- Updated all skins.
- Disabled pitt and concept : wrong versions.
- New correct skindir detection thanks to Dam's.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Fri Mar 21 2003 Matthias Saou <http://freshrpms.net/>
- Updated many skins to 0.9.19 versions from J�r�me.

* Thu Feb 27 2003 Matthias Saou <http://freshrpms.net/>
- Added Keramic_rh8 and oms_legacy, thanks J�r�me!

* Thu Jan 30 2003 Matthias Saou <http://freshrpms.net/>
- Updated all skins to theur current versions (4.0 mostly).
- Added Keramic and Crystal.
- Removed the "concept" skin as it's *still* not near being finished :-(

* Wed Nov  6 2002 Matthias Saou <http://freshrpms.net/>
- Updated concept4, CelomaChrome251002 and CelomaGold271002.
- Added Centori_alpha and Keramic_alpha.

* Sun Aug  4 2002 Matthias Saou <http://freshrpms.net/>
- Updated the concept skin to version 3 and rebuilt for Red Hat Linux 8.0.

* Sun Aug  4 2002 Matthias Saou <http://freshrpms.net/>
- Removed cloudy and xinetic that got back into the main xine.

* Wed Jul 31 2002 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

