# $Id$
# Authority: dag

%define desktop_vendor rpmforge

Summary: Graphical front-end for the Subversion concurrent versioning system.
Name: rapidsvn
Version: 0.7.2
Release: 1
License: BSD
Group: Utilities/System
URL: http://rapidsvn.tigris.org/

Source: http://www.rapidsvn.org/download/rapidsvn-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: apr-devel, apr-util-devel, neon-devel
BuildRequires: autoconf >= 2.53, libtool >= 1.4.2
BuildRequires: docbook-style-xsl >= 1.58.1, doxygen, libxslt >= 1.0.27
BuildRequires: subversion-devel >= 1.0.0
BuildRequires: wxGTK-devel >= 2.4.2
BuildRequires: desktop-file-utils
Requires: subversion

%description
Subversion does the same thing CVS does (Concurrent Versioning System) but has
major enhancements compared to CVS.

This is a graphical front-end for Subversion.

%prep
%setup

%{__cat} <<EOF >rapidsvn.desktop
[Desktop Entry]
Name=RapidSVN Subversion Client
Comment=Manage SVN repositories
Icon=rapidsvn.png
Exec=rapidsvn
Terminal=false
Type=Application
Categories=Application;Development;
EOF

%build
export CPPFLAGS="-I/usr/include/subversion-1"
%configure \
	--with-svn-lib="%{_libdir}" \
	--with-docbook-xsl="%{_datadir}/sgml/docbook/xsl-stylesheets" \
	--disable-no-exceptions
# --with-wx-config="%{_bindir}/wxgtk-2.4-config" \
# --with-apr-config="%{_bindir}/apr-config" \
# --with-apu-config="%{_bindir}/apu-config" \
# --with-svn-include="%{_includedir}" \
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install \
	DESTDIR="%{buildroot}"

convert src/res/svn.ico rapidsvn.png
%{__install} -D -m0644 rapidsvn.png.0 %{buildroot}%{_datadir}/pixmaps/rapidsvn.png


%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor}    \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	rapidsvn.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc %{_mandir}/man1/rapidsvn.1*
%{_bindir}/rapidsvn
%exclude %{_libdir}/libsvncpp.a
%exclude %{_libdir}/libsvncpp.la
%{_libdir}/libsvncpp.so*
%{_includedir}/svncpp/
%{_datadir}/applications/%{desktop_vendor}-rapidsvn.desktop
%{_datadir}/pixmaps/rapidsvn.png

%changelog
* Tue Jan 04 2005 Dag Wieers <dag@wieers.com> - 0.7.2-1
- Initial package. (using DAR)
