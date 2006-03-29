# $Id$
# Authority: dries
# Upstream: John D. Porter <johndporter$yahoo,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Lingua-Ispell

Summary: Encapsulates access to the Ispell program
Name: perl-Lingua-Ispell
Version: 0.07
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lingua-Ispell/

Source: http://search.cpan.org/CPAN/authors/id/J/JD/JDPORTER/Lingua-Ispell-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Lingua::Ispell::spellcheck() takes one argument.  It must be
a string, and it should contain only printable characters.
One allowable exception is a terminal newline, which will be
chomped off anyway.  The line is fed to a coprocess running
ispell for analysis.  ispell parses the line into "terms"
according to the language-specific rules in effect.

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
%{perl_vendorlib}/Lingua/Ispell.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.07-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Initial package.
