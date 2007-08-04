# $Id$
# Authority: dag
# Upstream: Björn Höhrmann <bjoern$hoehrmann,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-Encoding

Summary: Perl module to determine the encoding of HTML/XML/XHTML documents
Name: perl-HTML-Encoding
Version: 0.53
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-Encoding/

Source: http://www.cpan.org/modules/by-module/HTML/HTML-Encoding-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-HTML-Encoding is a Perl module to determine the encoding
of HTML/XML/XHTML documents.

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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/HTML::Encoding.3pm*
%dir %{perl_vendorlib}/HTML/
%{perl_vendorlib}/HTML/Encoding.pm

%changelog
* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 0.53-1
- Initial package. (using DAR)
