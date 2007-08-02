# $Id$
# Authority: dries
# Upstream: William Ross <wross$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-TagFilter

Summary: Fine-grained html-filter, xss-blocker and mailto-obfuscator
Name: perl-HTML-TagFilter
Version: 1.03
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-TagFilter/

Source: http://search.cpan.org/CPAN/authors/id/W/WR/WROSS/HTML-TagFilter-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
HTML::TagFilter is a subclass of HTML::Parser with a
single purpose: it will remove unwanted html tags and attributes from a
piece of text. It can act in a more or less fine-grained way - you can
specify permitted tags, permitted attributes of each tag, and permitted
values for each attribute in as much detail as you like.

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
%{perl_vendorlib}/HTML/TagFilter.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.03-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 1.03-1
- Updated to release 1.03.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Updated to release 1.01.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.091-1
- Initial package.
