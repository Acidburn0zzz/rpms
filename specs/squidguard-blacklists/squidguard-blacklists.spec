# Authority: dag

%define dbhomedir %{_localstatedir}/lib/squidguard

Summary: Regularly updated blacklists for use with squidguard.
Name: squidguard-blacklists
Version: 20030922
Release: 0
License: GPL
Group: System Environment/Libraries
URL: http://dag.wieers.com/home-made/squidguard/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.teledanmark.no/pub/www/proxy/squidGuard/contrib/blacklists-%{version}.tar.gz
Source1: ftp://ftp.univ-tlse1.fr/pub/reseau/cache/squidguard_contrib/blacklists.tar.gz
Source2: http://www.ingrid.org/~harada/filtering/dmozlists/dmozlists-ages-adult-20020930.tar.gz
Source3: http://www.bn-paf.de/filter/de-blacklists.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: squidguard = 1.2.0
Requires: squidguard = 1.2.0

%description
Regularly updated blacklists for use with squidguard.

%prep
%{__rm} -rf %{_builddir}/%{name}-%{version}/
%setup -n %{name}-%{version}/squidguard -T -D -c -b0
%setup -n %{name}-%{version}/univtlse -T -D -c -b1
%setup -n %{name}-%{version}/dmoz -T -D -c -b2
%setup -n %{name}-%{version}/debnpaf -T -D -c -b3

cd %{_builddir}/%{name}-%{version}/

### Clean up squidguard blacklists
%{__mv} -f squidguard/blacklists/* squidguard/
%{__rm} -f squidguard/*/*.diff
%{__rm} -rf squidguard/blacklists/

### Clean up univtlse blacklists
%{__mv} -f univtlse/blacklists/* univtlse/
%{__rm} -f univtlse/ads univtlse/porn univtlse/proxy
%{__rm} -rf univtlse/blacklists/

### Clean up dmoz blacklists
%{__mv} -f dmoz/dmozlists/* dmoz/
%{__rm} -rf dmoz/dmozlists/

### Clean up debnpaf blacklists
%{__mv} -f debnpaf/de-blacklists/* debnpaf/
%{__rm} -rf debnpaf/de-blacklists/ debnpaf/*/.mappedfiles/ debnpaf/*/*.exclude

### Clean up empty blacklists and remove symlinks
find . -size 0 -exec %{__rm} -f {} \;
find . -type l -exec %{__rm} -f {} \;

%build

%install
%{__rm} -rf %{buildroot}

%{__install} -d -m0755 %{buildroot}%{dbhomedir}/ \
			%{buildroot}%{_sysconfdir}/squid/local/{bad,good}/ \
			%{buildroot}%{_sysconfdir}/logrotate.d/ \
			%{buildroot}%{_localstatedir}/log/squidguard/

### Copy all the blacklists over to the buildroot
%{__cp} -af  %{_builddir}/%{name}-%{version}/* %{buildroot}%{dbhomedir}/

### Create logrotate file
%{__cat} <<EOF >%{buildroot}%{_sysconfdir}/logrotate.d/squidguard-blacklists
%{_localstatedir}/log/squidguard/*.log {
	missingok
	copytruncate
	notifempty
}
EOF

### Creating default squidguard configfile and
### temporary configfile for generating databases
cd %{buildroot}%{dbhomedir}/
(
	echo -e "### This config-file is part of the squidguard-blacklists RPM package."
	echo -e "### More information about this package at:\n###\thttp://dag.wieers.com/home-made/squidguard/\n\n"
	echo -e "### Path configuration\ndbhome %{dbhomedir}\nlogdir %{_localstatedir}/log/squidguard\n\n"
	echo -e "### Generated blacklist definitions"
	for name in ads:publicite adult:porn aggressive:agressif audio-video drugs:drogue forums gambling hacking mail proxy:redirector violence warez; do
		echo -e "### Group '${name//:*}' containing entries for '$(echo $name | tr ':' ',')'\ndest ${name//:*} {\n\tlogfile ${name//:*}.log\n"
		echo -e "dest ${name//:*} {\n\tlogfile ${name//:*}.log\n" >&3
		for list in $(echo $name | tr ':' ' '); do
			find */$list/ -type f -name "domains" -size +0 -exec echo -e "\tdomainlist\t" {} \;
			find */$list/ -type f -name "urls" -size +0 -exec echo -e "\turllist\t\t" {} \;
			find */$list/ -type f -name "expressions" -size +0 -exec echo -e "\texpressionlist\t" {} \;
			find %{buildroot}%{dbhomedir}/*/$list/ -type f -name "domains" -size +0 -exec echo -e "\tdomainlist\t" {} >&3 \;
			find %{buildroot}%{dbhomedir}/*/$list/ -type f -name "urls" -size +0 -exec echo -e "\turllist\t\t" {} >&3 \;
		done
		echo -e "}\n"
		echo -e "}\n" >&3
	done
	echo -e "### Define your local blacklists here"
	echo -e "dest bad {\n\tlogfile localbad.log\n\n#\tdomainlist\tlocal/bad/domains\n#\turllist\t\tlocal/bad/urls\n#\texpressionlist\tlocal/bad/expressions\n}\n"
	echo -e "dest good {\n#\tdomainlist\tlocal/good/domains\n#\turllist\t\tlocal/good/urls\n#\texpressionlist\tlocal/good/expressions\n}\n\n"
	echo -e "### ACL definition\nacl {\n\tdefault {\n\t\tpass good !bad !adult !aggressive !audio-video !hacking !warez any\n#\t\tredirect 302:http://localhost/access-denied.html\n\t}\n}"
	echo -e "acl {\n\tdefault {\n\t\tpass any\n\t}\n}" >&3
) >%{buildroot}%{_sysconfdir}/squid/squidguard-blacklists.conf 3>temp.conf

### FIXME: If files are created that used to be directories, upgrading fails ;/
### Create 'local' demo files
#touch %{buildroot}%{_sysconfdir}/squid/local/{bad,good}/{expressions,domains,urls}
%{__ln_s} -f %{_sysconfdir}/squid/local/ %{buildroot}%{dbhomedir}/
echo -e "users.pandora.be\nerrors.pandora.be\nusers.pandora.be" >>%{buildroot}%{_sysconfdir}/squid/local/good/domains
echo '\.(ra?m|wma|mp2|mpv2|mp3|asx)($|\?)' >>%{buildroot}%{_sysconfdir}/squid/local/bad/expressions
echo '\.(mpe?g?|wmv|mov|movie|qt|avi|dvd?|divx)($|\?)' >>%{buildroot}%{_sysconfdir}/squid/local/bad/expressions

### Generating databases
squidGuard -d -c temp.conf -C all
%{__rm} -f temp.conf

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, squid, squid, 0755)
%config %{_sysconfdir}/squid/squidguard-blacklists.conf
%config %{_sysconfdir}/logrotate.d/*
%defattr(600, squid, squid, 0700)
#%config(noreplace) %{_sysconfdir}/squid/local/
%config(noreplace) %{_sysconfdir}/squid/local/
%{dbhomedir}/
%{_localstatedir}/log/squidguard/

%changelog
* Mon Sep 22 2003 Dag Wieers <dag@wieers.com> - 20030922-0
- Updated to release 20030922.

* Mon Aug 04 2003 Dag Wieers <dag@wieers.com> - 20030804-1
- Updated to release 20030804.
- Added local black and whitelist for overriding.
- Disabled local black and white lists by default.
- FIXME: still problem when installing files that used to be directories !

* Wed Mar 26 2003 Dag Wieers <dag@wieers.com> - 20030317-1
- Updated to release 20030317.
- Added debnpaf blacklists.

* Thu Jan 30 2003 Dag Wieers <dag@wieers.com> - 20030127-1
- Creating prebuilt databases automatically.

* Mon Jan 27 2003 Dag Wieers <dag@wieers.com> - 20030127-0
- Added dmozlists and univ-tlse blacklists.
- Updated to release 20030127.

* Thu Jan 09 2003 Dag Wieers <dag@wieers.com> - 20030105-0
- Initial package. (using DAR)
