# $Id$
# Authority: dries
# Upstream: Benjamin Trott <cpan$stupidfool,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Feed-Find

Summary: Class to perform autodiscovery of syndication feeds
Name: perl-Feed-Find
Version: 0.06
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Feed-Find/

Source: http://search.cpan.org/CPAN/authors/id/B/BT/BTROTT/Feed-Find-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl-Class-ErrorHandler
BuildRequires: perl-libwww-perl, perl-URI, perl-HTML-Parser, perl(ExtUtils::MakeMaker)

%description
A class to perform autodiscovery of syndication feeds.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Feed/Find.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.06-1.2
- Rebuild for Fedora Core 5.

* Thu Dec 22 2005 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Initial package.
