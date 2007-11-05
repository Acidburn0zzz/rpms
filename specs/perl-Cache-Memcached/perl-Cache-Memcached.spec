# $Id$
# Authority: dag
# Upstream: Brad Fitzpatrick <brad$danga,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Cache-Memcached

Summary: Perl module implements a client library for memcached
Name: perl-Cache-Memcached
Version: 1.24
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Cache-Memcached/

Source: http://www.cpan.org/modules/by-module/Cache/Cache-Memcached-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Cache-Memcached is a Perl module implements a client library
for memcached.

This package contains the following Perl module:

    Cache::Memcached

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
%doc ChangeLog MANIFEST MANIFEST.SKIP META.yml README TODO
%doc %{_mandir}/man3/Cache::Memcached.3pm*
%dir %{perl_vendorlib}/Cache/
%{perl_vendorlib}/Cache/Memcached/
%{perl_vendorlib}/Cache/Memcached.pm

%changelog
* Wed Oct 10 2007 Dag Wieers <dag@wieers.com> - 1.24-1
- Initial package. (using DAR)
