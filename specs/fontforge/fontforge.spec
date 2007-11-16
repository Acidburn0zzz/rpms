# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{!?dtag:%define _with_modxorg 1}
%{?fc7:  %define _with_modxorg 1}
%{?el5:  %define _with_modxorg 1}
%{?fc6:  %define _with_modxorg 1}
%{?fc5:  %define _with_modxorg 1}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

Summary: Outline and bitmap font editor
Name: fontforge
Version: 0.0
Release: 0.cvs20050502.2
License: BSD
Group: Applications/Publishing
URL: http://fontforge.sourceforge.net/

Source: http://dl.sf.net/fontforge/fontforge_full-20050502.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: freetype-devel, libuninameslist-devel
BuildRequires: libjpeg-devel, libpng-devel, libtiff-devel, libungif-devel
BuildRequires: libxml2-devel
%{?_with_modxorg:BuildRequires: libX11-devel, libSM-devel, libXi-devel}
%{!?_with_modxorg:BuildRequires: XFree86-devel}
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
Obsoletes: pfaedit

%description
FontForge (former PfaEdit) is a font editor for outline and bitmap
fonts. It supports a range of font formats, including PostScript
(ASCII and binary Type 1, some Type 3 and Type 0), TrueType, OpenType
(Type2) and CID-keyed fonts.

%prep
%setup -n %{name}-20050502

%{__perl} -pi.orig -e 's|-rpath \$\(libdir\)||' fontforge/Makefile*.in
%{__perl} -pi.orig -e 's|("mozilla", "opera",)|"htmlview", "firefox", $1|' fontforge/uiutil.c

%{__cat} <<EOF >fontforge.desktop
[Desktop Entry]
Name=FontForge Font Editor
Comment=Edit and convert fonts
Exec=fontforge
Icon=icon-accessories.png
Terminal=false
Type=Application
Categories=Application;Graphics;
Encoding=UTF-8
MimeType=application/x-font;application/x-font-bdf;application/x-font-ttf;application/x-font-truetype;application/x-truetype-font;application/font-tdpfr;application/x-font-afm;application/x-font-type1;application/x-font-bdf
EOF

%build
%configure \
	--with-freetype-bytecode="no" \
	--with-regular-link
%{__make} #%{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%if %{?_without_freedesktop:1}0
	%{__install} -Dp -m0644 fontforge.desktop %{buildroot}%{_datadir}/gnome/apps/Utilities/fontforge.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install \
		--vendor %{desktop_vendor} \
		--add-category X-Red-Hat-Base \
		--dir %{buildroot}%{_datadir}/applications \
		fontforge.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig 2>/dev/null
update-desktop-database %{_datadir}/applications &>/dev/null || :

%postun
/sbin/ldconfig 2>/dev/null
update-desktop-database %{_datadir}/applications &>/dev/null || :

%files
%defattr(-, root, root, 0755)
%doc AUTHORS LICENSE README README-unix
%doc %{_mandir}/man1/fontforge.1*
%doc %{_mandir}/man1/sfddiff.1*
%{_bindir}/fontforge
%{_bindir}/pfaedit
%{_bindir}/sfddiff
%{_libdir}/libg*.so.*
%{_libdir}/pkgconfig/fontforge.pc
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-fontforge.desktop}
%{?_without_freedesktop:%{_datadir}/gnome/apps/Utilities/fontforge.desktop}
%{_datadir}/fontforge/
%exclude %{_libdir}/*.la
%exclude %{_libdir}/*.so

%changelog
* Mon May 30 2005 Dag Wieers <dag@wieers.com> - 0.0-0.20050502
- Initial package. (using DAR)
