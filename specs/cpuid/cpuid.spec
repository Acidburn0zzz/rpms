# $Id$
# Authority: dag
# Upstream: Todd Allen <cpuid$etallen,com>

Summary: Provide processor CPUID information
Name: cpuid
%define real_version 20060730
Version: 0.0
Release: 20060730.1
License: BSD
Group: System Environment/Base
URL: http://www.etallen.com/cpuid.html

Source: http://www.etallen.com/cpuid/cpuid-%{real_version}.src.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
cpuid dumps detailed information about the CPU(s) gathered from the CPUID 
instruction, and also determines the exact model of CPU(s).

%prep
%setup -n %{name}-%{real_version}

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
### FIXME: Default install target makes setuid and root/root
#%{__make} install BUILDROOT="%{buildroot}"
%{__install} -D -m0755 cpuid %{buildroot}%{_sbindir}/cpuid
%{__install} -D -m0644 cpuid.man %{buildroot}%{_mandir}/man1/cpuid.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog FUTURE LICENSE
%doc %{_mandir}/man1/cpuid.1*
%{_sbindir}/cpuid

%changelog
* Mon Jul 31 2006 Dag Wieers <dag@wieers.com> - 0.0-20060730.1
- Initial package. (using DAR)
