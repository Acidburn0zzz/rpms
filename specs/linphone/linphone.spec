# $Id$
# Authority: dag
# Upstream: Simon Morlat <simon.morlat$linphone,org>

%{?fc1:%define _without_alsa 1}
%{?fc1:%define _without_gnome_applet 1}
%{?el3:%define _without_alsa 1}
%{?el3:%define _without_gnome_applet 1}
%{?rh9:%define _without_alsa 1}
%{?rh9:%define _without_gnome_applet 1}
%{?rh7:%define _without_alsa 1}
%{?rh7:%define _without_gnome_applet 1}
%{?el2:%define _without_alsa 1}
%{?el2:%define _without_gnome_applet 1}

%define desktop_vendor rpmforge

Summary: Software Internet phone using SIP
Name: linphone
Version: 0.12.2
Release: 1
License: GPL
Group: Applications/Communications
URL: http://www.linphone.org/

Source: http://simon.morlat.free.fr/download/%{version}/source/linphone-%{version}.tar.gz
Patch: linphone-0.12.2-speex.patch
Patch1: linphone-0.12.2-docs.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext, glib2-devel, libgnomeui-devel
BuildRequires: libosip-devel, speex-devel
%{!?_without_alsa:BuildRequires: alsa-lib-devel}
%{!?_without_gnome_applet:BuildRequires: gnome-panel-devel}
Requires: /sbin/ldconfig

%description
Linphone is a web phone: it let you phone to your friends anywhere in
the world, freely, simply by using the internet. The cost of the phone
call is the cost that you spend connected to the internet.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
%patch -p1 -b .speex
%patch1 -p1 -b .docs

%{__rm} -rf speex/ oRTP/docs/

%{__perl} -pi.orig -e 's|\$\(prefix\)/lib|\$(libdir)|g' share/Makefile.in

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install \
	--delete-original                          \
	--vendor %{desktop_vendor}                 \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/gnome/apps/Internet/linphone.desktop

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING NEWS README TODO
%doc %{_mandir}/man1/*
%doc %{_datadir}/gnome/help/linphone/
%doc %{_datadir}/gtk-doc/html/mediastreamer/
%{_bindir}/*
%{_libdir}/bonobo/servers/GNOME_LinphoneApplet.server
%{_libdir}/*.so.*
%{_libexecdir}/linphone_applet
%{_datadir}/applications/%{desktop_vendor}-linphone.desktop
%{_datadir}/gnome-2.0/ui/GNOME_LinphoneApplet.xml
%{_datadir}/linphonec/
%{_datadir}/pixmaps/linphone/
%{_datadir}/sounds/linphone/

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/linphone/
%{_includedir}/ortp/
%{_includedir}/osipua/
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/linphone.pc

%changelog
* Sun Mar 13 2005 Dag Wieers <dag@wieers.com> - 0.12.2-1
- Initial package. (using DAR)
