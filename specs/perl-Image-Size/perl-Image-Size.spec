# $Id$

# Authority: dries
# Upstream: Randy J Ray <rjray$blackperl,com>


%define real_name Image-Size
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Read the dimensions of images
Name: perl-Image-Size
Version: 2.992
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Image-Size/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/R/RJ/RJRAY/Image-Size-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module contains functions for reading the dimensions of images in several popular formats.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README ChangeLog
%{_bindir}/imgsize
%{_mandir}/man?/*
%{perl_vendorlib}/Image/Size.pm
%{perl_vendorlib}/auto/Image/Size/*

%changelog
* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 2.992
- Initial package.
