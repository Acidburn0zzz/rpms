# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Container

Summary: Glues object frameworks together transparently
Name: perl-Class-Container
Version: 0.12
Release: 1
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Container/

Source: http://www.cpan.org/modules/by-module/Class/Class-Container-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl-Params-Validate

%description
This class facilitates building frameworks of several classes that
inter-operate. It was first designed and built for "HTML::Mason", in
which the Compiler, Lexer, Interpreter, Resolver, Component, Buffer, and
several other objects must create each other transparently, passing the
appropriate parameters to the right class, possibly substituting other
subclasses for any of these objects.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean 
%{__rm} -rf %{buildroot}

%files 
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Class/
%{perl_vendorlib}/Class/Container.pm

%changelog
* Tue Mar 29 2005 Dag Wieers <dag@wieers.com> - 0.12-1
- Initial package contributed by Rudolf Kastle.
