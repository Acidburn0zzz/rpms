# $Id$
# Authority: matthias

Summary: Freshrpms.net release file and package configuration
Name: freshrpms-release
Version: 1
Release: 1
License: GPL
Group: System Environment/Base
Source0: GPL
Source1: RPM-GPG-KEY-freshrpms
Source2: freshrpms.repo
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

%description
Freshrpms.net release file. This package also contains yum configuration to
use the freshrpms.net provided rpm packages, as well as the public gpg key
used to sign them.


%prep


%build


%install
%{__rm} -rf %{buildroot}
# Install license and gpg key to be included in the docs
%{__cp} -a %{SOURCE0} %{SOURCE1} .
# Install yum repo file
%{__install} -D -m 0644 %{SOURCE2} \
    %{buildroot}%{_sysconfdir}/yum.repos.d/freshrpms.repo


%clean
%{__rm} -rf %{buildroot}


%post
# Import Freshrpms.net gpg key if needed
rpm -q gpg-pubkey-e42d547b-3960bdf1 >/dev/null 2>&1 || \
    rpm --import %{_defaultdocdir}/%{name}-%{version}/RPM-GPG-KEY-freshrpms
# We don't want a possible error to leave the previous package installed
exit 0


%files
%defattr(-, root, root, 0755)
%doc GPL RPM-GPG-KEY-freshrpms
%pubkey RPM-GPG-KEY-freshrpms
%config(noreplace) %{_sysconfdir}/yum.repos.d/freshrpms.repo


%changelog
* Wed Nov 10 2004 Matthias Saou <http://freshrpms.net/> 1-1
- Initial RPM release, inspired by fedora-release.
- No /etc/freshrpms-release (for now at least), as it's basically useless :-)

