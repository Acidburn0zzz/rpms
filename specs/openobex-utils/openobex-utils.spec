# $Id$

# Authority: dag

%define real_name openobex-apps

Summary: Utilities based on Openobex
Name: openobex-utils
Version: 1.0.0
Release: 0
License: LGPL
Group: System Environment/Base
URL: http://openobex.sourceforge.net/

Source0: http://dl.sf.net/openobex/openobex-apps-%{version}.tar.gz
Source1: http://www.frasunek.com/sources/unix/obexserver.c
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: openobex-devel
Obsoletes: openobex-apps <= %{release}
Provides: openobex-apps

%description
Utilities based on Openobex.

%prep
%setup -n %{real_name}-%{version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Ugly (smart?) hack to have obexserver when bluetooth is compiled in openobex.
cd src
${CC:-%{__cc}} %{optflags} -o obexserver %{SOURCE1} libmisc.a $(openobex-config --libs) && \
%{__install} -Dp -m0755 obexserver %{buildroot}%{_bindir}/obexserver || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/*

%changelog
* Wed Feb 04 2004 Dag Wieers <dag@wieers.com> - 1.0.0-0
- Initial package. (using DAR)
