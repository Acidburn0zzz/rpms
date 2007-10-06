# $Id$
# Authority: dries
# Upstream: Andy Wardley <cpan$wardley,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Template-Toolkit

Summary: Template processing system
Name: perl-Template-Toolkit
Version: 2.19
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Template-Toolkit/

Source: http://www.cpan.org/modules/by-module/Template/Template-Toolkit-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker), perl(AppConfig)

%description
The Template Toolkit is a collection of modules which implement a
fast, flexible, powerful and extensible template processing system.
It was originally designed and remains primarily useful for generating
dynamic web content, but it can be used equally well for processing
any other kind of text based documents: HTML, XML, POD, PostScript,
LaTeX, and so on.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" \
    TT_DBI="n" TT_XS_ENABLE="y" TT_ACCEPT="y"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}" \
    TT_PREFIX="%{_datadir}/tt2"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install \
    PREFIX="%{buildroot}%{_prefix}" \
    TT_PREFIX="%{buildroot}%{_datadir}/tt2"
#   PERLPREFIX=%{buildroot}/usr \
#   SITEPREFIX=%{buildroot}/usr \
#   VENDORPREFIX=%{buildroot}/usr \

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find docs/ examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes HACKING INSTALL MANIFEST META.yml README TODO docs/ examples/
%doc %{_mandir}/man1/*.1*
%doc %{_mandir}/man3/*.3pm*
#%{_datadir}/tt2/
%{_bindir}/tpage
%{_bindir}/ttree
%{perl_vendorarch}/Template/
%{perl_vendorarch}/Template.pm
%{perl_vendorarch}/auto/Template/

%changelog
* Fri Oct  5 2007 Dave Miller <justdave@mozilla.com> - 2.19-1
- Updated to release 2.19.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 2.15-1
- Updated to release 2.15.

* Thu Nov 04 2004 Dries Verachtert <dries@ulyssis.org> - 2.14-1
- Initial package.
