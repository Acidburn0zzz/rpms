# $Id$
# Authority: matthias

%define jpegmmxver 0.1.4

Summary: Tools for the movtar MJPEG video format
Name: libmovtar
Version: 0.1.3
Release: 3
License: GPL
Group: Applications/Multimedia
URL: http://mjpeg.sourceforge.net/
Source0: http://dl.sf.net/mjpeg/libmovtar-%{version}.tar.gz
Source1: http://dl.sf.net/mjpeg/jpeg-mmx-%{jpegmmxver}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: SDL, glib
BuildRequires: SDL-devel, glib-devel
# Sorry... :-(
ExclusiveArch: %{ix86}
%ifarch %{ix86}
BuildRequires: nasm
%endif

%description
This package includes libmovtar, the support library, and various
tools which together implement the movtar MJPEG video format.


%package devel
Summary: Development headers and libraries for the movtar MJPEG video format
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains static libraries and C system header files
needed to compile applications that use part of the libraries
of the mjpegtools package.


%prep
%setup -a 1
%{__mv} jpeg-mmx-* jpeg-mmx

%build
# For x86, we link against the bundled jpeg-mmx
%ifarch %{ix86}
    (cd jpeg-mmx && %configure && %{__make} libjpeg-mmx.a)
    %configure --with-jpeg-mmx="`pwd`/jpeg-mmx"
%else
    %configure
%endif
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README*
%{_bindir}/movtar_*
%{_bindir}/pnm2rtj
%{_bindir}/rtjshow

%files devel
%defattr(-, root, root, 0755)
%{_bindir}/movtar-config
%{_includedir}/*
%{_libdir}/*.a
%{_datadir}/aclocal/*

%changelog
* Tue Nov 11 2003 Matthias Saou <http://freshrpms.net/> 0.1.3-3.fr
- Rebuild for Fedora Core 1.
- Added missing nasm build requirement for jpeg-mmx.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Initial release for Red Hat Linux 9.

