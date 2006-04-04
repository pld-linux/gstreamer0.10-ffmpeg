#
# TODO
# Use shared ffmpeg lib instead of builtin - anyone wants to do it?
#
%define gstname gst-ffmpeg
%define gst_major_ver   0.10

Summary:	GStreamer Streaming-media framework plug-in using FFmpeg
Summary(pl):	Wtyczka do ¶rodowiska obróbki strumieni GStreamer u¿ywaj±ca FFmpeg
Name:		gstreamer-ffmpeg
Version:	0.10.1
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://gstreamer.freedesktop.org/src/gst-ffmpeg/%{gstname}-%{version}.tar.bz2
# Source0-md5:	e21aef9a84d67dea9a68c1379781f763
Patch0:		%{name}-nocpp.patch
URL:		http://gstreamer.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gstreamer-plugins-base-devel >= 0.10
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	gstreamer-plugins-base >= 0.10
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

%description -l pl
GStreamer to ¶rodowisko obróbki danych strumieniowych, bazuj±ce na
grafie filtrów operuj±cych na danych medialnych. Aplikacje u¿ywaj±ce
tej biblioteki mog± robiæ wszystko od przetwarzania d¼wiêku w czasie
rzeczywistym, do odtwarzania filmów i czegokolwiek innego zwi±zanego z
mediami. Architektura bazuj±ca na wtyczkach pozwala na ³atwe dodawanie
nowych typów danych lub mo¿liwo¶ci obróbki.

Wtyczka ta zawiera kodeki FFmpeg, potrafi±ce zdekodowaæ najpopularniejsze
formaty multimedialne.

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
%configure
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
