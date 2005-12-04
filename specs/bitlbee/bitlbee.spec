# $Id$
# Authority: dag
# Upstream: Wilmer van der Gaast <lintux$lintux,cx>

Summary: IRC to other chat networks gateway
Name: bitlbee
Version: 1.0
Release: 1
License: GPL
Group: System Environment/Daemons
URL: http://www.bitlbee.org/

Source: http://get.bitlbee.org/src/bitlbee-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gnutls-devel, libgcrypt-devel, glib-devel, perl, libxslt, xmlto

%description
Bitlbee is an IRC to other chat networks gateway. bitlbee can be used as
an IRC server which forwards everything you say to people on other chat
networks like MSN/ICQ/Jabber.

%prep
%setup

%{__perl} -pi.orig -e '
		s|\$\(BINDIR\)|\$(sbindir)|g;
		s|\$\(DATADIR\)|\$(datadir)/bitlbee|g;
		s|\$\(ETCDIR\)|\$(sysconfdir)/bitlbee|g;
		s|\$\(MANDIR\)|\$(mandir)|g;
	' Makefile */Makefile

%{__cat} <<EOF >bitlbee.xinet
# default: off
# description: Bitlbee is an IRC gateway to other networks.

service ircd
{
	disable		= yes
	socket_type	= stream
	protocol	= tcp
	wait		= no
	user		= daemon
	server		= %{_sbindir}/bitlbee
	port		= 6667
	log_on_failure	+= USERID
}
EOF

%build
./configure \
	--prefix="%{_prefix}" \
	--bindir="%{_sbindir}" \
	--etcdir="%{_sysconfdir}/bitlbee" \
	--mandir="%{_mandir}" \
	--datadir="%{_datadir}/bitlbee" \
	--config="%{_localstatedir}/lib/bitlbee"
%{__make} %{?_smp_mflags}
### FIXME: Documentation needs old sgmltools tool, deprecated.
#%{__make} -C doc

%install
%{__rm} -rf %{buildroot}
### FIXME: makeinstall-phase doesn't use autotool dirs and wants to change ownerships.
%makeinstall DATADIR=%{buildroot}%{_datadir}/bitlbee
#%{__install} -Dp -m0755 bitlbee %{buildroot}%{_sbindir}/bitlbee
##%{__install} -Dp -m0644 help.txt %{buildroot}%{_datadir}/bitlbee/help.txt
%{__install} -Dp -m0644 bitlbee.xinet %{buildroot}%{_sysconfdir}/xinetd.d/bitlbee

%{__install} -d -m0755 %{buildroot}%{_mandir}/man8/
%{__install} -p -m0644 doc/*.8 %{buildroot}%{_mandir}/man8/

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/lib/bitlbee/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc bitlbee.conf COPYING doc/AUTHORS doc/CHANGES doc/CREDITS motd.txt
%doc doc/user-guide/*.html doc/user-guide/*.txt doc/FAQ doc/INSTALL doc/README doc/TODO utils/
%doc %{_mandir}/man5/bitlbee.conf.5*
%doc %{_mandir}/man8/bitlbee.8*
%config %{_sysconfdir}/xinetd.d/bitlbee
%{_sbindir}/bitlbee
%{_datadir}/bitlbee/

%defattr(-, daemon, root, 0700)
%{_localstatedir}/lib/bitlbee/

%changelog
* Sun Dec 04 2005 Dries Verachtert <dries@ulyssis.org> - 1.0-1
- Updated to release 1.0.

* Sat Nov 05 2005 Dries Verachtert <dries@ulyssis.org> - 0.99-2
- Buildrequirements added, install of user-guide fixed.

* Fri Nov 04 2005 Dries Verachtert <dries@ulyssis.org> - 0.99-1
- Updated to release 0.99.

* Fri Feb 25 2005 Dag Wieers <dag@wieers.com> - 0.92-1
- Updated to release 0.92.

* Mon Sep 28 2004 Dag Wieers <dag@wieers.com> - 0.91-1
- Updated to release 0.91.

* Mon Jun 28 2004 Dag Wieers <dag@wieers.com> - 0.90-2.a
- Updated to release 0.90a.

* Sat May 29 2004 Dag Wieers <dag@wieers.com> - 0.90-1
- Updated to release 0.90.

* Thu Apr 08 2004 Dag Wieers <dag@wieers.com> - 0.85-2
- Fixed typo in config configure option. (Len Trigg)

* Sun Mar 14 2004 Dag Wieers <dag@wieers.com> - 0.85-1
- Updated to release 0.85.

* Mon Feb 16 2004 Dag Wieers <dag@wieers.com> - 0.84-0
- Updated to release 0.84.

* Wed Dec 31 2003 Dag Wieers <dag@wieers.com> - 0.83-0
- Updated to release 0.83.

* Thu Jun 26 2003 Dag Wieers <dag@wieers.com> - 0.80-0
- Updated to release 0.80.

* Wed Jun 11 2003 Dag Wieers <dag@wieers.com> - 0.74-0.a
- Updated to release 0.74a.

* Mon Jun 09 2003 Dag Wieers <dag@wieers.com> - 0.73-2
- Fixed bitlbee.xinet to use ircd/tcp.
- Added --datadir to configure.

* Sun Jun 08 2003 Dag Wieers <dag@wieers.com> - 0.73-0
- Initial package. (using DAR)
