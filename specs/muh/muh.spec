# $Id$
# Authority: dag
# Upstream: Sebastian Kienzl <seb$riot,org>

%define real_version 2.1rc1

Summary: IRC bouncer with IPV6-support
Name: muh
Version: 2.1
Release: 0.rc1
License: GPL 
Group: Applications/Internet
URL: http://mind.riot.org/muh/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/muh/muh-%{real_version}.tar.gz
Source1: muhrc
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
muh is a quite versatile irc-bouncer for unix. An irc-bouncer is a program
that acts as a middleman between your irc-client and your irc-server.
If you have no idea what this is good for you probably don't need it.

%prep
%setup -n %{name}-%{real_version}

%{__cp} -av %{SOURCE1} .

%build
%configure \
	--enable-ipv6
%{__make} %{?_smp_mflags}
%{__mv} src/muh src/muh-ipv6

%configure
%{__make} %{?_smp_mflags}

%install 
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -D -m0755 src/muh-ipv6 %{buildroot}%{_bindir}/muh-ipv6

%post
/sbin/install-info %{_infodir}/%{name}.info.gz %{_infodir}/dir

%preun
/sbin/install-info --delete %{_infodir}/%{name}.info.gz %{_infodir}/dir

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO VERSION muhrc
%doc %{_infodir}/*.info*
%{_bindir}/*
%exclude %{_datadir}/muhrc

%changelog
* Wed Apr 07 2004 Dag Wieers <dag@wieers.com> - 2.1-0.rc1
- Initial package. (using DAR)
