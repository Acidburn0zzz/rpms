# $Id$
# Authority: dag

# ExclusiveDist: rh8 rh9

%{?dist: %{expand: %%define %dist 1}}

Summary: The GNOME Structure file library
Name: libgsf
Version: 1.6.0
Release: 0.2
License: LGPL
Group: System Environment/Libraries
URL: http://ftp.acc.umu.se/pub/GNOME/sources/libgsf/1.6/

Source: http://ftp.acc.umu.se/pub/GNOME/sources/libgsf/1.6/libgsf-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: gnome-vfs2-devel >= 2.0.0, libbonobo-devel >= 2.0.0
BuildRequires: gtk-doc >= 0.9
%{?fc4:BuildRequires: pyorbit-devel}
%{?rh9:BuildRequires: pyorbit-devel}
%{?rh8:BuildRequires: orbit-python-devel}

%description
The GNOME Structured file library.  At its root it is a replacement
and generalization of libole2.  It can read & write MS OLE2 file, and
Zip files.

%package devel
Summary: Development files for the GNOME Structured File format
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
Headers and static libraries for libgsf.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog NEWS README TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc HACKING
%doc %{_datadir}/doc/libgsf/
%{_includedir}/libgsf-1/
%{_libdir}/pkgconfig/*
%{_libdir}/*.a
%{_libdir}/*.so
%exclude %{_libdir}/*.la

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.6.0-0.2
- Rebuild for Fedora Core 5.

* Wed Jan 22 2003 Dag Wieers <dag@wieers.com> - 1.4.0
- Initial package.
