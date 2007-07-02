# $Id$
# Authority: dag
# Upstream: <test-dev@httpd.apache.org>

%define real_version 20021203

Summary: Profile-driven HTTP load tester
Name: flood
Version: 0.4
Release: 1.cvs20021203
License: Apache
Group: Applications/Internet
URL: http://httpd.apache.org/test/flood/

Source: http://www.apache.org/dist/httpd/flood/flood-%{real_version}.tar.bz2
Patch: flood-openssl.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: httpd-devel

%description
Flood is a profile-driven HTTP load tester. It can be used to gather
important performance matrics for your website.

%prep
%setup -n %{name}
%patch

%build
#%{__autoconf}
#%{__libtoolize}
./buildconf
#CFLAGS="%{optflags}" \
#./configure \
#	--prefix="%{_prefix}" \
#	--bindir="%{_bindir}" \
%configure \
	--enable-ssl \
    --with-apr="%{_bindir}/apr-1-config" \
	--with-capath="%{_datadir}/ssl/certs" \
	--with-openssl="%{_includedir}/openssl"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 flood %{buildroot}%{_bindir}/flood

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES CONFIG DESIGN LICENSE STATUS examples/
%{_bindir}/flood

%changelog
* Sun Apr 04 2004 Dag Wieers <dag@wieers.com> - 0.4-1.cvs20021203
- Initial package. (using DAR)
