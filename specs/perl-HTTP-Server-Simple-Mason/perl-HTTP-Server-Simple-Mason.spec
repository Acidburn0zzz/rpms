# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTTP-Server-Simple-Mason

summary: A simple mason server
Name: perl-HTTP-Server-Simple-Mason
Version: 0.09
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTTP-Server-Simple-Mason/

Source: http://www.cpan.org/modules/by-module/HTTP/HTTP-Server-Simple-Mason-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(HTML::Mason) >= 1.25
Buildrequires: perl(HTTP::Server::Simple) >= 0.04, perl(Hook::LexWrap)

%description
An abstract baseclass for a standalone mason server.

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
%doc Changes MANIFEST SIGNATURE
%doc %{_mandir}/man3/*.3*
%dir %{perl_vendorlib}/HTTP/
%dir %{perl_vendorlib}/HTTP/Server/
%dir %{perl_vendorlib}/HTTP/Server/Simple/
%{perl_vendorlib}/HTTP/Server/Simple/Mason.pm

%changelog
* Mon Jun 05 2005 Dag Wieers <dag@wieers.com> - 0.09-1
- Initial package. (using DAR)
