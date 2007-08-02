# $Id$
# Authority: dries
# Upstream: Jose A. Rodriguez <Jose,Rodriguez+cpan$ac,upc,es>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name AsciiDB-TagFile

Summary: Tie class for a simple ASCII database
Name: perl-AsciiDB-TagFile
Version: 1.06
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/AsciiDB-TagFile/

Source: http://search.cpan.org/CPAN/authors/id/J/JO/JOSERODR/AsciiDB-TagFile-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
AsciiDB::Tag allows you to access a simple ASCII database using a
perl hash variable. The database format is straightforward so you can edit
it by hand if you need so. Each record is stored into a file, and a
record is just a set of values tagged by the field name.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/AsciiDB/TagFile.pm
%{perl_vendorlib}/AsciiDB/TagRecord.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.06-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.06-1
- Initial package.
