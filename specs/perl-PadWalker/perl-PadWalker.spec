# $Id$
# Authority: dag
# Upstream: Robin Houston <robin-cpan$kitsite,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name PadWalker

Summary: Perl module to play with other peoples' lexical variables
Name: perl-PadWalker
Version: 1.5
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/PadWalker/

Source: http://www.cpan.org/authors/id/R/RO/ROBIN/PadWalker-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 2:5.8.2, perl(ExtUtils::MakeMaker)

%description
perl-PadWalker is a Perl module to play with other peoples' lexical variables.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/PadWalker.3pm*
%{perl_vendorarch}/PadWalker.pm
%{perl_vendorarch}/auto/PadWalker/

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 1.5-1
- Initial package. (using DAR)
