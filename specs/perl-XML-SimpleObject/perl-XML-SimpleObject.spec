# $Id$
# Authority: dries
# Upstream: Dan Brian <dbrian$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-SimpleObject

Summary: Simple object representation of a parsed XML::Parser tree
Name: perl-XML-SimpleObject
Version: 0.53
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-SimpleObject/

Source: http://search.cpan.org/CPAN/authors/id/D/DB/DBRIAN/XML-SimpleObject-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl-XML-Parser, perl-XML-LibXML

%description
This is a small and simple package that takes the output of an XML parser
and gives simple methods for accessing the structure of an XML document. It 
is very lightweight, but provides the simplest access to an XML document 
possible. It does not subclass XML::Parser or XML::LibXML; rather, it is meant 
to serve purely as an object struct for an outgoing tree.

%prep
%setup -n %{real_name}%{version}

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
%{perl_vendorlib}/XML/SimpleObject.pm
%{perl_vendorlib}/XML/SimpleObject
%{perl_vendorlib}/XML/ex.pl

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.53-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.53-1
- Initial package.
