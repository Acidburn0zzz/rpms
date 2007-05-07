# $Id$
# Authority: dag
# Upstream: Derrik Pates <dpates$dsdk12,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IPTables-IPv4

Summary: Perl module for manipulating iptables rules for the IPv4 protocol
Name: perl-IPTables-IPv4
Version: 0.98
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IPTables-IPv4/

Source: http://www.cpan.org/modules/by-module/IPTables/IPTables-IPv4-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-IPTables-IPv4 is a Perl module for manipulating iptables rules
for the IPv4 protocol.

%prep
%setup -n %{real_name}-%{version}

%build
#%{expand: %%define optflags %{optflags} -fPIC}
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
%doc COPYING Changes MANIFEST README Todo
%doc %{_mandir}/man3/IPTables::IPv4.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/IPTables/
%{perl_vendorarch}/IPTables/IPv4.pm
%dir %{perl_vendorarch}/auto/IPTables/
%{perl_vendorarch}/auto/IPTables/IPv4/

%changelog
* Sat May 05 2007 Dag Wieers <dag@wieers.com> - 0.98-1
- Initial package. (using DAR)
