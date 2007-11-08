# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Socket6

Summary: IPv6 related part of the C socket.h defines and structure manipulators
Name: perl-Socket6
Version: 0.19
Release: 1.2
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Socket6/

Source: http://www.cpan.org/modules/by-module/Socket6/Socket6-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker) >= 0:5.00503
Requires: perl >= 0:5.00503

%description
This perl module supports getaddrinfo() and getnameinfo() to intend to
enable protocol independent programing.
If your environment supports IPv6, IPv6 related defines such as
AF_INET6 are included.


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
%doc ChangeLog MANIFEST README
%{perl_vendorarch}/Socket6.pm
%{perl_vendorarch}/auto/Socket6/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.19-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.19-1
- Updated to release 0.19.

* Wed Mar 30 2005 Dag Wieers <dag@wieers.com> - 0.18-1
- Initial package. (using DAR)
