# $Id$
# Authority: dag

Summary: Utility for formatting Phoenix NoteBIOS hibernation partitions under Linux
Name: lphdisk
Version: 0.9.1
Release: 0
License: Artistic License
Group: System Environment/Base
URL: http://www.procyon.com/~pda/lphdisk/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.procyon.com/~pda/lphdisk/lphdisk-%{version}.tar.gz
Patch: lphdisk-0.9.1-gcc33.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
lphdisk is a linux reimplementation of the PHDISK.EXE (DOS) utility provided
with most Phoenix NoteBIOS-equipped laptop models.  It will properly format a
NoteBIOS hibernation partition (type A0) to make it usable by the BIOS for
suspending to disk, avoiding the need to use buggy and outdated DOS utilities 
to perform this configuration step.

%prep
%setup
%patch -p0 -b .gcc33

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 lphdisk %{buildroot}%{_sbindir}/lphdisk
%{__install} -D -m0644 lphdisk.8 %{buildroot}%{_mandir}/man8/lphdisk.8

%clean
%{__rm} -rf ${buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog CREDITS LICENSE NEWS README TODO
%doc %{_mandir}/man?/lphdisk.8.gz
%{_sbindir}/*

%changelog
* Fri Apr 11 2003 Dag Wieers <dag@wieers.com> - 0.9.1-0
- Patch to build with gcc-3.3.
- Initial package. (using DAR)
