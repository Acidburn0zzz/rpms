# $Id$

# Authority: dries
# Upstream: Richard Clamp <richardc$unixbeard,net>

%define real_name Net-DAAP-Client
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Cient for Apple iTunes DAAP service
Name: perl-Net-DAAP-Client
Version: 0.42
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-DAAP-Client/

Source: http://search.cpan.org/CPAN/authors/id/R/RC/RCLAMP/Net-DAAP-Client-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
dapple is a DAAP library for Perl.  DAAP is the protocol built
on top of HTTP that Apple's iTunes 4 uses to share music.  Most
responses to DAAP requests contain a binary DMAP structure.
This is an incomplete release.  There are missing features.
See the TODO file for future plans.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Net/DAAP/Client.pm
%{perl_vendorlib}/Net/DAAP/Client/*

%changelog
* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.42-1
- Updated to release 0.42.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.41-1
- Initial package.
