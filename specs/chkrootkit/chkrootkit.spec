# $Id$
# Authority: dag

%{?dist: %{expand: %%define %dist 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

Summary: Check locally for signs of a rootkit
Name: chkrootkit
Version: 0.44
Release: 2
License: COPYRIGHTED
Group: Applications/System
URL: http://www.chkrootkit.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source0: ftp://ftp.pangeia.com.br/pub/seg/pac/chkrootkit-%{version}.tar.gz
Source1: chkrootkit.png
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: binutils

%description
chkrootkit is a tool to locally check for signs of a rootkit.

%prep
%setup

%{__cat} <<EOF >chkrootkit.apps
USER=root
PROGRAM=%{_libdir}/chkrootkit-%{version}/chkrootkit.sh
SESSION=true
EOF

%{__cat} <<EOF >chkrootkit.pam
#%PAM-1.0
auth       sufficient	pam_rootok.so
auth       sufficient   pam_timestamp.so
auth       required	pam_stack.so service=system-auth
session	   required	pam_permit.so
session    optional	pam_xauth.so
session    optional     pam_timestamp.so
account    required	pam_permit.so
EOF

%{__cat} <<'EOF' >chkrootkit.sh
#!/bin/sh
cd %{_libdir}/chkrootkit-%{version}
exec %{_libdir}/chkrootkit-%{version}/chkrootkit $@
EOF

%{__cat} <<EOF >xchkrootkit.sh
#!/bin/sh
%{_bindir}/chkrootkit
echo "Press ENTER to exit"
read ENDSCRIPT
EOF

%{__cat} <<EOF >chkrootkit.desktop
[Desktop Entry]
Name=Chkrootkit Rootkit Detection
Comment=Check your system for rootkits
Icon=chkrootkit.png
Exec=xchkrootkit
Terminal=true
Type=Application
Encoding=UTF-8
Categories=Application;System;
EOF

%build
%{__make} sense

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0644 chkrootkit.apps %{buildroot}%{_sysconfdir}/security/console.apps/chkrootkit
%{__install} -D -m0644 chkrootkit.pam %{buildroot}%{_sysconfdir}/pam.d/chkrootkit

%{__install} -D -m0755 xchkrootkit.sh %{buildroot}%{_bindir}/xchkrootkit
%{__ln_s} -f %{_bindir}/xchkrootkit %{buildroot}%{_bindir}/chkrootkitX
%{__ln_s} -f %{_bindir}/consolehelper %{buildroot}%{_bindir}/chkrootkit

%{__install} -d -m0755 %{buildroot}%{_libdir}/chkrootkit-%{version}/
%{__install} -m0755 check_wtmpx chkdirs chklastlog chkproc chkrootkit chkrootkit.sh chkwtmp ifpromisc strings-static %{buildroot}%{_libdir}/chkrootkit-%{version}/

%{__install} -D -m0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/chkrootkit.png

%if %{?_without_freedesktop:1}0
        %{__install} -D -m0644 chkrootkit.desktop %{buildroot}%{_datadir}/gnome/apps/Utilities/chkrootkit.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor %{desktop_vendor}    \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		chkrootkit.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ACKNOWLEDGMENTS COPYRIGHT README*
%config %{_sysconfdir}/pam.d/chkrootkit
%config %{_sysconfdir}/security/console.apps/chkrootkit
%{_bindir}/*
%{_libdir}/chkrootkit-%{version}/
%{_datadir}/pixmaps/chkrootkit.png
%{?_without_freedesktop:%{_datadir}/gnome/apps/Utilities/chkrootkit.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-chkrootkit.desktop}

%changelog
* Sun Jan 02 2005 Dag Wieers <dag@wieers.com> - 0.44-2
- Added binutils dependency. ()

* Mon Dec 06 2004 Dag Wieers <dag@wieers.com> - 0.44-2
- Fixed problem where options were discarded. (Steven Balthazor)

* Sun Oct 10 2004 Dag Wieers <dag@wieers.com> - 0.44-1
- Updated to release 0.44.

* Fri Mar 12 2004 Dag Wieers <dag@wieers.com> - 0.43-2
- Change to chkrootkit-path on execution. (gh)

* Tue Mar 02 2004 Dag Wieers <dag@wieers.com> - 0.43-1
- Fixed to the normal chkrootkit script. (Clifford Snow)

* Fri Feb 27 2004 Dag Wieers <dag@wieers.com> - 0.43-0
- Updated to release 0.43.

* Fri Aug 15 2003 Dag Wieers <dag@wieers.com> - 0.41-0
- Initial package. (using DAR)
