# $Id$

Summary: Portable C library for dynamically generating PDF files
Name: pdflib
Version: 4.0.3
Release: 1
License: Aladdin Free Public License
Group: System Environment/Libraries
URL: http://www.pdflib.com/
Source: http://www.pdflib.com/pdflib/download/pdflib-%{version}.tar.gz
Patch0: pdflib-4.0.3-DESTDIR.patch
Patch1: pdflib-4.0.3-shared-libs.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
# perl, python, tcl bindings are disabled on purpose : the goal was only to
# get the php module built
BuildRequires: libpng-devel, zlib-devel

%description
PDFlib is a C library for generating PDF files. It offers a graphics
API with support for drawing, text, fonts, images, and hypertext. Call
PDFlib routines from within your client program and voila: dynamic PDF
files! For detailed instructions on PDFlib programming and the
associated API, see the PDFlib Programming Manual, included in PDF
format in the PDFlib distribution.


%package devel
Summary: Development files for pdflib
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
PDFlib is a C library for generating PDF files. It offers a graphics
API with support for drawing, text, fonts, images, and hypertext. Call
PDFlib routines from within your client program and voila: dynamic PDF
files! For detailed instructions on PDFlib programming and the
associated API, see the PDFlib Programming Manual, included in PDF
format in the PDFlib distribution.

This package contains the files needed for compiling programs that will use
the PDFlib library.


%prep
%setup -q
%patch0 -p1 -b destdir
%patch1 -p1 -b shared


%build
%configure \
    --enable-cxx \
    --enable-shared-pdflib \
    --with-zlib \
    --with-pnglib
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0644 bind/cpp/pdflib.hpp %{buildroot}%{_includedir}/pdflib.hpp


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc readme.txt doc/*.txt doc/aladdin-license.pdf
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/PDFlib-manual.pdf
%{_bindir}/pdflib-config
%{_includedir}/*
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so


%changelog
* Wed Feb  9 2005 Matthias Saou <http://freshrpms.net/> 4.0.3-1
- Spec file cleanup.

* Wed Apr 16 2003 Matthias Saou <http://freshrpms.net/>
- Grrr, lost my old spec and .src.rpm, rebuilt one based on the PLD spec.

