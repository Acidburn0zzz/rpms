# $Id$
# Authority: dag
# Upstream: Fabrice Bellard <fabrice$bellard,org>

Summary: CPU emulator
Name: qemu
Version: 0.8.0
Release: 1
License: GPL
Group: Applications/Emulators
URL: http://fabrice.bellard.free.fr/qemu/

Source: http://fabrice.bellard.free.fr/qemu/qemu-%{version}.tar.gz
Patch0: qemu-0.7.0-build.patch
Patch1: qemu-0.7.0-dyngen.patch
Patch2: qemu-0.7.0-gcc4-x86.patch
Patch3: qemu-0.7.0-gcc4-ppc.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: SDL-devel

%description
QEMU is a FAST! processor emulator using dynamic translation to achieve good
emulation speed. QEMU has two operating modes:

	Full system emulation. In this mode, QEMU emulates a full system (for
	example a PC), including a processor and various peripherials. It can
	be used to launch different Operating Systems without rebooting the PC
	or to debug system code.

	User mode emulation (Linux host only). In this mode, QEMU can launch
	Linux processes compiled for one CPU on another CPU. It can be used to
	launch the Wine Windows API emulator or to ease cross-compilation and
	cross-debugging. 

As QEMU requires no host kernel patches to run, it is very safe and easy to use.
QEMU is a FAST! processor emulator. By using dynamic translation it achieves a
reasonnable speed while being easy to port on new host CPUs.

%prep
%setup
%patch0 -b .build
%patch1 -b .dyngen
%patch2
%patch3

%{__cat} <<'EOF' >qemu.sysv
#!/bin/sh
#
# Init file for configuring Qemu non-native binary formats
#
# Written by Dag Wieers <dag@wieers.com>
#
# chkconfig: 2345 35 98
# description: Qemu non-native binary formats

source %{_initrddir}/functions

RETVAL=0
prog="qemu"

start() {
	case "$(uname -m)" in
		(i386|i486|i586|i686|i86pc|BePC)
			cpu="i386";;
		("Power Macintosh"|ppc|ppc64)
			cpu="ppc";;
		(armv4l|armv5l)
			cpu="arm";;
	esac
	echo -n $"Registering non-native binary handler for Qemu"
	/sbin/modprobe binfmt_misc &>/dev/null
	if [ "$cpu" != "i386" -a -x "%{_bindir}/qemu-i386" -a -d "%{_prefix}/qemu-i386" ]; then
		echo ':qemu-i386:M::\x7fELF\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x03\x00:\xff\xff\xff\xff\xff\xfe\xfe\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfb\xff\xff\xff:%{_bindir}/qemu-i386:' >/proc/sys/fs/binfmt_misc/register
		echo ':qemu-i486:M::\x7fELF\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x06\x00:\xff\xff\xff\xff\xff\xfe\xfe\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfb\xff\xff\xff:%{_bindir}/qemu-i386:' >/proc/sys/fs/binfmt_misc/register
	fi
	if [ "$cpu" != "arm" -a -x "%{_bindir}/qemu-arm" -a -d "%{_prefix}/qemu-arm" ]; then
		echo ':qemu-arm:M::\x7fELF\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x28\x00:\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\xfb\xff\xff\xff:%{_bindir}/qemu-arm:' >/proc/sys/fs/binfmt_misc/register
	fi
	if [ "$cpu" != "ppc" -a -x "%{_bindir}/qemu-ppc" -a -d "%{_prefix}/qemu-ppc" ]; then
		echo ':ppc:M::\x7fELF\x01\x02\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x14:\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfb\xff\xff\xff:%{_bindir}/qemu-ppc:' >/proc/sys/fs/binfmt_misc/register
	fi
	if [ "$cpu" != "sparc" -a -x "%{_bindir}/qemu-sparc" -a -d "%{_prefix}/qemu-sparc" ]; then
		echo ':qemu-sparc:M::\x7fELF\x01\x02\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x02:\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfb\xff\xff\xff:$QEMU/qemu-sparc:' >/proc/sys/fs/binfmt_misc/register
	fi
	echo
}

stop() {
	echo -n $"Unregistering non-native binary handler for Qemu"
	for cpu in i386 i486 ppc arm sparc; do 
		if [ -r "/proc/sys/fs/binfmt_misc/qemu-$cpu" ]; then
			echo "-1" >/proc/sys/fs/binfmt_misc/qemu-$cpu
		fi
	done
	echo
}

restart() {
	stop
	start
}

status() {
	if ls /proc/sys/fs/binfmt_misc/qemu-* &>/dev/null; then 
		echo $"Qemu non-native binary format handlers registered."
		return 0
	else
		echo $"Qemu non-native binary format handlers not registered."
		return 1
	fi
}

case "$1" in
  start)
	start
	;;
  stop)
	stop
	;;
  restart|reload)
	restart
	;;
  condrestart)
	if status &>/dev/null; then
		restart
	fi
	;;
  status)
	status
	RETVAL=$?
	;;
  *)
	echo $"Usage: $prog {start|stop|restart|condrestart|status}"
	RETVAL=1
esac

exit $RETVAL
EOF



%build
%configure \
	--interp-prefix="%{_prefix}/qemu-%%M" \

%{__perl} -pi.orig -e '
		s|\$\(datadir\)|\$(datadir)/qemu|;
		s|\$\(sharedir\)|\$(datadir)/qemu|;
		s|\$\(prefix\)/bin|\$(bindir)|;
		s|/usr/share|\$(datadir)/qemu|;
	' Makefile* config-host.mak

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -Dp -m0755 qemu.sysv %{buildroot}%{_initrddir}/qemu

%post
/sbin/chkconfig --add qemu
/sbin/service qemu start &>/dev/null || :

%preun
if [ $1 -eq 0 ]; then
	/sbin/service qemu stop &>/dev/null || :
	/sbin/chkconfig --del qemu
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc *.html Changelog COPYING* README* TODO
%doc %{_mandir}/man1/qemu*
%config %{_initrddir}/qemu
%{_bindir}/qemu*
%dir %{_datadir}/qemu/
%{_datadir}/qemu/keymaps/
%{_datadir}/qemu/*.bin
%{_datadir}/qemu/*.elf
%{_datadir}/qemu/video.x
%exclude %{_datadir}/qemu/doc/

%changelog
* Thu Dec 29 2005 Dag Wieers <dag@wieers.com> - 0.8.0-1
- Updated to release 0.8.0.

* Sun Sep 11 2005 Dag Wieers <dag@wieers.com> - 0.7.2-1
- Updated to release 0.7.2.

* Sun May 01 2005 Dag Wieers <dag@wieers.com> - 0.7.0-1
- Updated to release 0.7.0.

* Wed Mar 23 2005 Dag Wieers <dag@wieers.com> - 0.6.1-3
- Removed erroneous dovecot reference. (Zolt�n V�r�sbaranyi)

* Mon Feb 28 2005 Dag Wieers <dag@wieers.com> - 0.6.1-2
- Added SDL-devel buildrequirement. (Matthias Saou)
- Fix for build problem on FC2.

* Wed Nov 17 2004 Dag Wieers <dag@wieers.com> - 0.6.1-1
- Updated to release 0.6.1.

* Tue Jul 20 2004 Dag Wieers <dag@wieers.com> - 0.6.0-1
- Updated to release 0.6.0.

* Fri May 28 2004 Dag Wieers <dag@wieers.com> - 0.5.5-3
- Fixed SDL relocation error on fc2. (David Woodhouse)

* Sun May 23 2004 Dag Wieers <dag@wieers.com> - 0.5.5-2
- Fixed libc.so.6(GLIBC_PRIVATE) dependency for fc2. (Christopher Stone)

* Wed May 12 2004 Dag Wieers <dag@wieers.com> - 0.5.5-1
- Updated to release 0.5.5.

* Fri Apr 30 2004 Dag Wieers <dag@wieers.com> - 0.5.4-1
- Initial package. (using DAR)
