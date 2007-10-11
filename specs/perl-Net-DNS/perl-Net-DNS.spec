# $Id$
# Authority: dag
# Upstream: Olaf Kolkman <olaf$net-dns,org>

##ExcludeDist: el4

%{?dist: %{expand: %%define %dist 1}}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-DNS

Summary: Perl DNS resolver module
Name: perl-Net-DNS
Version: 0.61
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-DNS/

Source: http://www.cpan.org/modules/by-module/Net/Net-DNS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.00503, perl(Digest::HMAC), perl(ExtUtils::MakeMaker)
%{!?el2:BuildRequires: perl(Digest::MD5) >= 2.12, perl(MIME::Base64) >= 2.11}
%{?el2:BuildRequires: perl-Digest-MD5 >= 2.12, perl-MIME-Base64 >= 2.11}
Requires: perl >= 0:5.00503, perl(Digest::HMAC)
%{!?el2:Requires: perl(Digest::MD5) >= 2.12, perl(MIME::Base64) >= 2.11}
%{?el2:Requires: perl-Digest-MD5 >= 2.12, perl-MIME-Base64 >= 2.11}

%description
Net::DNS is a DNS resolver implemented in Perl.  It allows the
programmer to perform nearly any type of DNS query from a Perl
script.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" \
    --no-online-tests
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find contrib/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README TODO contrib/
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Net/
%{perl_vendorarch}/Net/DNS/
%{perl_vendorarch}/Net/DNS.pm
%dir %{perl_vendorarch}/auto/Net/
%{perl_vendorarch}/auto/Net/DNS/

### Remove this file because it generates an rpm dependency for Win32::Registry
%exclude %{perl_vendorarch}/Net/DNS/Resolver/Win32.pm

%changelog
* Mon Aug 27 2007 Dag Wieers <dag@wieers.com> - 0.61-1
- Updated to release 0.61.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.59-1
- Updated to release 0.59.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.58-1
- Updated to release 0.58.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.57-1
- Updated to release 0.57.

* Sat Nov 05 2005 Dries Verachtert <dries@ulyssis.org> - 0.53-1
- Updated to release 0.53.

* Wed Oct 20 2004 Dries Verachtert <dries@ulyssis.org> - 0.48-1
- Updated to release 0.48.

* Sat Jun 19 2004 Dag Wieers <dag@wieers.com> - 0.47-1
- Updated to release 0.47.

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 0.38-0
- Updated to release 0.38.

* Sun Jan 26 2003 Dag Wieers <dag@wieers.com> - 0.33-0
- Initial package. (using DAR)
