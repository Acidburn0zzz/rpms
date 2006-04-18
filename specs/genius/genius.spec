# $Id$
# Authority: dag

Summary: Advanced calculator
Name: genius
Version: 0.5.6
Release: 0.2
License: GPL
Group: Applications/Engineering
URL: http://www.5z.com/jirka/genius.html

Source: http://ftp.5z.com/pub/genius/genius-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel, vte-devel, libgnomeui-devel >= 2.0, gcc-c++
BuildRequires: gtksourceview-devel >= 0.3, libglade2-devel >= 1.99
BuildRequires: readline-devel, ncurses-devel, gmp-devel, flex

%description
Genius is an advanced calculator and a mathematical programming language.
It handles multiple precision floating point numbers, infinite precision
integers, complex numbers and matrixes.

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
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/*
%{_datadir}/genius/
%{_libdir}/genius/
%{_libexecdir}/*
%{_includedir}/genius/
%{_datadir}/applications/*.desktop

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.5.6-0.2
- Rebuild for Fedora Core 5.

* Mon Nov 24 2003 Dag Wieers <dag@wieers.com> - 0.5.6-0
- Initial package. (using DAR)
