# $Id$

# Authority: dries
# Upstream: Jonathan Stowe <jns$gellyfish,com>


%define real_name XML-XSLT
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Module for processing XSLT
Name: perl-XML-XSLT
Version: 0.48
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-XSLT/

Source: http://search.cpan.org/CPAN/authors/id/J/JS/JSTOWE/XML-XSLT-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This is a Perl module to parse XSL Transformational sheets. For a
description of the XSLT, see http://www.w3.org/TR/xslt. Currently, it
uses XML::Parser and XML::DOM, but an effort is being made to use
XML::XPath.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README ChangeLog
%{_bindir}/xslt-parser
%{_mandir}/man?/*
%{perl_vendorlib}/XML/XSLT.pm

%changelog
* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.48-1
- Initial package.
