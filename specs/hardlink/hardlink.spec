# $Id$
# Authority: dag

Summary: Tool to hardlink duplicate files in a directory tree
Name: hardlink
Version: 1.2
Release: 1
License: GPL
Group: Applications/System
URL: ftp://ftp.redhat.com/pub/redhat/mirror-tools/

Source: ftp://ftp.redhat.com/pub/redhat/mirror-tools/hardlink.c
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
A utility to hardlink duplicate files in a directory tree.

%prep
%setup -c -T
%{__cp} -afp %{SOURCE0} .

%build
${CC:-%{__cc}} %{optflags} -o hardlink hardlink.c

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 hardlink %{buildroot}%{_bindir}/hardlink

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/hardlink

%changelog
* Tue Apr 29 2003 Dag Wieers <dag@wieers.com> - 1.2-1
- Build happens in its own buildsubdir.

* Sun Apr 20 2003 Dag Wieers <dag@wieers.com> - 1.2-0
- Initial build. (using DAR)
