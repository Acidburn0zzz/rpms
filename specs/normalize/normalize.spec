# $Id$
# Authority: dag

Summary: Audio file volume normalizer
Name: normalize
Version: 0.7.7
Release: 1
License: GPL
Group: Application/Multimedia
URL: http://www.cs.columbia.edu/~cvaill/normalize/

Source: http://savannah.nongnu.org/download/normalize/normalize-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib-devel, gtk2-devel, libmad-devel,
BuildRequires: xorg-x11-devel, xmms-devel, audiofile-devel

%description
Normalize is a tool for adjusting the volume of audio files to a
standard level. This is useful for things like creating mix CDs and MP3
collections, where different recording levels on different albums can
cause the volume to vary greatly from song to song.

%package -n xmms-plugins-normalize
Summary: xmms normalize plugin
Group: Application/Multimedia
Requires: xmms

%description -n xmms-plugins-normalize
A normalize plugin for the XMMS media player

%prep
%setup

%build
export CFLAGS="%{optflags}"
%configure --with-mad
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc COPYING NEWS README THANKS TODO doc/frontend.txt doc/normalize.1.sgml
%doc %{_mandir}/man1/normalize.1*
%doc %{_mandir}/man1/normalize-mp3.1*
%{_bindir}/normalize
%{_bindir}/normalize-mp3
%{_bindir}/normalize-ogg

%files -n xmms-plugins-normalize
%defattr(-, root, root, 0755)
%dir %{_libdir}/xmms/
%dir %{_libdir}/xmms/Effect/
%exclude %{_libdir}/xmms/Effect/librva.la 
%{_libdir}/xmms/Effect/librva.so

%changelog
* Thu Aug 17 2006 Dag Wieers <dag@wieers.com> - 0.7.7-1
- Initial package. (using DAR)
