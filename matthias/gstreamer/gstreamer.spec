Name: 		gstreamer
Version: 	0.6.5
Release: 	0.fdr.1
Summary: 	GStreamer streaming media framework runtime.

Group: 		System Environment/Libraries
License: 	LGPL
URL:		http://gstreamer.net/
Source: 	http://freedesktop.org/~gstreamer/src/gstreamer/gstreamer-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%define		majorminor	0.6
%define 	_glib2		2.0.1
%define 	_libxml2	2.4.0

Requires: 	glib2 >= %_glib2
Requires: 	libxml2 >= %_libxml2
Requires:	popt > 1.6

BuildRequires: 	glib2-devel >= %_glib2
BuildRequires: 	libxml2-devel >= %_libxml2
BuildRequires: 	bison
BuildRequires: 	flex
BuildRequires: 	m4
BuildRequires: 	gtk-doc >= 1.1
BuildRequires: 	gcc
BuildRequires: 	zlib-devel
BuildRequires:  popt > 1.6
Prereq:		/sbin/ldconfig

### documentation requirements
BuildRequires:  python2
BuildRequires:  openjade
BuildRequires:  jadetex
BuildRequires: 	libxslt
BuildRequires:  docbook-style-dsssl
BuildRequires:  docbook-style-xsl
BuildRequires:  docbook-utils
BuildRequires:	transfig
BuildRequires:	xfig
BuildRequires:	netpbm-progs
BuildRequires:	ghostscript

# sigh, libtool
BuildRequires:	gcc-c++

%description
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new 
plugins.

%package devel
Summary: 	Libraries/include files for GStreamer streaming media framework.
Group: 		Development/Libraries

Requires: 	%{name} = %{version}-%{release}
Requires: 	glib2-devel >= %_glib2
Requires: 	libxml2-devel >= %_libxml2

%description devel
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new   
plugins.

This package contains the libraries and includes files necessary to develop
applications and plugins for GStreamer.

%package -n gstreamer-tools
Summary: 	tools for GStreamer streaming media framework.
Group: 		Applications/Multimedia

%description -n gstreamer-tools
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new   
plugins.

This package contains the basic command-line tools used for GStreamer, like
gst-register and gst-launch.  It is split off to allow parallel-installability
in the future.

%prep
%setup -q -n gstreamer-%{version}

%build
%configure \
  --enable-debug \
  --with-cachedir=%{_localstatedir}/cache/gstreamer-%{majorminor} \
  --disable-tests --disable-examples
                                                                                
make %{?_smp_mflags}
                                                                                
%install
rm -rf $RPM_BUILD_ROOT

# build documentation to a different location so it doesn't end up in
# a gstreamer-devel-(version) dir and doesn't get deleted by %doc scripts
%makeinstall docdir=$RPM_BUILD_ROOT%{_datadir}/gstreamer-%{majorminor}/doc

# Clean out files that should not be part of the rpm.
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/cache/gstreamer-%{majorminor}
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
# Create empty cache directory
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/cache/gstreamer-%{major}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%{_bindir}/gst-register-%{majorminor} > /dev/null 2> /dev/null
                                                                                
%postun
/sbin/ldconfig

%files
%defattr(-, root, root, -)
%doc AUTHORS COPYING README TODO COPYING.LIB REQUIREMENTS DOCBUILDING
%{_libdir}/libgstreamer-%{majorminor}.so.*
%{_libdir}/libgstcontrol-%{majorminor}.so.*
%dir %{_libdir}/gstreamer-%{majorminor}
%{_libdir}/gstreamer-%{majorminor}/libgstautoplugcache.so
%{_libdir}/gstreamer-%{majorminor}/libgstautoplugger.so
%{_libdir}/gstreamer-%{majorminor}/libgstbasicomega*.so
%{_libdir}/gstreamer-%{majorminor}/libgstbasicwingo*.so
%{_libdir}/gstreamer-%{majorminor}/libgstoptscheduler.so
%{_libdir}/gstreamer-%{majorminor}/libgstoptomega*.so
%{_libdir}/gstreamer-%{majorminor}/libgstoptwingo*.so
%{_libdir}/gstreamer-%{majorminor}/libgstbasicgthreadscheduler*.so
%{_libdir}/gstreamer-%{majorminor}/libgstoptgthreadscheduler*.so
%{_libdir}/gstreamer-%{majorminor}/libgstelements*.so
%{_libdir}/gstreamer-%{majorminor}/libgstgetbits*.so
%{_libdir}/gstreamer-%{majorminor}/libgstputbits*.so
%{_libdir}/gstreamer-%{majorminor}/libgstspider*.so
%{_libdir}/gstreamer-%{majorminor}/libgststaticautoplug*.so
%{_libdir}/gstreamer-%{majorminor}/libgsttypes.so
%{_libdir}/gstreamer-%{majorminor}/libgstindexers.so
%{_libdir}/gstreamer-%{majorminor}/libgstbytestream.so
%{_bindir}/gst-xmlinspect-%{majorminor}
%{_bindir}/gst-complete-%{majorminor}
%{_bindir}/gst-compprep-%{majorminor}
%{_bindir}/gst-feedback-%{majorminor}
%{_bindir}/gst-inspect-%{majorminor}
%{_bindir}/gst-launch-%{majorminor}
%{_bindir}/gst-md5sum-%{majorminor}
%{_bindir}/gst-register-%{majorminor}
%{_bindir}/gst-xmllaunch-%{majorminor}
%{_bindir}/gst-typefind-%{majorminor}
%{_mandir}/man1/gst-xmllaunch-%{majorminor}.*
%{_mandir}/man1/gst-complete-%{majorminor}.*
%{_mandir}/man1/gst-compprep-%{majorminor}.*
%{_mandir}/man1/gst-feedback-%{majorminor}.*
%{_mandir}/man1/gst-inspect-%{majorminor}.*
%{_mandir}/man1/gst-launch-%{majorminor}.*
%{_mandir}/man1/gst-md5sum-%{majorminor}.*
%{_mandir}/man1/gst-register-%{majorminor}.*
%{_mandir}/man1/gst-typefind-%{majorminor}.*
%dir %{_localstatedir}/cache/gstreamer-%{majorminor}

%files -n gstreamer-tools
%defattr(-, root, root, -)
%{_bindir}/gst-complete
%{_bindir}/gst-compprep
%{_bindir}/gst-feedback
%{_bindir}/gst-inspect
%{_bindir}/gst-launch
%{_bindir}/gst-md5sum
%{_bindir}/gst-register
%{_bindir}/gst-typefind
%{_bindir}/gst-xmlinspect
%{_bindir}/gst-xmllaunch
                                                                                
%files devel
%defattr(-, root, root, -)
%dir %{_includedir}/gstreamer-%{majorminor}
%dir %{_includedir}/gstreamer-%{majorminor}/gst
%{_includedir}/gstreamer-%{majorminor}/gst/*.h
%dir %{_includedir}/gstreamer-%{majorminor}/gst/control
%{_includedir}/gstreamer-%{majorminor}/gst/control/*.h
%dir %{_includedir}/gstreamer-%{majorminor}/gst/getbits
%{_includedir}/gstreamer-%{majorminor}/gst/getbits/getbits.h
%dir %{_includedir}/gstreamer-%{majorminor}/gst/putbits
%{_includedir}/gstreamer-%{majorminor}/gst/putbits/putbits.h
%{_includedir}/gstreamer-%{majorminor}/gst/bytestream/bytestream.h
%{_libdir}/libgstreamer-%{majorminor}.so
%{_libdir}/libgstcontrol-%{majorminor}.so
%{_datadir}/aclocal/gst-element-check-%{majorminor}.m4
%{_libdir}/pkgconfig/gstreamer-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-control-%{majorminor}.pc
                                                                                
%{_datadir}/gstreamer-%{majorminor}/doc
%{_datadir}/gtk-doc/html/gstreamer-%{majorminor}/*
%{_datadir}/gtk-doc/html/gstreamer-libs-%{majorminor}/*


%changelog
* Thu Feb 12 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- updated spec file for 0.6.5 release

* Fri Oct 10 2003 Thomas Vander Stichele <thomas at apestaart dot org>
- added dependencies for docs build

* Tue Jun 10 2003 Thomas Vander Stichele <thomas at apestaart dot org>
- added gst-typefind

* Mon May 19 2003 Thomas Vander Stichele <thomas at apestaart dot org>
- defattr fixes

* Sun May 18 2003 Thomas Vander Stichele <thomas at apestaart dot org>
- adding ghostscript and libxlst BuildRequires: for xsltproc and fig2dev/gs

* Sun May 18 2003 Thomas Vander Stichele <thomas at apestaart dot org>
- reworked devhelp generation and changed spec to match

* Tue Jan 28 2003 Thomas Vander Stichele <thomas at apestaart dot org>
- added gstreamer-control.pc file

* Sat Dec 07 2002 Thomas Vander Stichele <thomas at apestaart dot org>
- define majorminor and use it everywhere
- full parallel installability

* Tue Nov 05 2002 Christian Schaller <Uraeus@linuxrising.org>
- Add optwingo scheduler

* Sat Oct 12 2002 Christian Schaller <Uraeus@linuxrising.org>
- Updated to work better with default RH8 rpm
- Added missing unspeced files
- Removed .a and .la files from buildroot

* Sat Sep 21 2002 Thomas Vander Stichele <thomas@apestaart.org>
- added gst-md5sum

* Tue Sep 17 2002 Thomas Vander Stichele <thomas@apestaart.org>
- adding flex to buildrequires

* Fri Sep 13 2002 Christian F.K. Schaller <Uraeus@linuxrising.org>
- Fixed the schedulers after the renaming
* Sun Sep 08 2002 Thomas Vander Stichele <thomas@apestaart.org>
- added transfig to the BuildRequires:

* Sat Jun 22 2002 Thomas Vander Stichele <thomas@apestaart.org>
- moved header location

* Mon Jun 17 2002 Thomas Vander Stichele <thomas@apestaart.org>
- added popt
- removed .la

* Fri Jun 07 2002 Thomas Vander Stichele <thomas@apestaart.org>
- added release of gstreamer to req of gstreamer-devel
- changed location of API docs to be in gtk-doc like other gtk-doc stuff
- reordered SPEC file

* Mon Apr 29 2002 Thomas Vander Stichele <thomas@apestaart.org>
- moved html docs to gtk-doc standard directory

* Tue Mar 5 2002 Thomas Vander Stichele <thomas@apestaart.org>
- move version defines of glib2 and libxml2 to configure.ac
- add BuildRequires for these two libs

* Sun Mar 3 2002 Thomas Vander Stichele <thomas@apestaart.org>
- put html docs in canonical place, avoiding %doc erasure
- added devhelp support, current install of it is hackish

* Sat Mar 2 2002 Christian Schaller <Uraeus@linuxrising.org>
- Added documentation to build

* Mon Feb 11 2002 Thomas Vander Stichele <thomas@apestaart.org>
- added libgstbasicscheduler
- renamed libgst to libgstreamer

* Fri Jan 04 2002 Christian Schaller <Uraeus@linuxrising.org>
- Added configdir parameter as it seems the configdir gets weird otherwise

* Thu Jan 03 2002 Thomas Vander Stichele <thomas@apestaart.org>
- split off gstreamer-editor from core
- removed gstreamer-gnome-apps

* Sat Dec 29 2001 Rodney Dawes <dobey@free.fr>
- Cleaned up the spec file for the gstreamer core/plug-ins split
- Improve spec file

* Sat Dec 15 2001 Christian Schaller <Uraeus@linuxrising.org>
- Split of more plugins from the core and put them into their own modules
- Includes colorspace, xfree and wav
- Improved package Require lines
- Added mp3encode (lame based) to the SPEC

* Wed Dec 12 2001 Christian Schaller <Uraeus@linuxrising.org>
- Thomas merged mpeg plugins into one
* Sat Dec 08 2001 Christian Schaller <Uraeus@linuxrising.org>
- More minor cleanups including some fixed descriptions from Andrew Mitchell

* Fri Dec 07 2001 Christian Schaller <Uraeus@linuxrising.org>
- Added logging to the make statement

* Wed Dec 05 2001 Christian Schaller <Uraeus@linuxrising.org>
- Updated in preparation for 0.3.0 release

* Fri Jun 29 2001 Christian Schaller <Uraeus@linuxrising.org>
- Updated for 0.2.1 release
- Split out the GUI packages into their own RPM
- added new plugins (FLAC, festival, quicktime etc.)

* Sat Jun 09 2001 Christian Schaller <Uraeus@linuxrising.org>
- Visualisation plugins bundled out togheter
- Moved files sections up close to their respective descriptions

* Sat Jun 02 2001 Christian Schaller <Uraeus@linuxrising.org>
- Split the package into separate RPMS, 
  putting most plugins out by themselves.

* Fri Jun 01 2001 Christian Schaller <Uraeus@linuxrising.org>
- Updated with change suggestions from Dennis Bjorklund

* Tue Jan 09 2001 Erik Walthinsen <omega@cse.ogi.edu>
- updated to build -devel package as well

* Sun Jan 30 2000 Erik Walthinsen <omega@cse.ogi.edu>
- first draft of spec file

