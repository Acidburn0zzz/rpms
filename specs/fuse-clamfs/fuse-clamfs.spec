# $Id$
# Authority: dag

%define real_name clamfs

Summary: FUSE-based user-space file system for Linux with on-access anti-virus file scanning
Name: fuse-clamfs
Version: 0.9.1
Release: 1
License: GPL
Group: System Environment/Kernel
URL: http://clamfs.sourceforge.net/

Source: http://dl.sf.net/clamfs/clamfs-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: fuse-devel >= 2.2, rlog-devel, poco-devel, commoncpp2-devel
Requires: fuse >= 2.2

Obsoletes: clamfs <= %{name}-%{version}
Provides: clamfs = %{name}-%{version}

%description
FUSE-based user-space file system for Linux with on-access anti-virus
file scanning through clamd daemon.

%prep
%setup -n %{real_name}-%{version}

%build
%configure \
	--disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO doc/clamfs.xml
%doc %{_mandir}/man1/clamfs.1*
%{_bindir}/clamfs

%changelog
* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 0.9.1-1
- Initial package. (using DAR)
