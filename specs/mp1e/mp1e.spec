# $Id$

# Authority: dag

Summary: Real-time software MPEG-1 video/audio encoder.
Name: mp1e
Version: 1.9.3
Release: 1
License: GPL
Group: Applications/Multimedia

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/zapping/mp1e-%{version}.tar.bz2
Patch0: mp1e-1.9.3-common.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: esound-devel, audiofile-devel
#BuildRequires: alsa-lib-devel >= 0.9.0

%description
Real-time software MPEG-1 video/audio encoder.

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
%patch0

%build
%{__libtoolize} --force
%{__aclocal} -I macros
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-dependency-tracking \
	--enable-shared \
	--enable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr (-, root, root, 0755)
%doc ChangeLog README
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr (-, root, root, 0755)
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so

%changelog
* Sat Mar 13 2004 Dag Wieers <dag@wieers.com> - 1.9.3-1
- Initial package. (using DAR)
