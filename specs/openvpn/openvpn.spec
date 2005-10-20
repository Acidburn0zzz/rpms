# $Id$
# Authority: dag
# Upstream: James Yonan <jim$yonan,net>

Summary: Robust and highly flexible VPN daemon
Name: openvpn
Version: 2.0.2
Release: 1
License: GPL
Group: Applications/Internet
URL: http://openvpn.net/

Source: http://openvpn.net/release/openvpn-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: lzo-devel >= 1.07, openssl-devel >= 0.9.6, pkgconfig, pam-devel

%description
OpenVPN is a robust and highly flexible tunneling application.

OpenVPN supports SSL/TLS security, ethernet bridging, TCP or UDP tunnel
transport through proxies or NAT, support for dynamic IP addresses and
DHCP, scalability to hundreds or thousands of users, and portability to
most major OS platforms.


%prep
%setup


%build
if pkg-config openssl; then
    CFLAGS="%{optflags} `pkg-config --cflags openssl`"
    LDFLAGS="$LDFLAGS `pkg-config --libs-only-L openssl`"
fi
%configure \
	--program-prefix="%{?_program_prefix}" \
	--enable-iproute2 \
	--enable-pthread
%{__make} %{?_smp_mflags}

### Build plugins
for pi in auth-pam down-root; do
	%{__make} %{?_smp_mflags} -C plugin/$pi
done


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

### Install provided init script
%{__install} -Dp -m0755 sample-scripts/openvpn.init %{buildroot}%{_initrddir}/openvpn

### Install empty configuration directory
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/openvpn/

### Install plugins and move plugin documentation
for pi in auth-pam down-root; do
	%{__mv} -f plugin/$pi/README plugin/README.$pi
	%{__install} -Dp -m0755 plugin/$pi/openvpn-$pi.so %{buildroot}%{_datadir}/openvpn/plugin/lib/openvpn-$pi.so
done
%{__mv} -f plugin/README plugin/README.plugins

### Disable find-requires for documentation
find contrib/ easy-rsa/ sample-*/ -type f -exec %{__chmod} -x {} \;


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/chkconfig --add openvpn

%preun
if [ $1 -eq 0 ]; then
    /sbin/service openvpn stop &>/dev/null || :
    /sbin/chkconfig --del openvpn
fi

%postun
/sbin/service openvpn condrestart &>/dev/null || :


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING COPYRIGHT.GPL INSTALL NEWS PORTS README
%doc contrib/ easy-rsa/ management/ plugin/README.* sample-*/
%doc %{_mandir}/man8/openvpn.8*
%dir %{_sysconfdir}/openvpn/
%config %{_initrddir}/openvpn
%{_datadir}/openvpn/
%{_sbindir}/openvpn


%changelog
* Thu Sep 08 2005 Dag Wieers <dag@wieers.com> - 2.0.2-1
- Updated to release 2.0.2.

* Thu Aug 18 2005 Dag Wieers <dag@wieers.com> - 2.0.1-1
- Added pam-devel build requirement. (Greg Cope)
- Updated to release 2.0.1.

* Sat Apr 30 2005 Dag Wieers <dag@wieers.com> - 2.0-1
- Updated to release 2.0.

* Mon Apr 04 2005 Dag Wieers <dag@wieers.com> - 2.0-0.rc20.1
- Updated to release 2.0_rc20.

* Sat Apr 02 2005 Dag Wieers <dag@wieers.com> - 2.0-0.rc19.2
- Disabled find-requires for %%doc.

* Fri Apr 01 2005 Dag Wieers <dag@wieers.com> - 2.0-0.rc19.1
- Updated to release 2.0_rc19.

* Wed Oct  6 2004 Matthias Saou <http://freshrpms.net/> 2.0-0.beta11.1
- Update to 2.0_beta11.
- Add cleaner dev entries to %file instead of using mknod in post.
- Add openssl krb5 include error workaround for older releases.

* Tue May 11 2004 Dag Wieers <dag@wieers.com> - 1.6.0-1
- Updated to release 1.6.0.

* Tue Nov 25 2003 Dag Wieers <dag@wieers.com> - 1.5.0-0
- Updated to release 1.5.0.

* Tue Sep 09 2003 Dag Wieers <dag@wieers.com> - 1.5-0.beta7
- Create /dev/net/tun only for RH62 and RH73. (Rudolf Kastl)
- Updated to release 1.5-beta7.

* Sat Aug 16 2003 Dag Wieers <dag@wieers.com> - 1.4.3-0
- Initial package. (using DAR)
