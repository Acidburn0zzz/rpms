# $Id$
# Authority: dag

%define real_version 0.7.4

Summary: Graphical music notation program
Name: denemo
Version: 0.7.4
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://denemo.sourceforge.net/

Source: http://dl.sf.net/denemo/denemo-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gtk+-devel, libxml2-devel, pkgconfig, gcc-c++
BuildRequires: gtk2-devel

%description
Denemo is a graphical music notation program written in C with
gtk+. It is intended to be used in conjunction with GNU Lilypond
(http://www.cs.uu.nl/hanwen/lilypond/), but is adaptable to other
computer-music-related purposes as well. 

%prep
%setup -n %{name}-%{real_version}

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
%doc AUTHORS ChangeLog COPYING DESIGN GOALS NEWS README TODO
%config(noreplace) %{_datadir}/denemo/denemo.conf
%config %{_datadir}/denemo/*.keymaprc
%dir %{_datadir}/denemo/
%{_datadir}/denemo/
%{_bindir}/*
%{_includedir}/denemo/

%changelog
* Mon Dec 12 2005 Dries Verachtert <dries@ulyssis.org> - 0.7.4-1
- Updated to release 0.7.4.

* Sat Mar 06 2004 Dag Wieers <dag@wieers.com> - 0.7.2-0.a
- Updated to release 0.7.2a.

* Wed Oct 15 2003 Dag Wieers <dag@wieers.com> - 0.7.1-0
- Initial package. (using DAR)
