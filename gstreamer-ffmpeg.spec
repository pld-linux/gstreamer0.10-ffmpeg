# 
# TODO
# Use shared ffmpeg lib instead of builtin - anyone wants to do it?
#
%define gstname gst-ffmpeg
%define gst_major_ver   0.8
%define gstreg  %{_var}/cache/gstreamer/registry.xml

Summary:	GStreamer Streaming-media framework plug-in using FFmpeg
Summary(pl):	Wtyczka do ¶rodowiska obróbki strumieni GStreamer u¿ywaj±ca FFmpeg
Name:		gstreamer-ffmpeg
Version:	0.8.2
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://gstreamer.freedesktop.org/src/%{gstname}/%{gstname}-%{version}.tar.bz2
# Source0-md5:	834270830aa7a4c07485d5185b77af17
URL:		http://gstreamer.net/
BuildRequires:	gstreamer-devel >= 0.8.3
Requires(post,postun):  %{_bindir}/gst-register
Requires:	gstreamer >= 0.8.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%build
cp /usr/share/automake/config.sub .
cp /usr/share/automake/config.sub gst-libs/ext/ffmpeg
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
	
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{gst_major_ver}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_bindir}/gst-register --gst-registry=%{gstreg} > /dev/null 2> /dev/null

%postun
%{_bindir}/gst-register --gst-registry=%{gstreg} > /dev/null 2> /dev/null

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/gstreamer-%{gst_major_ver}/libgstffmpeg.so
