# $Id$
# Authority: dries
# Upstream: Adam Kennedy <cpan$ali,as>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Module-Extract

Summary: Base class for creating modules
Name: perl-Module-Extract
Version: 0.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Extract/

Source: http://search.cpan.org//CPAN/authors/id/A/AD/ADAMK/Module-Extract-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Module::Extract is a convenience base class for creating module that
work with Perl distributions.

Its purpose is to take care of the mechanisms of locating and extracting
a Perl distribution so that your module can do something specific to the
distribution.

This module was originally created to provide an abstraction for the
extraction logic for both Module::Inspector and Module::P4P and to allow
additional features to be added in the future without having to modify
both of them, because the general problem of "locate, download, and
expand a distribution" is one that is almost ideal for adding additional
features down the line.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Module::Extract*
%{perl_vendorlib}/Module/Extract.pm

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
