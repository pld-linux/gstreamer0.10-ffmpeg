#
# TODO
# Use shared ffmpeg lib instead of builtin - anyone wants to do it?
#
%define gstname gst-ffmpeg
%define gst_major_ver   0.10

Summary:	GStreamer Streaming-media framework plug-in using FFmpeg
Summary(pl.UTF-8):	Wtyczka do środowiska obróbki strumieni GStreamer używająca FFmpeg
Name:		gstreamer-ffmpeg
Version:	0.10.3
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://gstreamer.freedesktop.org/src/gst-ffmpeg/%{gstname}-%{version}.tar.bz2
# Source0-md5:	c07fd2da0835989fc4eae291cbc05f09
Patch0:		%{name}-nocpp.patch
URL:		http://gstreamer.net/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.4
BuildRequires:	liboil-devel >= 0.3.6
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	gstreamer-plugins-base >= 0.10.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags_ppc	-maltivec

%description
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related. Its plugin-based architecture means
that new data types or processing capabilities can be added simply by
installing new plug-ins.

This plugin contains the FFmpeg codecs, containing codecs for most
popular multimedia formats.

%description -l pl.UTF-8
GStreamer to środowisko obróbki danych strumieniowych, bazujące na
grafie filtrów operujących na danych medialnych. Aplikacje używające
tej biblioteki mogą robić wszystko od przetwarzania dźwięku w czasie
rzeczywistym, do odtwarzania filmów i czegokolwiek innego związanego z
mediami. Architektura bazująca na wtyczkach pozwala na łatwe dodawanie
nowych typów danych lub możliwości obróbki.

Wtyczka ta zawiera kodeki FFmpeg, potrafiące zdekodować
najpopularniejsze formaty multimedialne.

%prep
%setup -q -n %{gstname}-%{version}
%patch0 -p1

%build
cd gst-libs/ext/ffmpeg
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
cd ../../..
%{__libtoolize}
%{__aclocal} -I common/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{gst_major_ver}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/gstreamer-%{gst_major_ver}/libgstffmpeg.so
%attr(755,root,root) %{_libdir}/gstreamer-%{gst_major_ver}/libgstpostproc.so
