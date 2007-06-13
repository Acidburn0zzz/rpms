# $Id$
# Authority: dries
# Upstream: Lyo Kato <lyo,kato$gmail,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Plugin-Charsets-Japanese

Summary: Japanese specific charsets handler
Name: perl-Catalyst-Plugin-Charsets-Japanese
Version: 0.06
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Plugin-Charsets-Japanese/

Source: http://search.cpan.org//CPAN/authors/id/L/LY/LYOKATO/Catalyst-Plugin-Charsets-Japanese-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Japanese specific charsets handler.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Catalyst::Plugin::Charsets::Japanese*
%{perl_vendorlib}/Catalyst/Plugin/Charsets/Japanese.pm
%{perl_vendorlib}/Catalyst/Plugin/Charsets/Japanese/
%exclude %{perl_vendorlib}/Catalyst/Plugin/Charsets/.Japanese.pm.swp

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Initial package.
