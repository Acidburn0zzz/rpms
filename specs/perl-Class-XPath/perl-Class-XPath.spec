# $Id$
# Authority: dries
# Upstream: Sam Tregar <sam$tregar,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-XPath

Summary: Adds xpath matching to object trees
Name: perl-Class-XPath
Version: 1.4
Release: 1.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-XPath/

Source: http://www.cpan.org/modules/by-module/Class/Class-XPath-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
This module adds XPath-style matching to your object trees. This means
that you can find nodes using an XPath-esque query with "match()" from
anywhere in the tree. Also, the "xpath()" method returns a unqique path
to a given node which can be used as an identifier.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Class/

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.4-1.2
- Rebuild for Fedora Core 5.

* Tue Dec 07 2004 Dries Verachtert <dries@ulyssis.org> - 1.4-1
- Initial package.
