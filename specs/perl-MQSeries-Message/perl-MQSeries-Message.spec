# $Id$
# Authority: dag
# Upstream: Hildo Biersma <Hildo,Biersma$MorganStanley,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MQSeries-Message
%define real_version 1.25

Summary: Perl module named MQSeries-Message
Name: perl-MQSeries-Message
Version: 1.25
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MQSeries-Message/

Source: http://www.cpan.org/modules/by-module/MQSeries/MQSeries-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-MQSeries-Message is a Perl module.

%prep
%setup -n MQSeries-%{version}

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
%doc COPYRIGHT LICENSE MANIFEST README
%doc %{_mandir}/man3/MQSeries::Message.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/MQSeries/
%{perl_vendorarch}/MQSeries/Message.pm
%dir %{perl_vendorarch}/auto/MQSeries/
%{perl_vendorarch}/auto/MQSeries/Message/

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 1.25-1
- Initial package. (using DAR)
