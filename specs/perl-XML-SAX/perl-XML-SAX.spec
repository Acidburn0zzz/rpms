# $Id$

# Authority: dag

%define rname XML-SAX

Summary: XML-SAX Perl module.
Name: perl-XML-SAX
Version: 0.12
Release: 3
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-SAX/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://search.cpan.org/CPAN/authors/id/M/MS/MSERGEANT/%{rname}-%{version}.tar.gz
Source1: ParserDetails.ini
Patch0: perl-XML-SAX-parsers.patch
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildArch: noarch
BuildRequires: perl
Requires: perl(XML::NamespaceSupport)
Obsoletes: perl-XML-SAX-PurePerl <= 0.80, perl-XML-SAX-Base <= 1.04

Provides: perl(XML::SAX::PurePerl::DocType), perl(XML::SAX::PurePerl::DTDDecls)
Provides: perl(XML::SAX::PurePerl::EncodingDetect), perl(XML::SAX::PurePerl::NoUnicodeExt)
Provides: perl(XML::SAX::PurePerl::UnicodeExt), perl(XML::SAX::PurePerl::XMLDecl)

%description
XML-SAX Perl module.

%prep
%setup -n %{rname}-%{version}
%patch

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/perl5/*/*/perllocal.pod

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST README
%doc %{_mandir}/man?/*
%{_libdir}/perl5/

%changelog
* Mon Aug 25 2003 Dag Wieers <dag@wieers.com> - 0.12-3
- Added missing provides. (Ville Skytt�)
- Obsoletes perl-XML-SAX-PurePerl and perl-XML-SAX-Base.

* Sun Aug 24 2003 Dag Wieers <dag@wieers.com> - 0.12-1
- Fixed site -> vendor. (Matthew Mastracci)

* Wed May 28 2003 Dag Wieers <dag@wieers.com> - 0.12-0
- Initial package. (using DAR) 
