# $Id$
# Authority: dag

# Tag: test

%define _use_internal_dependency_generator 0

Summary: Multi Router Traffic Grapher
Name: mrtg
Version: 2.12.1
Release: 1.2
License: GPL
Group: Applications/Internet
URL: http://ee-staff.ethz.ch/~oetiker/webtools/mrtg/mrtg.html

Source: http://www.ee.ethz.ch/~oetiker/webtools/mrtg/pub/mrtg-%{version}.tar.gz
Source4: README-14allcgi
Source5: 14all.cgi
Source6: filter-requires-mrtg.sh
Patch: mrtg-2.9.17-lib64.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: freetype-devel, gd-devel, libjpeg-devel, libpng-devel
Requires: perl >= 0:5.004, gd
Requires: vixie-cron, /sbin/service

%define __find_requires %{SOURCE6}

%description
The Multi Router Traffic Grapher (MRTG) is a tool to monitor the traffic
load on network-links. MRTG generates HTML pages containing PNG
images which provide a LIVE visual representation of this traffic.

%prep
%setup
%patch -p0 -b .lib64

%{__cat} <<EOF >mrtg.cfg
######################################################################
# Multi Router Traffic Grapher -- Example Configuration File
######################################################################
# This file is for use with mrtg-2.0
#
# Note:
#
# * Keywords must start at the begin of a line.
#
# * Lines which follow a keyword line which do start
#   with a blank are appended to the keyword line
#
# * Empty Lines are ignored
#
# * Lines starting with a # sign are comments.

# Where should the logfiles, and webpages be created?

# Minimal mrtg.cfg
#--------------------

WorkDir: %{_localstatedir}/www/mrtg/
#Target[r1]: 2:public@myrouter.somplace.edu
#MaxBytes[r1]: 1250000
#Title[r1]: Traffic Analysis
#PageTop[r1]: <H1>Stats for our Ethernet</H1>
EOF

%{__cat} <<EOF >mrtg.cron
0-59/5 * * * * root %{_bindir}/mrtg %{_sysconfdir}/mrtg/mrtg.cfg
EOF

%{__cat} <<EOF >mrtg.httpd
### This configuration file maps the mrtg output (generated daily)
### into the URL space.  By default these results are only accessible
### from the local host.

Alias /mrtg %{_localstatedir}/www/mrtg

<Location /mrtg>
    Order deny,allow
    Deny from all
    Allow from localhost
    # Allow from .example.com
</Location>
EOF

%build
export LIBS="-lgd -lpng -lz -lfreetype"
%configure
%{__make} %{?_smp_mflags}
find contrib -type f -exec %{__perl} -e 's|^#!/.*|#!%{__perl}|gi' -p -i \{\} \;
find contrib -name "*.pl" -exec %{__perl} -e 's|\015||gi' -p -i \{\} \;

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0644 mrtg.cfg %{buildroot}%{_sysconfdir}/mrtg/mrtg.cfg
%{__install} -Dp -m0644 mrtg.cron %{buildroot}%{_sysconfdir}/cron.d/mrtg
%{__install} -Dp -m0644 mrtg.httpd %{buildroot}%{_sysconfdir}/httpd/conf.d/mrtg.conf

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/www/mrtg/
%{__install} -Dp -m0644 images/*   %{buildroot}%{_localstatedir}/www/mrtg/
%{__install} -Dp -m0644 doc/*.html %{buildroot}%{_localstatedir}/www/mrtg/

%{__install} -Dp -m0644 %{SOURCE4} contrib/14all/README
%{__install} -Dp -m0755 %{SOURCE5} contrib/14all/14all.cgi

%{__install} -d -m0755 %{buildroot}%{_bindir}
for bin in bin/mrtg bin/rateup bin/cfgmaker bin/indexmaker; do
	%{__install} -p -m0755 $bin %{buildroot}%{_bindir}
done
for bin in mrtg cfgmaker indexmaker; do
	%{__perl} -pi -e 's|\@\@lib\@\@|%{_lib}|g' %{buildroot}%{_bindir}/$bin
done

%{__install} -dp -m0755 %{buildroot}%{_libdir}/mrtg2/Pod/
for i in lib/mrtg2/*.pm; do
	%{__install} -p -m0644 $i %{buildroot}%{_libdir}/mrtg2/
done
for i in lib/mrtg2/Pod/*.pm; do
	%{__install} -p -m0644 $i %{buildroot}%{_libdir}/mrtg2/Pod/
done

%{__install} -dp -m0755 %{buildroot}%{_mandir}/man1/
for i in doc/*.1; do
	%{__install} -p -m0644 $i %{buildroot}%{_mandir}/man1/
done
%{__perl} -pi -e 's|\@\@lib\@\@|%{_lib}|g' %{buildroot}%{_mandir}/man1/*.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ANNOUNCE CHANGES COPYING COPYRIGHT MANIFEST README THANKS contrib/
%doc %{_mandir}/man1/*
%config(noreplace) %{_sysconfdir}/httpd/conf.d/mrtg.conf
%config(noreplace) %{_sysconfdir}/mrtg/
%config %{_sysconfdir}/cron.d/mrtg
%{_localstatedir}/www/mrtg/
%{_bindir}/*
%{_libdir}/mrtg2/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.12.1-1.2
- Rebuild for Fedora Core 5.

* Wed May 18 2005 Dag Wieers <dag@wieers.com> - 2.12.1-1
- Initial package. (using DAR)
