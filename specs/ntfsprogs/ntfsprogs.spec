# Authority: dag

%define vfs 1
%{?rh73:%undefine vfs}
%{?rhel21:%undefine vfs}
%{?rh62:%undefine vfs}

Summary: NTFS filesystem libraries and utilities.
Name: ntfsprogs
Version: 1.8.5
Release: 0
License: GPL
Group: System Environment/Base
URL: http://linux-ntfs.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/linux-ntfs/ntfsprogs-%{version}.tar.gz
Buildroot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%{?vfs:BuildRequires: glib2-devel, gnome-vfs2-devel}

%description
The Linux-NTFS project aims to bring full support for the NTFS filesystem
to the Linux operating system. Linux-NTFS currently consists of a static
library and utilities such as mkntfs, ntfscat, ntfsls, ntfsresize, and
ntfsundelete (for a full list of included utilities see man 8 ntfsprogs).

%package -n gnome-vfs2-ntfs
Summary: NTFS GNOME virtual filesystem module.
Group: System Environment/Base
Requires: %{name} = %{version}-%{release}

%description -n gnome-vfs2-ntfs
This package contains the NTFS GNOME virtual filesystem (VFS) module which
allows GNOME VFS clients to seamlessly utilize the NTFS library.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure \
%{?vfs:	--enable-gnome-vfs}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__mv} -f %{buildroot}%{_libdir}/gnome-vfs-2.0/modules/libntfs-gnomevfs.so.?.?.? \
		%{buildroot}%{_libdir}/gnome-vfs-2.0/modules/libntfs-gnomevfs.so

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la \
		%{buildroot}%{_libdir}/gnome-vfs-2.0/modules/*.{a,la,so.*}

%post
/sbin/ldconfig &>/dev/null

%postun
/sbin/ldconfig &>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING CREDITS ChangeLog NEWS README TODO*
%doc %{_mandir}/man8/mkntfs.8*
%doc %{_mandir}/man8/ntfs*.8*
%{_bindir}/*
%{_sbindir}/*
%{_libdir}/*.so.*

%if %{?vfs:1}%{!?vfs:0}
%files -n gnome-vfs2-ntfs
%defattr(-, root, root, 0755)
%doc %{_mandir}/man8/libntfs-gnomevfs.8*
%config %{_sysconfdir}/gnome-vfs-2.0/modules/libntfs.conf
%{_libdir}/gnome-vfs-2.0/modules/*.so
%endif

%files devel
%defattr(-, root, root, 0755)
%doc doc/CodingStyle doc/attribute_definitions doc/*.txt doc/tunable_settings doc/template.c doc/template.h
%{_includedir}/ntfs/
%{_libdir}/*.so
%{_libdir}/*.a

%changelog
* Mon Mar 01 2004 Dag Wieers <dag@wieers.com> - 1.8.5-0
- Updated to release 1.8.5.

* Fri Feb 13 2004 Dag Wieers <dag@wieers.com> - 1.8.4-0
- Initial package. (using DAR)
