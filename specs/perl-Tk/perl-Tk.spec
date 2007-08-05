# $Id$
# Authority: dries
# Upstream: Nick Ing-Simmons <nick$ing-simmons,net>

%{?dist: %{expand: %%define %dist 1}}

%{!?dist:%define _with_modxorg 1}
%{?fc7:  %define _with_modxorg 1}
%{?el5:  %define _with_modxorg 1}
%{?fc6:  %define _with_modxorg 1}
%{?fc5:  %define _with_modxorg 1}

%{?rh9:%define _without_tcltk_devel 1}
%{?rh8:%define _without_tcltk_devel 1}
%{?rh7:%define _without_tcltk_devel 1}
%{?el2:%define _without_tcltk_devel 1}
%{?rh6:%define _without_tcltk_devel 1}

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tk

Summary: Object Oriented Tk extension for Perl
Name: perl-Tk
Version: 804.027
Release: 3.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tk/

Source: http://www.cpan.org/modules/by-module/Tk/Tk-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 1:5.7.0, libpng-devel, libjpeg-devel
%{?_with_modxorg:BuildRequires: libX11-devel}
%{!?_with_modxorg:BuildRequires: XFree86-devel}
%{!?_without_tcltk_devel:BuildRequires: tk-devel}
%{?_without_tcltk_devel:BuildRequires: tk}
Provides: perl(Tk::LabRadio), perl(Tk::TextReindex)

%description
This module contains an object oriented Tk extension for Perl.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL XFT=1 INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" X11LIB=%{_prefix}/X11R6/%{_lib}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__perl} -pi -e 's|/bin/perl|%{_bindir}/perl|g' %{buildroot}%{perl_vendorarch}/Tk/reindex.pl
%{__perl} -pi -e 's|/usr/local/bin/perl|%{_bindir}/perl|g' \
	%{buildroot}%{perl_vendorarch}/Tk/demos/widtrib/plop.pl \
	%{buildroot}%{perl_vendorarch}/Tk/demos/widtrib/npuz.pl \
	%{buildroot}%{perl_vendorarch}/Tk/pTk/mkVFunc \
	%{buildroot}%{perl_vendorarch}/Tk/pTk/Tcl-pTk \
	%{buildroot}%{perl_vendorarch}/Tk/Text.pod
%{__rm} -rf %{buildroot}%{perl_archlib}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%doc %{_mandir}/man1/*
%{_bindir}/gedi
%{_bindir}/ptked
%{_bindir}/ptksh
%{_bindir}/tkjpeg
%{_bindir}/widget
%{perl_vendorarch}/Tie/Watch.pm
%{perl_vendorarch}/Tk.pm
%{perl_vendorarch}/Tk.pod
%{perl_vendorarch}/Tk/
%{perl_vendorarch}/auto/Tk/
%{perl_vendorarch}/fix_4_os2.pl

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 804.027-3.2
- Rebuild for Fedora Core 5.

* Sun Aug 14 2005 Dries Verachtert <dries@ulyssis.org> - 804.027-3
- Enable XFT support (thanks to Void Main).

* Sun Aug 14 2005 Dries Verachtert <dries@ulyssis.org> - 804.027-2
- Fix for x86_64.

* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 804.027-1
- Initial package.
