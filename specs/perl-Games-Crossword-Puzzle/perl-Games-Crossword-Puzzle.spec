# $Id$
# Authority: dries
# Upstream: Ricardo SIGNES <rjbs$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Games-Crossword-Puzzle

Summary: Module for crossword puzzles
Name: perl-Games-Crossword-Puzzle
Version: 0.001
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Games-Crossword-Puzzle/

Source: http://search.cpan.org//CPAN/authors/id/R/RJ/RJBS/Games-Crossword-Puzzle-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Module for crossword puzzles.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Games::Crossword::Puzzle*
%{perl_vendorlib}/Games/Crossword/Puzzle.pm
%{perl_vendorlib}/Games/Crossword/Puzzle/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.001-1
- Initial package.
