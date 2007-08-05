# $Id$
# Authority: dag
# Upstream: Matt Sergeant <msergeant$cpan,org>

# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Parser

Summary: XML-Parser Perl module
Name: perl-XML-Parser
Version: 2.34
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Parser/

Source: http://www.cpan.org/modules/by-module/XML/XML-Parser-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.004, expat-devel, perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.004

%description
XML-Parser Perl module.

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

### Clean up docs
find samples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README samples/
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/XML/
%{perl_vendorarch}/XML/Parser/
%{perl_vendorarch}/XML/Parser.pm
%dir %{perl_vendorarch}/auto/XML/
%{perl_vendorarch}/auto/XML/Parser/Expat/

%changelog
* Fri Nov 12 2004 Dag Wieers <dag@wieers.com> - 2.34-1
- Workaround directory-conflicts bug in up2date. (RHbz #106123)

* Sat Dec 20 2003 Dag Wieers <dag@wieers.com> - 2.34-0
- Initial package. (using DAR)
