# $Id$
# Authority: dag

Summary: Monitors hardware sensors
Name: gnome-sensors
Version: 0.9a
Release: 0
License: GPL
Group: Applications/System
URL: http://vkcorp.org/

Source: http://vedder.homelinux.org:81/%{name}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: lm_sensors-devel

%description
Monitors hardware sensors.

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
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/*
%{_libdir}/bonobo/servers/*

%changelog
* Tue Jan 28 2003 Dag Wieers <dag@wieers.com> - 0.9a
- Initial package. (using DAR)

