# $Id$
# Authority: dries
# Upstream: Damian Conway <damian$conway,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Perl6-Slurp

Summary: Implements the Perl 6 'slurp' built-in
Name: perl-Perl6-Slurp
Version: 0.03
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Perl6-Slurp/

Source: http://www.cpan.org/modules/by-module/Perl6/Perl6-Slurp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This package implements the Perl 6 'slurp' built-in.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Perl6/
%{perl_vendorlib}/Perl6/Slurp.pm

%changelog
* Tue Dec 07 2004 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
