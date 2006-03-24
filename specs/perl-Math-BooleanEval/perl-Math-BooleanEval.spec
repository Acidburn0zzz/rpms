# $Id$
# Authority: dries
# Upstream: Miko O'Sullivan <miko$idocs,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-BooleanEval

Summary: Boolean expression parser
Name: perl-Math-BooleanEval
Version: 1.00
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-BooleanEval/

Source: http://search.cpan.org/CPAN/authors/id/M/MI/MIKO/Math-BooleanEval-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
BooleanEval parses a boolean expression and creates an array of elements
in the expression. By setting each element to 1 or 0 you can evaluate
the expression.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" "PREFIX=%{buildroot}%{_prefix}"
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
%{perl_vendorlib}/Math/BooleanEval.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.00-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  2 2005 Dries Verachtert <dries@ulyssis.org> - 1.00-1
- Initial package.
