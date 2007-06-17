# $Id$
# Authority: dries
# Upstream: Lee Goddard <REMOVETHISlgoddard$cpan,orgREMOVETHIS>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Language-DATR-DATR2XML

Summary: Manipulate DATR .dtr, XML, HTML, XML
Name: perl-Language-DATR-DATR2XML
Version: 0.901
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Language-DATR-DATR2XML/

Source: http://search.cpan.org/CPAN/authors/id/L/LG/LGODDARD/Language-DATR-DATR2XML-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Manipulate DATR .dtr, XML, HTML, XML.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README.txt
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Language/DATR/DATR2XML.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.901-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.901-1
- Initial package.
