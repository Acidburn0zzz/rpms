# $Id$
# Authority: dries
# Upstream: Stanislav Malyshev <frodo$sharat,co,il>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Lingua-IW-Logical

Summary: Module for working with logical and visual hebrew
Name: perl-Lingua-IW-Logical
Version: 0.5
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lingua-IW-Logical/

Source: http://search.cpan.org/CPAN/authors/id/S/SM/SMALYSHEV/Lingua-IW-Logical-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module allows to convert logical Hebrew representation (like used in
Windows and defined in Unicode standard) to logical representation (like
in iso-8859-8). These represetation differ in the way they represent
bi-directional texts. See Unicode book for more info.

This is very common task for Hebrew HTML developers, since
most of the Hebrew pages are written in visual represetation (in order to
allow users of non-Hebrew-enabled OSes to viw them) but most Windows
programs use logical one. Also, some basic formatting options are
available while converting.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Lingua/IW/Logical.p*

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.5-1
- Initial package.
