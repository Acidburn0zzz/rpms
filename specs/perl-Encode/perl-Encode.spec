# $Id$
# Authority: dag
# Upstream: Dan Kogai <dankogai$dan,co,jp>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Encode

Summary: Perl module that implements character encodings
Name: perl-Encode
Version: 2.20
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Encode/

Source: http://www.cpan.org/modules/by-module/Encode/Encode-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 1:5.7.3, perl(ExtUtils::MakeMaker)

%description
perl-Encode is a Perl module that implements character encodings.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS Changes MANIFEST META.yml README
%{_bindir}/enc2xs
%{_bindir}/piconv
%{perl_vendorarch}/Encode/
%{perl_vendorarch}/Encode.pm
%{perl_vendorarch}/encoding.pm
%{perl_vendorarch}/auto/Encode/

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 2.20-1
- Initial package. (using DAR)
