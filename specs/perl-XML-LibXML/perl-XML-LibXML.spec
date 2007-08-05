# $Id$
# Authority: dag
# Upstream: Petr Pajas <pajas$matfyz,cz>

### EL4 and EL5 ship with perl-XML-LibXML 1.58
# ExcludeDist: el4 el5

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-LibXML

Summary: Perl module that implements binding for libxml2
Name: perl-XML-LibXML
Version: 1.63
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-LibXML/

Source: http://www.cpan.org/modules/by-module/XML/XML-LibXML-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 2:5.8.0, libxml2-devel >= 2.4.20
BuildRequires: perl(XML::LibXML::Common), perl(XML::NamespaceSupport), perl(XML::SAX)

Requires: perl >= 2:5.8.0

%description
perl-XML-LibXML is a Perl module that implements binding for libxml2.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" \
	SKIP_SAX_INSTALL=1
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/XML/
%{perl_vendorarch}/XML/LibXML.pm
%{perl_vendorarch}/XML/LibXML.pod
%{perl_vendorarch}/XML/LibXML/
%dir %{perl_vendorarch}/auto/XML/
%{perl_vendorarch}/auto/XML/LibXML/

%changelog
* Wed Jun 20 2007 Dag Wieers <dag@wieers.com> - 1.63-1
- Updated to release 1.63.

* Sat Mar 05 2005 Dag Wieers <dag@wieers.com> - 1.58-1
- Changed to binary package, removed noarch.

* Wed Oct 20 2004 Dries Verachtert <dries@ulyssis.org> - 1.58-0
- Updated to release 1.58.

* Thu Nov 20 2003 Dag Wieers <dag@wieers.com> - 1.56-0
- Updated to release 1.56.

* Sun Aug 24 2003 Dag Wieers <dag@wieers.com> - 1.55-0
- Fixed site -> vendor. (Matthew Mastracci)
- Updated to release 1.55.

* Wed May 28 2003 Dag Wieers <dag@wieers.com> - 1.54-0
- Updated to release 1.54.
- Initial package. (using DAR)
