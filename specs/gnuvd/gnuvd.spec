# $Id$

# Authority: dries
# Upstream: Dirk-Jan C. Binnema <djcb$djcbsoftware,nl>
# Screenshot: http://www.djcbsoftware.nl/projecten/gnuvd/gnuvd1.png

Summary: Dutch online dictionary
Name: gnuvd
Version: 1.0.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.djcbsoftware.nl/projecten/gnuvd/

Source: http://www.djcbsoftware.nl/code/gnuvd/gnuvd-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++
Obsoletes: %{name}-devel < %{version}

%description
A program which searches Dutch words in the online dictionary Van Dale.

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

#%package devel
#Summary: Header files, libraries and development documentation for %{name}.
#Group: Development/Libraries
#Requires: %{name} = %{version}-%{release}

#%description devel
#This package contains the header files, static libraries and development
#documentation for %{name}. If you like to develop programs using %{name},
#you will need to install %{name}-devel.

#%post
#/sbin/ldconfig 2>/dev/null

#%postun
#/sbin/ldconfig 2>/dev/null

%files
%defattr(-, root, root, 0755)
%doc README AUTHORS COPYING ChangeLog INSTALL NEWS README.nl
%{_bindir}/gnuvd
%doc %{_mandir}/man?/*
#%{_libdir}/*.so.*

#%files devel
#%defattr(-, root, root, 0755)
#%{_includedir}/libgnuvd/*.h
#%{_libdir}/*.a
#%{_libdir}/*.so
#%exclude %{_libdir}/*.la

%changelog
* Tue Aug 02 2005 Dries Verachtert <dries@ulyssis.org> 1.0.1-1
- Update to release 1.0.1.

* Tue Feb 08 2005 Dries Verachtert <dries@ulyssis.org> 1.0-1
- Update to release 1.0.

* Mon Oct 25 2004 Dries Verachtert <dries@ulyssis.org> 1.0beta5
- Update to release 1.0beta5

* Sat May 5 2004 Dries Verachtert <dries@ulyssis.org> 1.0beta4
- initial package
