# $Id$
# Authority: dag
# Upstream: Samuel Demeulemeester <memtest$memtest,org>

# Screenshot: http://www.memtest.org/pics/i875-big.gif

# ExcludeDist: el4
##ExcludeDist: fc2

%define _prefix /boot

Summary: Thorough, stand-alone memory tester
Name: memtest86+
Version: 1.50
Release: 1
License: GPL
Group: System Environment/Kernel
URL: http://www.memtest.org/

Source: http://www.memtest.org/download/%{version}/memtest86+-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

ExclusiveArch: i386 i486 i586 i686 x86_64

%description
Memtest86+ is a thorough, stand alone memory test for 386, 486, Pentium and
AMD64 systems. Memtest86+ is a stand alone program and can be loaded from
either a disk partition via lilo or a floppy disk. Memtest86+ uses a
"moving inversions" algorithm that is proven to be effective in finding
memory errors. The BIOS based memory test is just a quick check that will
often miss many of the failures that are detected by Memtest86+.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0644 memtest.bin %{buildroot}%{_prefix}/%{name}-%{version}

%clean
%{__rm} -rf %{buildroot}

%post
if [ -x /sbin/grubby ] ; then
        /sbin/grubby --add-kernel="%{_prefix}/%{name}-%{version}" \
		--title "Memtest86+ v%{version}"
fi

%postun
if [ -x /sbin/grubby ] ; then
        /sbin/grubby --remove-kernel="%{_prefix}/%{name}-%{version}"
fi

%files
%defattr(-, root, root, 0755)
%doc README
%{_prefix}/%{name}-%{version}

%changelog
* Thu Feb 10 2005 Dag Wieers <dag@wieers.com> - 1.50-1
- Updated to release 1.50.

* Mon Nov 29 2004 Dag Wieers <dag@wieers.com> - 1.40-1
- Updated to release 1.40.

* Thu Nov 04 2004 Dag Wieers <dag@wieers.com> - 1.27-1
- Updated to release 1.27.

* Sun Jul 18 2004 Dag Wieers <dag@wieers.com> - 1.20-1
- Updated to release 1.20.

* Mon Mar 22 2004 Dag Wieers <dag@wieers.com> - 1.11-1
- Updated to release 1.11.

* Wed Jan 21 2004 Dag Wieers <dag@wieers.com> - 1.0-0
- Initial package. (using DAR)
