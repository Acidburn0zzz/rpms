# $Id$

# Authority: dag
# Upstream: <gossip-dev@lists.imendio.com>

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: Jabber instant messaging client.
Name: gossip
Version: 0.7.2
Release: 1
License: GPL
Group: Applications/Internet
URL: http://gossip.imendio.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://ftp.imendio.com/pub/imendio/gossip/src/gossip-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: gtk2-devel >= 2.0.4, libxslt-devel, libglade2-devel >= 2.0.0
BuildRequires: loudmouth

%description
Gossip is a Jabber instant messaging program.

%prep
%setup

%build
%configure \
	--enable-dbus="no"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall
%find_lang %{name}

%if %{dfi}
%else
	desktop-file-install --vendor gnome --delete-original \
		--add-category X-Red-Hat-Base                 \
		--dir %{buildroot}%{_datadir}/applications    \
		%{buildroot}%{_datadir}/applications/%{name}.desktop
%endif

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/gossip/
%{_datadir}/pixmaps/*.png

%changelog
* Mon Mar 15 2004 Dag Wieers <dag@wieers.com> - 0.7.2-1
- Updated to release 0.7.2.

* Wed Dec 17 2003 Dag Wieers <dag@wieers.com> - 0.6-0
- Initial package. (using DAR)
