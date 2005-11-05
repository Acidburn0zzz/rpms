# $Id$
# Authority: dag
# Upstream: <capps$iozone,org>
# Upstream: William Norcott <William,Norcott$oracle,com>

Summary: IOzone Filesystem Benchmark
Name: iozone
%define real_version 3_254
Version: 3.254
Release: 1
License: Freeware
Group: Applications/System
URL: http://www.iozone.org/

Source: http://www.iozone.org/src/current/iozone%{real_version}.tar
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
IOzone is a filesystem benchmark tool. The benchmark generates and
measures a variety of file operations. Iozone has been ported to
many machines and runs under many operating systems.

Iozone is useful for performing a broad filesystem analysis of a vendors
computer platform. The benchmark tests file I/O performance for the following
operations: Read, write, re-read, re-write, read backwards, read strided,
fread, fwrite, random read, pread ,mmap, aio_read, aio_write.

%prep
%setup -n %{name}%{real_version}

%build
%{__make} %{?_smp_mflags} -C src/current linux

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 src/current/iozone %{buildroot}%{_bindir}/iozone
%{__install} -Dp -m0755 src/current/Generate_Graphs %{buildroot}%{_datadir}/iozone/Generate_Graphs
%{__install} -Dp -m0755 src/current/gengnuplot.sh %{buildroot}%{_datadir}/iozone/gengnuplot.sh
%{__install} -Dp -m0755 src/current/gnu3d.dem %{buildroot}%{_datadir}/iozone/gnu3d.dem

%{__install} -Dp -m0644 docs/iozone.1 %{buildroot}%{_mandir}/man1/iozone.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc docs/IOzone_msword_98.pdf docs/Iozone_ps.gz src/current/Gnuplot.txt
%doc %{_mandir}/man1/iozone.1*
%{_bindir}/iozone
%{_datadir}/iozone/

%changelog
* Fri Nov 04 2005 Dries Verachtert <dries@ulyssis.org> - 3.254-1
- Updated to release 3.254.

* Mon Sep 05 2005 Dag Wieers <dag@wieers.com> - 3.248-1
- Updated to release 3.248.

* Wed Jul 13 2005 Dag Wieers <dag@wieers.com> - 3.242-1
- Updated to release 3.242.

* Tue May 10 2005 Dag Wieers <dag@wieers.com> - 3.239-1
- Updated to release 3.239.

* Thu Mar 24 2005 Dag Wieers <dag@wieers.com> - 3.235-1
- Updated to release 3.235.

* Mon Feb 21 2005 Dag Wieers <dag@wieers.com> - 3.233-1
- Updated to release 3.233.

* Wed Jan 19 2005 Dag Wieers <dag@wieers.com> - 3.228-1
- Updated to release 3.228.

* Mon Nov 01 2004 Dag Wieers <dag@wieers.com> - 3.226-1
- Updated to release 3.226.

* Tue Jul 20 2004 Dag Wieers <dag@wieers.com> - 3.221-1
- Updated to release 3.221.

* Sat Jun 19 2004 Dag Wieers <dag@wieers.com> - 3.218-1
- Initial package. (using DAR)
