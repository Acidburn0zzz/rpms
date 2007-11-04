# $Id$
# Authority: dag
# Upstream: Dan Kogai <dankogai$dan,co,jp>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name URI-Escape-XS

Summary: Perl module that is a drop-in replacement for URI::Escape
Name: perl-URI-Escape-XS
Version: 0.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/URI-Escape-XS/

Source: http://www.cpan.org/modules/by-module/URI/URI-Escape-XS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-URI-Escape-XS is a Perl module that is a drop-in replacement
for URI::Escape.

This package contains the following Perl module:

    URI::Escape::XS

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/URI::Escape::XS.3pm*
%dir %{perl_vendorarch}/URI/
%dir %{perl_vendorarch}/URI/Escape/
%{perl_vendorarch}/URI/Escape/XS.pm
%dir %{perl_vendorarch}/auto/URI/
%dir %{perl_vendorarch}/auto/URI/Escape/
%{perl_vendorarch}/auto/URI/Escape/XS/

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
