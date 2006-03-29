# $Id$
# Authority: dries
# Upstream: Alan Barclay <gorilla$elaine,drink,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Set-NestedGroups

Summary: Grouped data
Name: perl-Set-NestedGroups
Version: 0.01
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Set-NestedGroups/

Source: http://search.cpan.org/CPAN/authors/id/A/AB/ABARCLAY/Set-NestedGroups-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
Provides: perl(Set::NestedGroups::Member)

%description
Set::NestedGroups gives an implementation of nested groups, access
control lists (ACLs) would be one example of nested groups.
	
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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Set/NestedGroups.pm
%{perl_vendorlib}/Set/NestedGroups

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.01-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
