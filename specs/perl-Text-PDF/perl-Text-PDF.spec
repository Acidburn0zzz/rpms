# $Id$
# Authority: dries
# Upstream: Martin Hosken <martin_hosken$sil,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-PDF

Summary: PDF Functions
Name: perl-Text-PDF
Version: 0.29
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-PDF/

Source: http://www.cpan.org/modules/by-module/Text/Text-PDF-%{version}a.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
PDF functions for Perl.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST MANIFEST.SKIP META.yml readme.txt examples/
%doc %{_mandir}/man3/Text::PDF.3pm*
%doc %{_mandir}/man3/Text::PDF::*.3pm*
%{_bindir}/pdfbklt
%{_bindir}/pdfrevert
%{_bindir}/pdfstamp
%dir %{perl_vendorlib}/Text/
%{perl_vendorlib}/Text/PDF/
%{perl_vendorlib}/Text/PDF.pm

%changelog
* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.29-1
- Updated to release 0.29.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.25-1
- Initial package.
