# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-SNMP

Summary: Net-SNMP Perl module
Name: perl-Net-SNMP
Version: 5.2.0
Release: 1
License: distributable
Group: Development/Libraries
URL: http://search.cpan.org/dist/Net-SNMP/

Source: http://www.cpan.org/modules/by-module/Net/Net-SNMP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.6, perl(Digest::HMAC), perl(Crypt::DES)
Requires: perl >= 0:5.6

%description
The Net::SNMP module implements an object oriented interface to the
Simple Network Management Protocol.

%prep
%setup -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/snmpkey.1*
%doc %{_mandir}/man3/*
%{_bindir}/snmpkey
%dir %{perl_vendorlib}/Net/
%{perl_vendorlib}/Net/SNMP/
%{perl_vendorlib}/Net/SNMP.pm

%changelog
* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 5.2.0-1
- Updated to release 5.2.0.

* Tue Mar 29 2005 Dag Wieers <dag@wieers.com> - 5.0.1-1
- Updated to release 5.0.1.

* Fri Mar 12 2004 Dag Wieers <dag@wieers.com> - 4.1.2-1
- Added perl-Crypt-DES BuildRequires. (Russ Herrold)

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 4.1.0-0
- Updated to release 4.1.0.

* Mon Feb 17 2003 Dag Wieers <dag@wieers.com> - 4.0.3-0
- Initial package. (using DAR)
