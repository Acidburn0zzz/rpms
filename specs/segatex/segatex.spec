# $Id$
# Authority: dries
# Upstream: Shintaro Fujiwara <shin216$xf7,so-net,ne,jp>

Summary: Create SELinux policies
Name: segatex
Version: 3.05
Release: 1
License: GPL
Group: Applications/System
URL: http://sourceforge.net/projects/segatex/

Source: http://dl.sf.net/segatex/segatex-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, gettext, boost-devel, qt-devel >= 1:3.3
BuildRequires: desktop-file-utils, libselinux-devel

%description
Segatex is a tool to configure SELinux policy with the help of GUI.
Just push a button and it will generate a .te file in the same
directory. You can then edit your .te file, make a module, and
install.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Segatex
Comment=Create SELinux policies
Exec=segatex
Terminal=false
Type=Application
StartupNotify=true
Categories=Application;Development;
Encoding=UTF-8
EOF

%build
qmake segatex.pro
%{__make} %{?_smp_mflags} SUBLIBS="-lboost_regex -lselinux"

%install
%{__rm} -rf %{buildroot}
%{__install} -D segatex %{buildroot}%{_bindir}/segatex

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor rpmforge             \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_bindir}/segatex
%{_datadir}/applications/*-segatex.desktop

%changelog
* Tue Jul 10 2007 Dries Verachtert <dries@ulyssis.org> - 3.05-1
- Updated to release 3.05.

* Tue Nov 21 2006 Dries Verachtert <dries@ulyssis.org> - 3.04-1
- Updated to release 3.04.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 3.03-1
- Updated to release 3.03.

* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 3.02-1
- Updated to release 3.02.

* Thu Aug 24 2006 Dries Verachtert <dries@ulyssis.org> - 2.11-1
- Updated to release 2.11.

* Mon Aug 21 2006 Dries Verachtert <dries@ulyssis.org> - 2.09-1
- Updated to release 2.09.

* Mon Aug 21 2006 Dries Verachtert <dries@ulyssis.org> - 2.08-1
- Updated to release 2.08.

* Fri Aug 11 2006 Dries Verachtert <dries@ulyssis.org> - 2.03-1
- Initial package.
