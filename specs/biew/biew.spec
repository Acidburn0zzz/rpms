# $Id$
# Authority: dag
# Upstream: <biew-general$lists,sf,net>

%define real_version 562

Summary: Console hex viewer/editor with disassembler
Name: biew
Version: 5.6.2
Release: 2
License: GPL
Group: Development/Tools
URL: http://biew.sourceforge.net/

Source: http://dl.sf.net/biew/biew%{real_version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

ExcludeArch: sparc sparc64

%description
BIEW (Binary vIEW) is a free, portable, advanced file viewer with
built-in editor for binary, hexadecimal and disassembler modes.

It contains a highlight PentiumIII/K7 Athlon/Cyrix-M2 disassembler,
full preview of MZ, NE, PE, LE, LX, DOS.SYS, NLM, ELF, a.out, arch,
coff32, PharLap, rdoff executable formats, a code guider, and lot of
other features, making it invaluable for examining binary code.

%prep
%setup -n %{name}-%{real_version}

### Change default prefix to %{_prefix}
%{__perl} -pi.orig -e 's|/usr/local|%{_prefix}|' biewlib/sysdep/generic/unix/os_dep.c

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 biew  %{buildroot}%{_bindir}/biew
%{__install} -Dp -m0644 bin_rc/biew.hlp %{buildroot}%{_datadir}/biew/biew.hlp

%{__install} -d -m0755 %{buildroot}%{_datadir}/biew/{skn,xlt}/
%{__install} -p -m0644 bin_rc/skn/*.skn %{buildroot}%{_datadir}/biew/skn/
%{__cp} -apuvx bin_rc/xlt/* %{buildroot}%{_datadir}/biew/xlt/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc doc/*.en doc/*.txt
%{_bindir}/biew
%{_datadir}/biew/

%changelog
* Mon Oct 09 2006 Dag Wieers <dag@wieers.com> - 5.6.2-2
- Fixed group name.

* Wed Sep 29 2004 Dag Wieers <dag@wieers.com> - 5.6.2-1
- Updated to release 5.6.2.

* Sat May 22 2004 Dag Wieers <dag@wieers.com> - 5.6.1-1
- Updated to release 5.6.1.

* Tue Jan 06 2004 Dag Wieers <dag@wieers.com> - 5.5.0-0
- Updated to release 5.5.0.

* Fri Apr 18 2003 Dag Wieers <dag@wieers.com> - 5.3.2-0
- Initial package. (using DAR)
