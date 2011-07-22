#
# Conditional build:
%bcond_without	vdpau		# build FFmpeg without VDPAU support
%bcond_without	system_ffmpeg	# system FFmpeg (note: upstream does not accept bugs with system ffmpeg)

%define		gstname gst-ffmpeg
%define		gst_major_ver   0.10
%define		gst_req_ver	0.10.31

%include	/usr/lib/rpm/macros.gstreamer
Summary:	GStreamer Streaming-media framework plug-in using FFmpeg
Summary(pl.UTF-8):	Wtyczka do środowiska obróbki strumieni GStreamer używająca FFmpeg
Name:		gstreamer-ffmpeg
Version:	0.10.12
Release:	1
# the ffmpeg plugin is LGPL, the postproc plugin is GPL
License:	GPL v2+ and LGPL v2+
Group:		Libraries
Source0:	http://gstreamer.freedesktop.org/src/gst-ffmpeg/%{gstname}-%{version}.tar.bz2
# Source0-md5:	8507f33c56e6155a3d450dfe6de835a9
URL:		http://gstreamer.net/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.10
BuildRequires:	gstreamer-devel >= %{gst_req_ver}
BuildRequires:	gtk-doc >= 1.3
BuildRequires:	gstreamer-plugins-base-devel >= %{gst_req_ver}
BuildRequires:	libtool
BuildRequires:	orc-devel >= 0.4.6
BuildRequires:	pkgconfig
BuildRequires:	python >= 2.1
BuildRequires:	rpmbuild(macros) >= 1.470
%if %{with system_ffmpeg}
# libavutil,libswscale needed
BuildRequires:	ffmpeg-devel >= 0.7
%else
BuildRequires:	bzip2-devel
# TODO: fill the rest of ffmpeg dependencies used here
%if %{with vdpau}
BuildRequires:	libvdpau-devel
BuildRequires:	xorg-lib-libXvMC-devel
%endif
%endif
Requires:	gstreamer-plugins-base >= %{gst_req_ver}
Requires:	orc >= 0.4.6
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

%build
%{__libtoolize}
%{__aclocal} -I common/m4
%{__autoconf}
%{__autoheader}
%{__automake}

%configure \
	CPPFLAGS="%{rpmcppflags}" \
	%{?with_system_ffmpeg:--with-system-ffmpeg} \
	%{?with_vdpau:--with-ffmpeg-extra-configure="--enable-vdpau"} \
	--disable-silent-rules \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{gst_major_ver}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/gstreamer-%{gst_major_ver}/libgstffmpeg.so
%attr(755,root,root) %{_libdir}/gstreamer-%{gst_major_ver}/libgstffmpegscale.so
%attr(755,root,root) %{_libdir}/gstreamer-%{gst_major_ver}/libgstpostproc.so
