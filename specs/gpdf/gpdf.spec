# $Id$

# Authority: dag

Summary: Grpahical PDF viewer
Name: gpdf
Version: 0.103
Release: 0
Group: Applications/Publishing
License: GPL
URL: http://www.inf.tu-dresden.de/~mk793652/gpdf/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://ftp.gnome.org/pub/GNOME/sources/gpdf/%{version}/gpdf-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libbonobo-devel >= 2.2.1
BuildRequires: libgnomeui-devel >= 2.0, libbonoboui-devel >= 2.0, gnome-vfs2-devel >= 2.0
BuildRequires: libgnomeprint22-devel >= 2.2, libgnomeprintui22-devel >= 2.2, libglade2-devel >= 2.0

%description
gpdf is a GNOME PDF viewer, based on Xpdf.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog CHANGES COPYING NEWS README
%{_bindir}/*
%{_libexecdir}/*
%{_libdir}/bonobo/servers/*.server
%{_datadir}/gpdf/
%{_datadir}/applications/*.desktop
%{_datadir}/application-registry/*.applications
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/mime-info/*.keys
%{_datadir}/pixmaps/gpdf/

%changelog
* Fri May 23 2003 Dag Wieers <dag@wieers.com> - 0.102-0
- Updated to release 0.102.

* Mon May 05 2003 Dag Wieers <dag@wieers.com> - 0.101-0
- Updated to release 0.101.

* Fri Apr 11 2003 Dag Wieers <dag@wieers.com> - 0.100-0
- Initial package. (using DAR)
