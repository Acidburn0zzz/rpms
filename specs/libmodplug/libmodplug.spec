# $Id$
# Authority: dag

Summary: MOD music file playing library
Name: libmodplug
Version: 0.7
Release: 1
License: Public Domain
Group: System Environment/Libraries
URL: http://modplug-xmms.sourceforge.net/

Source: http://dl.sf.net/modplug-xmms/libmodplug-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Libmodplug is the library behind Modplug-XMMS, a fully featured, complete
input plugin for XMMS which plays mod-like music formats.

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

%build
%configure --enable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README TODO
%{_libdir}/libmodplug.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libmodplug/
%{_libdir}/libmodplug.a
%exclude %{_libdir}/libmodplug.la
%{_libdir}/libmodplug.so
%{_libdir}/pkgconfig/libmodplug.pc

%changelog
* Wed Apr 06 2005 Dag Wieers <dag@wieers.com> - 0.7-1
- Initial package. (using DAR)
