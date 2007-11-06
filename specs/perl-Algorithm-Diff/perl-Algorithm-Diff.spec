# $Id$
# Authority: dries
# Upstream: Tye McQueen <tyemq$cpan,org>

%define real_name Algorithm-Diff
%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

Summary: Compute intelligent differences between two files or lists
Name: perl-Algorithm-Diff
Version: 1.1902
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Algorithm-Diff/

Source: http://search.cpan.org/CPAN/authors/id/T/TY/TYEMQ/Algorithm-Diff-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
This is a module for computing the difference between two files, two
strings, or any other two lists of things.  It uses an intelligent
algorithm similar to (or identical to) the one used by the Unix "diff"
program.  It is guaranteed to find the *smallest possible* set of
differences.

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
%{perl_vendorlib}/Algorithm/

%changelog
* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.1902-1
- Updated to release 1.1902.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.1901-1.2
- Rebuild for Fedora Core 5.

* Fri Jan  7 2005 Dries Verachtert <dries@ulyssis.org> - 1.1901-1
- Initial package.
